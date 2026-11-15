---
Nội dung: Giao việc W13–W14 (16–29/11) cho TV1
Người nhận: Nguyễn Đức Nghĩa (TV1, PM)
Phiên bản: 0.1
Giờ: do TV1 ước lượng lại (tham chiếu baseline V1.0: A45 15,5h; A42 10,3h; A36 24,8h và A57 10,3h chạy nền đến cuối kỳ; A47 2,1h; phần "cả nhóm" A44, A46, A54 chia chung)
Trạng thái: Nháp AI (Claude Code, 16/11); AI hỗ trợ soạn nháp báo cáo và V2.0, TV1 duyệt
---

# TV1: W13–W14

R19: khối lượng quản trị và báo cáo vượt năng lực khoảng 14h/tuần. Giảm bằng nháp có AI hỗ trợ (ghi AI Log), cắt phần không bắt buộc và để thành viên tự viết phần cá nhân.

## Task 1: Thông báo nhóm và đồng bộ Jira (17/11)

**Các bước:** gửi tin nhắn `thong-bao-nhom-16-11.md`; chờ phản hồi 24h; sửa lịch nếu ai báo không khả thi. Jira: dời hạn theo `lich-rut-gon.md`; A51 sang Done sau khi ghi CP4; xóa tay SCRUM-115 đến 119 (sub-task tạo nhầm); A33, A34 sang In Review; log work A36, A51, A57.

**Hoàn thành khi:** cả nhóm đã nhận và phản hồi hoặc hết 24h; Jira khớp lịch mới.

## Task 2: Baseline V2.0 (hạn nội dung 20/11, chốt 22/11)

**Đầu vào:** `baseline-v2-danh-sach-thay-doi.md`; log work (hạn 19/11); CR-01..03; Risk Register.

**Các bước:** thu giờ còn lại từ owner (20/11); điền các mục "TV1 điền"; kiểm lịch sử Overleaf hoặc Drive để lấy V1.0 gần 25/10, không có thì dùng báo cáo 22/10 kèm biên bản A23 và viết câu nguồn ở Phụ lục C; gửi nhóm, chờ 24h; xuất `v2.0.pdf` và `v1.0.pdf` mỗi file một PR riêng; gắn tag `baseline-v1.0`, `baseline-v2.0`.

**Đầu ra:** V2.0 và V1.0 trong `docs/baseline/`, tag, dòng Biên bản CP.

**Hoàn thành khi:** `v2.0.pdf` đã merge, tag đã gắn, Phụ lục C ghi nguồn V1.0 trung thực.

## Task 3: Planned vs actual và log (A42, A36, A57; 20–25/11)

Tổng hợp giờ thực tế (tab 3), so với baseline theo activity và theo tuần; ghi hạn chế dữ liệu (giờ hồi tưởng, I02) thay vì kết luận quá mức. Dòng Weekly Log W13 (CN 22/11), W14 (CN 29/11). Sửa Traceability: REQ-10, REQ-11 theo Q21 và mã T-REG. Cập nhật Risk Register theo tuần.

**Hoàn thành khi:** bảng planned vs actual có ghi chú về độ tin cậy; Weekly Log đến W14.

## Task 4: Báo cáo (A45, 17–28/11)

Làm theo `bao-cao-hoan-thien.md`: Chương 1, 2, 3.2–3.4, 3.6–3.8 (3.6: thầy chưa đưa change event, ghi trung thực), Chương 5, Phụ lục A, B, C, D, F; Chương 4 nháp từ 24/11. Mỗi lần dùng AI soạn phải có dòng AI Log. Phần 4.6 và Phụ lục E mỗi thành viên tự viết; nhắc từng người trước 25/11.

**Hoàn thành khi:** biên dịch được, không còn `\todo` ngoài chỗ ghi trung thực "chưa có"; sơ đồ đọc được.

## Task 5: UAT, tổng duyệt, nộp (A41, A46, A47)

- **A41 (26–27/11, cùng TV2):** chốt có mời thầy hay không; biên bản UAT.
- **A46 (28/11):** tổng duyệt; mỗi người trả lời được về estimate, rủi ro, thay đổi lịch, client, scope.
- **A47 (29/11):** nộp báo cáo PDF, link repo và hướng dẫn chạy, Baseline V1.0 và V2.0, Client Log và weekly logs, khai báo AI.

## Việc nền

- Báo nhóm quyết định quyền Sheet (giữ nguyên) và ghi R20.
- Đưa `v1.0.pdf`, `v2.0.pdf` và tài liệu mới vào `pm-docs` bằng PR riêng; PR #6 là bản cập nhật hiện tại.
- Sửa `.gitignore` của `pm-docs`: `*-PLAN.md` khớp nhầm 2.10, 2.12 trên Windows; đổi thành `PHASE*-PLAN.md`.
- Mục D8 (không gửi email thầy): nếu thầy thông báo ngày demo thì cập nhật ngay lịch và R25.
