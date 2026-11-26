"""Nhúng style.css vào architecture.html (nguồn viết tay) và ghi HTML độc lập.
Dùng: python arch.py <file-ra.html>"""
import sys, pathlib
from common import css

src = pathlib.Path(__file__).with_name('architecture.html').read_text(encoding='utf-8')
pathlib.Path(sys.argv[1]).write_text(src.replace('/*STYLE*/', css()), encoding='utf-8')
print(sys.argv[1])
