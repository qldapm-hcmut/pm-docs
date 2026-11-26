"""Vẽ 3 hình mạng activity (activity-on-node, từ trên xuống) ra HTML theo 2.4 v1.0 và lịch A21.
Ô theo dạng PDM: hàng trên ES | thời lượng | EF, hàng dưới LS | float | LF (ngày thứ n kể từ 23/09, ngày 0).
Đường nối vuông góc, chạy trong khe giữa các hàng; mỗi đoạn ngang một làn riêng nên không chồng nhau, không đi qua ô.
Dùng: python network.py <master.xlsx> <config.json> <kết-quả.json> <thư-mục-ra>"""
import sys, html
from common import load, owners, ddmm, num, css as css_base, rounded

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
W, H, GW, GH, DW, GX, PAD = 212, 84, 150, 48, 12, 18, 12
TRK, GAP0 = 8, 24          # bước giữa hai làn ngang; chiều cao khe tối thiểu


def fm(v):
    if v is None or v == '':
        return '–'
    f = float(v)
    return str(int(f)) if f == int(f) else num(f)


def cpm(a):
    if a in RES_:
        x = RES_[a]
        return x['ES'], x['EF'], x['LS'], x['LF'], x['float'], x['dur']
    s = R[a]['cpm']
    return (*s, R[a]['dur'])


def label(a, k):
    name = html.escape(R[a]['name'])
    if k == 'ghost':
        return f'<div class="nm"><b>{a}</b> {name}</div>'
    if k == 'buffer':
        return f'<div class="nm"><b>A38</b> {name}</div><div class="dt">30h quỹ dự phòng · ngoài chuỗi phụ thuộc (L6)</div>'
    es, ef, ls, lf, fl, dur = cpm(a)
    eff = '1h còn lại' if a == 'A25' else (num(R[a]['eff']) + 'h' if R[a]['eff'] else '')
    if k == 'done':
        tail = 'đã xong 20–21/10' if a in ('A21', 'A50') else ('không trình bày (05/10)' if a == 'A49' else 'đã xong')
        det = ' · '.join(t for t in (eff, tail) if t)
    else:
        x = RES_[a]
        d = ddmm(x['start']) if x['start'] == x['end'] else f'{ddmm(x["start"])}–{ddmm(x["end"])}'
        det = f'{eff} · {owners(x)} · {d}' + (' (cố định)' if a in FIXED else '')
    d1 = f'{fm(dur)} ngày' if dur not in (None, '') else '–'
    return (f'<div class="r"><span>ES <b>{fm(es)}</b></span><span>{d1}</span><span>EF <b>{fm(ef)}</b></span></div>'
            f'<div class="nm"><b>{a}</b> {name}</div><div class="dt">{html.escape(det)}</div>'
            f'<div class="r"><span>LS <b>{fm(ls)}</b></span><span>float <b>{fm(fl)}</b></span><span>LF <b>{fm(lf)}</b></span></div>')


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
    size = {a: (GW, GH) if kind(a, fig) == 'ghost' else (W, H) for a in real}
    chains, adj = {}, []
    for p, a in edges:                      # nút trung gian giữ chỗ cho cạnh đi qua nhiều tầng
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
    for it in range(12):                    # giảm giao cắt bằng trọng tâm
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
    xl = {}
    for l, r in rows.items():
        x = (width - widths[l]) / 2
        for n in r:
            xl[n] = x
            x += size[n][0] + GX
    cx = {n: xl[n] + size[n][0] / 2 for n in layer}

    # cổng vào/ra: nhiều cạnh cùng một ô được rải đều trên cạnh dưới/trên, sắp theo vị trí đầu bên kia
    outs, ins = {}, {}
    for (p, a), pts in chains.items():
        outs.setdefault(p, []).append(((p, a), cx[pts[1]]))
        ins.setdefault(a, []).append(((p, a), cx[pts[-2]]))

    def spread(lst, n, shift):
        lst.sort(key=lambda t: t[1])
        return {k: xl[n] + size[n][0] * (i + 1) / (len(lst) + 1) + shift for i, (k, _) in enumerate(lst)}
    oport, iport = {}, {}
    for n, lst in outs.items():
        oport.update(spread(lst, n, -3))
    for n, lst in ins.items():
        iport.update(spread(lst, n, 3))

    # các đoạn ngang trong từng khe, gán làn để không chồng nhau
    jogs = {}
    for (p, a), pts in chains.items():
        for i in range(len(pts) - 1):
            xu = oport[(p, a)] if i == 0 else cx[pts[i]]
            xv = iport[(p, a)] if i == len(pts) - 2 else cx[pts[i + 1]]
            if abs(xu - xv) > .5:
                jogs.setdefault(layer[pts[i]], []).append((min(xu, xv), max(xu, xv), (p, a), i))
    lane, ntr = {}, {}
    for l, js in jogs.items():
        ends = []
        for x1, x2, k, i in sorted(js, key=lambda j: (j[0], j[1])):
            t = next((t for t, e in enumerate(ends) if e < x1 - 6), None)
            if t is None:
                ends.append(x2); t = len(ends) - 1
            else:
                ends[t] = x2
            lane[(k, i)] = t
        ntr[l] = len(ends)

    # toạ độ y: chiều cao hàng theo ô cao nhất, chiều cao khe theo số làn
    top, bot, ytop, y = {}, {}, {}, PAD
    for l in sorted(rows):
        rh = max(size[n][1] for n in rows[l] if '#' not in n) if any('#' not in n for n in rows[l]) else H
        top[l], bot[l] = y, y + rh
        for n in rows[l]:
            ytop[n] = y + (rh - size[n][1]) / 2 if '#' not in n else y
        gap = max(GAP0, 13 + (ntr.get(l, 0) - 1) * TRK + 19) if ntr.get(l) else GAP0
        y += rh + gap
    height = y - gap + PAD
    for b in fig.get('buffer', []):
        size[b] = (W, H)
        xl[b], ytop[b] = width - PAD - W, max(ytop[n] + size[n][1] for n in real) + 26
        height = ytop[b] + H + PAD
    legend_y = height
    height += 92

    svg = {'n': [], 'new': [], 'crit': []}
    for (p, a), pts in chains.items():
        P = [(oport[(p, a)], ytop[p] + size[p][1])]
        for i in range(len(pts) - 1):
            u, v = pts[i], pts[i + 1]
            xu = oport[(p, a)] if i == 0 else cx[u]
            xv = iport[(p, a)] if i == len(pts) - 2 else cx[v]
            if abs(xu - xv) > .5:
                ty = bot[layer[u]] + 13 + lane[((p, a), i)] * TRK
                P += [(xu, ty), (xv, ty)]
            else:
                xv = xu
            if v == a:
                P.append((xv, ytop[a] - 1))
            else:
                P += [(xv, top[layer[v]]), (xv, bot[layer[v]])]
        cls = 'crit' if (p, a) in CRIT_E else ('new' if (p, a) in NEW else 'n')
        svg[cls].append(f'<path class="{cls}" d="{rounded(P)}" marker-end="url(#m{cls})"/>')
    divs = ''.join(f'<div class="n {kind(a, fig)}" style="left:{xl[a]:.1f}px;top:{ytop[a]:.1f}px;width:{size[a][0]}px;'
                   f'height:{size[a][1]}px">{label(a, kind(a, fig))}</div>' for a in real + fig.get('buffer', []))
    sw = [('crit', 'đường găng sau san tải'), ('act', 'activity'), ('done', 'đã xong'), ('ghost', 'thuộc hình khác')]
    if fig.get('buffer'):
        sw.append(('buffer', 'quỹ dự phòng'))
    legend = (f'<div class="lg" style="top:{legend_y}px">' + ''.join(f'<i class="{c}"></i>{t}' for c, t in sw) +
              '<b class="ln"></b>phụ thuộc ' + ('<b class="ln new"></b>cạnh sửa ở L8–L11' if any(e in NEW for e in edges) else '') +
              '<span class="note">Ô: hàng trên ES | thời lượng | EF, hàng dưới LS | float | LF. ES, EF, LS, LF là ngày thứ n kể từ 23/09/2026 (ngày 0); '
              'float theo CPM, âm là trễ so với mốc cố định 09/11 hoặc 07/12.</span>'
              '<span class="note">Ngày dương lịch theo lịch đã san tải (A23 họp 25/10). Ô nét đứt thuộc hình khác.</span></div>')
    css = css_base() + f'''
@page {{ size: {width:.0f}px {height:.0f}px; margin: 0 }}
html,body {{ width:{width:.0f}px; height:{height:.0f}px }}
.n {{ position:absolute; box-sizing:border-box; border:1.5px solid var(--navy); border-radius:4px; background:#fff; color:var(--ink);
  overflow:hidden; display:flex; flex-direction:column; justify-content:space-between }}
.n .r {{ display:flex; justify-content:space-between; font-size:11px; color:var(--mute); padding:0 7px; background:var(--t1); line-height:1.4 }}
.n .r:first-child {{ border-bottom:1px solid var(--t3) }} .n .r:last-child {{ border-top:1px solid var(--t3) }}
.n .r b {{ color:var(--ink) }}
.n .nm {{ font-size:12.5px; line-height:1.22; padding:1px 7px 0; flex:1; overflow:hidden }}
.n .nm b {{ color:var(--navy) }}
.n .dt {{ font-size:10.5px; color:var(--mute); padding:0 7px 1px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis }}
.lg {{ left:{PAD}px; right:{PAD}px }}
.lg b.ln {{ display:inline-block; width:26px; border-top:1.5px solid var(--mute); vertical-align:middle; margin:0 5px 0 14px }}
.lg b.ln.new {{ border-top:2px dashed var(--navy) }}
.crit {{ border:2.5px solid var(--crit); background:var(--critbg) }}
.crit .nm b {{ color:var(--crit) }} .crit .r {{ background:#fbd9d5 }}
.done {{ border-color:var(--grey); background:#f6f7f9; color:var(--mute) }}
.done .nm b {{ color:var(--mute) }} .done .r {{ background:#eceff2 }}
.ghost {{ border:1.4px dashed var(--grey); color:var(--mute); background:#fff; justify-content:center }}
.ghost .nm {{ font-size:11px; flex:none; padding:3px 7px }} .ghost .nm b {{ color:var(--mute) }}
.buffer {{ border:2px dashed var(--navy); background:var(--t2); justify-content:center }}
.buffer .nm {{ flex:none }}
.lg i.ghost {{ border:1.4px dashed var(--grey) }} .lg i.crit {{ border:2.5px solid var(--crit); background:var(--critbg) }}
.lg i.done {{ border-color:var(--grey); background:#f6f7f9 }} .lg i.buffer {{ border:2px dashed var(--navy); background:var(--t2) }}
path {{ fill:none; stroke:var(--mute); stroke-width:1.4 }}
path.new {{ stroke:var(--navy); stroke-width:1.8; stroke-dasharray:6 3 }}
path.crit {{ stroke:var(--crit); stroke-width:2.4 }}'''
    mk = ''.join(f'<marker id="m{i}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">'
                 f'<path d="M0,0 L8,4 L0,8 z" style="fill:{c};stroke:none"/></marker>'
                 for i, c in (('n', '#52606d'), ('crit', '#b42318'), ('new', '#1d3b5c')))
    page = (f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><style>{css}</style></head><body>'
            f'<svg width="{width:.0f}" height="{height:.0f}"><defs>{mk}</defs>{"".join(svg["n"] + svg["new"] + svg["crit"])}</svg>'
            f'{divs}{legend}</body></html>')
    open(f'{OUT}/{key}.html', 'w', encoding='utf-8').write(page)
    print(key, round(width), round(height), 'cạnh sửa L8–L11:', sorted(e for e in edges if e in NEW))


for k, f in FIGS.items():
    build(k, f)
