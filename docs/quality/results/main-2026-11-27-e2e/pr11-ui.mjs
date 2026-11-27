import assert from 'node:assert/strict';

export async function runPr11({ BASE, page, tok, sql, shot, apiWait, step, field, fieldGroup, fillSchedule, inMin, tag, waitForCamera }) {
  const button = (p, name) => p.getByRole('button', { name, exact: typeof name === 'string' });
  const shown = (p, text) => p.getByText(text, { exact: typeof text === 'string' }).first().waitFor();
  const auth = (role) => ({ Authorization: 'Bearer ' + tok[role] });
  const unit = sql("SELECT id FROM units WHERE code='DEMO';");

  async function call(role, endpoint, status, data) {
    const p = await page(role);
    const r = await p.request.post(BASE + '/api/v1' + endpoint, { headers: auth(role), data: data ?? {} });
    assert.equal(r.status(), status, endpoint);
    return (await r.json()).data;
  }

  async function fixture(label, capacity = 2) {
    const title = `P1 ${tag} ${label}`;
    const e = await call('organizer', '/events', 201, {
      title, unitId: unit, location: 'H6-111', capacity, waitlistLimit: 2,
      startAt: inMin(72 * 60).toISOString(), endAt: inMin(74 * 60).toISOString(),
      registrationOpensAt: inMin(-10).toISOString(), registrationClosesAt: inMin(60 * 60).toISOString(),
    });
    await call('organizer', `/events/${e.id}/submit`, 200);
    await call('admin', `/events/${e.id}/approve`, 200);
    return { ...e, title };
  }
  const register = (e, role) => call(role, `/events/${e.id}/registrations`, 201);

  async function parts(id, title, run) {
    const components = [];
    await step(id, title, async () => {
      await run(async (label, p, fn) => {
        let detail;
        let ok = false;
        let outcome;
        try {
          detail = await fn();
          outcome = typeof detail === 'object' ? detail.outcome : 'pass';
          if (outcome === 'not_applicable') detail = detail.detail;
          ok = outcome === 'pass';
        } catch (error) {
          outcome = 'fail';
          detail = String(error.message).split('\n').filter(Boolean).slice(0, 4).join(' | ');
        }
        const screenshot = `${id}-${label}`;
        if (p) await shot(p, screenshot);
        components.push({ label, ok, outcome, detail, ...(p ? { screenshot: `shots/${screenshot}.png` } : {}) });
      });
      return components.filter((part) => part.ok).length + '/' + components.length + ' kiểm tra thành phần';
    }, components);
  }

  await parts('U1', 'Vé của tôi, ba tab, trạng thái vé, QR và mã dự phòng', async (check) => {
    const p = await page('studentA');
    const registered = await fixture('U1-REGISTERED');
    const waiting = await fixture('U1-WAITLISTED', 1);
    const cancelled = await fixture('U1-CANCELLED');
    const rr = await register(registered, 'studentA');
    await register(waiting, 'studentB');
    const rw = await register(waiting, 'studentA');
    const rc = await register(cancelled, 'studentA');
    await call('studentA', `/registrations/${rc.id}/cancel`, 200);
    const dbStatus = (reg) => sql(`SELECT status FROM registrations WHERE id='${reg.id}';`);
    const card = (e, badge) => p.getByText(e.title, { exact: true })
      .locator('xpath=ancestor::div').filter({ has: p.getByText(badge, { exact: true }) }).last();
    async function readTab(name, filter, initial = false) {
      const response = apiWait(p, 'GET', /\/me\/registrations(?:\?|$)/);
      if (initial) await p.goto(BASE + '/my-registrations');
      else await button(p, name).click();
      const r = await response;
      assert.equal(r.status(), 200);
      assert.equal(new URL(r.url()).searchParams.get(filter[0]), filter[1]);
      return (await r.json()).data;
    }
    async function matches(e, reg, status, badge, data) {
      assert.equal(dbStatus(reg), status);
      assert.equal(data.find((row) => row.id === reg.id)?.status, status);
      await card(e, badge).waitFor();
    }
    await check('sap-toi', p, async () => {
      const data = await readTab('Sắp tới', ['upcoming', 'true'], true);
      await button(p, /^Sắp tới/).waitFor();
      await matches(registered, rr, 'REGISTERED', 'Đã đăng ký', data);
      await matches(waiting, rw, 'WAITLISTED', 'Chờ #1', data);
      return 'GET upcoming=true, thẻ REGISTERED và WAITLISTED đúng dữ liệu';
    });
    await check('tat-ca', p, async () => {
      const data = await readTab('Tất cả', ['status', null]);
      await matches(registered, rr, 'REGISTERED', 'Đã đăng ký', data);
      await matches(waiting, rw, 'WAITLISTED', 'Chờ #1', data);
      await matches(cancelled, rc, 'CANCELLED', 'Đã hủy', data);
      return 'GET tất cả, 3 thẻ và trạng thái khớp DB';
    });
    await check('da-huy', p, async () => {
      const data = await readTab('Đã hủy', ['status', 'CANCELLED']);
      await matches(cancelled, rc, 'CANCELLED', 'Đã hủy', data);
      assert(data.every((row) => row.status === 'CANCELLED'));
      assert.equal(await p.getByText(registered.title, { exact: true }).count(), 0);
      assert.equal(await p.getByText(waiting.title, { exact: true }).count(), 0);
      return 'GET status=CANCELLED, chỉ có thẻ đã hủy';
    });
    await check('qr', p, async () => {
      await button(p, 'Tất cả').click();
      const response = apiWait(p, 'GET', new RegExp(`/registrations/${rr.id}$`));
      await p.locator(`a[href="/registrations/${rr.id}"]`).click();
      const r = await response;
      assert.equal(r.status(), 200);
      const { data } = await r.json();
      assert(Boolean(data.qrToken), 'API chi tiết phải cấp QR');
      await p.locator('canvas').waitFor();
      const pixels = await p.locator('canvas').evaluate((canvas) => {
        const data = canvas.getContext('2d').getImageData(0, 0, canvas.width, canvas.height).data;
        return data.some((value, index) => index % 4 === 0 && value === 0);
      });
      assert(pixels, 'QR canvas phải có hình được vẽ');
      const code = sql(`SELECT checkin_code FROM registrations WHERE id='${rr.id}';`);
      assert(Boolean(code) && data.checkinCode.replace(/-/g, '') === code, 'Mã API phải khớp DB');
      assert((await p.locator('main').innerText()).replace(/-/g, '').includes(code), 'Mã trên UI phải khớp DB');
      return 'QR được vẽ, mã UI và API khớp DB';
    });
  });

  await parts('U2', 'Thống kê, ba tab check-in, mã sai và MANUAL', async (check) => {
    const p = await page('organizer');
    const e = await fixture('U2');
    const r = await register(e, 'studentA');
    sql(`UPDATE events SET start_at=now()+interval '30 minutes', end_at=now()+interval '2 hours',
         registration_closes_at=now()+interval '20 minutes' WHERE id='${e.id}';`);
    await p.goto(`${BASE}/manage/events/${e.id}/check-in`);
    async function stats(expected) {
      const db = sql(`SELECT count(*) FILTER (WHERE checked_in_at IS NOT NULL) || ',' || count(*)
                      FROM registrations WHERE event_id='${e.id}' AND status='REGISTERED';`);
      const [checked, registered] = db.split(',').map(Number);
      assert.equal(checked, expected);
      assert.equal(registered, 1);
      const rate = Math.round(100 * checked / registered);
      await p.locator(`[role=progressbar][aria-valuenow="${rate}"]`).waitFor();
      const values = await p.locator('div').filter({ has: p.getByText('Tỉ lệ', { exact: true }) })
        .filter({ has: p.getByText('Đã đăng ký', { exact: true }) }).last().innerText();
      assert.deepEqual(values.trim().split(/\s*\n\s*/).filter(Boolean),
        [String(checked), 'Đã check-in', String(registered), 'Đã đăng ký', rate + '%', 'Tỉ lệ']);
      return `UI = DB, ${checked} check-in / ${registered} đăng ký / ${rate}%`;
    }
    await check('thong-ke-truoc', p, () => stats(0));
    await check('quet-qr', p, async () => {
      await button(p, 'Quét QR').click();
      await p.getByText(/Đưa mã QR vào khung|Không mở được camera|Bạn cần cấp quyền camera/).first().waitFor();
      const camera = await p.getByText(/Không mở được camera|Bạn cần cấp quyền camera/).count();
      return camera ? 'Tab Quét QR mở và hiện trạng thái camera headless' : 'Tab Quét QR mở và hiện khung quét';
    });
    await check('nhap-ma', p, async () => {
      await waitForCamera(p);
      await button(p, 'Nhập mã').click();
      await field(p, 'Mã check-in').waitFor({ timeout: 3000 });
      return 'Tab Nhập mã mở và có ô mã';
    });
    await check('ma-sai', p, async () => {
      const missingCode = 'Z'.repeat(8);
      assert(await field(p, 'Mã check-in').isVisible(), 'Ô nhập mã đã biến mất sau khi chuyển tab');
      assert.equal(sql(`SELECT count(*) FROM registrations WHERE checkin_code='${missingCode}';`), '0');
      await field(p, 'Mã check-in').fill(missingCode);
      const response = apiWait(p, 'POST', /\/check-ins$/);
      await button(p, 'Check-in').click();
      const result = await response;
      assert.equal(result.status(), 404);
      assert.equal((await result.json()).error?.code, 'NOT_FOUND');
      await shown(p, 'Không tìm thấy nội dung bạn yêu cầu.');
      return '404 NOT_FOUND và UI hiển thị thông báo lỗi';
    });
    await check('danh-sach', p, async () => {
      assert(await button(p, 'Danh sách').isVisible(), 'Tab Danh sách đã biến mất sau khi chuyển tab');
      await button(p, 'Danh sách').click();
      assert(await p.getByPlaceholder('Tìm theo tên hoặc MSSV…').isVisible(), 'Không truy cập được danh sách để thực hiện MANUAL');
      await shown(p, 'E2E Student A');
      return 'Tab Danh sách mở và có Student A';
    });
    await check('thu-cong', p, async () => {
      await p.getByPlaceholder('Tìm theo tên hoặc MSSV…').waitFor();
      const manual = button(p, 'Check-in');
      if (await manual.count() === 0) return { outcome: 'not_applicable', detail: 'UI thiếu nút check-in thủ công.' };
      await manual.click();
      const dialog = p.getByRole('dialog');
      const submit = button(dialog, 'Xác nhận check-in');
      assert(await submit.isDisabled(), 'Phải có ghi chú trước khi xác nhận');
      await dialog.locator('textarea').fill('P1 kiểm thử, đã đối chiếu thẻ SV');
      const response = apiWait(p, 'POST', /\/check-ins$/);
      await submit.click();
      const result = await response;
      assert.equal(result.status(), 201);
      assert.equal((await result.json()).data?.method, 'MANUAL');
      assert.equal(sql(`SELECT checkin_method FROM registrations WHERE id='${r.id}';`), 'MANUAL');
      assert.equal(sql(`SELECT count(*) FROM activity_logs WHERE event_id='${e.id}' AND action='MANUAL_CHECKIN';`), '1');
      await dialog.waitFor({ state: 'hidden' });
      await button(p, 'Hoàn tác').waitFor();
      return '201 MANUAL, DB ghi MANUAL và đúng 1 log MANUAL_CHECKIN';
    });
    await check('thong-ke-sau', p, async () => {
      assert(await p.getByRole('progressbar').isVisible(), 'Trang trắng, không thể đọc thống kê sau');
      return stats(1);
    });
  });

  await parts('U3', 'Form sự kiện, kiểm lỗi tại trường và lưu thay đổi', async (check) => {
    const p = await page('organizer');
    const title = `P1 ${tag} U3`;
    let id;
    const requests = [];
    const countMutation = (r) => {
      if (/\/api\/v1\/events(?:\/[^/]+)?$/.test(r.url()) && ['POST', 'PATCH'].includes(r.method())) requests.push(r);
    };
    p.on('request', countMutation);
    try {
      await p.goto(BASE + '/manage/events/new');
      await field(p, 'Đơn vị tổ chức', 'select').selectOption(unit);
      await field(p, 'Địa điểm').fill('H6-113');
      await field(p, 'Sức chứa').fill('3');
      await fillSchedule(p, inMin(4320), inMin(4440), inMin(-5), inMin(3600));

      async function blocked(action, label, message) {
        const before = requests.length;
        await button(p, action).click();
        await shown(p, message);
        const sent = requests.length - before;
        const inline = (await fieldGroup(p, label).getByText(message, { exact: true }).count()) > 0;
        assert(sent === 0 && inline, `Request tạo/sửa=${sent}, lỗi tại trường "${label}"=${inline}; thông báo trên UI: ${message}`);
        return `0 request, lỗi hiển thị tại trường ${label}`;
      }

      await check('tao-thieu-tieu-de', p, () => blocked('Tạo nháp', 'Tiêu đề', 'Vui lòng nhập tiêu đề.'));
      await field(p, 'Tiêu đề').fill(title);
      await field(p, 'Kết thúc').fill(await field(p, 'Bắt đầu').inputValue());
      const dateError = 'Thời gian kết thúc phải sau thời gian bắt đầu.';
      await check('tao-sai-lich', p, () => blocked('Tạo nháp', 'Kết thúc', dateError));
      await fillSchedule(p, null, inMin(4440), null, null);
      await check('tao-hop-le', p, async () => {
        const response = apiWait(p, 'POST', /\/api\/v1\/events$/);
        await button(p, 'Tạo nháp').click();
        const r = await response;
        assert.equal(r.status(), 201);
        const { data } = await r.json();
        id = data.id;
        assert.equal(data.status, 'DRAFT');
        await p.waitForURL(new RegExp(`/manage/events/${id}$`));
        assert.equal(sql(`SELECT title FROM events WHERE id='${id}';`), title);
        return '201 DRAFT và DB lưu đúng tiêu đề';
      });

      assert(id, 'Cần nháp đã tạo để kiểm được form sửa');
      await field(p, 'Tiêu đề').fill('');
      await check('sua-thieu-tieu-de', p, () => blocked('Lưu thay đổi', 'Tiêu đề', 'Vui lòng nhập tiêu đề.'));
      await field(p, 'Tiêu đề').fill(title);
      const end = await field(p, 'Kết thúc').inputValue();
      await field(p, 'Kết thúc').fill(await field(p, 'Bắt đầu').inputValue());
      await check('sua-sai-lich', p, () => blocked('Lưu thay đổi', 'Kết thúc', dateError));
      await field(p, 'Kết thúc').fill(end);
      await check('sua-hop-le', p, async () => {
        const location = 'H6-114 cập nhật';
        await field(p, 'Địa điểm').fill(location);
        const response = apiWait(p, 'PATCH', new RegExp(`/api/v1/events/${id}$`));
        await button(p, 'Lưu thay đổi').click();
        const r = await response;
        assert.equal(r.status(), 200);
        assert.equal((await r.json()).data?.location, location);
        await p.reload();
        assert.equal(await field(p, 'Địa điểm').inputValue(), location);
        assert.equal(sql(`SELECT location FROM events WHERE id='${id}';`), location);
        return 'PATCH 200, địa điểm sau tải lại khớp response và DB';
      });
    } finally {
      p.off('request', countMutation);
    }
  });
}
