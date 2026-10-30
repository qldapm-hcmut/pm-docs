---
Activity: A23 (CP2: chốt Baseline V1.0)
Chủ sở hữu: TV1 (chủ trì, ký); cả nhóm xác nhận
Phiên bản: 0.2
Cập nhật: 22/10/2026 (thêm mục 17)
Trạng thái: AI hỗ trợ soạn (Claude Code, 21–22/10); TV1 duyệt 22/10. Họp 25/10: TV1 báo cả nhóm đồng ý toàn bộ 18 mục, mục 17 chọn V0 (cột Kết quả điền 27/10 theo lời TV1; chi tiết sửa, nếu có, TV1 bổ sung)
---

# A23: checklist họp chốt Baseline V1.0

- **Thời gian:** 15h Chủ nhật 25/10 (họp định kỳ; TV1 chốt 21/10). Cả 5 thành viên.
- **Kết quả cần có:** cả nhóm xác nhận từng mục ở phần 2, TV1 ký; biên bản ghi vào tab Biên bản CP (mục CP2, bổ sung cho biên bản 18/10).
- **Nguồn:** `../task2/2.4-activity-network.md` v1.0, `2.5-checkpoints.md` v0.5, `2.6-estimates.md` v0.3, `2.10-resource-plan.md` v0.3, `2.11-schedule.md` v0.3, `../task3/increment1-task-specs.md` v0.1, báo cáo chương 1–2.

## 1. Điều kiện trước họp (hạn 24/10)

| # | Việc | Ai | Trạng thái 21/10 |
|---|---|---|---|
| 1 | A21 lịch, Gantt, cost baseline; A50 san tải | TV1 | Xong 20–21/10 (TV1 báo) |
| 2 | A22 quality plan và test strategy (quy ước mã test) | TV2 thực hiện, TV1 duyệt | Jira In Progress; lịch xong 22/10 |
| 3 | A25: TV3 xác nhận phần bổ sung PD-02 (bảng units, notifications; migration) | TV3 | Jira In Review |
| 4 | A58: gửi email (bản v0.3), ghi Client Log; nếu 24/10 chưa có trả lời thì ghi giả định còn mở | TV1 | Đã gửi 23/10 15:10 (Q21, Q22); thầy trả lời 25/10 07:32, đồng ý cả hai |
| 5 | Dán `../sheet-import/10-activity-A23-25-10.tsv` vào tab 10 (cột A–P các dòng có trong file) | TV1 | Chưa |
| 6 | Time Tracking hồi tưởng đến 20/10 (I02), hạn 23/10 | Cả nhóm | Đang thu |
| 7 | TV3, TV5, TV4, TV2 đọc mô tả task Increment 1 và ghi ý kiến vào phần cần duyệt | TV2–TV5 | Chưa |
| 8 | Biên dịch lại báo cáo (`latexmk -pdf main.tex`) sau khi sửa theo các mục trên | TV1 | Đã biên dịch 21/10 (115 trang) |

## 2. Các mục nhóm phải xác nhận tại họp

Ghi kết quả từng dòng: **Đồng ý / Sửa (ghi nội dung) / Không đồng ý (ghi lý do, ai xử lý, hạn)**.

| # | Mục | Nội dung cần xác nhận | Nguồn | Kết quả |
|---|---|---|---|---|
| 1 | L8 | Gối đầu Increment 1: A24, A28, A31 sau A25; A26 sau A24; A27 chờ A23 | 2.11, 2.4 | Đồng ý |
| 2 | L9 | TV1 owner/duyệt, TV2 thực hiện khoảng 19h (A22, A43, phần A42, A45); TV5 làm chung A34; TV4 làm chung A39. TV2, TV4, TV5 đã xác nhận riêng (TV1 báo 21/10), nay xác nhận trước cả nhóm | 2.10 | Đồng ý |
| 3 | L10 | Việc đóng dự án bắt đầu sớm (A42 sau A51; A43, A45 sau A30; A44 sau A39; A46, A47, A54 theo 2.4) | 2.11 | Đồng ý |
| 4 | L11 | A32 sau A62, song song A30 | 2.11 | Đồng ý |
| 5 | REQ-21 | Giữ REQ-21 (Should), không cắt lúc chốt; nếu A27 trễ quá 1 ngày thì TV1 xem xét cắt | 2.11 | Đồng ý |
| 6 | Năng lực | 14h/tuần mỗi người, cao điểm 16h; E01 sửa theo | 2.10, 2.6 | Đồng ý |
| 7 | Estimate | Giữ số PM chốt 20/10; implement/test còn ý kiến trái chiều, theo dõi qua R02 và Time Tracking; chưa có ước lượng chéo độc lập (ghi trung thực ở báo cáo 2.6) | 2.6 | Đồng ý |
| 8 | Cost baseline | **364,2 person-hours + quỹ A38 30h = 394,2** (cộng từ PERT đã làm tròn; PM chọn 21/10) | 2.6, 2.11 | Đồng ý |
| 9 | Lịch và mốc | A23 25/10; CP3 11–16/11 (trễ 15 ngày); Progress Check 09/11 **chưa có QR check-in**; A37 23–24/11; UAT 01–05/12 (trễ 11 ngày); A47 06–07/12; **0 ngày dự trữ** trước demo 07/12 | 2.11, 2.5 | Đồng ý |
| 10 | Đường găng | A24 → A26 → A27 → A29 → A62 → A32 → A35 → A37 → A39 → A53 → A41 → A47 → A54 | 2.11 | Đồng ý |
| 11 | CP4 | Tiêu chí giữ nguyên đến khi thầy trả lời A58; nếu chưa có trả lời thì ghi giả định: demo đến đăng ký, hủy, waitlist và spike QR | 2.5, A58 | Đồng ý. Thầy đã trả lời 25/10 07:32 (Q21): QR, báo cáo không bắt buộc tại Progress Check; phần đã xong phải demo chạy được. CP4 sửa theo ngày 27/10 |
| 12 | Notification | Trong ứng dụng là bắt buộc, email là Should (giả định nhóm, chờ A58) | A58 | Đồng ý. Thầy đồng ý 25/10 07:32 (Q22), không còn là giả định |
| 13 | A38 | Quỹ 30h ngoài chuỗi, dùng giờ dư TV2–TV5; nếu change event rơi vào chuỗi găng thì cắt Could rồi Should hoặc lập Baseline V2.0 | 2.11 | Đồng ý |
| 14 | Rủi ro | R15 (lịch vượt mốc) đã cập nhật 21/10; owner các rủi ro cấp activity đủ | Sheet tab 4, 12 | Đồng ý |
| 15 | Traceability | Objective → Product → Activity → Resource → Risk → Test → Checkpoint không mâu thuẫn giữa báo cáo, Sheet, file md (A57) | chương 5, tab 6 | Đồng ý |
| 16 | Task Increment 1 | Mô tả task do AI soạn đã được TV3, TV5, TV4, TV2 duyệt phần của mình; CI dùng Jenkins (TV1 báo 21/10); TV5 kiểm stage `Baseline frozen` trong `Jenkinsfile` chạy được với merge request | increment1-task-specs | Đồng ý |
| 17 | Chia giờ A26, A24 | Lịch V0 chia A26 đều 3 người nên A26 chờ TV4 xong A24 (28/10), TV3, TV5 trống 24–28/10. Mô hình chạy thử 22/10 (AI hỗ trợ, chưa sửa config): **V1** A26 theo đề xuất TV3 14/10 (TV3 5,5h, TV5 5h, TV4 0h; màn hình đăng nhập do TV5 làm hoặc gộp vào A28) → A47 xong 06/12, dự trữ 1 ngày; **V2** thêm A24 TV5 6,9h, TV4 2h (khung React, TV4 xác nhận) → A47 05/12, dự trữ 2 ngày. TV1 giữ V0 khi giao việc 22/10; nhóm chọn V0, V1 hay V2. Chọn V1/V2 thì tạo config mới trong `tools/schedule/` và chạy lại | 2.11, `../task3/sprint6-7/` | Đồng ý: chọn V0 (giữ lịch, 0 ngày dự trữ) |
| 18 | Repo và CI (I03) | GitLab tự host trên máy cá nhân, nhóm không truy cập được. Chọn nơi chứa repo chung (cũng là bản công khai gửi thầy) và nơi chạy CI; ai tạo, ai có quyền quản trị. Phải chốt trong họp: A24 (găng) cần repo ngày 26/10 để làm CI, deploy, Merge Request. Nếu đổi khỏi Jenkins thì ghi đính chính quyết định "CI dùng Jenkins" (21/10) và viết lại kiểm tra `Baseline frozen` cho nền tảng mới | `../task3/issues.md` (I03) | Đồng ý chọn nơi chứa repo chung và CI. Giữ GitLab (repo) và Jenkins (CI), do Phan Huy Quang Minh (TV3) giữ; không đổi khỏi Jenkins nên không cần đính chính quyết định 21/10. Cách các thành viên truy cập và bản công khai gửi thầy: TV1 bổ sung nếu đã chốt |

Nếu một mục không đạt: TV1 quyết sửa ngay trong họp, hoặc chốt có điều kiện kèm hạn (như CP2 18/10). Không chốt nếu mục 8, 9, 15 hoặc 18 chưa được đồng ý (mục 18 thêm 22/10, TV1 duyệt).

## 3. Kế hoạch Sprint 7 (28/10–03/11)

Giờ theo lịch đã san tải (`2.11-schedule.md` v0.3), chỉ tính phần rơi vào 28/10–03/11.

| Task | Jira | Giờ trong sprint | Người | Ngày theo lịch | Ghi chú |
|---|---|---:|---|---|---|
| A24 Set up codebase, CI & deployment | SCRUM-88 | 1,0 | TV4 | kết thúc 28/10 | Phần còn lại từ Sprint 6 |
| A31 Write test cases for increment 1 | SCRUM-93 | 0,5 | TV2 | kết thúc 28/10 | Phần còn lại từ Sprint 6 |
| A26 Implement authentication & roles | SCRUM-91 | 10,5 | TV3, TV4, TV5 (3,5 mỗi người) | 29–30/10 | Găng |
| A27 Implement event management | SCRUM-94 | 24,0 trên 25,3 | TV3, TV4, TV5 (8 mỗi người) | 31/10–04/11 | Găng; 1,3h còn lại sang Sprint 8 |
| A36, A57 (hammock) | | khoảng 6,6 | TV1 | cả sprint | Weekly log, rà traceability |

**Phân task vào sprint (sprint 1 tuần; task vào sprint chứa phần lớn giờ của nó theo lịch đã san tải):**

| Sprint | Ngày | Task |
|---|---|---|
| 6 | 20–27/10 | A21, A50, A22, A25, A58, A20, A23, A28, A24, A31 (A24, A31 dự kiến dư khoảng 1h sang 28/10) |
| 7 | 28/10–03/11 | A26, A27 (A27 dư 1,3h sang 04/11) |
| 8 | 04–10/11 | A29, A62, A51 (Progress Check 09/11) |
| 9 | 11–17/11 | A32, A30 (CP3), A33, A40 |
| 10 | 18–24/11 | A35, A34, A37, A43, A45 |
| 11 | 25/11–01/12 | A39, A53, A44, A42 |
| 12 | 02–08/12 | A41 (CP5), A46, A47, A54 |
| ngoài sprint | | A36, A57 (hammock, log work trực tiếp), A38 (quỹ dự phòng) |

- **Mục tiêu sprint:** đăng nhập và phân quyền chạy trên bản deploy (T-AUTH-01…03); quản lý sự kiện gần xong (tạo, duyệt, công bố).
- **Việc TV1 làm trên Jira:** thêm A26, A27 vào Sprint 7; **A62 (SCRUM-72) đang nằm trong Sprint 7 nhưng lịch là 08–10/11**, chuyển sang sprint của tuần 04–10/11.
- **Tải trong sprint:** TV3, TV5 khoảng 11,5h; TV4 khoảng 12,5h; TV2 khoảng 0,5h (TV2 dư, có thể nhận phần kiểm thử sớm cho A26 nếu A22 cho phép); TV1 khoảng 6,6h.

## 4. Kế hoạch Weekly Log W9, W10

Dữ liệu dán tab 2 ở `../sheet-import/2-weekly-log-W9-W10-ke-hoach.tsv` (cột A–J như bảng Weekly Log). Cột "Công việc thực tế" W9 chỉ ghi những gì TV1 đã báo hoặc trạng thái Jira 21/10; TV1 điền tiếp ở họp 25/10. Cột "Người cập nhật" để trống, ai cập nhật thì ghi tên mình. Effort KH là giờ theo lịch đã san tải rơi vào tuần đó.

## 5. Sau khi chốt: xuất PDF và gắn tag

1. Sửa trạng thái các file nguồn (mục đầu) từ "chờ nhóm xác nhận tại A23" thành "nhóm xác nhận tại A23 ngày 25/10", kèm mục nào được sửa trong họp; sửa `\kiemtra` tương ứng ở báo cáo 2.4, 2.5, 2.6, 2.10, 2.11, 2.12 và điền ngày chốt ở mục 2.12, Phụ lục C.
2. Cập nhật bảng trong `README.md` (thư mục này): ngày duyệt 25/10, người duyệt.
3. Biên dịch báo cáo: trong `report/`, chạy `latexmk -pdf main.tex`.
4. Tạo `v1.0.pdf`: **[TV1 quyết]** dùng toàn bộ `report/main.pdf` ngày chốt (chương 1–2 là nội dung baseline), hay chỉ chương 1–2 cộng phụ lục C. Phương án đơn giản là chép nguyên `main.pdf` thành `docs/baseline/v1.0.pdf`.
5. Trong bản clone repo GitLab của nhóm (thư mục local `D:\QLDAPM\co3011-bootstrap` hiện không phải repo git): tạo nhánh, chép các file đã sửa và `v1.0.pdf` vào, mở **một merge request riêng** cho `docs/baseline/v1.0.pdf`; TV1 duyệt. Stage `Baseline frozen` của Jenkins chỉ chặn sửa/xóa file `v*.pdf` đã có, nên thêm `v1.0.pdf` lần đầu không bị chặn (xem `README.md`).
6. Sau khi merge, gắn tag trên commit đó:
   ```bash
   git tag -a baseline-v1.0 -m "Baseline V1.0 approved 25/10/2026"
   git push origin baseline-v1.0
   ```
7. Ghi Weekly Log W9 (hành động quản lý: chốt Baseline V1.0), AI Log các phiên đã dùng, PROGRESS.md.
