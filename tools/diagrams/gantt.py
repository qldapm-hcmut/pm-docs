"""Vẽ Gantt (đã san tải) ra HTML từ kết quả sched.py.
Dùng: python gantt.py <master.xlsx> <config.json> <kết-quả.json> <file-ra.html>"""
import sys, html, datetime as dt
from common import load, owners, num

XLSX, CFG, RES, OUT = sys.argv[1:5]
R, SC, RES_, PRED, NEW = load(XLSX, CFG, RES)
T0, T1 = dt.date(2026, 10, 19), dt.date(2026, 12, 8)
CRIT = set(SC['critical']) | {'A54'}
FIXED = set(SC['fixed'])
DONE_BARS = {'A21': ('2026-10-20', '2026-10-21'), 'A50': ('2026-10-20', '2026-10-21')}
HAM = {'A36': ('2026-10-25', '2026-12-07'), 'A57': ('2026-10-25', '2026-12-07')}
LW, DAY, RH, TOP, PAD = 330, 19, 21, 50, 12
days = (T1 - T0).days
width = PAD * 2 + LW + days * DAY + 120


def X(iso):
    return PAD + LW + (dt.date.fromisoformat(iso) - T0).days * DAY


sections = [list(s) for s in SC['gantt_sections']]
sections[0][1] = ['A21', 'A50'] + [a for a in sections[0][1] if a not in ('A21', 'A50')]
sections.insert(-1, ['Quản lý xuyên suốt (hammock)', ['A36', 'A57']])
rows, y = [], TOP
for name, ids in sections:
    rows.append(('sec', name, y)); y += RH
    for a in ids:
        rows.append(('act', a, y)); y += RH
chart_bottom = y
height = y + 70
svg, txt, bg = [], [], []
for i in range(days):
    d = T0 + dt.timedelta(days=i)
    x = PAD + LW + i * DAY
    if d.weekday() == 0:
        wk = (d - dt.date(2026, 8, 24)).days // 7 + 1
        svg.append(f'<rect x="{x}" y="{TOP - 34}" width="{7 * DAY}" height="16" class="wk{wk % 2}"/>')
        txt.append(f'<text x="{x + 3.5 * DAY}" y="{TOP - 22}" class="wkt">W{wk} · {d:%d/%m}</text>')
        svg.append(f'<line x1="{x}" y1="{TOP - 34}" x2="{x}" y2="{chart_bottom}" class="wl"/>')
    if d.weekday() >= 5:
        bg.append(f'<rect x="{x}" y="{TOP}" width="{DAY}" height="{chart_bottom - TOP}" class="we"/>')
    txt.append(f'<text x="{x + DAY / 2}" y="{TOP - 6}" class="dt">{d.day}</text>')
for kind, v, ry in rows:
    if kind == 'sec':
        bg.insert(0, f'<rect x="{PAD}" y="{ry}" width="{width - 2 * PAD}" height="{RH}" class="sec"/>')
        txt.append(f'<text x="{PAD + 4}" y="{ry + 15}" class="sect">{html.escape(v)}</text>')
        continue
    a = v
    name = html.escape(R[a]['name'])
    if a in DONE_BARS:
        s, e, cls, lab = *DONE_BARS[a], 'done', f'{num(R[a]["eff"])}h · đã xong'
    elif a in HAM:
        s, e, cls, lab = *HAM[a], 'ham', f'{num(R[a]["eff"])}h · TV1, rải đều'
    else:
        x = RES_[a]
        s, e = x['start'], x['end']
        cls = 'crit' if a in CRIT else 'bar'
        eff = '1h còn lại' if a == 'A25' else f'{num(R[a]["eff"])}h'
        lab = f'{eff} · {owners(x)}'
    txt.append(f'<text x="{PAD + 4}" y="{ry + 15}" class="lbl"><tspan class="id">{a}</tspan> {name}</text>')
    x1 = X(s)
    x2 = X(e) + DAY
    if a in FIXED or a in ('A44', 'A46'):
        cx, cy = x1 + DAY / 2, ry + RH / 2
        svg.append(f'<polygon points="{cx},{cy - 8} {cx + 8},{cy} {cx},{cy + 8} {cx - 8},{cy}" class="{cls} ms"/>')
        txt.append(f'<text x="{cx + 12}" y="{ry + 15}" class="bl">{lab}{" · cố định" if a in FIXED else ""}</text>')
    else:
        h = 6 if cls == 'ham' else 13
        svg.append(f'<rect x="{x1 + 1}" y="{ry + (RH - h) / 2}" width="{x2 - x1 - 2}" height="{h}" rx="2" class="{cls}"/>')
        tx = x2 + 4 if x2 + 150 < width else x1 - 4
        anchor = 'start' if tx > x1 else 'end'
        txt.append(f'<text x="{tx}" y="{ry + 15}" class="bl" text-anchor="{anchor}">{lab}</text>')
marks = [('2026-10-25', 'A23 chốt Baseline V1.0', 'mk'), ('2026-11-01', 'CP3 kế hoạch ban đầu', 'old'),
         ('2026-11-09', 'Progress Check', 'mk'), ('2026-11-23', 'CP5 kế hoạch ban đầu', 'old'),
         ('2026-12-07', 'Final demo & viva', 'mk')]
for i, (d, t, c) in enumerate(marks):
    x = X(d) + DAY / 2
    bg.append(f'<line x1="{x}" y1="{TOP}" x2="{x}" y2="{chart_bottom + 6 + 13 * (i % 2)}" class="{c}"/>')
    txt.append(f'<text x="{x}" y="{chart_bottom + 17 + 13 * (i % 2)}" class="{c}t">{t} ({d[8:]}/{d[5:7]})</text>')
legend = (f'<div class="lg" style="top:{chart_bottom + 40}px"><i class="crit"></i>đường găng sau san tải <i class="bar"></i>activity '
          '<i class="done"></i>đã xong <i class="ham"></i>hammock <b>◆</b> họp/mốc trong một ngày · '
          'năng lực 14h/tuần mỗi người, khoảng 2h/ngày; cột nền xám là cuối tuần; A38 (30h) là quỹ dự phòng, không có ngày</div>')
page = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>
@page {{ size: {width}px {height}px; margin: 0 }}
html,body {{ margin:0; width:{width}px; height:{height}px; background:#fff; font-family:"Segoe UI",Arial,sans-serif }}
svg {{ position:absolute; left:0; top:0 }}
.wk0 {{ fill:#e8eef3 }} .wk1 {{ fill:#d6e0e8 }} .we {{ fill:#f4f4f4 }} .wl {{ stroke:#b0bec5; stroke-width:1 }}
.sec {{ fill:#eceff1 }} .wkt {{ font-size:11px; text-anchor:middle; fill:#263238; font-weight:600 }}
.dt {{ font-size:9px; text-anchor:middle; fill:#607d8b }}
.sect {{ font-size:12px; font-weight:700; fill:#263238 }} .lbl {{ font-size:11.5px; fill:#1a1a1a }} .id {{ font-weight:700 }}
.bl {{ font-size:10.5px; fill:#37474f }}
.bar {{ fill:#5b8db8 }} .crit {{ fill:#c62828 }} .done {{ fill:#b0b0b0 }} .ham {{ fill:#8e6bb0 }}
.ms {{ stroke:#fff; stroke-width:1 }}
.mk {{ stroke:#263238; stroke-width:1.4 }} .old {{ stroke:#9e9e9e; stroke-width:1.2; stroke-dasharray:4 3 }}
.mkt, .oldt {{ font-size:10.5px; text-anchor:middle }} .mkt {{ fill:#263238; font-weight:600 }} .oldt {{ fill:#777 }}
.lg {{ position:absolute; left:{PAD}px; right:{PAD}px; font-size:11.5px; color:#333 }}
.lg i {{ display:inline-block; width:22px; height:10px; vertical-align:middle; margin:0 4px 0 10px; border-radius:2px }}
.lg i.bar {{ background:#5b8db8 }} .lg i.crit {{ background:#c62828 }} .lg i.done {{ background:#b0b0b0 }} .lg i.ham {{ background:#8e6bb0; height:5px }}
.lg b {{ margin-left:10px }}
</style></head><body><svg width="{width}" height="{height}">{"".join(bg)}{"".join(svg)}{"".join(txt)}</svg>{legend}</body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print(OUT, width, height)
