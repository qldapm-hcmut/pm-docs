---
Activity: A36
Chủ sở hữu: TV1
Trạng thái: đang cập nhật
---

# Issue log

Issue là sự việc **đã xảy ra** (khác rủi ro là sự việc có thể xảy ra).

| ID | Ngày phát hiện | Mô tả | Ảnh hưởng (activity, mốc) | Người xử lý | Hành động | Ngày đóng | Rủi ro liên quan |
|---|---|---|---|---|---|---|---|
| I01 | 2026-10-02 | Milestone 1 là buổi trình bày trên lớp thứ Hai 05/10, không phải hạn nộp 11/10 như nhóm đã hiểu. Thời gian còn lại giảm từ 9 ngày xuống 3 ngày. | Toàn bộ chuỗi Task 1 → M1; A15–A22 | TV1 | Thu hẹp nội dung M1 theo bảng milestone của đề: chỉ Initiation & Definition (client consultation, evaluation, objectives, stakeholders, infrastructure, lifecycle); ước lượng effort thuộc Milestone 2. Thêm A61 (dựng khung slide) và A59 (điền slide, tập trình bày). Dời toàn bộ Task 2 (PBS, PD, PFD, activity network, estimate A18, risk, quality plan) sang 06–12/10, vẫn kịp chốt baseline trong tuần nghỉ. Email vòng 2 chuyển sang sau buổi M1 để gộp nhận xét của thầy. | | R10 |
| I02 | 2026-10-20 | Chưa thành viên nào log work trên Jira từ đầu dự án; tab Time Tracking của Sheet master trống (TV1 kiểm tra JQL `worklogDate >= "2026-09-01"` ngày 20/10, không có kết quả). Không có số liệu actual effort cho các activity đã làm (A01–A23). | Task 3.2–3.3 (weekly log, planned vs actual); Progress Check 09/11 (báo cáo actual effort); R02, R07 | TV1 | Thu giờ hồi tưởng bằng mẫu `Time-Tracking-ghi-lai-den-20-10.xlsx`, mỗi dòng ghi rõ "ước tính hồi tưởng"; từ W9 log work trên Jira khi làm; rà ở họp 15h Chủ nhật | | R02, R07 |
| I03 | 2026-10-22 | GitLab của nhóm chạy trên máy cá nhân, các thành viên khác không truy cập được. Chưa có repo chung để dựng codebase, review Merge Request, chạy CI và deploy. | A24 (găng, xong 28/10), A28, A20; stage `Baseline frozen`; R11 (giảng viên truy cập repo) | TV1 | Tạm đến họp 25/10: tài liệu nộp file `.md` lên thư mục Drive `Sprint 6-7/`; code dùng git trên máy từng người, đẩy lên repo chung sau; CI, deploy, Merge Request dời sang 26–28/10 (giờ trống của TV5). Họp A23 ngày 25/10 chọn nơi chứa repo và CI (TV1 raise). Nếu lùi quá 25/10 thì A24 trễ, kéo A26 và demo | | R11, R15 |

**Cập nhật 30/10/2026 (TV1 báo):** nhóm đã chuyển từ GitLab tự host sang GitHub (tổ chức `qldapm-hcmut`; code ở `ticket-system-uni`, tài liệu quản lý ở `pm-docs`). Repo chung đã có nên nguyên nhân của I03 (không có nơi chứa repo chung) không còn. Ngày đóng I03 chờ TV1 xác nhận; dòng I03 ở trên giữ nguyên như nhật ký.
