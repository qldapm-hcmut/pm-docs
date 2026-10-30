"""CPM (A21) và san tải theo năng lực từng người (A50) từ tab 10 Sheet master.
Dùng: python sched.py <master.xlsx> <giờ/tuần> <config.json> <kết-quả.json>"""
import sys, json, math, datetime as dt, openpyxl

sys.stdout.reconfigure(encoding='utf-8')
XLSX, CAP, SC, OUT = sys.argv[1], float(sys.argv[2]), json.load(open(sys.argv[3], encoding='utf-8')), sys.argv[4]
P0, T0 = dt.date(2026, 9, 23), dt.date.fromisoformat(SC['start'])
OFF = (T0 - P0).days
ALL = ['TV1', 'TV2', 'TV3', 'TV4', 'TV5']
BG = {'A36', 'A57'}


def d(s): return (dt.date(T0.year, int(s[3:5]), int(s[0:2])) - T0).days
def ds(i): return T0 + dt.timedelta(days=i)
def week(i): return (ds(i) - dt.date(2026, 8, 24)).days // 7 + 1


ws = openpyxl.load_workbook(XLSX, data_only=True)['10. Activity']
R = {}
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[0] and str(r[0]).startswith('A'):
        R[r[0]] = dict(name=r[1], owner=r[3] or '', eff=float(r[4] or 0),
                       pred=[p.strip() for p in (r[6] or '').split(',') if p.strip()])
for a, p in SC['pred'].items():
    R[a]['pred'] = p
DONE, FIXED, PRE, MEET = set(SC['done']), {a: d(v) for a, v in SC['fixed'].items()}, set(SC['pre_baseline']), set(SC['meetings'])
NB = {a: d(v) for a, v in SC.get('not_before', {}).items()}
acts = [a for a in R if a not in DONE and a not in BG and a != 'A38']


def owners(a):
    o = R[a]['owner']
    return ALL if 'cả nhóm' in o.lower() else [t for t in ALL if t in o.split('(')[0]]


need = {a: dict(SC['remain'][a]) if a in SC['remain'] else {p: R[a]['eff'] / len(owners(a)) for p in owners(a)} for a in acts}
pred = {a: [p for p in R[a]['pred'] if p in acts] for a in acts}
succ = {a: [b for b in acts if a in pred[b]] for a in acts}
daily = CAP / 7
bg = sum(R[a]['eff'] for a in BG) / (d('07/12') - d('31/10'))


def cap(p, a): return daily - (bg if p == 'TV1' and a not in PRE else 0)


dur = {a: 1 if a in FIXED or a in MEET else max(1, math.ceil(max(h / cap(p, a) for p, h in need[a].items()) - 1e-9)) for a in acts}

order, seen = [], set()
def visit(a):
    if a not in seen:
        for p in pred[a]:
            visit(p)
        seen.add(a)
        order.append(a)
for a in acts:
    visit(a)
ES, EF, LS, LF = {}, {}, {}, {}
for a in order:
    ES[a] = FIXED[a] if a in FIXED else max([EF[p] for p in pred[a]] + [NB.get(a, 0)])
    EF[a] = ES[a] + dur[a]
for a in reversed(order):
    LF[a] = FIXED[a] + 1 if a in FIXED else min([LS[s] for s in succ[a]] + [d('07/12') + 1])
    LS[a] = LF[a] - dur[a]

left = {a: dict(need[a]) for a in acts}
st, fin, load = {}, {}, {p: {} for p in ALL}
for day in range(150):
    if len(fin) == len(acts):
        break
    c = {p: daily for p in ALL}
    if 'A23' in fin and day >= fin['A23']:
        c['TV1'] -= bg
        load['TV1'][week(day)] = load['TV1'].get(week(day), 0) + bg
    ready = sorted([a for a in acts if a not in fin and (day == FIXED[a] if a in FIXED else day >= NB.get(a, 0) and all(p in fin and fin[p] <= day for p in pred[a]))],
                   key=lambda a: (LS[a], a))
    today = []
    for a in ready:
        if a in FIXED or a in MEET:
            for p in left[a]:
                load[p][week(day)] = load[p].get(week(day), 0) + left[a][p]
                left[a][p] = 0
        for p in left[a]:
            u = min(c[p], left[a][p])
            if u > 1e-9:
                left[a][p] -= u
                c[p] -= u
                st.setdefault(a, day)
                load[p][week(day)] = load[p].get(week(day), 0) + u
        if all(v < 1e-6 for v in left[a].values()):
            st.setdefault(a, day)
            today.append(a)
    for a in today:
        fin[a] = day + 1

res = []
for a in sorted(acts, key=lambda a: (st[a], a)):
    res.append(dict(id=a, name=R[a]['name'], dur=dur[a], ES=ES[a] + OFF, EF=EF[a] + OFF, LS=LS[a] + OFF, LF=LF[a] + OFF,
                    float=LS[a] - ES[a], start=ds(st[a]).isoformat(), end=ds(fin[a] - 1).isoformat(), week=week(st[a]),
                    eff=round(sum(need[a].values()), 1), owners='/'.join(need[a])))
    x = res[-1]
    print(f"{a:4} {x['owners']:20} {x['eff']:5}h d{dur[a]:<3} float {x['float']:4} | {ds(st[a]):%d/%m} → {ds(fin[a] - 1):%d/%m}  {R[a]['name']}")
for p in ALL:
    print(p, {w: round(v, 1) for w, v in sorted(load[p].items())})
json.dump(dict(res=res, load={p: {str(w): round(v, 2) for w, v in load[p].items()} for p in ALL}, bg=bg, daily=daily),
          open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
