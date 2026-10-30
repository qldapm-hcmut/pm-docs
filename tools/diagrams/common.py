"""Dữ liệu chung cho các hình: tab 10 Sheet master, config lịch và kết quả sched.py."""
import json, datetime as dt, openpyxl


def load(xlsx, config, result):
    ws = openpyxl.load_workbook(xlsx, data_only=True)['10. Activity']
    R = {}
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] and str(r[0]).startswith('A'):
            R[r[0]] = dict(name=r[1], owner=r[3] or '', eff=r[4],
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
