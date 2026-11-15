---
Nội dung: Giao việc W13–W14 (16–29/11) cho TV4
Người nhận: Nguyễn Đắc Nghĩa (TV4, Frontend)
Phiên bản: 0.1
Giờ: do TV4 ước lượng lại trước 20/11 (tham chiếu baseline V1.0: A28 10,5h; A35 14,8h; A37 8,4h chia chung)
Trạng thái: Nháp AI (Claude Code, 16/11); TV1 chốt phạm vi 16/11 (không làm trang quản lý đơn vị, người dùng); bước kỹ thuật là đề xuất AI, chờ TV3, TV5 duyệt
---

# TV4: W13–W14

Giao diện đang nằm ở nhánh `feat/A35-checkin-ui` và PR #6, chưa trên `main` (R23, owner TV4). Mục tiêu: luồng chính chạy từ `main` trước 19/11, rồi kiểm tra từng màn hình với backend thật.

## Task 1: Xác nhận hiện trạng (hạn 17/11)

**Mục tiêu:** biết chính xác phần nào đã xong, phần nào còn thiếu.

**Đầu vào:** repo `ticket-system-uni-fe`: PR #1 (scaffold, đã vào `main`); PR #2–#5 (02/11: đăng nhập, sự kiện, đăng ký, check-in) merge vào nhánh xếp chồng, chưa vào `main`; PR #6 (12/11) tích hợp luồng, thêm Dockerfile, `nginx.conf`, xuất đăng ký.

**Các bước:** so sánh `main` với nhánh PR #6 và `feat/A35-checkin-ui`; xác nhận tài khoản `InterValiCanis` là của bạn hay không; báo trên chat: phần đã xong, phần dở, phần ở máy riêng chưa đẩy.

**Đầu ra:** tin nhắn hiện trạng; Jira A28, A35 cập nhật theo thực tế.

**Hoàn thành khi:** TV1 và TV5 biết PR #6 có chạy được hay chưa.

## Task 2: Đưa PR #6 vào `main` (hạn 19/11)

**Các bước:** cùng TV5 (tác giả PR #6) và TV3 (review) xử lý nhận xét; `npm install`, `npm run build` phải qua; đóng các PR xếp chồng không còn dùng, để lịch sử rõ. Mô tả PR nêu màn hình đã thử và với backend nào.

**Hoàn thành khi:** PR #6 merge vào `main`, `main` build được. (Theo quy tắc nhóm: review của người khác tác giả.)

**Phụ thuộc:** TV5, TV3.

## Task 3: Kiểm tra từng màn hình với backend thật (A35, A37; 19–24/11)

**Mục tiêu:** các màn hình có trong PR #6 chạy đúng với API thật, không chỉ build được.

| Màn hình | API chính | Mã test (TV2) |
|---|---|---|
| Đăng nhập, thông tin tài khoản | `/auth/google`, `/auth/refresh`, `/me` | T-AUTH-01..03 |
| Danh sách, chi tiết sự kiện | `/events`, `/events/{id}` | T-EV |
| Organizer tạo, sửa, gửi duyệt | `/manage/events`, `/events/{id}/submit` | T-EV-01..05 |
| Admin duyệt, từ chối | `/approvals/pending`, `/events/{id}/approve`, `/events/{id}/reject` | T-AUTH-04 |
| Đăng ký, hủy, "Đăng ký của tôi" và QR | `/events/{id}/registrations`, `/registrations/{id}/cancel`, `/me/registrations` | T-REG, T-WL |
| Check-in (QR, mã, thủ công), danh sách | `/registrations/{id}/check-in`, `/events/{id}/check-ins` | T-CI, T-UI-01 |
| Thống kê và xuất CSV | `/events/{id}/reports/summary`, `/events/{id}/exports/{kind}` | T-RP |

**Các bước:** chạy từng luồng với backend local (hướng dẫn TV3); ghi lỗi giao diện vào `docs/quality/defects.md` hoặc cho TV2; sửa lỗi bằng PR nhỏ. Không làm trang quản lý đơn vị, người dùng (đã chốt không làm).

**Hoàn thành khi:** luồng chính chạy từ đăng nhập đến báo cáo trên giao diện, lỗi còn lại có trong danh sách lỗi.

## Task 4: Điện thoại (R21, T-UI-01)

Thử màn hình check-in và "Đăng ký của tôi" trên điện thoại thật, màn hình nhỏ. **Cần xác minh:** camera quét QR trên trình duyệt thường chỉ cho dùng khi trang chạy trên HTTPS hoặc `localhost`. Nếu mở bằng địa chỉ mạng LAN (http) thì có thể không bật được camera; chọn cách demo (ví dụ nhập mã hoặc xác nhận thủ công làm dự phòng, hoặc dùng HTTPS) cùng TV5, và ghi kết quả thật.

**Hoàn thành khi:** có kết quả thử trên điện thoại (ảnh hoặc ghi chú), kể cả khi không bật được camera.

## Giờ thực tế và hồ sơ

Điền giờ thực tế 22/10–15/11 vào tab 3 trước 19/11 (A28 và giao diện; ngày commit 02/11 không chắc là ngày làm, ghi theo thực tế). Log work Jira từ 16/11. Tham gia A39 regression cùng TV2 (23–24/11); phần cá nhân cuối báo cáo bạn tự viết.
