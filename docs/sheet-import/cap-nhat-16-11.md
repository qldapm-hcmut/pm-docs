---
Nội dung: Hướng dẫn dán Sheet master sau rà tiến độ 16/11
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11). Chưa ghi vào Sheet. TV1 duyệt rồi dán, hoặc cho phép AI ghi.
---

# Cập nhật Sheet 16/11

## 1. Dán trực tiếp

| Tab | File | Cách dán |
|---|---|---|
| 2. Weekly Log | `2-weekly-log-W11-W13.tsv` | Dán vào dòng trống đầu tiên cột A (12 dòng) |
| 9. AI Log | `9-ai-log-16-11.tsv` | Dán vào dòng trống đầu tiên; cột "Nhóm đã kiểm tra" TV1 sửa sau khi duyệt |

## 2. Biên bản CP: dòng CP4 (nối thêm, không xóa nội dung cũ)

Ô "Ngày thực tế" nối: `SỬA 16/11: 09/11/2026 (buổi Progress Check đã diễn ra).`

Ô "Kết quả" nối:

> SỬA 16/11: Nhóm 9 không được gọi, không trình bày, không có nhận xét của client (TV1 báo 16/11). Q21 vẫn là cơ sở phạm vi; không có xác nhận nào của thầy về phần demo. Tình trạng thực tế lúc đó: backend đã có code trên main, frontend và CI chưa lên main (xem Weekly Log W12).

Ô "Người duyệt" giữ "Client (giảng viên)" nhưng thêm: `Không có nhận xét; TV1 ghi nhận.`

## 3. Risk Register (chờ TV1 duyệt, không tự dán)

| Mã | Việc | Đề xuất |
|---|---|---|
| R11 | Đã có dòng "đề xuất đóng 08/11" | TV1 duyệt đóng |
| R15 | Ghi "Đang xảy ra (08/11)" | Thêm: "16/11: Progress Check không có nhận xét; demo và viva dồn vào hai tuần cuối; mốc nộp dự kiến 29/11 [TV1 duyệt]"; P, I [TV1 chấm] |
| R23 | Giao diện chưa trên main | Cập nhật: FE chỉ có scaffold trên main; PR #6 đang mở; owner [TV1 chọn] |
| R24 | Backend một người, chưa review chéo | Cập nhật: vẫn gần như chỉ một tác giả backend (PR #28 của tài khoản khác đang mở); owner [TV1 chọn] |
| R25 (mới, đề xuất) | Demo và viva của nhóm có thể sớm hơn mốc 07/12; lịch V1.0 không còn dự trữ | Nhóm: Schedule; owner TV1; P, I [TV1 chấm]; giảm thiểu: lịch rút gọn, mốc sẵn sàng 29/11; dự phòng: cắt Should theo thứ tự đã cam kết |
| R26 (mới, đề xuất) | Kiểm thử chưa có bằng chứng ở cuối W12: không có kết quả trong docs/quality/results/ | Nhóm: Quality; owner TV2; P, I [TV1 chấm]; giảm thiểu: TV2 chạy test API đã merge từ 16/11 |

R25 và R26 do AI đề xuất. Nhóm tự chấm P, I.

## 4. Change Request

- CR-02, CR-03: vẫn chưa duyệt; chờ TV3 gửi effort, lịch, cách demo.
- Đề xuất xem xét CR mới nếu TV1/TV3 xác nhận PR #31 (import sinh viên, admin CLI) nằm ngoài Must V1.0: ghi mô tả, phương án (merge hoặc hoãn), ảnh hưởng effort và lịch. Chưa lập khung vì chưa biết quyết định D4.

## 5. Việc ngoài Sheet

- Time Tracking: các dòng mẫu từ dòng 58 còn trống; hạn thu giờ 19/11.
- Link PR trong Time Tracking trỏ `ticket-system-uni`; repo hiện là `ticket-system-uni-be` và `-fe`. TV1 quyết định có sửa link hay ghi chú đổi tên (không xóa lịch sử).
