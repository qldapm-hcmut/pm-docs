---
Nội dung: Khung nội dung và kịch bản Progress Check 09/11 (CP4, A51)
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 08/11/2026
Trạng thái: Nháp AI (Claude Code, 08/11), số liệu đối chiếu GitHub, Jira, Sheet lúc 08/11. Phần [ngoặc vuông] nhóm phải điền hoặc xác nhận. TV1 chưa duyệt.
---

# Progress Check 09/11: khung nội dung

## 1. Ràng buộc từ client (Q21, thầy trả lời 25/10 07:32)

- Chưa bắt buộc hoàn thiện toàn bộ workflow, gồm QR check-in và báo cáo/Excel/CSV.
- Chức năng đã hoàn thành phải **demo chạy được**, không chỉ giao diện hoặc mô tả thiết kế.
- Chức năng đang làm phải thể hiện tiến độ và kế hoạch hoàn thành.
- Theo đề: báo cáo actual effort, lịch, cập nhật risks/issues.

## 2. Hiện trạng (đối chiếu 08/11)

| Hạng mục | Bằng chứng | Demo được? |
|---|---|---|
| Đăng nhập, phân quyền | `ticket-system-uni` PR #4–#8 (merge đến 29/10) | Có code trên `main`; [TV3 xác nhận chạy được] |
| Tạo/sửa nháp, gửi duyệt, duyệt/từ chối, công bố, hủy sự kiện | PR #9, #10, #12, #16, #20, #22 | Có code; [TV3 xác nhận] |
| Đăng ký, hủy, waitlist FIFO tự chuyển, hết hạn waitlist | PR #11, #21 | Có code; [TV3 xác nhận] |
| Check-in CODE, MANUAL, hoàn tác, QR riêng từng đăng ký | PR #13, #14, #15 | Có code; trên `main` chưa có kết quả spike A20 |
| Báo cáo tổng hợp và xuất CSV | PR #17 | Có code (Q21: chưa bắt buộc) |
| Thông báo trong ứng dụng | PR #18 | Có code |
| **Giao diện web** | Chưa có mã frontend trên `main`; nhánh `fix/frontend-api-integration` rỗng | **Chưa**; [TV4 cho biết có gì ở máy riêng] |
| CI, Dockerfile, deploy | Chưa có `.github/workflows`, Dockerfile | **Chưa** (A24) |
| Đăng nhập demo | Chỉ ở nhánh `feature/dev-login-demo` (chưa merge) | **Chưa** trên `main` |
| Email thông báo, xuất xlsx | Không thấy code | Chưa (Should/phụ) |

Ghi chú trung thực: "Có code" nghĩa là có trên `main` theo PR và danh sách API; **chưa ai chạy kiểm chứng end-to-end**. Chưa có kết quả test nào trong `docs/quality/results/`. Không được nói "đã kiểm thử" khi chưa có bằng chứng.

## 3. Phương án demo (TV1 chọn trước 15h 08/11)

| Phương án | Mô tả | Điều kiện |
|---|---|---|
| D1 | Demo API trực tiếp (Swagger/Postman/script) với dữ liệu seed, theo kịch bản tạo sự kiện → duyệt → đăng ký → đầy chỗ → waitlist → hủy → tự chuyển → check-in | TV3 chuẩn bị máy chạy Postgres + seed + token; có kịch bản từng bước |
| D2 | D1 cộng giao diện của TV4 cho phần đã nối được | TV4 đẩy code lên PR (draft) trước buổi demo và đã nối API thật |
| D3 | Video quay sẵn D1 làm dự phòng | Quay trước, ghi rõ là bản ghi |

Khuyến nghị (AI): D1 là bản chắc chắn nhất; D2 chỉ nếu TV4 xác nhận chạy được; luôn có D3 dự phòng. Phải nói rõ với thầy phần nào là API, phần nào có giao diện.

## 4. Kế hoạch và thực tế (hạn theo Jira, tình trạng theo Jira và GitHub lúc 08/11)

| Activity | Hạn | Jira | GitHub | Nhận xét |
|---|---|---|---|---|
| A22 Quality plan (TV2) | 22/10 | In Progress | 2.12 vẫn nháp | Quá hạn |
| A25 DB schema, API contract | 20/10 | Report | Có `api/openapi.yaml`, migration | Code đã dùng; Jira chưa cập nhật |
| A20 Spike QR (TV5) | 24/10 | In Review | Chưa thấy kết quả | Quá hạn; PR #15 QR của TV3 đã merge |
| A24 Repo, CI, deploy (TV5) | 28/10 | Backlog | Không có CI/deploy | Quá hạn, nằm trên chuỗi găng |
| A28 Layout UI (TV4) | 25–26/10 | Backlog | Không có frontend | Quá hạn, găng |
| A31 Test case (TV2) | 28/10 | Backlog | Chưa có | Quá hạn |
| A26 Đăng nhập | 30/10 | In Progress | Merge | Sớm hơn hoặc đúng; Jira lệch |
| A27 Quản lý sự kiện | 04/11 | In Progress | Merge | Jira lệch |
| A29 Đăng ký/hủy | 07/11 | In Progress | Merge | Jira lệch |
| A62 Waitlist | 10/11 | In Progress | Merge (#11, #21) | Sớm |

Nói rõ với thầy: backend (A26, A27, A29, A62, một phần A33) tiến độ tốt, frontend và hạ tầng chậm. Đây là deviation thật; không làm đẹp.

## 5. Effort thực tế (chưa đủ để kết luận)

- Time Tracking trong Sheet: 52,5h trên cost baseline 394,2h (13,3%), chỉ phủ đến 22/10; TV4, TV5 gần như chưa có giờ.
- Jira worklog: 9h, chỉ của TV1; mới nhất 27/10.
- **Không được trình bày 13,3% như mức hoàn thành.** Phải nói: dữ liệu chưa đủ, đang thu giờ hồi tưởng 22/10–08/11 (xem `w11/thu-gio-thuc-te.md`), chưa có độ lệch effort tin cậy. Nếu kịp thu giờ trước 09/11 thì chèn bảng: [điền sau khi nhóm gửi giờ].
- R02 (estimate thấp) chưa kiểm chứng được vì thiếu actual.

## 6. Risks và issues cần báo

- R15 (lịch 0 ngày dự trữ): đang thành hiện thực; float âm -9 đến -12 trên chuỗi A24 → A37 theo Sheet.
- Issues: I02 (thiếu worklog) vẫn tồn tại; I03 (GitLab) đã kết thúc khi chuyển GitHub 30/10.
- Rủi ro mới đề xuất (chờ TV1 duyệt, xem `sheet-import/cap-nhat-08-11.md`): frontend trễ làm Progress Check không có giao diện; toàn bộ code do một người; chưa bật branch protection và review chéo; quyền sửa Sheet/Drive mở công khai.
- Change: CR-01 đã duyệt (01/11). CR-02, CR-03 chưa duyệt, nhóm tự quyết, **không** nói thầy đồng ý. Q17: thầy chưa đưa change event; A38 (30h) chưa dùng [TV1 xác nhận].

## 7. Kế hoạch hoàn thành (nhóm phải chốt, AI chỉ đề xuất cấu trúc)

Mốc cố định đang có trong baseline: CP3 11–16/11, A37 23–24/11 (có QR), CP5 UAT 01–05/12, nộp 06–07/12, demo 07/12, 0 ngày dự trữ.

| Phương án | Nội dung | Đánh đổi |
|---|---|---|
| P1 | Giữ toàn bộ Must; TV4 và TV5 nhận thêm giờ để bù frontend, deploy | Vượt năng lực 14h/tuần (E01) nếu không giảm việc khác; rủi ro R03 |
| P2 | Giữ Must, cắt Should (email, REQ-21 nếu chưa làm) theo quy tắc cắt Could rồi Should | Hợp quy tắc baseline; giảm phạm vi |
| P3 | Dùng quỹ A38 (30h) cho phần trễ | A38 sinh ra để chứa change event của thầy (Q17); dùng cho việc khác phải ghi quyết định |
| P4 | Lập Baseline V2.0 (giữ V1.0) kèm CR-02, CR-03 | Bắt buộc ghi CR và lý do |

Điền: [phương án nhóm chọn, ngày chốt, người duyệt]. Mỗi việc trễ cần: owner, ngày hoàn thành mới, giờ, phụ thuộc: [TV4, TV5, TV2 điền].

## 8. Dàn slide gợi ý (viva: ai cũng có thể bị hỏi)

1. Mục tiêu Progress Check theo Q21 và phạm vi demo.
2. Demo chạy được (D1/D2) — người trình bày: [điền].
3. Đang làm: frontend, CI/deploy, test — tiến độ và kế hoạch.
4. Kế hoạch vs thực tế (mục 4).
5. Effort: thực trạng thu giờ, hạn có số liệu (mục 5).
6. Risks/issues cập nhật (mục 6).
7. Thay đổi (CR-01 đến 03) và Q17.
8. Kế hoạch đến 07/12 (mục 7).

## 9. Câu hỏi thầy có thể hỏi (cần trả lời bằng sự thật)

- Vì sao frontend và deploy trễ? Ai chịu trách nhiệm, lịch mới là gì?
- Backend sớm hơn lịch, sao không dùng thời gian cho frontend? (phân vai: TV3, TV5 backend; TV4 frontend)
- Actual effort đâu? Vì sao Jira gần như không có worklog? (I02)
- Vì sao Google OIDC và phạm vi xem dữ liệu khác nội dung đã thống nhất? (CR-02, CR-03: nhóm tự quyết, chưa hỏi thầy)
- Tất cả PR do một người tạo; review chéo được thực hiện thế nào? (chưa có bằng chứng review chéo; không bịa)

## 10. Việc phải xong trước buổi demo

- [ ] TV3 chạy thử toàn bộ kịch bản D1 và gửi xác nhận.
- [ ] TV4, TV5 báo cáo hiện trạng thật (có gì ở máy riêng, đẩy lên draft PR).
- [ ] Chốt người trình bày từng mục, tổng duyệt 15h 08/11.
- [ ] Đồng bộ Jira (xem `jira-dong-bo-08-11.md`).
- [ ] Bổ sung dòng AI Log cho lần dùng AI chuẩn bị tài liệu này.
