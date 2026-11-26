"""Vẽ PBS (cây phân rã sản phẩm, từ trái sang phải) ra HTML từ pbs.json.
Dùng: python tree.py <file-ra.html>"""
import sys, json, html, pathlib
from common import css as css_base

OUT = sys.argv[1]
D = json.load(open(pathlib.Path(__file__).with_name('pbs.json'), encoding='utf-8'))
N = {n['id']: n for n in D['nodes']}
kids = {}
for n in D['nodes']:
    if n['parent']:
        kids.setdefault(n['parent'], []).append(n['id'])

COLX, COLW = [16, 238, 460, 770], [190, 190, 270, 300]
NH, NH0, PITCH, GAP, TOP, PAD = 42, 74, 52, 14, 16, 16


def depth(i):
    return 0 if N[i]['parent'] is None else 1 + depth(N[i]['parent'])


y, row = {}, [TOP]


def place(i):
    ks = kids.get(i, [])
    if not ks:
        y[i] = row[0] + NH / 2
        row[0] += PITCH
    else:
        for k in ks:
            place(k)
        y[i] = (y[ks[0]] + y[ks[-1]]) / 2
    if depth(i) == 1 or (depth(i) == 2 and N[i]['parent'] == 'S'):
        row[0] += GAP


place('P0')
bottom = row[0] - PITCH - GAP + NH + PAD
height = bottom + 72
width = COLX[3] + COLW[3] + PAD

paths, boxes = [], []
for i, n in N.items():
    d = depth(i)
    h = NH0 if d == 0 else NH
    boxes.append(f'<div class="n d{d}" style="left:{COLX[d]}px;top:{y[i] - h / 2:.1f}px;width:{COLW[d]}px;height:{h}px">'
                 f'<span><b>{i}</b> {html.escape(n["name"])}</span></div>')
    if n['parent']:
        p = n['parent']
        dp = depth(p)
        xp, xc = COLX[dp] + COLW[dp], COLX[d]
        xm = xp + (xc - xp) / 2
        paths.append(f'<path d="M{xp},{y[p]:.1f} H{xm:.1f} V{y[i]:.1f} H{xc - 1}" marker-end="url(#a)"/>')

legend = (f'<div class="lg" style="top:{bottom + 6}px"><i class="d1"></i>nhóm sản phẩm <i class="d2"></i>nhóm con hoặc sản phẩm '
          '<i class="d3"></i>sản phẩm con'
          '<span class="note">M: sản phẩm quản lý; S: sản phẩm kỹ thuật. Mã M/S là mã sản phẩm chính thức của dự án (TV1 chốt 20/10).</span></div>')
page = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{css_base()}
@page {{ size: {width}px {height:.0f}px; margin: 0 }}
html,body {{ width:{width}px; height:{height:.0f}px }}
.n {{ position:absolute; box-sizing:border-box; border:1.5px solid var(--navy); border-radius:4px; padding:0 10px;
  display:flex; align-items:center; font-size:14px; line-height:1.25; background:#fff; color:var(--ink) }}
.n b {{ color:var(--navy) }}
.d0 {{ background:var(--navy); color:#fff; font-size:15px }} .d0 b {{ color:#fff }}
.d1 {{ background:var(--t3); border-width:2px }}
.d2 {{ background:var(--t1) }}
.d3 {{ background:#fff }}
.lg {{ left:{PAD}px; right:{PAD}px }}
.lg i.d1 {{ background:var(--t3); border-width:2px }} .lg i.d2 {{ background:var(--t1) }} .lg i.d3 {{ background:#fff }}
path {{ fill:none; stroke:var(--mute); stroke-width:1.4 }}
</style></head><body><svg width="{width}" height="{height:.0f}"><defs>
<marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" style="fill:#52606d;stroke:none"/></marker>
</defs>{"".join(paths)}</svg>{"".join(boxes)}{legend}</body></html>'''
open(OUT, 'w', encoding='utf-8').write(page)
print(OUT, width, round(height))
