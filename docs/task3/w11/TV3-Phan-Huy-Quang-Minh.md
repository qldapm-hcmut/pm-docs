---
Nội dung: Giao việc W11 (02–08/11) cho TV3
Người nhận: Phan Huy Quang Minh (TV3, Tech Lead)
Phiên bản: 0.3 (02/11: cập nhật theo PR #14 đã merge, PR #15 đang mở)
Giờ đề xuất: 14h (check-in còn lại 3h, đăng nhập demo 2h, review và thông tin CR 4h, hỗ trợ frontend 5h)
Trạng thái: AI hỗ trợ soạn (Claude Code, 01–02/11); TV1 duyệt hướng làm 01/11, đồng ý cập nhật 02/11; số giờ và bước kỹ thuật là đề xuất AI, chờ TV3 duyệt
---

# TV3: W11

Backend A26, A27, A29, A62 đã merge sớm hơn lịch. Check-in CODE, MANUAL và hoàn tác đã merge ở PR #14; backend QR đang ở PR #15. Tuần này ưu tiên chuyển sang giúp cả nhóm có bản demo.

## Đăng nhập demo (2h, làm đầu tuần, A26)

**Mục tiêu:** TV2, TV4 và buổi demo đăng nhập được bằng tài khoản mẫu đủ ba vai trò (ASM-06).

**Các bước:** review cơ chế login mẫu ở nhánh `feature/dev-login-demo`, bảo đảm chỉ dùng cho local và demo, rồi đưa vào; seed Student, Organizer, Admin; ghi cách dùng vào README.

**Hoàn thành khi:** TV2, TV4 đăng nhập được cả ba vai trò.

## Check-in còn lại (3h, A33)

**Mục tiêu:** hoàn tất backend check-in theo `api/openapi.yaml`.

**Các bước:**
1. Xác nhận với TV1 PR #14 được merge có chủ ý, vì comment cuối của PR vẫn ghi "Wrong contract, will close this pr".
2. Nhờ TV5 review PR #15 rồi merge. Đối chiếu kết quả spike A20; token hiện dài khoảng 141 ký tự.
3. Thêm C2 `GET /events/{eventId}/check-ins`, hiện chưa có route.
4. Ghi lịch hoàn thành phần còn lại của A33 trên SCRUM-98. Nếu ưu tiên demo cần giờ thì báo TV1 để dời.

**Hoàn thành khi:** C1 (QR, CODE, MANUAL), C2, C3 qua test tích hợp; lịch đã ghi trên Jira.

## Hỗ trợ frontend (5h)

**Mục tiêu:** giảm tải cho TV4 để có bản demo trước 07/11.

**Các bước:** ở họp đầu tuần, chốt với TV4 màn hình TV3 nhận, ưu tiên 4 hoặc 5 trong file TV4. Mỗi màn hình một PR nhỏ.

**Hoàn thành khi:** màn hình đã nhận được merge và chạy trên bản deploy.

## Review, hỗ trợ và thông tin CR (4h)

1. Review PR frontend và CI của TV4, TV5; trả lời câu hỏi API trong ngày.
2. CR-03: tổng hợp số giờ thực tế của Google OIDC; xác nhận cách demo sau khi review login mẫu.
3. CR-02: chốt effort rà soát tài liệu, test và ảnh hưởng lịch.
4. Sửa `docs/db-schema-and-api-contract.md`: mã Q theo Client Log; ghi 50 sự kiện, 1.000 chỗ là mức thiết kế dư, số chính thức là ASM-02.
5. Log work giờ thật của A25, A26, A27, A29, A62, A33 trên Jira.

**Hoàn thành khi:** CR-02, CR-03 đủ thông tin để TV1 duyệt; không có PR chờ review quá 1 ngày.
