# Hình cho báo cáo (kiến trúc, PBS, PFD, mạng activity, Gantt V1.0 và V2.0)

Mỗi hình là một file HTML/SVG độc lập (nhúng sẵn `style.css`), chụp thành PNG độ nét cao bằng Playwright (Chromium). Kiểu chung nằm ở `style.css`: nền trắng, một màu nhấn xanh navy, đỏ chỉ cho đường găng, phân biệt loại phần tử bằng độ đậm nền và nét đứt để in đen trắng vẫn đọc được. Làm lại ngày 23/11/2026 (AI hỗ trợ, TV1 duyệt kiểu); bản trước (PDF, TikZ) lưu ở `_archive/figures-truoc-23-11/`.

## Chạy

Cần Python 3 với `openpyxl`, và một Python có gói `playwright` (đặt `PW_PYTHON` nếu khác Python đang chạy). Trình duyệt dùng bản Chromium do Playwright tải (`~/AppData/Local/ms-playwright/chromium-*`) hoặc đặt `PW_CHROME`.

```bash
cd tools/diagrams
PW_PYTHON=<python-có-playwright> python build.py "<master.xlsx>" [thư-mục-ra]   # mặc định ra ./out
```

`build.py` chạy `sched.py` (lịch san tải từ `baseline-v1-a23-25-10.json`), sinh 8 file HTML rồi chụp PNG. Sau đó chép các file `.png` trong thư mục ra vào `report/image/`. `SCALE` đổi độ nét (mặc định 3).

| Hình | Sinh bởi | Dữ liệu |
|---|---|---|
| `architecture` | `arch.py` (nhúng `style.css` vào `architecture.html`, viết tay) | Viết tay theo hiện trạng; nét đứt là phần chưa có |
| `pbs` | `tree.py` | `pbs.json` (khớp `docs/task2/2.1-pbs.md`) |
| `pfd` | `flow.py` | `pfd.json` (toạ độ cm lấy từ bản TikZ cũ) |
| `network-a/b/c` | `network.py` | Tab 10 Sheet master + lịch A21. Ô dạng PDM (ES, thời lượng, EF / LS, float, LF; ngày thứ n kể từ 23/09), đường nối vuông góc chạy trong khe giữa các hàng, mỗi đoạn ngang một làn riêng; đường găng đỏ |
| `gantt` | `gantt.py` | Như trên; Gantt Baseline V1.0; A21, A50 là đã xong, A36, A57 là hammock |
| `gantt-v2` | `gantt_v2.py` | `gantt-v2.json` (ngày V2.0 theo `docs/task3/w13/`, ghi nguồn từng ngày) + khoảng ngày V1.0 từ `sched.py` |

Các script khác: `render.py` xuất PDF vector bằng Chrome/Edge headless (không còn dùng cho báo cáo, giữ để xuất bản in); `shot.py` chụp PNG bằng Playwright.

Sơ đồ trong `docs/task2/` (`2.1-pbs.md`, `2.4-activity-network.md`, `2.11-schedule.md`, `A15_PBS_PFD.md`) dùng cùng các hình, chép vào `docs/task2/img/` (PNG và HTML); Mermaid cũ lưu ở `_archive/figures-truoc-23-11/docs-md/`.

## Kiểm tra dữ liệu sau khi đổi

- Mạng activity, Gantt: xuất văn bản (PDF hoặc HTML) bản cũ và bản mới, so từng activity, ngày, giờ, owner; mạng activity so thêm số nút và số cạnh (21, 22, 16 nút; 27, 28, 21 cạnh) và ES, EF, LS, LF với `sched.py` và tab 10.
- PBS, PFD: nút và cạnh trong JSON phải khớp bản vẽ nguồn (TikZ cũ ở `_archive/`, hoặc `2.1-pbs.md`).

## Lưu ý

- Hình kiến trúc phải sửa tay khi hạ tầng đổi (CI, hosting, email); ghi ngày hiện trạng ở chân hình và để TV3, TV5 duyệt.
- Windows: chạy Python với `-X utf8` hoặc đặt `PYTHONUTF8=1` (đã đặt sẵn trong `build.py`), nếu không `print` tiếng Việt lỗi mã hoá.
- `out/` chứa HTML và PNG vừa dựng; HTML mở thẳng bằng trình duyệt để xem hoặc gửi cho người khác.
