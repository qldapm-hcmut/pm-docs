---
Nội dung: Giao việc W13–W14 (16–29/11) cho TV3
Người nhận: Phan Huy Quang Minh (TV3, Tech Lead, Backend)
Phiên bản: 0.1
Giờ: do TV3 ước lượng lại trước 20/11 (tham chiếu baseline V1.0 cho phần còn mở: A37 8,4h; A53 12,6h chia chung)
Trạng thái: Nháp AI (Claude Code, 16/11); TV1 chốt phạm vi 16/11; **bước kỹ thuật là đề xuất AI, chờ TV3 duyệt**
---

# TV3: W13–W14

Backend đã vượt kế hoạch. Mục tiêu hai tuần này: cho TV2 và cả nhóm môi trường kiểm thử chạy được, kiểm chứng luồng thật, sửa lỗi và có bằng chứng review chéo (R24).

## Task 1: Môi trường test cho TV2 (hạn 17/11)

**Mục tiêu:** TV2 chạy được API local và đăng nhập ba vai trò.

**Đầu vào:** README, `Makefile`, `.env.example`, `db/seed/seed.sql` của repo backend.

**Các bước:**
1. Viết hướng dẫn ngắn (README hoặc tin nhắn) cho TV2: `.env` (`DATABASE_URL`, `GOOGLE_CLIENT_ID`, `JWT_SECRET`, `QR_HMAC_SECRET`; sinh khóa bằng `openssl rand -hex 32` hai lần), `make db-up`, `make migrate-up`, `make seed ADMIN_EMAIL=<email>`, `make run`, `make worker`.
2. Gửi tài khoản hoặc token mẫu cho Student, Organizer, Admin (sau khi PR #28 merge; trước đó nêu cách tạm). Chỉ dùng cho local và demo.
3. Trả lời câu hỏi API của TV2 trong ngày.

**Đầu ra:** hướng dẫn gửi TV2; README cập nhật tên repo mới (`ticket-system-uni-be`, `ticket-system-uni-fe`).

**Hoàn thành khi:** TV2 gọi được `/me` bằng ba vai trò.

## Task 2: Review chéo PR #28 và PR #6 (hạn 19/11)

**Mục tiêu:** hai PR có review thật của người khác tác giả rồi merge.

**Các bước:** TV5 rebase PR #28 lên `main` (đang xung đột sau PR #30); bạn review code và chạy `make lint test`, `make test-int` nếu có `TEST_DATABASE_URL`; review PR #6 (frontend) ở phần gọi API và xử lý lỗi theo mã lỗi OpenAPI. Ghi nhận xét trên PR, không chỉ "LGTM".

**Hoàn thành khi:** cả hai PR có approve của người khác tác giả và đã merge, hoặc ghi lý do hoãn.

**Phụ thuộc:** TV5 rebase; TV4 xác nhận PR #6.

## Task 3: Kiểm chứng end-to-end (A33, A34, hạn 20–22/11)

**Mục tiêu:** xác nhận luồng thật chạy được, để Jira và test không chỉ dựa trên "đã merge".

**Các bước:** chạy kịch bản: tạo sự kiện → gửi duyệt → Admin duyệt → đăng ký đến đầy → vào waitlist → hủy → tự chuyển người đầu waitlist → check-in bằng QR, mã, thủ công (`/registrations/{id}/check-in`) → `reports/summary` và xuất CSV. Với QR trên điện thoại, làm cùng TV5 (R04). Ghi kết quả từng bước.

**Đầu ra:** tin nhắn hoặc file xác nhận cho TV1, TV2 (bước nào chạy, bước nào lỗi).

**Hoàn thành khi:** kịch bản chạy hết hoặc ghi rõ bước lỗi; Jira A33, A34 chuyển trạng thái theo kết quả TV2 (Done chỉ khi có kết quả test).

## Task 4: Sửa lỗi (A53, 24–26/11)

Nhận danh sách lỗi từ TV2 (`docs/quality/defects.md`); mỗi lỗi một PR nhỏ, có review. Không thêm tính năng sau 24/11.

## Task 5: Thông tin CR, PR #31, bảo vệ nhánh

- **CR-02, CR-03:** đã duyệt phương án A (16/11). Điền giờ thực tế phần liên quan vào Time Tracking trước 19/11 để TV1 lấy effort từ log work.
- **PR #31 (import, admin CLI, email):** hoãn. Giữ mở. Sau 24/11, nếu còn giờ và TV1 đồng ý, tách thành PR nhỏ để review; nếu merge thì phải lập CR.
- **Branch protection:** bật cho `main` hai repo (chủ repo), yêu cầu 1 review trước merge; nếu không phải chủ repo, báo TV1 người có quyền.
- **Báo cáo:** TV1 viết phần hiện thực; bạn cung cấp một trang tóm tắt kiến trúc, stack, các module đã làm, ví dụ endpoint, và duyệt đoạn TV1 viết trong 24h.

**Giờ thực tế:** điền tab 3 Sheet cho các dòng "[TV3 chọn]" và PR #23–#30 trước 19/11; log work Jira từ 16/11.
