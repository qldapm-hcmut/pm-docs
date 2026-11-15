---
Nội dung: Chỉ mục gói cập nhật W13 (16–22/11) và danh sách việc TV1 cần duyệt
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11). Số liệu đối chiếu GitHub, Jira, Sheet lúc 16/11. Phần [ngoặc vuông] nhóm phải điền hoặc xác nhận. TV1 chưa duyệt.
---

# W13: gói cập nhật sau Progress Check

## Bối cảnh (sự thật đã biết)

- Progress Check 09/11: nhóm 9 không được gọi, không trình bày, không có nhận xét (TV1 báo 16/11), giống M1.
- Thầy thông báo hai tuần cuối các nhóm demo và viva (TV1 báo 16/11). Ngày của nhóm 9 chưa biết; tuần 15 bắt đầu 30/11, tuần 16 bắt đầu 07/12. TV1 muốn chừa thêm 1 tuần so với mốc 07/12.
- Backend trên `main` có luồng chính (đăng nhập Google, sự kiện, duyệt, đăng ký, waitlist FIFO, hủy và tự chuyển, check-in QR/mã/thủ công, thống kê, CSV, đơn vị, thông báo in-app, audit, worker). Email chưa nằm trên `main`.
- Frontend `main` chỉ có scaffold; màn hình đăng nhập, sự kiện, đăng ký, check-in nằm ở nhánh `feat/A35-checkin-ui` (chưa vào `main`); PR #6 tích hợp đang mở.

## File trong gói

| File | Nội dung |
|---|---|
| `lich-rut-gon.md` | Lịch rút gọn về mốc sẵn sàng 29/11, phương án, thứ tự cắt, task điều chỉnh |
| `cap-nhat-theo-nguoi.md` | Việc từng thành viên cần cập nhật trên Jira, Time Tracking, PR |
| `bao-cao-hoan-thien.md` | 49 `\todo` của báo cáo chia theo việc làm được ngay hay chờ số liệu |
| `thong-bao-nhom-16-11.md` | Tin nhắn báo nhóm các quyết định D1–D12, nhờ phản hồi trong 24h |
| `baseline-v2-danh-sach-thay-doi.md` | Danh sách thay đổi V2.0 so với V1.0 và câu nguồn V1.0 cho Phụ lục C |
| `giao-viec/` | Giao việc W13–W14 theo người (README + TV1–TV5), theo khung mục tiêu, đầu vào, bước, đầu ra, hoàn thành khi |
| `../../sheet-import/2-weekly-log-W11-W13.tsv` | Dòng Weekly Log W11–W13 |
| `../../sheet-import/9-ai-log-16-11.tsv` | Dòng AI Log lần dùng AI này |
| `../../sheet-import/cap-nhat-16-11.md` | Câu SỬA cho Biên bản CP4, đề xuất rủi ro mới, hướng dẫn dán |

## TV1 cần duyệt (theo thứ tự ưu tiên)

| # | Quyết định | Lựa chọn | Hạn gợi ý |
|---|---|---|---|
| D1 | Mốc sẵn sàng thực tế | **Đã chốt 16/11 (TV1): Chủ nhật 29/11.** Thầy chỉ nói hai tuần cuối demo và viva; chưa có ngày nộp riêng hay slot của nhóm 9 | Xong |
| D2 | Phương án lịch | **Đã chốt 16/11 (TV1): P-A, bỏ UI quản trị đơn vị và người dùng** (thiết lập bằng seed hoặc admin CLI). PR #6 không có trang quản lý đơn vị, người dùng | Xong |
| D3 | Triển khai | **Đã chốt 16/11 (TV1): Docker local + video dự phòng**; hosting chỉ làm nếu dư giờ (Could). Kéo theo: đổi ASM-05 (hosting free-tier), ghi vào danh sách thay đổi Baseline V2.0 và sửa báo cáo mục 1.2 | Xong |
| D4 | Phạm vi PR #31 (import sinh viên, admin CLI, email) và PR #28 | **Đã chốt 16/11 (TV1): merge #28 (TV5 rebase, vì đang xung đột với `main`) trước 19/11; hoãn #31** (3.662 dòng, 55 file, 1 commit), chỉ xét merge sau regression nếu còn giờ. Chưa cần CR cho #31 vì chưa merge. Mỗi PR cần review chéo trước khi merge | Xong |
| D5 | CR-02, CR-03 | **Đã chốt 16/11 (TV1): duyệt phương án A cho cả hai.** Ghi là quyết định của nhóm, không ghi thầy đồng ý; code làm trước CR nên CR chỉ ghi nhận; effort ghi "chưa có, lấy từ log work TV3". Việc sau duyệt: ghi tab 5 (chờ TV1 xác nhận câu lý do), sửa báo cáo 1.2 (ASM-06, câu "không tích hợp SSO thật") và Exclusions 1.4, đưa vào Baseline V2.0 | Xong (chờ ghi Sheet) |
| D6 | Baseline V2.0 (giữ V1.0) | **Đã chốt 16/11 (TV1): lập V2.0.** TV1 chốt nội dung, không họp; sau đó báo nhóm các điểm cần chốt (theo R22, nhóm phản hồi trong 24h, quá hạn TV1 tự duyệt). Nguồn V1.0: **TV1 thử lịch sử Overleaf/Drive trước**; không có thì dùng bản 22/10 cộng biên bản A23, ghi rõ nguồn và khác biệt ở Phụ lục C. Việc chờ: owner ước lượng lại effort còn lại trước 20/11 | Nội dung: 20/11 |
| D7 | Risk Register | **Đã chốt 16/11 (TV1):** duyệt R23 (owner TV4) và R24 (owner TV2); đóng R11; R15 chấm lại P5, I4 = 20 và cập nhật mô tả theo mốc 29/11; thêm R25 (P5, I4 = 20, owner TV1) và R26 (P4, I4 = 16, owner TV2). Chờ TV1 xác nhận để ghi Sheet | Xong (chờ ghi Sheet) |
| D8 | Email thầy | **Đã chốt 16/11 (TV1): không gửi email.** Giữ mốc 29/11 theo suy luận, chờ thầy thông báo; Q17 (change event) vẫn là uncertainty, quỹ A38 giữ nguyên; không có Q23, Q24 | Xong |
| D9 | Time Tracking | **Đã chốt 16/11 (TV1): hạn 19/11 (Thứ Năm)**, phạm vi 22/10–15/11; mỗi người tự điền tab 3, ghi "hồi tưởng", log Jira từ 16/11. Bảng gợi nhớ: `goi-nho-gio-theo-nguoi.md` (dữ kiện GitHub, không phải giờ) | Xong |
| D10 | Quyền Sheet/Drive (R20) | **Đã chốt 16/11 (TV1): giữ nguyên hiện trạng** (Sheet master: bất kỳ ai có link là người chỉnh sửa; kiểm 16/11, chỉ TV1 có trong danh sách theo email). TV1 chấp nhận rủi ro, sẽ báo nhóm; ghi vào R20 ngày 16/11. Drive nhóm chưa kiểm lại | Xong |
| D11 | Phân công báo cáo | **Đã chốt 16/11 (TV1): TV1 viết gần hết** (có AI hỗ trợ soạn nháp, ghi AI Log). Thành viên cung cấp dữ kiện, duyệt phần liên quan và tự viết 4.6, Phụ lục E. Rủi ro R19 (TV1 quá tải) tăng; theo dõi ở tab 4 | Xong |
| D13 | Theo dõi Baseline V2.0 trên Jira | **Đã chốt 16/11 (TV1 đồng ý đề xuất AI): theo dõi tại A38 (SCRUM-104), không tạo activity mới.** Log work V2.0 ghi "V2.0" đầu ghi chú để tách khỏi dự phòng change event (Q17); mức trần giờ V2.0 trong quỹ 30h do TV1 quyết. Sub-task SCRUM-115 đến 119 (tạo nhầm 08/11) gắn nhãn `can-xoa`; connector Jira không có thao tác xóa nên TV1 xóa bằng JQL `labels = can-xoa` | Xong (chờ TV1 xóa tay) |
| D12 | Đưa `docs/` mới vào `pm-docs` | **Đã chốt 16/11 (TV1): AI chuẩn bị và tạo PR** (nhánh feature, không tự merge, `v1.0.pdf` đi PR riêng). Hợp nhất hai chiều: giữ bản `pm-docs` cho 8 file đã sửa sang GitHub, dùng bản local cho CR-02, CR-03, thêm file mới; loại `goi-nho-gio-theo-nguoi.md` khỏi PR vì ghép tài khoản GitHub với vai trò khi chưa ai xác nhận. PR: `pm-docs` #6 (nhánh `docs/w13-progress-update`, chờ review và merge) | Xong |
