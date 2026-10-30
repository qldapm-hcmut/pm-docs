# Tính lịch (A21) và san tải (A50)

Đọc tab 10 (Activity) và 11 (Estimation) của Sheet master đã export `.xlsx`, tính CPM, san tải theo năng lực từng người và xuất bảng dán Sheet. AI hỗ trợ viết (Claude Code, 20/10/2026); kết quả và cách tính mô tả ở `docs/task2/2.11-schedule.md` và `docs/task2/2.10-resource-plan.md`.

Cần Python 3 và `openpyxl`.

```bash
python sched.py "<đường dẫn>/QLDAPM - L01 - Nhóm 9 - Master.xlsx" 14 baseline-v1.json ket-qua.json
python export.py "<đường dẫn>/QLDAPM - L01 - Nhóm 9 - Master.xlsx" ket-qua.json baseline-v1.json <thư mục ra>
```

- Tham số `14` là giờ/tuần mỗi người.
- `baseline-v1.json` là cấu hình của Baseline V1.0: activity đã xong (`done`), đang làm (`in_progress`), phần giờ chia theo người (`remain`), mốc cố định, các cuộc họp, phụ thuộc đã sửa (L8–L11), chữ ghi ở cột Owner/Ràng buộc, đường găng tô trên Gantt, nhóm giai đoạn cho cost baseline.
- `baseline-v1-a23-25-10.json` (21/10): như `baseline-v1.json`, thêm A21, A50 vào `done`, A23 cố định 25/10 và khóa `not_before` (A20, A58 không bắt đầu trước 22/10). Đây là bản dùng cho `2.11` v0.3 và `10-activity-A23-25-10.tsv`. Khóa `not_before` là tùy chọn; config không có khóa này cho kết quả như cũ (đã kiểm `baseline-v1.json` trước và sau khi thêm: giống hệt).
- `export.py` tạo `10-activity-A21.tsv` (cột A–P tab 10), `tbl-schedule.md`, `gantt.md`, `tbl-load.md`, `tbl-cost.md`.

Khi lịch thay đổi (actual, change event, Baseline V2.0): sao chép `baseline-v1.json` thành file mới, sửa `start`, `done`, `remain`, phụ thuộc, rồi chạy lại. Không sửa file của V1.0.

Giả định của mô hình: giờ rảnh rải đều 7 ngày; effort chia đều cho các owner nếu `remain` không ghi; A36, A57 trừ đều vào năng lực TV1 từ sau A23; họp diễn ra trọn trong một ngày. Sai lệch khoảng 1–2 ngày.
