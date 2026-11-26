"""Dữ liệu chung cho các hình: tab 10 Sheet master, config lịch và kết quả sched.py."""
import json, pathlib, datetime as dt, openpyxl


def css():
    """Nội dung style.css để nhúng vào từng file HTML (mỗi hình là một file độc lập)."""
    return (pathlib.Path(__file__).parent / 'style.css').read_text(encoding='utf-8')


def load(xlsx, config, result):
    ws = openpyxl.load_workbook(xlsx, data_only=True)['10. Activity']
    R = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] and str(r[0]).startswith('A'):
            R[r[0]] = dict(name=r[1], owner=r[3] or '', eff=r[4], dur=r[5], cpm=tuple(r[8:13]),
                           pred=[p.strip() for p in (r[6] or '').split(',') if p.strip()])
    sc = json.load(open(config, encoding='utf-8'))
    res = {x['id']: x for x in json.load(open(result, encoding='utf-8'))['res']}
    pred, new = {}, set()
    for a in R:
        old = R[a]['pred']
        pred[a] = sc['pred'].get(a, old)
        new |= {(p, a) for p in pred[a] if p not in old}
    return R, sc, res, pred, new


def owners(x):
    o = x['owners'].split('/')
    return 'Cả nhóm' if len(o) == 5 else ', '.join(sorted(o))


def ddmm(iso):
    return dt.date.fromisoformat(iso).strftime('%d/%m')


def num(v):
    return ('%.1f' % float(v)).rstrip('0').rstrip('.').replace('.', ',')


def rounded(P, r=7):
    """Đường gấp khúc vuông góc qua các điểm P, bo góc bán kính r; bỏ điểm trùng và điểm thẳng hàng."""
    Q = [P[0]]
    for p in P[1:]:
        if abs(p[0] - Q[-1][0]) > .01 or abs(p[1] - Q[-1][1]) > .01:
            Q.append(p)
    k = [Q[0]]
    for i in range(1, len(Q) - 1):
        (ax, ay), (bx, by), (cx, cy) = Q[i - 1], Q[i], Q[i + 1]
        if not ((ax == bx == cx) or (ay == by == cy)):
            k.append(Q[i])
    k.append(Q[-1])
    d = f'M{k[0][0]:.1f},{k[0][1]:.1f}'
    for i in range(1, len(k) - 1):
        (px, py), (cx, cy), (nx, ny) = k[i - 1], k[i], k[i + 1]
        l1, l2 = abs(cx - px) + abs(cy - py), abs(nx - cx) + abs(ny - cy)
        rr = min(r, l1 / 2, l2 / 2)
        ax, ay = cx - rr * (cx - px) / l1, cy - rr * (cy - py) / l1
        bx, by = cx + rr * (nx - cx) / l2, cy + rr * (ny - cy) / l2
        d += f' L{ax:.1f},{ay:.1f} Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}'
    return d + f' L{k[-1][0]:.1f},{k[-1][1]:.1f}'
