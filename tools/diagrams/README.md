# Hình cho báo cáo (mạng activity, Gantt, kiến trúc)

Vẽ bằng HTML/SVG rồi xuất PDF vector bằng Chrome/Edge headless (cùng engine với Playwright; máy nhóm chưa cài gói `playwright`). AI hỗ trợ viết (Claude Code, 21/10/2026). Kết quả đặt ở `report/image/`.

Cần Python 3, `openpyxl` và Chrome hoặc Edge (đặt biến `CHROME` nếu không ở đường dẫn mặc định).

```bash
cd tools/schedule
python sched.py "<master.xlsx>" 14 baseline-v1-a23-25-10.json ket-qua.json
cd ../diagrams
python network.py "<master.xlsx>" ../schedule/baseline-v1-a23-25-10.json ../schedule/ket-qua.json <thư mục tạm>
python gantt.py   "<master.xlsx>" ../schedule/baseline-v1-a23-25-10.json ../schedule/ket-qua.json <thư mục tạm>/gantt.html
python render.py <thư mục tạm> <thư mục tạm>/network-a.html <thư mục tạm>/network-b.html <thư mục tạm>/network-c.html <thư mục tạm>/gantt.html architecture.html
```

Sau đó chép `network-a.pdf`, `network-b.pdf`, `network-c.pdf`, `gantt.pdf`, `architecture.pdf` vào `report/image/`. `render.py` cũng xuất PNG cùng tên để xem nhanh.

- `network.py`: 3 hình activity-on-node, bố cục từ trên xuống; cạnh dài đi qua điểm trung gian để không chui dưới nút. Tô đỏ đường găng sau san tải (`critical` trong config, thêm A54); nét đứt xanh là cạnh có trong config `pred` nhưng không có ở cột G tab 10 (tức cạnh sửa ở L8–L11). Nhóm nút của từng hình khai báo ở `FIGS`.
- `gantt.py`: Gantt theo ngày bắt đầu/kết thúc sau san tải; A21, A50 vẽ là đã xong 20–21/10; A36, A57 vẽ dải hammock từ 25/10.
- `architecture.html`: sửa tay; nét đứt là phần chưa chốt.
