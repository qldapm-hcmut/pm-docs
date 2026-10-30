"""Xuất HTML ra PDF vector (và PNG để xem nhanh) bằng Chrome/Edge headless.
Dùng: python render.py <thư-mục-ra-pdf> <file1.html> [file2.html ...]
Đặt biến CHROME nếu trình duyệt không nằm ở đường dẫn mặc định."""
import os, sys, glob, subprocess, pathlib, re

CANDIDATES = [os.environ.get('CHROME', ''),
              r'C:\Program Files\Google\Chrome\Application\chrome.exe',
              r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
              *glob.glob(os.path.expanduser(r'~\AppData\Local\ms-playwright\chromium-*\chrome-win64\chrome.exe')),
              '/usr/bin/google-chrome', '/usr/bin/chromium', '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
CHROME = next(c for c in CANDIDATES if c and os.path.exists(c))
out = pathlib.Path(sys.argv[1]).resolve()
for f in sys.argv[2:]:
    src = pathlib.Path(f).resolve()
    w, h = map(int, re.search(r'size:\s*(\d+)px\s+(\d+)px', src.read_text(encoding='utf-8')).groups())
    common = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={out / ".chrome"}']
    subprocess.run(common + ['--no-pdf-header-footer', f'--print-to-pdf={out / (src.stem + ".pdf")}', src.as_uri()],
                   check=True, capture_output=True)
    subprocess.run(common + [f'--window-size={w},{h}', '--force-device-scale-factor=1',
                             f'--screenshot={out / (src.stem + ".png")}', src.as_uri()], check=True, capture_output=True)
    print(src.stem, w, h)
