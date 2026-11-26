"""Vẽ Gantt Baseline V2.0 (lịch rút gọn, mốc sẵn sàng 29/11) ra HTML từ gantt-v2.json; vẽ kèm khoảng ngày V1.0 để thấy độ dời.
Dùng: python gantt_v2.py <master.xlsx> <config.json> <kết-quả.json> <file-ra.html>"""
import sys, html, json, pathlib, datetime as dt
from common import load, owners, css as css_base

XLSX, CFG, RES, OUT = sys.argv[1:5]
R, SC, RES_, PRED, NEW = load(XLSX, CFG, RES)
D = json.load(open(pathlib.Path(__file__).with_name('gantt-v2.json'), encoding='utf-8'))
iso = dt.date.fromisoformat
T0, T1, TODAY = iso(D['start']), iso(D['end']), iso(D['today'])
days = (T1 - T0).days + 1
LW, DAY, RH, TOP, PAD, RT = 330, 36, 30, 66, 16, 230
width = PAD * 2 + LW + days * DAY + RT


def X(s):
    return PAD + LW + (iso(s) - T0).days * DAY


def dm(s):
    return iso(s).strftime('%d/%m')


def rng(a, b):
    return dm(a) if a == b else f'{dm(a)}–{dm(b)}'


rows, y = [], TOP
for sec in D['sections'] + [dict(name='Quản lý xuyên suốt (hammock)', rows=[dict(h, type='ham') for h in D['hammock']])]:
    rows.append(('sec', sec['name'], y)); y += RH
    for r in sec['rows']:
        rows.append(('act', r, y)); y += RH
bottom = y
height = y + 118
bg, svg, txt = [], [], []
for i in range(days):
    d = T0 + dt.timedelta(days=i)
    x = PAD + LW + i * DAY
    if d.weekday() == 0 or i == 0:
        n = min(7 - d.weekday(), days - i)
        wk = (d - dt.date(2026, 8, 24)).days // 7 + 1
        svg.append(f'<rect x="{x}" y="{TOP - 40}" width="{n * DAY}" height="18" class="wk{wk % 2}"/>')
        txt.append(f'<text x="{x + n * DAY / 2}" y="{TOP - 27}" class="wkt">W{wk} · {d:%d/%m}</text>')
        svg.append(f'<line x1="{x}" y1="{TOP - 40}" x2="{x}" y2="{bottom}" class="wl"/>')
    if d.weekday() >= 5:
        bg.append(f'<rect x="{x}" y="{TOP}" width="{DAY}" height="{bottom - TOP}" class="we"/>')
    txt.append(f'<text x="{x + DAY / 2}" y="{TOP - 8}" class="dt">{d.day}</text>')
# tuần dự trữ 30/11–06/12
bg.append(f'<rect x="{X("2026-11-30")}" y="{TOP}" width="{7 * DAY}" height="{bottom - TOP}" class="resv"/>')
txt.append(f'<text x="{X("2026-11-30") + 3.5 * DAY}" y="{TOP + 19}" class="rsv">tuần dự trữ: chỉ sửa lỗi, chờ slot demo</text>')

for kind, v, ry in rows:
    if kind == 'sec':
        bg.insert(0, f'<rect x="{PAD}" y="{ry}" width="{width - 2 * PAD}" height="{RH}" class="sec"/>')
        txt.append(f'<text x="{PAD + 4}" y="{ry + 19}" class="sect">{html.escape(v)}</text>')
        continue
    a = v['id']
    txt.append(f'<text x="{PAD + 4}" y="{ry + 19}" class="lbl"><tspan class="id">{a}</tspan> {html.escape(R[a]["name"])}</text>')
    ow = owners(RES_[a]) if a in RES_ else ''
    t = v['type']
    if t == 'ham':
        x1, x2 = X(v['from']), X(v['to']) + DAY
        svg.append(f'<rect x="{x1 + 1}" y="{ry + 10}" width="{x2 - x1 - 2}" height="8" rx="2" class="ham"/>')
        info, end = f'{ow} · rải đều đến nộp', x2
    else:
        cls = 'crit' if v.get('crit') else 'bar'
        if t == 'bar':
            x1, x2 = X(v['from']), X(v['to']) + DAY
            svg.append(f'<rect x="{x1 + 1}" y="{ry + 5}" width="{x2 - x1 - 2}" height="13" rx="2" class="{cls}"/>')
            when, end = rng(v['from'], v['to']), x2
        else:
            cx = X(v['at']) + DAY / 2
            pts = f'{cx},{ry + 3} {cx + 9},{ry + 11.5} {cx},{ry + 20} {cx - 9},{ry + 11.5}'
            svg.append(f'<polygon points="{pts}" class="{"dueq" if t == "due" else cls}{" crit" if v.get("crit") and t == "due" else ""}"/>')
            when, end = ('hạn ' if t == 'due' else '') + dm(v['at']), cx + 12
        if v.get('actual'):
            a0, a1 = v['actual']
            svg.append(f'<rect x="{X(a0) + 1}" y="{ry + 8}" width="{X(a1) + DAY - X(a0) - 2}" height="7" rx="1.5" class="actual"/>')
        parts = [ow, when]
        if v.get('actual'):
            parts.append('thực tế ' + rng(*v['actual']))
        if v.get('note'):
            parts.append(v['note'])
        info = ' · '.join(p for p in parts if p)
    # khoảng ngày V1.0 (vẽ mảnh dưới thanh V2.0); ngoài khung thì ghi chữ
    if a in RES_:
        s1, e1 = RES_[a]['start'], RES_[a]['end']
        if iso(e1) < T0 or iso(s1) > T1:
            info += f' · V1.0 {rng(s1, e1)}'
        else:
            c0, c1 = max(iso(s1), T0), min(iso(e1), T1)
            svg.append(f'<rect x="{X(c0.isoformat()) + 1}" y="{ry + 22}" width="{X(c1.isoformat()) + DAY - X(c0.isoformat()) - 2}" height="5" rx="1.5" class="v1"/>')
            info += f' · V1.0 {rng(s1, e1)}'
    tx = end + 6
    if tx + 300 > width:
        txt.append(f'<text x="{X(v["from"]) - 6 if "from" in v else end - 24}" y="{ry + 18}" class="bl" text-anchor="end">{html.escape(info)}</text>')
    else:
        txt.append(f'<text x="{tx}" y="{ry + 18}" class="bl">{html.escape(info)}</text>')

marks = [(D['today'], f'Chốt V2.0 ({dm(D["today"])})', 0), ('2026-11-29', 'Mốc sẵn sàng (29/11)', 1), ('2026-12-07', 'Final demo & viva (07/12)', 0)]
for d, t, k in marks:
    x = X(d) + DAY / 2
    bg.append(f'<line x1="{x}" y1="{TOP}" x2="{x}" y2="{bottom + 4 + 14 * k}" class="mk"/>')
    txt.append(f'<text x="{x}" y="{bottom + 17 + 14 * k}" class="mkt">{t}</text>')
legend = (f'<div class="lg" style="top:{bottom + 44}px"><i class="bar"></i>V2.0 khoảng ngày <i class="crit"></i>chuỗi găng theo lịch rút gọn '
          '<i class="v1"></i>V1.0 (25/10) <i class="actual"></i>thực tế đã chạy (TV2) <i class="ham"></i>hammock '
          '<b>◇</b> hạn (chưa có ngày bắt đầu) <b>◆</b> mốc trong một ngày'
          '<span class="note">Ngày V2.0 theo lịch rút gọn (TV1 chốt nội dung 23/11; chủ task xác nhận giờ còn lại sau). Chuỗi găng ở đây lấy từ lich-rut-gon.md, không phải tính CPM lại. '
          'Ngày demo của nhóm do giảng viên xếp, chưa biết; 07/12 là mốc môn học.</span></div>')
page = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{css_base()}
@page {{ size: {width}px {height}px; margin: 0 }}
html,body {{ width:{width}px; height:{height}px }}
.wk0 {{ fill:#eef2f6 }} .wk1 {{ fill:#e1e8ef }} .we {{ fill:#f6f7f9 }} .wl {{ stroke:#c3d1e0; stroke-width:1 }}
.resv {{ fill:#eaf0f6 }} .rsv {{ font-size:11px; fill:var(--mute); text-anchor:middle; font-style:italic }}
.sec {{ fill:#eef2f6 }} .wkt {{ font-size:11.5px; text-anchor:middle; fill:var(--ink); font-weight:600 }}
.dt {{ font-size:10px; text-anchor:middle; fill:var(--mute) }}
.sect {{ font-size:13px; font-weight:700; fill:var(--navy) }} .lbl {{ font-size:12.5px; fill:var(--ink) }} .id {{ font-weight:700; fill:var(--navy) }}
.bl {{ font-size:11px; fill:var(--mute); paint-order:stroke; stroke:#fff; stroke-width:3.5px; stroke-linejoin:round }}
.bar {{ fill:#7f9bbb }} .crit {{ fill:var(--crit) }} .v1 {{ fill:#c5ccd3 }} .actual {{ fill:var(--ink) }}
.dueq {{ fill:#fff; stroke:var(--navy); stroke-width:1.8 }} .dueq.crit {{ stroke:var(--crit) }}
polygon.bar {{ fill:var(--navy) }} polygon.crit {{ fill:var(--crit) }}
.ham {{ fill:url(#hatch); stroke:var(--navy); stroke-width:.8 }}
.mk {{ stroke:var(--ink); stroke-width:1.4 }} .mkt {{ font-size:11px; text-anchor:middle; fill:var(--ink); font-weight:600 }}
.lg {{ left:{PAD}px; right:{PAD}px }}
.lg i.bar {{ background:#7f9bbb; border-color:#7f9bbb }} .lg i.crit {{ background:var(--crit); border-color:var(--crit) }}
.lg i.v1 {{ background:#c5ccd3; border-color:#c5ccd3; height:6px }} .lg i.actual {{ background:var(--ink); border-color:var(--ink); height:7px }}
.lg i.ham {{ height:8px; border-color:var(--navy); background:repeating-linear-gradient(45deg,#fff 0 2px,var(--navy) 2px 3.5px) }}
.lg b {{ margin-left:12px; color:var(--ink) }}
</style></head><body><svg width="{width}" height="{height}"><defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#fff"/><rect width="2.2" height="6" fill="#1d3b5c"/></pattern></defs>{"".join(bg)}{"".join(svg)}{"".join(txt)}</svg>{legend}</body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print(OUT, width, height)
