"""Xuất kết quả sched.py: TSV dán tab 10 (cột A–P), bảng lịch, Gantt mermaid, tải theo tuần, cost baseline.
Dùng: python export.py <master.xlsx> <kết-quả.json> <config.json> <thư-mục-ra>"""
import sys, json, datetime as dt, openpyxl

sys.stdout.reconfigure(encoding='utf-8')
XLSX, J, SC, OUTDIR = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8')), json.load(open(sys.argv[3], encoding='utf-8')), sys.argv[4]
wb = openpyxl.load_workbook(XLSX, data_only=True)
R = {r[0]: r for r in wb['10. Activity'].iter_rows(min_row=2, values_only=True) if r[0] and str(r[0]).startswith('A')}
EST = {r[0] for r in wb['11. Estimation'].iter_rows(min_row=3, values_only=True) if r[0] and r[3] is not None}
OWNER, CONS = SC['owner_text'], SC['constraint_text']
PRED = {a: ', '.join(p) for a, p in SC['pred'].items()}
res = {x['id']: x for x in J['res']}


def f(iso): return dt.date.fromisoformat(iso).strftime('%d/%m')
def owner(a): return OWNER.get(a, R[a][3] or '')
def write(name, lines): open(f'{OUTDIR}/{name}', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')


tsv = ['\t'.join(['ID', 'Activity', 'Task', 'Owner', 'Effort (h)', 'Thời lượng (ngày)', 'Phụ thuộc', 'Ràng buộc', 'ES', 'EF',
                  'LS', 'LF', 'Float', 'Bắt đầu', 'Kết thúc', 'Tuần', 'Cột đã đổi (theo chữ cái tab 10)'])]
a23 = res['A23']
for a, r in R.items():
    pred = PRED.get(a, r[6] or '')
    changed = [c for c, cond in (('D', a in OWNER), ('G', a in PRED), ('H', a in CONS)) if cond]
    if a in res:
        x = res[a]
        row = [a, r[1], r[2], owner(a), r[4], r[5] if a in SC['in_progress'] else x['dur'],
               pred, CONS.get(a, r[7] or ''), x['ES'], x['EF'], x['LS'], x['LF'], x['float'], f(x['start']), f(x['end']), x['week']]
        changed.append('F, I–P')
    elif a in ('A36', 'A57'):
        row = [a, r[1], r[2], owner(a), r[4], (dt.date(2026, 12, 7) - dt.date.fromisoformat(a23['end'])).days, pred,
               'Hammock: chạy nền từ sau A23 đến A54', '', '', '', '', '', f(a23['end']), '07/12', a23['week']]
        changed.append('F, H, N–P; I–M để trống')
    elif a == 'A38':
        row = [a, r[1], r[2], owner(a), r[4], '', '', 'Quỹ dự phòng ngoài chuỗi (L6 = B), dùng giờ dư của TV2–TV5',
               '', '', '', '', '', '', '', '']
        changed.append('H; F, I–P để trống (xóa lịch cũ)')
    else:
        continue
    row.append(', '.join(changed))
    tsv.append('\t'.join('' if v is None else str(v) for v in row))
write('10-activity-A21.tsv', tsv)

md = ['| ID | Activity | Owner | Effort (h) | Thời lượng CPM (ngày) | Bắt đầu | Kết thúc | Float CPM (ngày) |',
      '|---|---|---|---:|---:|---|---|---:|']
md += [f"| {x['id']} | {x['name']} | {owner(x['id'])} | {x['eff']} | {x['dur']} | {f(x['start'])} | {f(x['end'])} | {x['float']} |" for x in J['res']]
write('tbl-schedule.md', md)

g = ['```mermaid', 'gantt', '  title Lịch Baseline V1.0 (đã san tải)', '  dateFormat YYYY-MM-DD', '  axisFormat %d/%m']
for name, ids in SC['gantt_sections']:
    g.append(f'  section {name}')
    for a in ids:
        x = res[a]
        if a in SC['fixed']:
            g.append(f"  {a} {x['name']} :milestone, {a}, {x['start']}, 1d")
        else:
            e = (dt.date.fromisoformat(x['end']) + dt.timedelta(days=1)).isoformat()
            g.append(f"  {a} {x['name']} :{'crit, ' if a in SC['critical'] else ''}{a}, {x['start']}, {e}")
g.append('```')
write('gantt.md', g)

wk = sorted({int(w) for p in J['load'] for w in J['load'][p]})
t = ['| Thành viên | ' + ' | '.join(f'W{w}' for w in wk) + ' | Tổng |', '|---|' + '---:|' * (len(wk) + 1)]
t += [f'| {p} | ' + ' | '.join(f"{v.get(str(w), 0):.1f}" for w in wk) + f" | {sum(v.values()):.1f} |" for p, v in J['load'].items()]
write('tbl-load.md', t)

c, tot = ['| Giai đoạn | Activity | Effort (person-hours) |', '|---|---|---:|'], 0
for n, ids in SC['cost_phases']:
    missing = [i for i in ids if i not in EST]
    assert not missing, missing
    s = sum(float(R[i][4]) for i in ids)
    tot += s
    c.append(f'| {n} | {", ".join(ids)} | {s:.1f} |')
a38 = float(R['A38'][4])
c += [f'| **Cộng effort kế hoạch** | | **{tot:.1f}** |', f'| Quỹ dự phòng A38 (change event, tách riêng) | A38 | {a38:.1f} |',
      f'| **Cost baseline** | | **{tot + a38:.1f}** |']
write('tbl-cost.md', c)
print('\n'.join(c + [''] + t))
