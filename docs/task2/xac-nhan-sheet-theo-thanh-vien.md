---
Chủ sở hữu: TV1 (gửi nhóm)
Phiên bản: 0.2
Cập nhật: 13/10/2026
Trạng thái: nháp — TV1 duyệt trước khi gửi
---

# Nội dung Sheet master cần từng thành viên xác nhận

Các tab Risk Register, Product Description, Traceability, Biên bản CP, Weekly Log, AI Log và Estimation đã có **bản nháp** (một phần do AI đề xuất). Mỗi người mở các mục có tên mình, **sửa trực tiếp nếu thấy chưa đúng**, rồi ghi "đã duyệt – tên – ngày" vào cột *Người duyệt / Ngày duyệt*.

## TV1 làm trước khi gửi file này cho nhóm

| # | Việc | Vì sao |
|---|---|---|
| 1 | **Xóa hoặc ẩn các cột O, M, P, PERT đang có sẵn trong tab 11 (Estimation).** Số đó là đề xuất AI (trùng `A18-de-xuat-ai.md`), chưa phải của nhóm | Để ước lượng thực sự độc lập, không bị neo số. Giữ bản AI trong `A18-de-xuat-ai.md` để đối chiếu sau |
| 2 | Loại khỏi tab 11 các activity **đã hoàn thành** (A01–A14 và A55, A59, A61): ghi actual ở Time Tracking, không ước lượng lại | Theo `2.6-estimates.md`: activity đã xong dùng actual |
| 3 | ~~Duyệt L1–L6~~ **Đã chốt 13/10** (xem "Ghi chú nguồn quyết định" ở `2.4-activity-network.md`): tách A29/A62; A53 gộp triển khai; **A34 gối đầu A33** (phụ thuộc A32 và A25, TV3 xác nhận khả thi); **A38 là quỹ dự phòng ngoài chuỗi**; dùng float trước A21 và A23. Việc còn lại: đồng bộ tên và phụ thuộc vào tab Activity, Estimation, Jira | Danh sách activity phải khớp giữa các nơi trước khi ước lượng |
| 4 | Gửi kèm `A18-huong-dan-uoc-luong.md` | Hướng dẫn cách ước lượng và vòng ước lượng chéo |

## Lịch

| Hạn | Việc | Ghi chú |
|---|---|---|
| Tối 14/10 | Điền O/M/P **độc lập** (tab 11), duyệt PD, rủi ro, traceability phần của mình | Chưa xem số của nhau |
| 15/10 | Review chéo: ước lượng chéo theo vòng, PD review chéo; **TV3 tổng hợp PERT**, bàn giao bảng cho A21 | Lệch >50% thì hai người giải thích và thống nhất |
| 15–16/10 | A21 Gantt và đường găng (TV3); A50 cân bằng tài nguyên (TV1, TV3); TV1 quyết A58 | Tuần nghỉ chỉ ~6h/người (E02) |
| 16/10 | CP2: chốt Baseline V1.0 (mốc nội bộ, không phải milestone của môn) | **Nếu A21 chưa xong hoặc số cho thấy phải cắt scope, TV1 quyết định lùi CP2 sang 17–18/10 (vẫn trước 20/10) hay cắt scope để giữ ngày** |

## Theo từng người

### TV2 — Ngô Thanh Hùng (BA/QA)

| Tab | Mục | Cần chốt |
|---|---|---|
| 7. Product Description | PD-01 (S1), PD-04 (S41), PD-05 (S51) | Đọc, sửa 8 trường, kiểm tiêu chí đo được; bỏ nhãn "nháp AI" |
| 6. Traceability | Cột "Verification / Test" | Duyệt mã test T-xxx (quy ước chính thức ở A22) |
| 1. Client Log | Cột "Tác động" của Q10–Q20 | Rà lại (đề xuất AI); ghi tên ảnh bằng chứng |
| 11. Estimation | Activity của mình (A16, A22, A31, A40, A44...) | O/M/P riêng; ước lượng chéo cho TV3 |
| 10. Activity | A17 | Kiểm lại phụ thuộc theo PFD; kiểm bản nháp AI của mạng (`2.4`, `2.5`) |
| 4. Risk Register | R01, R12 | Xác nhận P, I, biện pháp |
| A22 Quality plan | Mức kiểm thử (unit, integration, e2e, UAT), quy ước mã T#, nơi lưu bằng chứng (cùng TV4) | Chốt mã test chính thức để Traceability dùng |

### TV3 — Phan Huy Quang Minh (Tech Lead)

| Tab | Mục | Cần chốt |
|---|---|---|
| 11. Estimation | A20, A21, A25, A26, A27, A29, A62, A34, A37, A53... | O/M/P riêng; ước lượng chéo cho TV4; tổng hợp PERT toàn nhóm |
| 10. Activity | Tách A29/A62; **A34 phụ thuộc A32 và A25 (gối đầu A33)**; A37 chỉ gồm A33 + A35; A39 nhận A51, A40, A34; A53 gồm triển khai; A38 là quỹ dự phòng ngoài chuỗi | Xác nhận mạng đã chỉnh, **và xác nhận A34 có bắt đầu được ngay sau A25 không** |
| 4. Risk Register | R02, R06, R14, R16, R17 | P, I, biện pháp; đặc biệt R17 (tranh chấp waitlist) |
| 6. Traceability | Dòng A27, A29, A62, A34 | Mã test và activity |
| 7. Product Description | PD-02 (database) | Review cùng TV4: ràng buộc Q14, Q15, Q19 |
| A25 DB và API contract | ERD (users, roles, events, registrations, waitlist, attendance), ràng buộc, endpoint | Cùng TV4 review; đưa Q14, Q15, Q19 vào thiết kế |
| A21 Gantt | Sau khi tổng hợp PERT: đường găng, Gantt, cost baseline theo giờ người (E04) | Chạy lại nếu cắt scope |

### TV4 — Nguyễn Đắc Nghĩa (Frontend)

| Tab | Mục | Cần chốt |
|---|---|---|
| 7. Product Description | PD-02 (S21), PD-03 (S34) | Đọc, sửa 8 trường; bỏ nhãn "nháp AI" |
| 11. Estimation | A28, A35... (A06 đã xong: dùng actual) | O/M/P riêng; ước lượng chéo cho TV5 |
| 4. Risk Register | Rủi ro UI, tài liệu (cùng TV5 ở A19) | Thêm rủi ro cấp activity cho frontend, UI, tài liệu |
| A22 Quality plan | Cách review tài liệu, chọn công cụ test frontend và e2e (cùng TV2) | |
| A25 API contract | Ghép từng màn hình với endpoint, xác nhận đồng ý contract | Review cho TV3 |
| 6. Traceability | Dòng A35 (T-UI-01) | Xác nhận |
| Báo cáo mục 1.3 | Business case | Cập nhật theo E04 (giờ người, không VND) |

### TV5 — Hà Cao Đức Minh (Fullstack/DevOps)

| Tab | Mục | Cần chốt |
|---|---|---|
| 4. Risk Register | R04, R09, R11, R18, R20 + rủi ro cấp cao (báo cáo 1.8) | P, I, Exposure, owner, biện pháp; thêm rủi ro backend, CI/CD, check-in |
| 11. Estimation | A24, A33, A20, A43... | O/M/P riêng; ước lượng chéo cho TV1 |
| 10. Activity | A24 (chưa có owner trên Jira) | Nhận hoặc từ chối owner |
| Kỹ thuật | Stack, mirror công khai | Chốt stack; rà secret trước khi mirror (R20) |
| A19 Rủi ro cấp activity | Gộp rủi ro của TV4 vào Register; thêm activity phản hồi cho rủi ro exposure ≥12 | Chặn A21 |
| A20 Spike QR | Chờ chốt stack | Cập nhật R04 sau khi thử trên 3–4 thiết bị |

### TV1 — Nguyễn Đức Nghĩa (PM)

| Tab | Mục | Cần chốt |
|---|---|---|
| 8. Biên bản CP | CP1, M1 | Kết quả thật; nhận xét của thầy ngày 05/10 |
| 2. Weekly Log | W7, W8 | Rà "Công việc thực tế" |
| 9. AI Log | Cột "Nhóm đã kiểm tra" | Xác nhận |
| 12. Risk History | Dòng 08/10 và 13/10 | Xác nhận |
| 11. Estimation | A36, A41, A42, A57, A58 (A08, A14 đã xong: dùng actual) | O/M/P riêng; ước lượng chéo cho TV2 |
| 10. Activity | Ràng buộc A51, A54 | Thống nhất mốc sau khi ước lượng |
| 2.4 Network | L1–L6 đã chốt 13/10 (L1 = C, L6 = B, L5 dùng float) | Báo TV2 kiểm mạng; báo TV3 xác nhận A34 gối đầu A33 khả thi |
| A50 Resource | Thu lịch rảnh và lịch thi của từng người, gán owner, bảng tải theo tuần | Xử lý R19 (TV1 quá tải: chuyển một phần A57 cho TV2?) |
| A58 | Quyết gửi hay không: kênh notification, phạm vi tối thiểu tại Progress Check | Chỉ hỏi điểm 2 nếu A18 cho thấy lịch vượt |
| Quyết định phạm vi | Cắt Could rồi Should nếu số ước lượng vượt mốc | Chạy lại A21 và A50 sau khi cắt |

## Cả nhóm

| Tab | Việc |
|---|---|
| 3. Time Tracking | Ghi giờ thực tế theo Activity ID. Hiện trống nên cột Effort TT và Chênh lệch không tính được |
| Chốt kỹ thuật | **Stack** (chặn A20, A24 và estimate code); **GitLab CI hay Jenkins**; **kênh notification** (đề xuất: trong ứng dụng bắt buộc, email tùy chọn; ảnh hưởng A62 và A27) |
| 11. Estimation | Điền O/M/P độc lập, chưa xem số của nhau; vòng ước lượng chéo TV1→TV2→TV3→TV4→TV5→TV1 |
| Mọi tab | Ghi "đã duyệt – tên – ngày" vào cột *Người duyệt / Ngày duyệt* |

## Lưu ý

- **Đề xuất của AI** (O/M/P, P và I của rủi ro, mã test, nội dung PD) chưa phải số của nhóm cho đến khi người phụ trách duyệt. Khi duyệt, ghi vào cột "Nhóm đã kiểm tra và điều chỉnh thế nào" ở tab 9 (AI Log) nếu có chỉnh sửa.
- Viva có thể hỏi bất kỳ thành viên nào về ước lượng, rủi ro, tài nguyên: nên hiểu và giải thích được phần mình đã duyệt.
