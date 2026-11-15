---
Nội dung: Giao việc W11 (02–08/11) cho TV2
Người nhận: Ngô Thanh Hùng (TV2, Tester)
Giờ đề xuất: 14h (A22 2h, A31 8h, kiểm thử API 4h)
Trạng thái: AI hỗ trợ soạn (Claude Code, 01/11); TV1 duyệt hướng làm 01/11; số giờ là đề xuất AI
---

# TV2: W11

Trên Jira, A22 đang In Progress (hạn 22/10), A31 đang Backlog (hạn 28/10). Nếu đã làm phần nào, đẩy lên ngay, cập nhật trạng thái và log giờ thật; giờ đề xuất dưới đây trừ đi phần đã làm.

## A22 Quality plan (2h)

**Mục tiêu:** chốt quality plan và test strategy.

**Đầu ra:** bản hoàn chỉnh đưa vào `docs/quality/` của repo `pm-docs` qua PR; A22 chuyển Done.

**Hoàn thành khi:** TV1 duyệt.

## A31 Test case Increment 1 (8h)

**Mục tiêu:** có test case cho luồng đã có backend.

**Đầu vào:** `api/openapi.yaml`, `docs/db-schema-and-api-contract.md` của repo `ticket-system-uni`; `docs/quality/test-cases.md` của `pm-docs`.

**Các bước:**
1. Viết test case cho: đăng nhập và phân quyền; tạo, sửa, gửi duyệt, duyệt, từ chối sự kiện; đăng ký, hủy; hết chỗ vào waitlist; tự chuyển người đầu waitlist; đăng ký trùng; hạn hủy 24 giờ.
2. Đổi mã `T-RG` trong file thành `T-REG` theo chuẩn truy vết.
3. Thêm 2 ca check-in (ghi ở A40, TV2 chốt mã): Admin không phải Organizer bị từ chối; Organizer không tự check-in cho đăng ký của mình.

**Hoàn thành khi:** mỗi REQ Must đã có backend có ít nhất một test case; TV3 review xong.

## Kiểm thử API đã merge (4h)

**Mục tiêu:** có kết quả chạy thật làm bằng chứng cho 09/11.

**Các bước:**
1. Chạy bản deploy của TV5, hoặc chạy local theo README repo nếu chưa có deploy.
2. Chạy test case trên API (ví dụ bằng Postman), ghi đạt/không đạt, ngày chạy và người chạy.
3. Lỗi tìm thấy ghi vào `docs/quality/defects.md` và báo TV3.

**Đầu ra:** bảng kết quả trong `docs/quality/`, nộp bản sao vào thư mục W11 trên Drive.

**Hoàn thành khi:** đã chạy hết test case của phần đã merge trước 07/11; kết quả là số liệu thật.

**Phụ thuộc:** TV3 cung cấp cách đăng nhập demo và tài khoản mẫu.
