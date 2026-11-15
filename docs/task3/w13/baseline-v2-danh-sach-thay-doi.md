---
Nội dung: Danh sách thay đổi Baseline V2.0 so với V1.0 và câu giải thích nguồn V1.0
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11), dựa trên quyết định D1–D12 TV1 chốt 16/11. Chưa xuất `v2.0.pdf`. Chỗ [ngoặc vuông] TV1 hoặc chủ task điền. V1.0 không được sửa.
---

# Baseline V2.0: danh sách thay đổi

**Nguyên tắc (docs/baseline/README):** V1.0 là bất biến; V2.0 là file mới (`v2.0.pdf`), chỉ lập sau khi có CR đã duyệt (CR-01, CR-02, CR-03 đều đã duyệt). Quy trình đề xuất: TV1 chốt nội dung → gửi nhóm → nhóm phản hồi trong 24h (R22) → xuất `v2.0.pdf` → PR riêng → tag `baseline-v2.0`.

## 1. Danh sách thay đổi

| # | Hạng mục | V1.0 (25/10) | V2.0 (đề xuất) | Nguồn quyết định | Cần xác nhận |
|---|---|---|---|---|---|
| 1 | Mốc nộp và dự trữ | A47 nộp 06–07/12; demo 07/12; 0 ngày dự trữ | Mốc sẵn sàng 29/11; tuần 30/11–06/12 dự trữ; ngày demo do thầy xếp [chờ thầy] | D1, TV1 16/11; thầy thông báo hai tuần cuối demo và viva | TV1 |
| 2 | Lịch các activity còn mở | A30 11–16/11; A39 25–27/11; A53 28–30/11; A41 01–05/12; A42–A46 đến 03/12 | A30 20/11; A39 23–24/11; A53 24–26/11; A41 26–27/11; A45 đến 27/11; A42 20–25/11; A43 23–25/11; A44 26/11; A46 28/11; A47 29/11 | `lich-rut-gon.md` | TV2, TV3, TV4, TV5 xác nhận phần mình |
| 3 | Phạm vi: UI quản trị | Không có REQ riêng về trang quản lý đơn vị, người dùng (Traceability V1.0: REQ-01..15, REQ-21) | Xác nhận không làm UI này; thiết lập bằng seed hoặc admin CLI | D2 | TV1, TV4 |
| 4 | Phạm vi: email | Q22: thông báo in-app là Must, email là Should | Email chưa làm (PR #31 hoãn); chỉ xét lại nếu còn giờ sau regression | D4, Q22 | TV3 |
| 5 | Hosting | ASM-05: hosting free-tier; A24 gồm CI, deploy | ASM-05 đổi thành chạy local bằng Docker kèm video dự phòng; hosting là Could; A24 thu hẹp (Docker local, CI tối thiểu) | D3 | TV5 |
| 6 | Quyền điểm danh | PD-03 ghi Organizer hoặc Admin | Chỉ Organizer (CR-01, duyệt 01/11) | CR-01 | — |
| 7 | Phạm vi xem dữ liệu | Q20: Organizer chỉ xem sự kiện của mình | Organizer xem mọi sự kiện thuộc đơn vị được gán; Admin xem toàn trường (CR-02, phương án A; code làm trước CR) | CR-02, TV1 16/11 | TV3 điền effort từ log work |
| 8 | Đăng nhập | Q02, Q10, ASM-06: không SSO thật, tài khoản mẫu | Google OIDC (domain hcmut.edu.vn) kèm tài khoản mẫu cho demo (CR-03, phương án A; code làm trước CR) | CR-03, TV1 16/11 | TV3 điền effort từ log work |
| 9 | Activity đóng hoặc gộp | A32, A33, A34, A35, A20 theo V1.0 | A32 đóng; A33, A34 đóng sau khi TV2 có kết quả test; A35 gộp vào PR #6; A20 đóng bằng kiểm chứng QR trên điện thoại hoặc ghi lý do bỏ spike [TV5] | `lich-rut-gon.md` | TV3, TV5 |
| 10 | Rủi ro | R01–R22 (R13 đã đóng) | Đóng R11; R15 chấm P5, I4 = 20; R20 giữ P, I, TV1 chấp nhận rủi ro quyền Sheet; thêm R23 (TV4), R24 (TV2), R25 (TV1), R26 (TV2) | D7, D10 | Owner xác nhận R23–R26 |
| 11 | Quỹ A38 | 30h cho change event (Q17) | Giữ nguyên, chưa dùng; thầy chưa đưa change event; không gửi email hỏi thêm (D8) | D8 | TV1 |
| 12 | Effort | Cost baseline 394,2 person-hours (364,2 + A38 30) | Giữ số V1.0 làm tham chiếu; giờ còn lại do owner ước lượng lại [trước 20/11]; effort thực tế dùng log work (thu đến 19/11) | D6, D9 | Từng owner |
| 13 | Quality | Quality plan 2.12 nháp; test case chưa có | Test case theo mã T-… (Traceability), kết quả lưu `docs/quality/results/`, UAT 26–27/11 | `giao-viec/` TV2 | TV2 |
| 14 | Checkpoint | CP3 01/11 (lịch A21), CP4 09/11, CP5 01–05/12 | CP3 20/11; CP4 đã diễn ra 09/11, không có nhận xét (ghi ở Biên bản CP); CP5 26–27/11 | Biên bản CP | TV1 |

## 2. Việc TV1 điền trước khi chốt

- Số giờ còn lại của từng activity (từ owner), tổng effort V2.0.
- Ngày demo nếu thầy thông báo; nếu chưa có, giữ "[chờ thầy]".
- Lý do chọn phương án A của CR-02, CR-03 (đang `[TV1 điền]` ở Sheet tab 5).
- Ảnh hưởng của CR-02, CR-03 lên effort, lịch: lấy từ log work của TV3, không ước đoán.

## 3. Nguồn V1.0 (câu cho Phụ lục C của báo cáo)

Chưa có bản chụp báo cáo đúng ngày 25/10. Bản `report/main.pdf` hiện có ngày 01/11 (đã chứa sửa đổi sau baseline). Bản gần nhất trước baseline là báo cáo ngày 22/10.

Câu đề xuất, điền theo kết quả TV1 kiểm lịch sử Overleaf hoặc Drive:

> Baseline V1.0 được nhóm duyệt tại họp A23 ngày 25/10/2026 (Biên bản CP, dòng CP2 bổ sung). File `v1.0.pdf` được lập ngày [../11/2026] từ [**phương án a:** bản lịch sử Overleaf/Drive ngày [../10/2026] | **phương án b:** bản báo cáo ngày 22/10/2026 kèm biên bản họp A23], không phải bản chụp đúng ngày 25/10. So với trạng thái ngày 25/10, [không có khác biệt đã biết | các khác biệt sau: [TV1 rà và liệt kê]]. Nhóm không chỉnh sửa nội dung V1.0 sau khi lập.

Lưu ý: V1.0 chỉ chấp nhận nội dung có ngày thật. Không dựng lại từ nội dung hiện tại rồi ghi là bản 25/10.

## 4. Các bước sau khi TV1 chốt

1. TV1 điền mục 2, gửi nhóm danh sách này, chờ phản hồi 24h.
2. Xuất `v2.0.pdf` (nội dung V2.0) và `v1.0.pdf` (theo mục 3) vào `docs/baseline/`; mỗi file một PR riêng.
3. Gắn tag `baseline-v1.0` và `baseline-v2.0`; ghi vào Biên bản CP và Phụ lục C.
4. Sửa trạng thái 2.4, 2.5, 2.6, 2.10, 2.11 theo V2.0; thêm dòng Weekly Log và AI Log.
