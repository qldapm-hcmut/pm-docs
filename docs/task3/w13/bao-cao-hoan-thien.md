---
Nội dung: Kế hoạch hoàn thiện báo cáo LaTeX (49 \todo / \kiemtra)
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11). Số `\todo` đếm bằng Grep trên `report/` (49 lần gồm cả `\kiemtra`). Chưa biên dịch lại; thiếu gói LaTeX thì báo, không tự cài. TV1 chưa duyệt.
---

# Hoàn thiện báo cáo

## 1. Nguyên tắc

- Không bịa số liệu, ngày, câu trả lời client, giờ công. Chỗ chưa có dữ liệu giữ `\todo{}` hoặc ghi "chưa có".
- Nội dung đã duyệt chỉ ghi "X duyệt ngày Y" nếu lần dùng AI đó đã vào AI Log; bổ sung dòng AI Log trước khi gỡ nhãn.
- Phần cá nhân (4.6, Phụ lục E) **mỗi thành viên tự viết**; AI chỉ làm khung và gợi ý câu hỏi.
- Giữ V1.0 nguyên vẹn ở Phụ lục C; mọi thay đổi ghi vào V2.0.
- Báo cáo bám Sheet master; sửa Sheet trước, báo cáo sau (R08).
- **D11 (TV1 chốt 16/11): TV1 viết gần hết**, AI hỗ trợ soạn nháp và ghi AI Log; cột "Người" ở bảng dưới là người cung cấp dữ kiện hoặc duyệt, trừ 4.6 và Phụ lục E do từng người tự viết. Mỗi thành viên đọc duyệt phần liên quan trong 24h để trả lời được khi viva.

## 2. Chia theo thời điểm làm được

| Phần | `\todo` | Làm được ngay? | Cần gì | Người |
|---|---:|---|---|---|
| Ch1: bằng chứng client đổi quyết định; stakeholder; ảnh hạ tầng; standards | 11 | Có | Client Log (Q10–Q22), ảnh truy cập GitHub/Jira; chuẩn đặt tên, quy trình CR từ `docs/setup-tools.md` | TV1; TV3, TV5 cho ảnh hạ tầng |
| Ch2 (2.x còn lại) | 9 | Có | Số trong Sheet đã chốt; thêm ghi chú lịch rút gọn khi TV1 duyệt | TV1 |
| Ch3: 3.1 hiện thực, kiến trúc, stack | 8 (cả chương) | Có phần lớn | Repo `-be`, `-fe`, `docs/db-schema-and-api-contract.md` | TV3 cung cấp, TV1 tổng hợp |
| Ch3: 3.2 weekly log, 3.3 planned vs actual | | Một phần | Giờ thực tế (hạn 19/11) | TV1 |
| Ch3: 3.4 risk và issue | | Có | Risk Register sau khi TV1 duyệt R23–R26 | TV1 |
| Ch3: 3.5 chất lượng | | Chưa | Kết quả test của TV2, CI nếu có | TV2 viết |
| Ch3: 3.6 change event | | **Chưa có dữ kiện** | Thầy chưa đưa change event (Q17); xem D8. Không tạo sự kiện giả; nếu không có thì ghi trung thực và trình bày cách xử lý CR-01 đến CR-03 | TV1 |
| Ch3: 3.7 Baseline V2.0, 3.8 lower-level plan | | Sau D6 | Quyết định V2.0; `lich-rut-gon.md` làm lower-level plan | TV1 |
| Ch4: 4.1–4.5 | 6 | Chưa | Sản phẩm cuối, giờ thực tế, kết quả UAT; làm bản nháp khung từ 24/11 | TV1; TV2 phần chất lượng |
| Ch4: 4.6 đóng góp và reflection | | Chưa | Mỗi người tự viết | Từng người |
| Ch5 ma trận truy vết | 1 | Có | Traceability sau khi sửa REQ-10/11 theo Q21; mã T-REG | TV1, TV2 |
| Phụ lục A (Client Log) | 4 | Có | Q21, Q22 và ảnh email; Q18 đã bỏ | TV1 |
| Phụ lục B (weekly logs) | 1 | Có | `2-weekly-log-W11-W13.tsv` sau khi duyệt; cập nhật hàng tuần | TV1 |
| Phụ lục C (baselines) | 2 | Một phần | `v1.0.pdf` chưa xuất; V2.0 sau D6 | TV1 |
| Phụ lục D (khai báo AI) | 2 | Cuối cùng | Đối chiếu AI Log đủ dòng | TV1 |
| Phụ lục E (đóng góp) | 1 | Cuối cùng | Jira, GitHub, Time Tracking | Từng người xác nhận |
| Phụ lục F (repository) | 3 | Có | Tên repo `-be`, `-fe`, `pm-docs`; hướng dẫn chạy; kiểm quyền Sheet/Drive | TV1, TV5 |
| `main.tex` | 1 | Có | Bìa, ngày nộp | TV1 |

## 3. Chỗ báo cáo đang lỗi thời cần sửa

- Chương 2, 3, Phụ lục B, D còn nhắc GitLab, Jenkins: giữ như lịch sử nhưng thêm câu đính chính chuyển GitHub 30/10 (I03 chấm dứt).
- Báo cáo 1.2: ASM-06, câu "không tích hợp SSO thật", Exclusions 1.4 chỉ sửa khi CR-03 được duyệt.
- Ghi nhận trung thực: M1 và Progress Check đều không được gọi, không có nhận xét; Baseline V1.0 là mốc nội bộ.
- Lịch demo thay đổi (R10-tương tự): ghi vào Issues, không viết lại lịch sử.

## 4. Lịch viết (theo P-A)

| Ngày | Việc |
|---|---|
| 16–19/11 | Ch1, Ch2, Phụ lục A, B, F, Ch5: điền phần đã có dữ liệu; thu giờ |
| 20–25/11 | Ch3.1–3.4, 3.7, 3.8; A42 planned vs actual |
| 24–27/11 | Khung Ch4 và bản nháp; TV2 viết 3.5 sau kết quả test |
| 27–28/11 | Phụ lục C, D, E; mỗi người xong phần cá nhân; biên dịch, rà `\todo` còn lại |
| 29/11 | Xuất PDF, kiểm đọc được sơ đồ, nộp |
