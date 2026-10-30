---
Activity: A18
Chủ sở hữu: cả nhóm (TV3 chủ trì)
Phiên bản: 0.1
Cập nhật: 12/10/2026
Trạng thái: **đề xuất của AI — nhóm chốt lại**, chưa phải số của nhóm
---

# A18 — Đề xuất effort và thời lượng (nháp AI)

> Mục đích: cho nhóm một điểm xuất phát để chốt nhanh. **Không thay thế** ước lượng độc lập của từng người (A18). Khuyến nghị: mỗi người ước lượng phần mình trước, rồi mới mở bảng này để đối chiếu; chỗ nào lệch trên 50% thì giải thích và thống nhất.

## Cách tính

| Đại lượng | Cách tính | Cơ sở |
|---|---|---|
| M (khả dĩ nhất) | Giữ số effort trong kế hoạch nháp | Chưa có cơ sở tốt hơn; stack kỹ thuật chưa chốt |
| O, P | O = M × hệ số, P = M × hệ số theo nhóm bất định | Xem bảng bên dưới |
| PERT | (O + 4M + P) / 6, làm tròn 0,5h trước khi tính | Phương pháp ở 2.6 |
| Thời lượng | ceil((PERT / số owner) / (giờ tuần của owner / 7)); nếu mỗi người ≤ 5h thì tối đa 2 ngày; không ngắn hơn số nháp. **Ngoại lệ:** A11–A23, A25, A50, A58 giữ effort và ngày đã chốt ở phân công 06/10 | E01: 12h/tuần TV2–TV5, 7h/tuần TV1 |

| Nhóm bất định | O | P | Áp dụng cho |
|---|---|---|---|
| Tài liệu, quản lý | 0,8 M | 1,4 M | A16–A19, A21, A22, A25, A32, A42, A43, A45, A50, A58 |
| Hiện thực | 0,7 M | 1,6 M | A26–A29, A34, A35, A37, A53 |
| Rủi ro kỹ thuật cao | 0,7 M | 2,0 M | A20 (spike QR), A24 (CI/deploy), A33 (QR check-in), A62 (waitlist đồng thời) |
| Kiểm thử | 0,8 M | 1,5 M | A30, A31, A39–A41 |
| Sự kiện, họp | 1,0 M | 1,2 M | A23, A44, A46, A47, A51, A54 |
| Dự phòng | 0,5 M | 1,5 M | A38 |

Hệ số là **giả định của AI**, không dựa trên số liệu lịch sử của nhóm.

## Bảng đề xuất

| ID | Activity | Owner | Nháp (h/ngày) | O | M | P | PERT (h) | Thời lượng đề xuất (ngày) |
|---|---|---|---|---|---|---|---|---|
| A16 | Write product descriptions | TV2, TV4 | 8/2 | 6,5 | 8 | 11 | 8,3 | 2 |
| A17 | Construct activity network & checkpoints | TV1, TV2 | 6/2 | 5 | 6 | 8,5 | 6,3 | 2 |
| A18 | Estimate activity effort bottom-up | TV1, TV2, TV3, TV4, TV5 | 10/2 | 8 | 10 | 14 | 10,3 | 2 |
| A19 | Assess activity risks & plan responses | TV5, TV4 | 8/2 | 6,5 | 8 | 11 | 8,3 | 2 |
| A22 | Write quality plan & test strategy | TV2, TV4 | 6/2 | 5 | 6 | 8,5 | 6,3 | 2 |
| A21 | Draft schedule & Gantt | TV3 | 5/1 | 4 | 5 | 7 | 5,2 | 1 |
| A20 | Prototype QR check-in (spike) | TV3, TV5 | 6/3 | 4 | 6 | 12 | 6,7 | 3 |
| A25 | Design database schema & API contract | TV3, TV4 | 6/3 | 5 | 6 | 8,5 | 6,3 | 3 |
| A50 | Allocate resources & level schedule | TV1, TV3 | 6/3 | 5 | 6 | 8,5 | 6,3 | 3 |
| A24 | Set up codebase, CI & deployment | TV5 | 8/3 | 5,5 | 8 | 16 | 8,9 | 6 |
| A58 | Confirm scope-affecting points with client | TV1 | 2/2 | 1,5 | 2 | 3 | 2,1 | 2 |
| A23 | Approve Project Baseline V1.0 (team) | TV1, TV2, TV3, TV4, TV5 | 5/1 | 5 | 5 | 6 | 5,2 | 1 |
| A26 | Implement authentication & roles | TV3, TV5 | 10/3 | 7 | 10 | 16 | 10,5 | 4 |
| A28 | Build UI layout & shared components | TV4, TV2 | 10/4 | 7 | 10 | 16 | 10,5 | 4 |
| A31 | Write test cases for increment 1 | TV2 | 10/5 | 8 | 10 | 15 | 10,5 | 7 |
| A27 | Implement event management | TV3, TV4, TV5 | 24/4 | 17 | 24 | 38,5 | 25,3 | 5 |
| A29 | Implement event registration & cancellation | TV3, TV4, TV5 | 12/2 | 8,5 | 12 | 19 | 12,6 | 2 |
| A62 | Implement waitlist & auto-promotion | TV3, TV4, TV5 | 12/2 | 8,5 | 12 | 24 | 13,4 | 2 |
| A30 | Test & demo increment 1 | TV1, TV2, TV3, TV4, TV5 | 10/1 | 8 | 10 | 15 | 10,5 | 2 |
| A36 | Monitor progress & update logs | TV1 | 24/49 | 19 | 24 | 33,5 | 24,8 | 49 (hammock) |
| A57 | Chair traceability & consistency reviews | TV1 | 10/40 | 8 | 10 | 14 | 10,3 | 40 (hammock) |
| A32 | Plan increment 2 in detail | TV1 | 4/1 | 3 | 4 | 5,5 | 4,1 | 2 |
| A33 | Implement QR check-in & attendance | TV5, TV2 | 16/5 | 11 | 16 | 32 | 17,8 | 6 |
| A35 | Build check-in & report UI | TV4 | 14/5 | 10 | 14 | 22,5 | 14,8 | 9 |
| A34 | Implement attendance reports & export | TV3 | 14/4 | 10 | 14 | 22,5 | 14,8 | 9 |
| A40 | Write test cases for increment 2 | TV2 | 8/4 | 6,5 | 8 | 12 | 8,4 | 5 |
| A37 | Integrate core workflow | TV3, TV4, TV5 | 8/1 | 5,5 | 8 | 13 | 8,4 | 2 |
| A51 | Present progress check | TV1, TV2, TV3, TV4, TV5 | 5/1 | 5 | 5 | 6 | 5,2 | 2 |
| A38 | Hold contingency buffer (change event) | TV1, TV2, TV3, TV4, TV5 | 30/8 | 15 | 30 | 45 | 30 | 8 |
| A39 | Test increment 2 & regression | TV2, TV4 | 10/3 | 8 | 10 | 15 | 10,5 | 4 |
| A53 | Fix defects & deploy release | TV3, TV4, TV5 | 12/2 | 8,5 | 12 | 19 | 12,6 | 2 |
| A41 | Conduct user acceptance test | TV2, TV1 | 6/2 | 5 | 6 | 9 | 6,3 | 2 |
| A42 | Analyse planned vs actual performance | TV1, TV3 | 10/4 | 8 | 10 | 14 | 10,3 | 6 |
| A43 | Prepare closure & handover plan | TV5 | 5/3 | 4 | 5 | 7 | 5,2 | 4 |
| A44 | Hold retrospective & record lessons | TV1, TV2, TV3, TV4, TV5 | 5/1 | 5 | 5 | 6 | 5,2 | 2 |
| A45 | Compile final report | TV2, TV4, TV5 | 15/4 | 12 | 15 | 21 | 15,5 | 4 |
| A46 | Rehearse demo & viva | TV1, TV2, TV3, TV4, TV5 | 10/2 | 10 | 10 | 12 | 10,3 | 2 |
| A47 | Submit final deliverables | TV1 | 2/1 | 2 | 2 | 2,5 | 2,1 | 2 |
| A54 | Present final demo & viva | TV1, TV2, TV3, TV4, TV5 | 5/1 | 5 | 5 | 6 | 5,2 | 2 |

Tổng PERT (không tính hammock A36, A57): **360,2h**, so với **343h** trong kế hoạch nháp.

## Phát hiện cần nhóm quyết

### 1. Số nháp vượt năng lực E01 ở nhiều tuần

Tải theo tuần tính từ 12/10 theo lịch nháp (trải đều effort trên thời lượng nháp). Dấu * là vượt năng lực (12h TV2–TV5, 7h TV1, tuần nghỉ 6h).

| Tuần | TV1 | TV2 | TV3 | TV4 | TV5 |
|---|---|---|---|---|---|
| 12/10 (nghỉ) | 7,5* | 1,0 | 12,0* | 1,0 | 12,0* |
| 19/10 | 5,2 | 15,0* | 9,0 | 9,0 | 9,0 |
| 26/10 | 7,2* | 2,0 | 14,0* | 14,0* | 14,0* |
| 02/11 | 9,2* | 16,0* | 3,5 | 14,0* | 8,0 |
| 09/11 | 7,7* | 2,5 | 15,7* | 5,2 | 5,2 |
| 16/11 | 9,7* | 6,2 | 4,5 | 6,2 | 4,5 |
| 23/11 | 9,4* | 7,3 | 6,3 | 8,3 | 6,7 |

TV1 vượt 7h/tuần gần như mọi tuần vì A36 (giám sát) và A57 (truy vết) kéo dài cả giai đoạn. Đây là đầu vào cho A50 (cân bằng tài nguyên).

### 2. Thời lượng theo năng lực làm lịch dài hơn 07/12

Chạy lại lịch với thời lượng đề xuất (mô hình đơn giản, xem lưu ý):

| Kịch bản | A37 xong | CP4 (A51) | CP5 (A41) | Demo (A54) |
|---|---|---|---|---|
| Mốc kế hoạch | trước 09/11 | 09/11 | 23/11 | 07/12 |
| A. Theo E01 (12h/tuần) | 18/11 | 19/11 | 05/12 | 21/12 |
| B. Cao điểm 16h/tuần (TV1 9h) | 13/11 | 14/11 | 28/11 | 13/12 |
| C. Như B, thêm owner thứ hai cho A31, A34, A35, A40 | 11/11 | 12/11 | 26/11 | 11/12 |

Ngay cả kịch bản C cũng không đạt mốc kế hoạch. Từ 13/10 A34 không còn chặn A37 (báo cáo tích hợp ở A39), nên Progress Check chỉ phụ thuộc A33 và A35. Nguyên nhân còn lại: các activity do một người làm kéo dài theo E01 (A24 6 ngày, A31 7 ngày, A35 9 ngày). Các activity đã chốt ở phân công 06/10 (A11–A23, A25, A50, A58) giữ nguyên số đã chốt. Mô hình chưa tính việc A17, A18 đã trễ so với lịch ban đầu. Kịch bản C thêm người nhưng chưa xét tuần nghỉ (E02), nên thực tế còn chậm hơn.

### 3. Lựa chọn (PM chốt 13/10: cắt phạm vi theo thứ tự Could rồi Should, không bỏ core workflow)

| Hướng | Được | Mất |
|---|---|---|
| Cắt scope Increment 2 (bỏ Could rồi Should) | Giữ mốc CP4 và demo | Giảm giá trị bàn giao |
| Dời CP4 (hỏi thầy qua A58) | Giữ scope | Phụ thuộc lịch của thầy |
| Tăng giờ cao điểm hoặc thêm owner | Giữ scope và mốc | Rủi ro quá tải, cần TV2–TV5 đồng ý |
| Nhóm ước lượng lại thấp hơn nháp | Giữ mọi thứ | Cần cơ sở thật, không phải chỉnh số cho vừa |

## Lưu ý về mô hình

- Mỗi owner được giả định dành toàn bộ giờ tuần cho activity đó trong thời lượng của nó, trải đều theo ngày. Người thật làm theo đợt nên có thể nhanh hơn với việc nhỏ, chậm hơn với việc gối nhau.
- Không xét xung đột giữa các activity chạy song song cùng một người (việc của A50).
- Không xét tuần nghỉ giữa kỳ (E02) và lịch thi.
- Hệ số O/P và thời lượng là đề xuất của AI. Số cuối cùng do nhóm chốt, ghi vào AI Log phần "Nhóm đã kiểm tra và điều chỉnh thế nào".
