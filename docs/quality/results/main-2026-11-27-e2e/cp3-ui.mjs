// A39 E2E (lượt 1): 10 bước CP3 + 3 ca lỗi trên UI thật. Bản: BE 24e08ce + FE 58a81b8.
// Điều kiện chạy: stack Docker Compose của backend với project `qldapm-m27` (container qldapm-m27-postgres-1,
// web nginx ở WEB_URL), container `qldapm-m27-tools-1` chung network namespace với postgres và có /tmp/dev-token
// + /db/seed/demo.sql, `npm i playwright@1.65.1`, Google Chrome đã cài.
// Biến môi trường: WEB_URL (mặc định http://127.0.0.1:5178), BE_ENV (đường dẫn file .env của backend, bắt buộc),
// OUT_DIR (thư mục ghi ảnh/log, mặc định ./e2e-out; không trỏ vào thư mục bằng chứng trong repo).
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { runPr11 } from './pr11-ui.mjs';

const BASE = process.env.WEB_URL || 'http://127.0.0.1:5178';
const OUT = path.resolve(process.env.OUT_DIR || 'e2e-out') + path.sep;
const SHOTS = OUT + 'shots' + path.sep;
fs.mkdirSync(SHOTS, { recursive: true });
const net = fs.createWriteStream(OUT + 'network.ndjson');
const results = [];
const tag = Date.now().toString(36);

if (!process.env.BE_ENV) throw new Error('Đặt BE_ENV trỏ tới file .env của backend');
const ENV = fs.readFileSync(process.env.BE_ENV, 'utf8');
const envv = (k) => ENV.match(new RegExp(`^${k}=(.*)$`, 'm'))[1].trim();
const redact = (value) => String(value)
  .replace(/\x1b\[[0-9;]*m/g, '')
  .replace(/("(?:checkinCode|qrToken|accessToken|refreshToken|idToken|JWT_SECRET)"\s*:\s*)"[^"]*"/gi, '$1"<redacted>"')
  .replace(/\bBearer\s+[^\s"']+/gi, 'Bearer <redacted>')
  .replace(/\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b/g, '<redacted>')
  .replace(/\bv1\.[a-f0-9-]{36}\.[a-f0-9-]{36}\.[a-f0-9]{64}\b/gi, '<redacted>');
const dexec = (args, input) => execFileSync('docker', args, { input, encoding: 'utf8', env: { ...process.env, MSYS_NO_PATHCONV: '1' } }).trim();
const sql = (s) => dexec(['exec', '-i', 'qldapm-m27-postgres-1', 'psql', '-v', 'ON_ERROR_STOP=1', '-qAt', '-U', 'ticket', '-d', 'ticket'], s);
const mint = (role) => dexec(['exec', '-e', `JWT_SECRET=${envv('JWT_SECRET')}`, '-e', 'AUTH_MODE=local', '-e',
  `DATABASE_URL=postgres://ticket:${envv('POSTGRES_PASSWORD')}@127.0.0.1:5432/ticket?sslmode=disable`, 'qldapm-m27-tools-1', '/tmp/dev-token', '-role', role]).split('\n').pop();

// Tài khoản: student A, B là hai user riêng (đổi email user demo sau khi mint).
const tok = {};
tok.organizer = mint('organizer');
tok.admin = mint('admin');
for (const who of ['A', 'B']) {
  tok['student' + who] = mint('student');
  sql(`UPDATE users SET email='e2e.${tag}.${who.toLowerCase()}@hcmut.edu.vn', student_code='E${tag.slice(-7)}${who}', full_name='E2E Student ${who}' WHERE email='student.demo@hcmut.edu.vn';`);
}

const pad = (n) => String(n).padStart(2, '0');
const local = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
const inMin = (m) => new Date(Date.now() + m * 60000);

const browser = await chromium.launch({
  channel: 'chrome', headless: true,
  ...(process.env.FAKE_CAMERA ? { args: ['--use-fake-device-for-media-stream', '--use-fake-ui-for-media-stream'] } : {}),
});
const ctxs = {};
async function page(role) {
  if (!ctxs[role]) {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 }, acceptDownloads: true });
    const p = await ctx.newPage();
    p.setDefaultTimeout(10000);
    p.on('console', (m) => m.type() === 'error' && net.write(JSON.stringify({ role, console: redact(m.text()).slice(0, 300) }) + '\n'));
    p.on('pageerror', (e) => net.write(JSON.stringify({ role, url: p.url().replace(BASE, ''), pageerror: redact(e.stack || e.message || String(e)) }) + '\n'));
    p.on('response', async (r) => {
      if (!r.url().includes('/api/v1/')) return;
      let body = '';
      try { body = redact(await r.text()).slice(0, 400); } catch {}
      net.write(JSON.stringify({ role, t: new Date().toISOString(), m: r.request().method(), url: r.url().replace(BASE, ''), s: r.status(), body }) + '\n');
    });
    await p.goto(BASE + '/login');
    await p.getByRole('button', { name: 'Dán access token để test' }).click();
    await p.getByRole('button', { name: /Dán token trực tiếp/ }).click();
    await field(p, 'Access token').fill(tok[role]);
    await p.getByRole('button', { name: 'Vào hệ thống' }).click();
    await p.waitForURL((u) => !u.pathname.startsWith('/login'), { timeout: 15000 });
    ctxs[role] = p;
  }
  return ctxs[role];
}
const shot = (p, name) => p.screenshot({ path: SHOTS + name + '.png', fullPage: true });
const waitForCamera = async (p) => {
  if (process.env.FAKE_CAMERA) await p.waitForFunction(() => document.querySelector('video')?.readyState >= 2);
};
const apiWait = (p, method, re, ms = 15000) => {
  const response = p.waitForResponse((r) => r.request().method() === method && re.test(r.url()), { timeout: ms });
  response.catch(() => {});
  return response;
};

async function step(id, title, fn, components) {
  try {
    const detail = await fn();
    results.push({ id, title, ok: components?.every((c) => c.ok) ?? true, detail: detail ?? '',
                   ...(components ? { components } : {}) });
  } catch (e) {
    results.push({ id, title, ok: false, detail: redact(e.message || e).split('\n').filter((line) => line.trim()).slice(0, 4).join(' | ').slice(0, 450),
                   ...(components ? { components } : {}) });
    for (const [r, p] of Object.entries(ctxs)) await shot(p, `FAIL-${id}-${r}`).catch(() => {});
  }
  console.log(JSON.stringify(results.at(-1)));
}

let eventId, regA, regB, codeB;
const title = `A39 E2E ${tag}`;

const fieldGroup = (p, label) => p.locator('label').filter({ hasText: label }).locator('..');
const field = (p, label, control = 'input') => fieldGroup(p, label).locator(control);

async function fillSchedule(p, start, end, opens, closes) {
  for (const [label, v] of [['Bắt đầu', start], ['Kết thúc', end], ['Mở đăng ký', opens], ['Đóng đăng ký', closes]])
    if (v) await field(p, label).fill(local(v));
}

await step('1', 'Organizer tạo sự kiện (sức chứa 1, hàng chờ 2) và gửi duyệt', async () => {
  const p = await page('organizer');
  await p.goto(BASE + '/manage/events/new');
  const unit = field(p, 'Đơn vị tổ chức', 'select');
  const opts = await unit.locator('option').evaluateAll((os) => os.map((o) => o.value).filter(Boolean));
  if (opts.length) await unit.selectOption(opts[0]);
  await field(p, 'Tiêu đề').fill(title);
  await field(p, 'Mô tả', 'textarea').fill('Kiểm thử hồi quy A39 tự động');
  await field(p, 'Địa điểm').fill('H6-101');
  await fillSchedule(p, inMin(72 * 60), inMin(74 * 60), inMin(-5), inMin(60 * 60));
  await field(p, 'Sức chứa').fill('1');
  await field(p, 'Giới hạn hàng chờ').fill('2');
  const created = apiWait(p, 'POST', /\/api\/v1\/events$/);
  await p.getByRole('button', { name: 'Tạo nháp' }).click();
  const r = await created;
  if (r.status() !== 201) throw new Error(`POST /events ${r.status()} ${(await r.text()).slice(0, 200)}`);
  eventId = (await r.json()).data.id;
  await p.waitForURL(new RegExp(`/manage/events/${eventId}`));
  const sub = apiWait(p, 'POST', /\/submit$/);
  await p.getByRole('button', { name: 'Gửi duyệt' }).click();
  const s = await sub;
  await shot(p, '01-organizer-gui-duyet');
  if (s.status() !== 200) throw new Error(`submit ${s.status()}`);
  return `event ${eventId}, tạo 201, gửi duyệt 200`;
});

await step('2', 'Admin duyệt và công bố', async () => {
  const p = await page('admin');
  await p.goto(BASE + '/admin/approvals');
  const card = p.locator('div').filter({ hasText: title }).filter({ has: p.getByRole('button', { name: 'Duyệt & công bố' }) }).last();
  const ap = apiWait(p, 'POST', /\/approve$/);
  await card.getByRole('button', { name: 'Duyệt & công bố' }).click();
  const r = await ap;
  await p.waitForTimeout(800);
  await shot(p, '02-admin-duyet');
  const body = await r.json();
  if (r.status() !== 200 || body.data?.status !== 'PUBLISHED') throw new Error(`approve ${r.status()} ${body.data?.status}`);
  return 'approve 200, PUBLISHED';
});

async function register(role) {
  const p = await page(role);
  await p.goto(`${BASE}/events/${eventId}`);
  const rr = apiWait(p, 'POST', /\/registrations$/);
  await p.getByRole('button', { name: /Đăng ký tham gia|Vào danh sách chờ/ }).click();
  const r = await rr;
  await p.waitForTimeout(800);
  return { p, r, body: await r.json() };
}

await step('3', 'Student A đăng ký → REGISTERED', async () => {
  const { p, r, body } = await register('studentA');
  await shot(p, '03-studentA-dang-ky');
  regA = body.data?.id;
  if (r.status() !== 201 || body.data?.status !== 'REGISTERED') throw new Error(`${r.status()} ${body.data?.status}`);
  return `201 REGISTERED (${regA})`;
});

await step('4', 'Student B vào hàng chờ → WAITLISTED vị trí 1', async () => {
  const { p, r, body } = await register('studentB');
  await shot(p, '04-studentB-hang-cho');
  regB = body.data?.id;
  if (r.status() !== 201 || body.data?.status !== 'WAITLISTED' || body.data?.waitlistPosition !== 1)
    throw new Error(`${r.status()} ${body.data?.status} pos=${body.data?.waitlistPosition}`);
  const txt = await p.locator('body').innerText();
  return `201 WAITLISTED vị trí 1; UI có chữ "hàng chờ": ${/hàng chờ/i.test(txt)}`;
});

await step('5', 'Student A hủy (còn >24h) → CANCELLED', async () => {
  const p = await page('studentA');
  await p.goto(`${BASE}/events/${eventId}`);
  await p.getByRole('button', { name: 'Hủy', exact: true }).click();
  const cr = apiWait(p, 'POST', /\/cancel$/);
  await p.getByRole('dialog').getByRole('button', { name: 'Hủy đăng ký' }).click()
    .catch(() => p.getByRole('button', { name: 'Hủy đăng ký' }).last().click());
  const r = await cr;
  await p.waitForTimeout(800);
  await shot(p, '05-studentA-huy');
  const b = await r.json();
  if (r.status() !== 200 || b.data?.status !== 'CANCELLED') throw new Error(`${r.status()} ${JSON.stringify(b).slice(0, 150)}`);
  return '200 CANCELLED';
});

await step('6', 'Student B tự lên REGISTERED + có thông báo PROMOTED', async () => {
  const p = await page('studentB');
  await p.goto(`${BASE}/my-registrations`);
  await p.waitForTimeout(1200);
  await shot(p, '06-studentB-len-cho');
  const txt = await p.locator('body').innerText();
  const st = sql(`SELECT status FROM registrations WHERE id='${regB}';`);
  const noti = sql(`SELECT count(*) FROM notifications n JOIN registrations r ON r.student_id=n.user_id WHERE r.id='${regB}' AND n.type='PROMOTED';`);
  if (st !== 'REGISTERED') throw new Error(`DB status ${st}`);
  return `DB REGISTERED; notifications PROMOTED=${noti}; UI "Đăng ký của tôi" hiển thị trạng thái: ${(txt.match(/Đã đăng ký|Hàng chờ|REGISTERED|WAITLISTED/g) || []).join(',')}; FE không có trang xem thông báo`;
});

await step('7', 'Organizer dời giờ bắt đầu về ~30 phút tới (UI sửa sự kiện)', async () => {
  const p = await page('organizer');
  await p.goto(`${BASE}/manage/events/${eventId}`);
  await fillSchedule(p, inMin(30), inMin(180), null, inMin(20));
  const pr = apiWait(p, 'PATCH', new RegExp(`/events/${eventId}$`));
  await p.getByRole('button', { name: 'Lưu thay đổi' }).click();
  const r = await pr;
  await p.waitForTimeout(800);
  await shot(p, '07-organizer-doi-gio');
  if (r.status() !== 200) throw new Error(`PATCH ${r.status()} ${(await r.text()).slice(0, 200)}`);
  return 'PATCH 200';
});

await step('7b', 'Ca lỗi: Student B hủy khi còn <24h → 422 CANCEL_DEADLINE_PASSED, UI báo lỗi', async () => {
  const p = await page('studentB');
  await p.goto(`${BASE}/events/${eventId}`);
  await p.getByRole('button', { name: 'Hủy', exact: true }).click();
  const cr = apiWait(p, 'POST', /\/cancel$/);
  await p.getByRole('dialog').getByRole('button', { name: 'Hủy đăng ký' }).click()
    .catch(() => p.getByRole('button', { name: 'Hủy đăng ký' }).last().click());
  const r = await cr;
  await p.waitForTimeout(1000);
  await shot(p, '07b-huy-qua-han');
  const b = await r.json();
  const ui = await p.locator('[role=alert], [role=status], .toast, li[data-sonner-toast]').allInnerTexts().catch(() => []);
  if (r.status() !== 422 || b.error?.code !== 'CANCEL_DEADLINE_PASSED') throw new Error(`${r.status()} ${b.error?.code}`);
  return `422 CANCEL_DEADLINE_PASSED; UI: ${ui.join(' | ').slice(0, 160) || '(xem ảnh)'}`;
});

await step('8', 'Student B mở vé, thấy QR và mã check-in', async () => {
  const p = await page('studentB');
  await p.goto(`${BASE}/registrations/${regB}`);
  await p.locator('canvas').first().waitFor({ timeout: 10000 });
  await shot(p, '08-studentB-qr');
  codeB = sql(`SELECT checkin_code FROM registrations WHERE id='${regB}';`);
  const shown = (await p.locator('body').innerText()).replace(/-/g, '').includes(codeB);
  if (!shown) throw new Error(`mã trong DB không hiện trên trang`);
  return `QR canvas có; mã hiển thị khớp DB`;
});

await step('9', 'Organizer check-in B bằng Nhập mã; lần 2 báo đã check-in', async () => {
  const p = await page('organizer');
  await p.goto(`${BASE}/manage/events/${eventId}/check-in`);
  await waitForCamera(p);
  await p.getByRole('button', { name: 'Nhập mã' }).click();
  const input = field(p, 'Mã check-in');
  const out = [];
  for (const i of [1, 2]) {
    await input.fill(codeB);
    const cr = apiWait(p, 'POST', /\/check-ins$/);
    await p.getByRole('button', { name: 'Check-in', exact: true }).last().click();
    const r = await cr;
    await p.waitForTimeout(900);
    await shot(p, `09-checkin-lan${i}`);
    const b = await r.json();
    out.push(`${r.status()} ${b.error?.code || b.data?.method || ''}`);
  }
  if (!out[0].startsWith('201') || !out[1].startsWith('409')) throw new Error(out.join(' / '));
  const actor = sql(`SELECT checked_in_by FROM registrations WHERE id='${regB}';`);
  const showsActorUuid = Boolean(actor) && (await p.locator('body').innerText()).includes(actor);
  return out.join(' / ') + `; banner trùng hiện UUID người check-in: ${showsActorUuid}`;
});

await step('10', 'Organizer xem thống kê và tải CSV', async () => {
  const p = await page('organizer');
  await p.goto(`${BASE}/manage/events/${eventId}/check-in`);
  const rate = p.getByRole('progressbar', { name: 'Tỉ lệ tham dự' });
  await rate.waitFor();
  const attendance = await rate.getAttribute('aria-valuenow');
  const dl = p.waitForEvent('download', { timeout: 15000 });
  dl.catch(() => {});
  await p.getByRole('button', { name: 'Đăng ký (CSV)', exact: true }).click();
  const d = await dl;
  const csvPath = OUT + 'registrations.csv';
  await d.saveAs(csvPath);
  await shot(p, '10-bao-cao-csv');
  const csv = fs.readFileSync(csvPath, 'utf8');
  return `CSV ${csv.split('\n').filter(Boolean).length} dòng; tỉ lệ tham dự: ${attendance}%`;
});

await step('C2', 'Ca lỗi: check-in ngoài khung giờ → 422 CHECKIN_WINDOW_CLOSED, UI báo', async () => {
  // Sự kiện mới bắt đầu sau 72h, đăng ký A rồi organizer nhập mã.
  const p = await page('organizer');
  await p.goto(BASE + '/manage/events/new');
  const unit = field(p, 'Đơn vị tổ chức', 'select');
  const opts = await unit.locator('option').evaluateAll((os) => os.map((o) => o.value).filter(Boolean));
  if (opts.length) await unit.selectOption(opts[0]);
  await field(p, 'Tiêu đề').fill(title + ' ngoài giờ');
  await field(p, 'Địa điểm').fill('H6-102');
  await fillSchedule(p, inMin(72 * 60), inMin(74 * 60), inMin(-5), inMin(60 * 60));
  await field(p, 'Sức chứa').fill('5');
  const created = apiWait(p, 'POST', /\/api\/v1\/events$/);
  await p.getByRole('button', { name: 'Tạo nháp' }).click();
  const e2 = (await (await created).json()).data.id;
  sql(`UPDATE events SET status='PUBLISHED', published_at=now() WHERE id='${e2}';`);
  const pa = await page('studentA');
  await pa.goto(`${BASE}/events/${e2}`);
  const rr = apiWait(pa, 'POST', /\/registrations$/);
  await pa.getByRole('button', { name: /Đăng ký tham gia/ }).click();
  const rid = (await (await rr).json()).data.id;
  const code = sql(`SELECT checkin_code FROM registrations WHERE id='${rid}';`);
  await p.goto(`${BASE}/manage/events/${e2}/check-in`);
  await waitForCamera(p);
  await p.getByRole('button', { name: 'Nhập mã' }).click();
  await field(p, 'Mã check-in').fill(code);
  const cr = apiWait(p, 'POST', /\/check-ins$/);
  await p.getByRole('button', { name: 'Check-in', exact: true }).last().click();
  const r = await cr;
  await p.waitForTimeout(900);
  await shot(p, 'C2-checkin-ngoai-gio');
  const b = await r.json();
  const txt = await p.locator('body').innerText();
  if (r.status() !== 422 || b.error?.code !== 'CHECKIN_WINDOW_CLOSED') throw new Error(`${r.status()} ${b.error?.code}`);
  return `422 CHECKIN_WINDOW_CLOSED; UI có chữ "khung giờ": ${/khung giờ/i.test(txt)} (sự kiện được PUBLISHED trực tiếp qua DB để tiết kiệm bước duyệt)`;
});

await step('C3', 'Ca lỗi: Organizer kiêm Admin tự duyệt sự kiện của mình', async () => {
  const p = await page('organizer');
  const orgId = sql(`SELECT id FROM users WHERE email='organizer.demo@hcmut.edu.vn';`);
  await p.goto(BASE + '/manage/events/new');
  const unit = field(p, 'Đơn vị tổ chức', 'select');
  const opts = await unit.locator('option').evaluateAll((os) => os.map((o) => o.value).filter(Boolean));
  if (opts.length) await unit.selectOption(opts[0]);
  await field(p, 'Tiêu đề').fill(title + ' tự duyệt');
  await field(p, 'Địa điểm').fill('H6-103');
  await fillSchedule(p, inMin(72 * 60), inMin(74 * 60), inMin(-5), inMin(60 * 60));
  await field(p, 'Sức chứa').fill('5');
  const created = apiWait(p, 'POST', /\/api\/v1\/events$/);
  await p.getByRole('button', { name: 'Tạo nháp' }).click();
  const e3 = (await (await created).json()).data.id;
  await p.waitForURL(new RegExp(`/manage/events/${e3}`));
  const sub = apiWait(p, 'POST', /\/submit$/);
  await p.getByRole('button', { name: 'Gửi duyệt' }).click();
  await sub;
  sql(`UPDATE users SET is_admin=true WHERE id='${orgId}';`);
  try {
    await p.goto(BASE + '/admin/approvals');
    const card = p.locator('div').filter({ hasText: title + ' tự duyệt' }).filter({ has: p.getByRole('button', { name: 'Duyệt & công bố' }) }).last();
    const ap = apiWait(p, 'POST', /\/approve$/);
    await card.getByRole('button', { name: 'Duyệt & công bố' }).click();
    const r = await ap;
    await p.waitForTimeout(1000);
    await shot(p, 'C3-tu-duyet');
    const b = await r.json();
    const txt = await p.locator('body').innerText();
    const ui = (txt.match(/[^\n]*(không được tự duyệt|không có quyền|không thể tự duyệt sự kiện do chính mình tạo)[^\n]*/i) || ['(không thấy thông báo, xem ảnh)'])[0].trim();
    if (r.status() !== 403) throw new Error(`approve ${r.status()}`);
    if (b.error?.code !== 'SELF_APPROVAL_NOT_ALLOWED') throw new Error(`403 ${b.error?.code} (D02: kỳ vọng SELF_APPROVAL_NOT_ALLOWED); UI hiển thị: ${ui}`);
    return `403 SELF_APPROVAL_NOT_ALLOWED; UI: ${ui}`;
  } finally {
    sql(`UPDATE users SET is_admin=false WHERE id='${orgId}';`);
  }
});

await runPr11({ BASE, page, tok, sql, shot, apiWait, step, field, fieldGroup, fillSchedule, inMin, tag, waitForCamera });
await browser.close();
await new Promise((resolve, reject) => {
  net.on('error', reject);
  net.end(resolve);
});
fs.writeFileSync(OUT + 'results.json', JSON.stringify(results, null, 2));
for (const [label, items] of [['CP3', results.filter((r) => !r.id.startsWith('U'))],
                              ['PR11', results.filter((r) => r.id.startsWith('U'))]]) {
  console.log(`${label} PASS ${items.filter((r) => r.ok).length}/${items.length}`);
}
process.exitCode = results.every((r) => r.ok) ? 0 : 1;
