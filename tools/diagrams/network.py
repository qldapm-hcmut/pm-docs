"""Vẽ 3 hình mạng activity (activity-on-node, từ trên xuống) ra HTML theo 2.4 v1.0 và lịch A21.
Dùng: python network.py <master.xlsx> <config.json> <kết-quả.json> <thư-mục-ra>"""
import sys, html
from common import load, owners, ddmm, num

XLSX, CFG, RES, OUT = sys.argv[1:5]
R, SC, RES_, PRED, NEW = load(XLSX, CFG, RES)
CHAIN = SC['critical'] + ['A54']
CRIT_E = set(zip(CHAIN, CHAIN[1:]))
FIXED, DONE = set(SC['fixed']), set(SC['done'])

FIGS = {
    'network-a': dict(nodes=['A49', 'A11', 'A15', 'A12', 'A17', 'A16', 'A18', 'A19', 'A22', 'A25', 'A21',
                             'A20', 'A50', 'A58', 'A23'],
                      ghost_in=[], ghost_out=['A24', 'A28', 'A31', 'A27', 'A33', 'A34']),
    'network-b': dict(nodes=['A24', 'A28', 'A31', 'A26', 'A27', 'A29', 'A62', 'A30', 'A32', 'A33', 'A35',
                             'A34', 'A40', 'A37', 'A51'],
                      ghost_in=['A25', 'A23', 'A20'], ghost_out=['A39', 'A42', 'A43', 'A45']),
    'network-c': dict(nodes=['A39', 'A53', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A54'],
                      ghost_in=['A37', 'A40', 'A34', 'A51', 'A30'], ghost_out=[], buffer=['A38']),
}
W, H, GW, GH, DW, GX, GY, PAD = 192, 76, 124, 46, 12, 18, 34, 16


def label(a, k):
    name = html.escape(R[a]['name'])
    if k == 'ghost':
        return f'<b>{a}</b> {name}'
    if k == 'buffer':
        return f'<b>A38</b> {name}<br><span>30h quỹ dự phòng · ngoài chuỗi phụ thuộc (L6)</span>'
    if k == 'done':
        tail = 'đã xong 20–21/10' if a in ('A21', 'A50') else ('không trình bày (05/10)' if a == 'A49' else 'đã xong')
        eff = f'{num(R[a]["eff"])}h · ' if R[a]['eff'] else ''
        return f'<b>{a}</b> {name}<br><span>{eff}{tail}</span>'
    x = RES_[a]
    d = ddmm(x['start']) if x['start'] == x['end'] else f'{ddmm(x["start"])}–{ddmm(x["end"])}'
    eff = '1h còn lại' if a == 'A25' else num(R[a]['eff']) + 'h'
    fx = ' (cố định)' if a in FIXED else ''
    return (f'<b>{a}</b> {name}<br><span>{eff} · {x["dur"]} ngày · {d}{fx}</span>'
            f'<br><span>{owners(x)} · float {x["float"]}</span>')


def kind(a, fig):
    if a in fig.get('buffer', []):
        return 'buffer'
    if a in fig['ghost_in'] or a in fig['ghost_out']:
        return 'ghost'
    if a in DONE:
        return 'done'
    return 'crit' if a in CHAIN else 'act'


def build(key, fig):
    real = fig['ghost_in'] + fig['nodes'] + fig['ghost_out']
    S, core = set(real), set(fig['nodes'])
    edges = [(p, a) for a in real for p in PRED[a]
             if p in S and (p in core or a in core) and p not in fig['ghost_out'] and a not in fig['ghost_in']]
    layer = {}
    def lay(a):
        if a not in layer:
            ps = [p for p, b in edges if b == a]
            layer[a] = 0 if not ps else 1 + max(lay(p) for p in ps)
        return layer[a]
    for a in real:
        lay(a)
    last = max(layer[n] for n in core) + 1
    for a in fig['ghost_out']:
        layer[a] = last
    # điểm trung gian cho cạnh đi qua nhiều tầng
    size = {a: (GW, GH) if kind(a, fig) == 'ghost' else (W, H) for a in real}
    chains, adj = {}, []
    for p, a in edges:
        pts, prev = [p], p
        for l in range(layer[p] + 1, layer[a]):
            dm = f'{p}>{a}#{l}'
            layer[dm], size[dm] = l, (DW, H)
            adj.append((prev, dm)); pts.append(dm); prev = dm
        adj.append((prev, a)); pts.append(a)
        chains[(p, a)] = pts
    rows = {}
    for n in layer:
        rows.setdefault(layer[n], []).append(n)
    order = {n: i for r in rows.values() for i, n in enumerate(sorted(r, key=lambda n: (real.index(n) if n in real else 99)))}
    for r in rows.values():
        r.sort(key=order.get)
    for it in range(12):
        seq = sorted(rows) if it % 2 == 0 else sorted(rows, reverse=True)
        for l in seq:
            def bc(n):
                nb = [order[u] for u, v in adj if v == n] if it % 2 == 0 else [order[v] for u, v in adj if u == n]
                return sum(nb) / len(nb) if nb else order[n]
            rows[l].sort(key=lambda n: (bc(n), order[n]))
            for i, n in enumerate(rows[l]):
                order[n] = i
    widths = {l: sum(size[n][0] for n in r) + GX * (len(r) - 1) for l, r in rows.items()}
    width = max(widths.values()) + 2 * PAD
    xy, y = {}, PAD
    for l in sorted(rows):
        x = (width - widths[l]) / 2
        rh = max(size[n][1] for n in rows[l] if not n.count('#')) if any('#' not in n for n in rows[l]) else H
        for n in rows[l]:
            xy[n] = (x, y + (rh - size[n][1]) / 2)
            x += size[n][0] + GX
        y += rh + GY
    height = y - GY + PAD
    for b in fig.get('buffer', []):
        size[b] = (W, H)
        xy[b] = (width - PAD - W, max(v[1] for v in xy.values()))
    legend_y = height
    height += 64
    svg = []
    for (p, a), pts in chains.items():
        P = [(xy[n][0] + size[n][0] / 2, xy[n][1] + size[n][1] / 2) for n in pts]
        P[0] = (P[0][0], xy[p][1] + size[p][1])
        P[-1] = (P[-1][0], xy[a][1] - 7)
        d = f'M{P[0][0]:.1f},{P[0][1]:.1f}'
        for (x1, y1), (x2, y2) in zip(P, P[1:]):
            m = (y2 - y1) / 2
            d += f' C{x1:.1f},{y1 + m:.1f} {x2:.1f},{y2 - m:.1f} {x2:.1f},{y2:.1f}'
        cls = ' '.join(c for c, ok in (('crit', (p, a) in CRIT_E), ('new', (p, a) in NEW)) if ok)
        mk = 'crit' if 'crit' in cls else ('new' if 'new' in cls else 'n')
        svg.append(f'<path class="{cls}" d="{d}" marker-end="url(#m{mk})"/>')
    divs = ''.join(f'<div class="n {kind(a, fig)}" style="left:{xy[a][0]:.1f}px;top:{xy[a][1]:.1f}px;width:{size[a][0]}px;'
                   f'height:{size[a][1]}px">{label(a, kind(a, fig))}</div>' for a in real + fig.get('buffer', []))
    sw = [('crit', 'đường găng sau san tải'), ('act', 'activity'), ('done', 'đã xong'), ('ghost', 'thuộc hình khác')]
    if fig.get('buffer'):
        sw.append(('buffer', 'quỹ dự phòng'))
    legend = (f'<div class="lg" style="top:{legend_y}px">' + ''.join(f'<i class="{c}"></i>{t}' for c, t in sw) +
              '<b class="ln"></b>phụ thuộc <b class="ln new"></b>cạnh sửa ở L8–L11'
              '<br>Ngày theo lịch đã san tải (A23 họp 25/10); float theo CPM, âm là trễ so với mốc cố định 09/11 hoặc 07/12.</div>')
    css = f'''@page {{ size: {width:.0f}px {height:.0f}px; margin: 0 }}
html,body {{ margin:0; width:{width:.0f}px; height:{height:.0f}px; background:#fff; font-family:"Segoe UI",Arial,sans-serif }}
.n {{ position:absolute; box-sizing:border-box; border:1.6px solid #455a64; border-radius:6px; padding:4px 7px;
  font-size:13px; line-height:1.25; background:#fff; color:#1a1a1a; overflow:hidden }}
.n span {{ font-size:11.5px; color:#333 }}
.lg {{ position:absolute; left:{PAD}px; right:{PAD}px; font-size:12px; color:#333; line-height:1.6 }}
.lg i {{ display:inline-block; width:22px; height:12px; vertical-align:middle; margin:0 4px 0 12px; border-radius:3px;
  border:1.6px solid #455a64; background:#fff }}
.lg i:first-child {{ margin-left:0 }}
.lg b.ln {{ display:inline-block; width:26px; border-top:1.6px solid #666; vertical-align:middle; margin:0 4px 0 12px }}
.lg b.ln.new {{ border-top:2px dashed #1565c0 }}
.crit {{ border:2.2px solid #c62828; background:#fdecea }}
.done {{ border-color:#9e9e9e; background:#f1f1f1; color:#555 }}
.ghost {{ border:1.4px dashed #8a8a8a; color:#666; background:#fff; font-size:11.5px; padding:3px 6px }}
.buffer {{ border:1.8px dashed #b8860b; background:#fff8d6 }}
.lg i.ghost {{ border:1.4px dashed #8a8a8a }} .lg i.crit {{ border:2px solid #c62828; background:#fdecea }}
.lg i.done {{ border-color:#9e9e9e; background:#f1f1f1 }} .lg i.buffer {{ border:1.6px dashed #b8860b; background:#fff8d6 }}
svg {{ position:absolute; left:0; top:0 }}
path {{ fill:none; stroke:#666; stroke-width:1.3 }}
path.new {{ stroke:#1565c0; stroke-width:1.8; stroke-dasharray:6 3 }}
path.crit {{ stroke:#c62828; stroke-width:2 }}'''
    mk = ''.join(f'<marker id="m{i}" markerWidth="8" markerHeight="8" refX="1" refY="4" orient="auto">'
                 f'<path d="M0,0 L8,4 L0,8 z" style="fill:{c};stroke:none"/></marker>'
                 for i, c in (('n', '#666'), ('crit', '#c62828'), ('new', '#1565c0')))
    page = (f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{css}</style></head><body>'
            f'<svg width="{width:.0f}" height="{height:.0f}"><defs>{mk}</defs>{"".join(svg)}</svg>{divs}{legend}</body></html>')
    open(f'{OUT}/{key}.html', 'w', encoding='utf-8').write(page)
    print(key, round(width), round(height), 'cạnh sửa L8–L11:', sorted(e for e in edges if e in NEW))


for k, f in FIGS.items():
    build(k, f)
