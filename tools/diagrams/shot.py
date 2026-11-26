"""Chụp từng file HTML thành PNG độ phân giải cao bằng Playwright (Chromium).
Dùng: python shot.py <thư-mục-ra> <file1.html> [file2.html ...]
Kích thước trang lấy từ khai báo `@page { size: Wpx Hpx }` trong HTML.
Biến PW_CHROME chỉ đến chrome.exe nếu không muốn dùng trình duyệt do Playwright tải; SCALE đổi độ nét (mặc định 3)."""
import os, re, sys, glob, pathlib
from playwright.sync_api import sync_playwright

out = pathlib.Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=True)
scale = float(os.environ.get('SCALE', '3'))
cands = [os.environ.get('PW_CHROME', ''),
         *glob.glob(os.path.expanduser(r'~\AppData\Local\ms-playwright\chromium-*\chrome-win64\chrome.exe'))]
exe = next((c for c in cands if c and os.path.exists(c)), None)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
    for f in sys.argv[2:]:
        src = pathlib.Path(f).resolve()
        w, h = map(int, re.search(r'size:\s*(\d+)px\s+(\d+)px', src.read_text(encoding='utf-8')).groups())
        page = browser.new_page(viewport={'width': w, 'height': h}, device_scale_factor=scale)
        page.goto(src.as_uri())
        page.evaluate('document.fonts.ready')
        page.screenshot(path=str(out / (src.stem + '.png')), clip={'x': 0, 'y': 0, 'width': w, 'height': h})
        page.close()
        print(src.stem, w, h, 'x', scale)
    browser.close()
