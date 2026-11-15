---
Nội dung: Danh sách đồng bộ Jira với GitHub (08/11)
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 08/11/2026
Trạng thái: Nháp AI (Claude Code, 08/11). Phần "Đã thực hiện 08/11" cuối file đã ghi lên Jira theo đồng ý của TV1; các mục còn lại chờ người làm activity xác nhận.
---

# Đồng bộ Jira (SCRUM, site minhphan.atlassian.net)

## Hiện trạng đọc được lúc 08/11

- 66 issue: 27 Done, 32 Backlog, 5 In Progress, 1 In Review, 1 Report.
- Sprint 6 (20/10–27/10) vẫn active, quá hạn 12 ngày. Sprint 7, 9, 10 là future.
- 9 issue chưa Done đã quá hạn; 8 issue chưa gán người.
- Worklog: 3 issue, 9h, đều của TV1, mới nhất 27/10.

## Đề xuất trạng thái từng issue (chờ người làm xác nhận)

Nguyên tắc: có PR merge **chưa** đủ để Done. Tiêu chí hoàn thành của từng activity có mã test T-…; `docs/quality/results/` đang rỗng, nên chưa có bằng chứng test.

| Issue | Activity | Người | Jira hiện tại | Hạn | Bằng chứng GitHub | Đề xuất |
|---|---|---|---|---|---|---|
| SCRUM-81 | A22 Quality plan | TV2 | In Progress | 22/10 | `2.12-quality-plan.md` vẫn nháp | Giữ; TV2 cập nhật ngày xong mới |
| SCRUM-82 | A25 DB schema, API contract | TV3 | Report | 20/10 | `api/openapi.yaml`, migration `0001` trên `main` | TV3 xác nhận, có thể chuyển Done nếu TV4 đã review contract |
| SCRUM-84 | A20 Spike QR | TV5 | In Review | 24/10 | Chưa thấy kết quả spike | Giữ; TV5 nộp kết quả hoặc ghi lý do |
| SCRUM-88 | A24 Repo, CI, deploy | TV5 | Backlog | 28/10 | Không có CI, Dockerfile, deploy | Chuyển In Progress nếu TV5 đang làm; nếu không, ghi lý do và ngày mới |
| SCRUM-91 | A26 Authentication | TV3 | In Progress | 30/10 | PR #4–#8 merge | In Review (chờ test); TV3 xác nhận |
| SCRUM-92 | A28 UI layout | TV4 | Backlog | 25/10 | Không có frontend | TV4 báo hiện trạng; chuyển In Progress nếu đang làm |
| SCRUM-93 | A31 Test case | TV2 | Backlog | 28/10 | Chưa có | TV2 báo hiện trạng |
| SCRUM-94 | A27 Event management | TV3 | In Progress | 04/11 | PR #9, #10, #12, #16, #20, #22 merge | In Review; TV3 xác nhận |
| SCRUM-95 | A29 Registration, cancellation | TV3 | In Progress | 07/11 | PR #11, #21 merge | In Review; TV3 xác nhận |
| SCRUM-72 | A62 Waitlist | TV3 | In Progress | 10/11 | PR #11, #21 merge | In Review; TV3 xác nhận |
| (tra Jira) | A33 Check-in QR | TV5/TV3 | In Progress | — | PR #13, #14, #15 merge; C2 chưa rõ | Giữ In Progress đến khi C2 xong |

Mã issue lấy từ truy vấn Jira 08/11; A33 chưa có mã trong báo cáo khảo sát, cần tra trước khi đổi.

## Việc cần quyền khác

- **Đóng Sprint 6, bắt đầu Sprint 7:** TV1 chỉ có quyền thành viên (CLAUDE.md mục 5); chủ site/Jira admin (tài khoản Minh Phan) làm. Đề xuất: đóng Sprint 6, chuyển issue chưa Done sang Sprint 7 với hạn mới do nhóm chốt, **không** đổi hạn gốc trong baseline khi chưa có quyết định.
- **Gán người** cho 8 issue chưa gán: TV1 rà theo bảng owner tab Activity.
- **Log work:** mỗi người log giờ của mình (xem `w11/thu-gio-thuc-te.md`); không log hộ.

## Đã thực hiện 08/11 (TV1 đồng ý, qua Jira MCP)

- **Trạng thái:** SCRUM-91 (A26), SCRUM-94 (A27), SCRUM-95 (A29), SCRUM-72 (A62) từ In Progress sang **In Review** (PR đã merge, chưa có kết quả test). Không có issue nào chuyển sang Done.
- **Sprint 10 (id 12, future, trước đó trống):** thêm SCRUM-96 (A30), 97 (A32), 98 (A33), 100 (A35), 101 (A40), 108 (A42). Đã kiểm lại bằng truy vấn sprint.
- **Sub-task: TV1 không dùng, cần xóa tay.** Đã lỡ tạo SCRUM-115 đến 119 (A36.1, A36.2, A24.1, A51.1, A51.2); Jira MCP không có thao tác xóa, TV1 xóa trên giao diện Jira. Không tạo sub-task nữa. Việc thu giờ, giới hạn quyền, branch protection, chạy thử demo đã nằm ở `thu-gio-thuc-te.md`, `cap-nhat-08-11.md` mục H và `progress-check-09-11.md` mục 10.
- **Đưa task lớn vào Sprint 6 (id 8, đang active) theo yêu cầu TV1 (22:28):** A51 (SCRUM-103, chuyển sang **In Progress**), A62 (SCRUM-72, In Review), A29 (SCRUM-95, In Review), A30 (SCRUM-96, Backlog), A32 (SCRUM-97, Backlog), A42 (SCRUM-108, Backlog). Đã kiểm lại bằng truy vấn. A30, A32, A42 chưa bắt đầu nên không đổi trạng thái. A33, A35, A40 (bắt đầu 15/11) vẫn ở Sprint 10. Sprint 6 vẫn quá hạn (hạn 27/10) và chưa đóng.
- **Không làm:** đóng Sprint 6 hay bắt đầu sprint khác (một chiều, cần quyền và quyết định của nhóm); đổi hạn gốc; đổi trạng thái A20, A22, A24, A25, A28, A31 (cần người làm báo hiện trạng); gán người cho 8 issue chưa gán; comment lên issue.
- **Còn lại cho nhóm:** Sprint 6 vẫn active quá hạn 12 ngày, A25 vẫn "Report", A24, A28, A31 vẫn Backlog; Sprint 9 (id 11) còn A29, A62, A51.
