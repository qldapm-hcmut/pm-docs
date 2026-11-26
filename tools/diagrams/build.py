"""Dựng cả 8 hình báo cáo: sinh HTML rồi chụp PNG bằng Playwright.
Dùng: python build.py "<master.xlsx>" [thư-mục-ra]    (mặc định ra: ./out)
Cần Python có openpyxl; chụp ảnh dùng PW_PYTHON (python có gói playwright), mặc định cùng python đang chạy.
Sau đó chép các file PNG trong thư-mục-ra vào report/image/."""
import os, sys, subprocess, pathlib

here = pathlib.Path(__file__).parent
xlsx = sys.argv[1]
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else here / 'out').resolve()
out.mkdir(parents=True, exist_ok=True)
sched = here.parent / 'schedule'
cfg, res = sched / 'baseline-v1-a23-25-10.json', out / 'ket-qua.json'
env = {**os.environ, 'PYTHONUTF8': '1'}
py = sys.executable


def run(args, cwd=here, exe=py):
    subprocess.run([exe, *map(str, args)], cwd=cwd, env=env, check=True)


run(['sched.py', xlsx, 14, cfg, res], cwd=sched)
run(['network.py', xlsx, cfg, res, out])
run(['gantt.py', xlsx, cfg, res, out / 'gantt.html'])
run(['gantt_v2.py', xlsx, cfg, res, out / 'gantt-v2.html'])
run(['tree.py', out / 'pbs.html'])
run(['flow.py', out / 'pfd.html'])
run(['arch.py', out / 'architecture.html'])
names = ['architecture', 'pbs', 'pfd', 'network-a', 'network-b', 'network-c', 'gantt', 'gantt-v2']
run(['shot.py', out, *[out / f'{n}.html' for n in names]], exe=os.environ.get('PW_PYTHON', py))
