# Phân công Task 2 theo từng người (06–16/10/2026)

> **Đã chốt bởi PM (TV1) ngày 06/10/2026.** Effort là ước lượng ban đầu; effort của việc làm chung được chia đều. Số liệu sẽ cập nhật sau A18.

## Tổng quan

| Mã | Activity | Mục đề | Người làm | Effort | Ngày | Phụ thuộc |
|---|---|---|---|---|---|---|
| A11 | Soạn câu hỏi vòng 2 | 1.1 | TV2, TV5 | 3h | 06/10 | — |
| A12 | Gửi email hỏi client vòng 2 | 1.1 | TV1, TV2 | 4h | 07–08/10 | A11, A49 |
| A15 | Dựng PBS và PFD | 2.1, 2.3 | TV3, TV5 | 10h | 06–07/10 | A49 |
| A17 | Dựng activity network và checkpoints | 2.4, 2.5, 2.7 | TV1, TV2 | 6h | 08–09/10 | A15 |
| A16 | Viết Product Descriptions (≥5) | 2.2 | TV2, TV4 | 8h | 09–10/10 | A15, A12 |
| A18 | Ước lượng effort từ dưới lên | 2.6 | Cả nhóm (TV3 chủ trì) | 10h | 10–11/10 | A17 |
| A19 | Rủi ro cấp activity và activity phản hồi | 2.8, 2.9 | TV5, TV4 | 8h | 10–11/10 | A17, A13 |
| A22 | Quality plan và chiến lược test | 2.12 | TV2, TV4 | 6h | 11–12/10 | A16 |
| A25 | Thiết kế database và API contract | — | TV3, TV4 | 6h | 11–13/10 | — |
| A21 | Lịch, Gantt, critical path | 2.11 | TV3 | 5h | 12/10 | A18, A19 |
| A20 | Làm thử check-in QR (spike) | 2.9 | TV3, TV5 | 6h | 13–15/10 | A21 |
| A50 | Phân bổ tài nguyên, cân bằng lịch | 2.10 | TV1, TV3 | 6h | 13–15/10 | A21 |
| A58 | Email hỏi client các điểm ảnh hưởng scope | 1.1 | TV1 | 2h | 13–14/10 | A21, A12 |
| A23 | CP2 – Chốt Baseline V1.0 | 2.12 | Cả nhóm | 5h | 16/10 | A50, A25, A22, A58 |

| | TV1 | TV2 | TV3 | TV4 | TV5 |
|---|---|---|---|---|---|
| Tổng 06–16/10 | ~13h | ~16,5h | ~22h | ~17h | ~16,5h |

## TV1 — Nguyễn Đức Nghĩa (PM) · ~13h

| Ngày | Mã | Việc cụ thể | Giờ | Bàn giao |
|---|---|---|---|---|
| 07/10 | A12 | Duyệt bộ câu hỏi A11, viết và gửi email vòng 2. Theo dõi phản hồi. Nếu sau 2 ngày chưa có trả lời thì quyết định ghi phần đó thành assumption | 2h | Báo TV2 ghi Client Log |
| 08–09/10 | A17 | Đặt các checkpoint, mỗi cái ghi rõ kiểm tra gì, ai duyệt, không đạt thì làm gì. Tách activity dài hơn 16h, gộp activity quá ngắn, ghi lý do. Rà để activity nào cũng có đầu ra | 3h | Network hoàn chỉnh → cả nhóm (cho A18) |
| 10–11/10 | A18 | Ước lượng 3 điểm cho activity của mình. Ước lượng độc lập lại activity của TV2. Ghi giả định năng lực (12h/người/tuần, TV1 ~7h, giảm tải tuần nghỉ), đơn giá giả định, tính cost | 2h | TV3 tổng hợp |
| 13–15/10 | A50 | Thu lịch rảnh và lịch thi của từng người. Gán owner cho từng activity, lập bảng tải theo tuần, quyết định chuyển việc khi ai đó quá tải | 3h | TV3 cập nhật Gantt |
| 13–14/10 | A58 | Lọc các assumption chưa xác nhận có ảnh hưởng lớn tới scope, effort hoặc lịch. Gom vào 1 email gửi thầy | 2h | TV2 ghi Client Log |
| 16/10 | A23 | Đưa nhận xét M1 và kết quả A58 vào baseline. Rà ma trận traceability. Ký duyệt cuối | 1h | — |

## TV2 — Ngô Thanh Hùng (BA/QA) · ~16,5h

| Ngày | Mã | Việc cụ thể | Giờ | Bàn giao |
|---|---|---|---|---|
| 06/10 | A11 | Lọc các câu "chưa rõ" ở vòng 1 và nhận xét ở buổi M1. Soạn bản tóm tắt scope, exclusions, objectives nháp để xin thầy xác nhận. Gộp và xếp ưu tiên cả bộ câu hỏi | 1,5h | Bộ câu hỏi → TV1 |
| 07–08/10 | A12 | Ghi Client Log trong 24h sau khi có trả lời (giờ gửi, giờ nhận, ảnh chụp email). Cập nhật scope và assumptions theo câu trả lời | 2h | Báo TV5 nếu có rủi ro mới |
| 08–09/10 | A17 | Từ PFD suy ra các activity, đặt tên dạng động từ + danh từ. Xác định phụ thuộc, vẽ activity network (activity-on-node) | 3h | Bản vẽ → TV1 đặt checkpoint |
| 09–10/10 | A16 | Viết 3 PD: SRS, Test plan, Hệ thống đã deploy (đủ 8 trường, quality criteria đo được). Review chéo 2 PD của TV4 | 4h | — |
| 10–11/10 | A18 | Ước lượng 3 điểm cho activity của mình. Ước lượng độc lập lại activity của TV3 | 2h | TV3 tổng hợp |
| 11–12/10 | A22 | Xác định các mức kiểm thử (unit, integration, e2e, UAT). Quy ước mã T# gắn với requirement. Chọn nơi lưu bằng chứng | 3h | — |
| 16/10 | A23 | Review chéo phần estimate và lịch (A18, A21, A50) theo checklist CP2. Viết biên bản CP2 | 1h | — |

## TV3 — Phan Huy Quang Minh (Tech Lead) · ~22h

| Ngày | Mã | Việc cụ thể | Giờ | Bàn giao |
|---|---|---|---|---|
| 06–07/10 | A15 | Liệt kê specialist products (SRS, thiết kế, các module Event/Registration/Check-in/Report, test, hệ thống đã deploy). Vẽ PFD | 5h | PBS và PFD → TV1, TV2 (A17); TV2, TV4 (A16) |
| 10–11/10 | A18 | Chủ trì: ước lượng activity của mình, ước lượng độc lập lại activity của TV4. Tính PERT, xử lý các chỗ lệch >50%, tách effort và thời lượng | 2h | Bảng estimate → A21 |
| 11–13/10 | A25 | Vẽ ERD (users, roles, events, registrations, attendance). Xác định ràng buộc (không đăng ký trùng, không vượt số chỗ). Liệt kê endpoint kèm request và response mẫu | 3h | → TV4 review |
| 12/10 | A21 | Nhập activity, thời lượng, phụ thuộc. Tính critical path, vẽ Gantt nháp (chưa ràng buộc tài nguyên) | 5h | → TV1 (A50, A58) |
| 13–15/10 | A20 | Thử QR trên 3–4 thiết bị và trình duyệt, kể cả khi mạng yếu. Đo thời gian check-in mỗi người. Cập nhật estimate của A33 | 3h | — |
| 13–15/10 | A50 | San tải: dời activity có float. Cập nhật Gantt có ràng buộc tài nguyên. So sánh với lịch lý tưởng và ghi lý do từng thay đổi | 3h | — |
| 16/10 | A23 | Review chéo PD và quality plan (A16, A22) theo checklist CP2 | 1h | — |

## TV4 — Nguyễn Đắc Nghĩa (Frontend) · ~17h

| Ngày | Mã | Việc cụ thể | Giờ | Bàn giao |
|---|---|---|---|---|
| 09–10/10 | A16 | Viết 2 PD: Thiết kế database, Module Check-in. Review chéo 3 PD của TV2 | 4h | — |
| 10–11/10 | A18 | Ước lượng 3 điểm cho activity của mình. Ước lượng độc lập lại activity của TV5 | 2h | TV3 tổng hợp |
| 10–11/10 | A19 | Thêm rủi ro cho các activity tài liệu, quản lý và frontend/UI. Chấm P, I, tính exposure, ghi owner, giảm thiểu, dự phòng cho phần này | 4h | → TV5 gộp vào register |
| 11–12/10 | A22 | Quy định cách review tài liệu (review chéo, checklist). Chọn công cụ test, nhất là cho frontend và e2e | 3h | — |
| 11–13/10 | A25 | Review API contract từ phía frontend. Ghép từng màn hình với endpoint, đề xuất chỉnh. Xác nhận đồng ý contract | 3h | — |
| 16/10 | A23 | Review chéo activity network và risk (A17, A19) theo checklist CP2 | 1h | — |

## TV5 — Hà Cao Đức Minh (Fullstack/DevOps) · ~16,5h

| Ngày | Mã | Việc cụ thể | Giờ | Bàn giao |
|---|---|---|---|---|
| 06/10 | A11 | Soạn câu hỏi phát sinh từ high-level risks và lifecycle (A13). Thêm câu hỏi về ngày M2, M3, thời điểm change event, và M1 có cần initial estimates không | 1,5h | → TV2 gộp |
| 06–07/10 | A15 | Liệt kê management products (kế hoạch, báo cáo, logs). Vẽ PBS dạng cây, đánh mã P#, đánh dấu deliverable hay intermediate | 5h | Thống nhất danh sách product với TV3 trong ngày 06/10 |
| 10–11/10 | A18 | Ước lượng 3 điểm cho activity của mình. Ước lượng độc lập lại activity của TV1 | 2h | TV3 tổng hợp |
| 10–11/10 | A19 | Thêm rủi ro cho các activity kỹ thuật (backend, check-in, CI/CD, deploy). Thêm activity phản hồi cho rủi ro có exposure ≥12. Gộp phần của TV4 vào Risk Register | 4h | → TV3 (A21) |
| 13–15/10 | A20 | Code thử tạo và quét QR bằng thư viện có sẵn, kèm phương án nhập mã dự phòng. Cùng TV3 chọn giải pháp, cập nhật R04 | 3h | — |
| 16/10 | A23 | Review chéo scope và Client Log (A12, A58). Export PDF và gắn tag `baseline-v1.0` | 1h | — |

## Quy ước chung

- **Ước lượng chéo ở A18** đi theo vòng: TV1 ước lượng lại cho TV2, TV2 cho TV3, TV3 cho TV4, TV4 cho TV5, TV5 cho TV1. Nếu lệch >50% thì hai người giải thích và thống nhất.
- **Review chéo ở A23**: không ai review phần do chính mình làm.
- **Phải bàn giao đúng hạn** để người khác không bị chặn:
  - A15 xong 07/10, vì A16 và A17 cần nó.
  - A17 xong 09/10, vì A18 và A19 cần nó.
  - A18 và A19 xong 11/10, vì A21 cần cả hai.
  - A21 xong 12/10, vì A20, A50 và A58 cần nó.
- Ghi actual effort vào Jira worklog hoặc tab Time Tracking ngay khi làm xong.
