"""Vẽ PFD (luồng sản phẩm) ra HTML từ pfd.json; toạ độ lấy từ bản TikZ cũ (1 cm = 62 px).
Dùng: python flow.py <file-ra.html>"""
import sys, json, html, pathlib
from common import css as css_base

OUT = sys.argv[1]
D = json.load(open(pathlib.Path(__file__).with_name('pfd.json'), encoding='utf-8'))
SX, W, H, PAD, TOPY = 62, 206, 56, 20, 24


def build(ox):
    pos = {n['id']: (ox + n['x'] * SX, TOPY + H / 2 - n['y'] * SX) for n in D['nodes']}
    paths, pts = [], []
    for e in D['edges']:
        a, b, kind = e[0], e[1], e[2]
        (xa, ya), (xb, yb) = pos[a], pos[b]
        if kind == 'v':
            p = (xa, ya + H / 2, xb, yb - H / 2)
            d = f'M{p[0]:.1f},{p[1]:.1f} L{p[2]:.1f},{p[3] - 1:.1f}'
            pts += [(p[0], p[1]), (p[2], p[3])]
        elif kind == 'o':
            x1, x2 = xa + W / 2, xb + W / 2
            chx, yb2 = x1 + e[3], yb + e[4]
            P = [(x1, ya), (chx, ya), (chx, yb2), (x2 + 1, yb2)]
            d, r = f'M{P[0][0]:.1f},{P[0][1]:.1f}', 10
            for i in range(1, len(P) - 1):
                (px, py), (cx, cy), (nx, ny) = P[i - 1], P[i], P[i + 1]
                l1, l2 = max(abs(cx - px), abs(cy - py)), max(abs(nx - cx), abs(ny - cy))
                ax, ay = cx - r * (cx - px) / l1, cy - r * (cy - py) / l1
                bx, by = cx + r * (nx - cx) / l2, cy + r * (ny - cy) / l2
                d += f' L{ax:.1f},{ay:.1f} Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}'
            d += f' L{P[-1][0]:.1f},{P[-1][1]:.1f}'
            pts += [(x, 0) for x, _ in P]
        else:
            sgn = -1 if kind == 'w' else 1
            x1, x2 = xa + sgn * W / 2, xb + sgn * W / 2
            dist = ((x2 - x1) ** 2 + (yb - ya) ** 2) ** .5
            bz = 0.3915 * e[3] * dist
            c1, c2 = x1 + sgn * bz, x2 + sgn * bz
            d = f'M{x1:.1f},{ya:.1f} C{c1:.1f},{ya:.1f} {c2:.1f},{yb:.1f} {x2 + sgn:.1f},{yb:.1f}'
            for t in [i / 20 for i in range(21)]:
                mt = 1 - t
                pts.append((mt ** 3 * x1 + 3 * mt ** 2 * t * c1 + 3 * mt * t ** 2 * c2 + t ** 3 * x2, 0))
        paths.append(d)
    xs = [p[0] for p in pts] + [v[0] - W / 2 for v in pos.values()] + [v[0] + W / 2 for v in pos.values()]
    return pos, paths, min(xs), max(xs)


pos, paths, lo, hi = build(100)
ox = 100 + PAD - lo
pos, paths, lo, hi = build(ox)
width = round(hi + PAD)
bottom = max(v[1] for v in pos.values()) + H / 2 + PAD
height = round(bottom + 72)

boxes = []
for n in D['nodes']:
    x, y = pos[n['id']]
    cls = 'src' if n['id'] == 'REQ' else n['group']
    boxes.append(f'<div class="n {cls}" style="left:{x - W / 2:.1f}px;top:{y - H / 2:.1f}px;width:{W}px;height:{H}px">'
                 f'<span>{html.escape(n["name"])}</span></div>')
legend = (f'<div class="lg" style="top:{bottom + 6:.0f}px"><i class="src"></i>yêu cầu (S1) <i class="in"></i>thiết kế (S2) '
          '<i class="sw"></i>phần mềm (S3) <i class="qa"></i>kiểm thử và phát hành (S4, S5)'
          '<span class="note">Mũi tên chỉ sản phẩm là đầu vào để tạo ra sản phẩm kế tiếp; đây không phải thứ tự công việc.</span></div>')
page = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{css_base()}
@page {{ size: {width}px {height}px; margin: 0 }}
html,body {{ width:{width}px; height:{height}px }}
.n {{ position:absolute; box-sizing:border-box; border:1.5px solid var(--navy); border-radius:4px; padding:0 10px;
  display:flex; align-items:center; justify-content:center; text-align:center; font-size:14px; line-height:1.25; background:#fff; color:var(--ink) }}
.src {{ background:var(--navy); color:#fff }}
.in {{ background:var(--t2) }}
.sw {{ background:#fff }}
.qa {{ background:var(--t3); border-width:2px }}
.lg {{ left:{PAD}px; right:{PAD}px }}
.lg i.src {{ background:var(--navy) }} .lg i.in {{ background:var(--t2) }} .lg i.sw {{ background:#fff }} .lg i.qa {{ background:var(--t3); border-width:2px }}
path {{ fill:none; stroke:var(--mute); stroke-width:1.4 }}
</style></head><body><svg width="{width}" height="{height}"><defs>
<marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" style="fill:#52606d;stroke:none"/></marker>
</defs>{"".join(f'<path d="{d}" marker-end="url(#a)"/>' for d in paths)}</svg>{"".join(boxes)}{legend}</body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print(OUT, width, height)
