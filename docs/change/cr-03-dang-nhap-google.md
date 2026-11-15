---
Mã: CR-03
Ngày nhận: 01/11/2026
Người yêu cầu: TV1 (phát hiện khi đối chiếu repo code với báo cáo mục 1.2)
Người phân tích: TV1, TV3
Trạng thái: đã duyệt phương án A (TV1, 16/11/2026); effort lấy từ log work TV3
---

# CR-03 — Đăng nhập bằng Google thay cho tài khoản mẫu

AI hỗ trợ soạn; đã bổ sung phản hồi của TV3 (TV1 chuyển 01/11/2026); còn thiếu số giờ thực tế và cách demo, chưa duyệt.

## Mô tả thay đổi và lý do

Q02 và Q10 xác định không tích hợp SSO thật. ASM-06 mô phỏng tài khoản trường bằng tài khoản mẫu và mật khẩu cục bộ.

Repo `ticket-system-uni` đã có xác thực Google OIDC, kiểm tra domain `hcmut.edu.vn` (PR #7, merge 28/10). Nhánh `feature/dev-login-demo` có đăng nhập local cho demo nhưng chưa merge vào `main`.

Lý do chọn Google OIDC: lựa chọn của nhóm để xác minh tài khoản trường, không phải yêu cầu của thầy (TV3).

Nhánh demo: TV3 sẽ review cơ chế login mẫu trước khi đưa vào; cơ chế này chỉ dùng cho local và demo.

Nhóm không hỏi thầy về thay đổi này (TV1 chốt 01/11). Báo cáo phải ghi đây là quyết định của nhóm, không ghi là client đồng ý.

## Phân tích tác động

| Hạng mục | Tác động | Chi tiết |
|---|---|---|
| Requirements / products | Có | Báo cáo 1.2: ASM-06 và câu "không tích hợp SSO thật"; danh sách Exclusions ở 1.4; chỉ sửa khi CR được duyệt |
| Activities (thêm, bỏ, sửa) | [TV3 xác nhận] | |
| Effort (h) | Chưa có số | TV3 chưa tổng hợp số giờ thực tế; lấy từ log work, không ước đoán |
| Resources | [TV3 xác nhận] | |
| Risks | Có | Bản demo phụ thuộc Google; người không có tài khoản `hcmut.edu.vn` không đăng nhập được nếu thiếu tài khoản mẫu |
| Schedule, critical path | [TV3 xác nhận] | |
| Cost | [TV3 xác nhận] | |
| Quality, test | Có | UAT và demo phải chạy được đủ ba vai trò bằng tài khoản mẫu |

## Phương án

| Phương án | Mô tả | Ưu | Nhược | Effort | Ảnh hưởng mốc |
|---|---|---|---|---|---|
| A | Giữ Google OIDC, thêm tài khoản mẫu cho demo | Giữ phần đã làm; demo không phụ thuộc Google | Vượt phần "không làm" đã thống nhất; phải khai báo | [TV3] | [TV3] |
| B | Bỏ Google OIDC, về tài khoản mẫu | Khớp Q02, Q10, ASM-06 | Bỏ phần đã làm; sửa lại xác thực | [TV3] | [TV3] |

## Quyết định

**Phương án chọn:** TV1 định hướng A ngày 01/11; chốt sau khi TV3 review xong cơ chế login mẫu và tổng hợp số giờ.

**SỬA 16/11/2026:** TV1 duyệt phương án A. Đây là quyết định của nhóm, không ghi là client đồng ý. Google OIDC (PR #7, merge 28/10) được làm trước khi có CR; CR này ghi nhận sau. Đăng nhập demo cục bộ nằm ở PR #28 (đang mở, dự kiến merge trước 19/11 sau review chéo). Effort: chưa có, lấy từ log work của TV3, không ước đoán. Báo cáo 1.2 (ASM-06, câu "không tích hợp SSO thật") và Exclusions ở 1.4 sửa theo CR này.

**Lý do:** [TV1 điền]

**Người duyệt và ngày duyệt:** TV1, 16/11/2026

**Có cần Baseline V2.0 không:** Có, đưa vào danh sách thay đổi của Baseline V2.0 (TV1 chốt 16/11).
