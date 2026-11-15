---
Nội dung: Danh sách chỉnh Sheet master sau khi kiểm tra tiến độ 08/11
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 08/11/2026
Trạng thái: Nháp AI (Claude Code, 08/11). Sau khi TV1 đồng ý, AI đã ghi một phần lên Sheet ngày 08/11 (xem mục "Đã ghi lên Sheet 08/11" cuối file); phần còn lại chờ TV1 quyết.
---

# Chỉnh Sheet master (08/11)

Nguyên tắc: tab nhật ký (Risk History, Weekly Log, AI Log, Biên bản CP) chỉ **nối thêm**; tab sống (Risk Register, Traceability, CR, Time Tracking) sửa thẳng khi lệch thực tế.

## A. Tab 4 Risk Register — sửa dòng cũ

| Dòng | Ô | Hiện tại | Đề xuất | Lý do |
|---|---|---|---|---|
| R11 | Trạng thái | Open | `Đã đóng 30/10 (chuyển GitHub, I03 chấm dứt)` | TV1 chốt 30/10 đã chuyển khỏi GitLab |
| R11 | Giảm thiểu, Dự phòng | Mirror công khai; backup; khôi phục từ mirror | `Không còn áp dụng` | GitLab tự host không còn dùng |
| R15 | Trạng thái | Open | `Đang xảy ra (08/11): A24, A28, A31, A20, A22 quá hạn; float -9 đến -12` | Đối chiếu Jira, GitHub, Sheet |
| R15 | P, Exposure | 4, 16 | 5, 20 (**TV1 quyết**, có thể giữ 4) | Rủi ro đã thành hiện thực một phần |
| R20 | Giảm thiểu | Quét secret trước khi mirror... | Thêm: `30/10 quét secret trước khi pm-docs public; 08/11 Sheet master vẫn cho bất kỳ ai có link sửa; thêm thành viên theo email rồi tắt chia sẻ bằng link` | Kiểm tra quyền chia sẻ 08/11 |
| R20 | P, Exposure | 2, 10 | 4, 20 đến khi giới hạn quyền xong (**TV1 quyết**) | Link nằm trong repo public |
| R02 | Giảm thiểu | (không đổi) | Thêm `08/11: chưa có actual để so; đang thu giờ 22/10–08/11` | Cần minh bạch |

Rủi ro mới R23, R24 (P, I là đề xuất AI): dán dòng từ `4-risk-register-R23-R24-nhap.tsv` vào cuối bảng; **owner TV1 chọn**, cột Người duyệt, Ngày duyệt để trống đến khi duyệt.

Risk History: dán `12-risk-history-08-11.tsv` (6 dòng). Lưu ý dòng 25/10 nằm trước dòng 22/10 ở bảng hiện tại; để nguyên (nhật ký), chỉ ghi chú nếu cần.

## B. Tab 5 Change Request

- Dán `5-change-request-CR-02-CR-03-nhap.tsv` vào ô C1 (CR-02 ở cột C, CR-03 ở cột D). Nội dung lấy từ `docs/change/cr-02`, `cr-03`; chỗ `[TV3 …]`, `[TV1 …]` giữ nguyên đến khi điền.
- Chưa duyệt: không điền người duyệt, ngày duyệt.
- Bổ sung vào dòng "Ảnh hưởng tới quality và test" của CR-01: mã test T-… cho 2 ca Admin bị từ chối và Organizer không tự điểm danh [TV2 cấp mã].

## C. Tab 8 Biên bản CP (nối thêm, không sửa lịch sử)

- Dòng "CP2 (bổ sung, A23)": thêm vào ô Hành động tiếp theo `SỬA 08/11: mục 18 (giữ GitLab và Jenkins) không còn áp dụng từ 30/10 (nhóm đã chuyển GitHub, CI do người dựng repo thiết lập); hạn [TV1 điền hạn] cho v1.0.pdf chưa có ngày, v1.0.pdf chưa xuất.`
- Dòng "CP2" 18/10: ô Kết quả còn câu "Còn mở: lịch A21 và san tải A50" trong khi ô Hành động tiếp theo ghi đã xong 21/10; thêm `SỬA 08/11: A21, A50 đã xong 21/10 (xem Hành động tiếp theo)`.
- Dòng CP4 (Progress Check): nên đổi ô Kết quả sau buổi 09/11, không đổi trước.

## D. Tab 6 Traceability

| Dòng | Lệch | Đề xuất |
|---|---|---|
| REQ-10, REQ-11 (A20/A33, A35), Checkpoint CP4 | Q21: QR chưa bắt buộc ở CP4; Weekly Log W9 (A58) ghi kiểm ở CP5 | Đổi Checkpoint thành CP5 (**TV1 quyết**), hoặc ghi rõ "CP4 chỉ báo tiến độ, kiểm ở CP5" |
| REQ-10 giao diện (A35) | Người duyệt là Đức Minh, nhưng A35 do TV4 làm | TV1 xác nhận người duyệt |
| REQ-01/02, REQ-04, REQ-15, S42 | "chờ duyệt" | TV3, TV5 duyệt, điền ngày |
| Thiếu | A22, A31/A40, A38 (R05), ca test CR-01 | Thêm dòng khi TV2 chốt mã test T-…; không tự đặt mã |
| REQ-04 → R14; O4 → R20 | Liên hệ lỏng | TV1 rà lại khi duyệt |

## E. Tab 3 Time Tracking và tab 11

- Sửa hai ô `E5` và `E16` (TV3, A02 và A09) từ "1.5" (đang là ngày) thành `1,5` (số); xem `task3/w11/thu-gio-thuc-te.md`. Sau khi sửa kiểm tab 11: A02 = 2,5; A09 = 3,0.
- Dán mẫu `3-time-tracking-22-10-08-11-mau.tsv` ở cuối tab 3; **cột Giờ do từng người điền**, không điền hộ.
- Cột Ngày (A) trống toàn tab; điền khi có ngày chính xác.

## F. Tab 2 Weekly Log — W11 (cột Công việc thực tế, điền nội dung đã có bằng chứng)

Chỉ điền khi TV1 duyệt; Effort TT để trống đến khi có giờ.

| Activity | Nội dung đề xuất cho cột "Công việc thực tế" (nguồn GitHub 08/11) |
|---|---|
| A33 | PR #15 (ký và quét QR, token QR riêng từng đăng ký) đã merge 01–02/11; chưa rõ danh sách đã check-in (C2) và kết quả spike A20 |
| A27 | PR #16, #20, #22 merge 02–05/11 (duyệt và danh mục sự kiện, hủy sự kiện, endpoint danh sách) |
| A29, A62 | PR #21 (hết hạn waitlist, hoàn thành sự kiện) merge 04/11 |
| A34 | PR #17 (báo cáo tổng hợp, xuất CSV) merge 03/11; thông báo trong ứng dụng PR #18 merge 04/11 |
| A24, A28, A31, A20, A22 | Chưa thấy bằng chứng trên GitHub, Jira đến 08/11; **người phụ trách điền hiện trạng thật** |
| A36 | Rà tiến độ 08/11: phát hiện lệch Jira–GitHub, Time Tracking dừng ở 22/10, Sheet/Drive còn chia sẻ công khai |

Cột "Issues / risks": R15, R23, R24, I02. Cột "Hành động quản lý": xem `task3/progress-check-09-11.md` mục 7 (phương án chờ nhóm chốt).

Sắp xếp: dòng W9/A58 hiện nằm sau W10; để nguyên, không viết lại lịch sử.

## G. Tab 9 AI Log

Dán `9-ai-log-08-11.tsv`. Cột "Nhóm đã kiểm tra" của các dòng 15/10, 20/10, 27/10, 02/11 còn trống hoặc "chờ" — TV1 điền khi đã duyệt.

## Đã ghi lên Sheet 08/11 (TV1 đồng ý)

- Tab 12 Risk History: dòng 27–32 (R11, R15, R20, R02, R23, R24).
- Tab 4 Risk Register: dòng R23, R24 mới (dòng 25–26, owner `[TV1 chọn owner]`, Người duyệt trống); R11 (H13, I13, K13: đề xuất đóng); R15 (K17: trạng thái); R20 (H22: giảm thiểu); R02 (H4: giảm thiểu). **Không đổi P, I của R15, R20.**
- Tab 5 Change Request: cột C (CR-02) và D (CR-03), chưa duyệt, giữ các `[TV3 …]`, `[TV1 …]`.
- Tab 8 Biên bản CP: F4 và F8 nối thêm "SỬA 08/11".
- Tab 9 AI Log: dòng 38.
- Tab 3 Time Tracking: sửa E5, E16 thành số 1,5 (định dạng số `0.0`); dán 18 dòng mẫu từ dòng 58, cột Giờ trống. Tab 11: A02 = 2,5, A09 = 3,0.
- **Chưa ghi (chờ TV1 quyết):** P, I của R15, R20; Traceability (mục D); Weekly Log W11 (mục F); owner R23, R24.

## H. Việc cần TV1 làm ngay, không phải chỉnh Sheet

- **Quyền chia sẻ:** kiểm tra 08/11, Google Sheet master vẫn là "bất kỳ ai có link → người chỉnh sửa", và link nằm trong repo `pm-docs` public (PR #5 merge 01/11). Tôi chưa kiểm tra thư mục Drive. Đề xuất: thêm 5 thành viên và thầy (nếu cần) theo email trước, rồi tắt chia sẻ bằng link; làm ngược lại sẽ khóa nhóm.
- **Branch protection:** chủ repo bật cho `main` ở cả hai repo (API trả "Branch not protected"; chưa chắc do tài khoản không đủ quyền xem).
