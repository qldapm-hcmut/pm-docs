---
Nội dung: Giao việc W11 (02–08/11) cho TV4
Người nhận: Nguyễn Đắc Nghĩa (TV4, Frontend)
Phiên bản: 0.2 (02/11: TV3 nhận hỗ trợ frontend; cập nhật theo PR #15)
Giờ đề xuất: 14h, tối đa 16h (A28 6h, giao diện A26, A27, A29 8h)
Trạng thái: AI hỗ trợ soạn (Claude Code, 01–02/11); TV1 duyệt hướng làm 01/11, đồng ý cập nhật 02/11; số giờ và bước kỹ thuật là đề xuất AI, chờ TV3, TV5 duyệt
---

# TV4: W11

Đây là việc quan trọng nhất tuần vì repo chưa có mã frontend. Nếu đã làm ở máy riêng, đẩy lên ngay trong ngày 02/11, kể cả chưa xong, và trừ phần đã làm khỏi giờ đề xuất.

## A28 Layout và component (6h)

**Mục tiêu:** có khung React chạy được và kết nối API.

**Đầu vào:** `api/openapi.yaml`; API base local `http://localhost:3000/api/v1`; tài khoản mẫu từ TV3.

**Các bước:**
1. **[Cần TV3, TV5 quyết]** vị trí mã frontend trong repo và công cụ build.
2. Dựng layout responsive, điều hướng theo vai trò, lớp gọi API, xử lý lỗi.

**Hoàn thành khi:** chạy local và gọi được `GET /me` sau khi đăng nhập.

## Màn hình theo thứ tự ưu tiên (8h)

Làm tuần tự; hết giờ thì dừng và báo TV1, phần còn lại ghi vào kế hoạch 09/11.

| Ưu tiên | Màn hình | API |
|---|---|---|
| 1 | Đăng nhập, thông tin tài khoản | A1, A2, A3, A4 |
| 2 | Danh sách, chi tiết sự kiện | E1, E2 |
| 3 | Organizer tạo, sửa, gửi duyệt | E3, E4, E5, P1 |
| 4 | Admin duyệt, từ chối | P2, P3, P4 |
| 5 | Sinh viên đăng ký, hủy, xem waitlist, "Đăng ký của tôi" | R1, R2, R3 |

**Các bước:** mỗi màn hình một PR nhỏ vào `main`, TV3 review. Thử trên điện thoại (R21). Màn hình quét QR để A35, nhưng chừa chỗ hiển thị QR ở "Đăng ký của tôi"; sau khi PR #15 merge, API trả `qrToken` để frontend tạo ảnh QR.

**Đầu ra:** các màn hình đã merge, chạy trên bản deploy của TV5.

**Hoàn thành khi:** đến 07/11 chạy được từ đăng nhập đến ít nhất ưu tiên 3 trên bản deploy, phần còn lại có tiến độ rõ. Mức này cần xác nhận ở họp đầu tuần.

**Phụ thuộc:** TV3 đăng nhập demo; TV5 deploy. TV3 dự kiến hỗ trợ màn hình ưu tiên 4 hoặc 5, chốt ở họp đầu tuần.

Log work trên Jira cho A28, A26, A27, A29.
