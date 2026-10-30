---
Activity: A58
Chủ sở hữu: TV1 (gửi), TV2 (ghi Client Log)
Phiên bản: 0.3
Cập nhật: 21/10/2026
Trạng thái: AI hỗ trợ soạn; TV1 sửa và gửi 23/10/2026 15:10 (Q21, Q22); thầy trả lời 25/10/2026 07:32, đồng ý cả hai (xem mục "Kết quả")
---

## Kết quả (TV1 cung cấp ảnh chụp email 27/10)

- **Gửi:** Thứ Sáu 23/10/2026 15:10, Nguyễn Đức Nghĩa (`nghia.nguyenhk2005@hcmut.edu.vn`). Bản gửi đánh mã hai câu là Q21, Q22; so với v0.3 có thêm câu "Tại Progress Check, nhóm cũng sẽ báo cáo actual effort, tiến độ so với kế hoạch và cập nhật risks/issues."
- **Thầy trả lời:** Chủ nhật 25/10/2026 07:32 (trước họp A23 15h cùng ngày):
  - Q21: "Mình đồng ý với phạm vi nhóm đề xuất. Tại Progress Check, nhóm chưa bắt buộc phải hoàn thiện toàn bộ workflow, bao gồm QR check-in và báo cáo/Excel/CSV. Tuy nhiên, các chức năng đã hoàn thành cần có bản demo chạy được, không chỉ trình bày giao diện hoặc mô tả thiết kế. Đối với những chức năng đang phát triển, nhóm cần thể hiện rõ tiến độ và kế hoạch hoàn thành."
  - Q22: "Mình đồng ý với đề xuất của nhóm."
- **Đã cập nhật (27/10):** tiêu chí CP4 (`../task2/2.5-checkpoints.md` v0.6, báo cáo 2.5, 2.11); báo cáo 1.1, 1.4, 2.9, Chương 5 (REQ-10, REQ-11 kiểm ở CP5), Phụ lục A. Dòng dán Sheet: `../sheet-import/1-client-log-Q21-Q22.tsv`, `2-weekly-log-W9-A58.tsv`.
- **Bằng chứng:** ảnh chụp email, TV1 lưu lên Drive, đề xuất tên `Q21-Q22-2026-10-25-email-tra-loi.png`.

# A58 — Email xác nhận các điểm còn ảnh hưởng scope và lịch

> **Bản nháp AI.** Phiên bản 0.2 viết lại sau khi đọc phản hồi của thầy ngày 08/10 (`Phản hồi 8_10.txt`). Phần lớn câu hỏi dự kiến ban đầu đã được trả lời, nên email ngắn lại đáng kể.

## Đã được thầy trả lời ngày 08/10, không hỏi lại

| Nội dung | Kết quả | Câu |
|---|---|---|
| Scope và exclusions | Đồng ý | Q10 |
| 4 objective và MoE | Đồng ý | Q11 |
| Role duyệt sự kiện | Admin duyệt, không cần role riêng; Organizer không được tự duyệt sự kiện của mình | Q12 |
| Hạn hủy đăng ký | Đồng ý: cố định 24 giờ trước giờ bắt đầu | Q13 |
| Chuyển người từ waitlist | Tự chuyển, gửi notification, thông báo lỗi vẫn tính đã đăng ký, không có trạng thái chờ xác nhận | Q14 |
| Đăng ký trùng | Mỗi sinh viên một đăng ký còn hiệu lực; hủy rồi được đăng ký lại, vào cuối waitlist nếu đầy | Q15 |
| Sửa hoặc hủy sự kiện đã công bố | Được; đổi thời gian hoặc địa điểm thì thông báo người đã đăng ký; hủy sự kiện thì hủy đăng ký, đóng waitlist | Q19 |
| Quyền xem dữ liệu | Đồng ý | Q20 |
| Milestone 2 và 3 | Không có; chỉ một lần Progress Check theo kế hoạch | Q16 |
| Change event | Thầy đưa ra trong quá trình thực hiện, không báo nội dung; coi là rủi ro và để contingency, không tạo activity riêng | Q17 |

## Còn lại có thể hỏi (nhóm quyết có gửi hay không)

Theo P05, chỉ hỏi điểm ảnh hưởng đáng kể tới scope hoặc planning. Ba điểm còn lại:

| # | Điểm | Vì sao | Gửi khi |
|---|---|---|---|
| 1 | Kênh notification tối thiểu (trong ứng dụng, email, hay cả hai) | Q14 và Q19 bắt buộc có notification nhưng không nêu kênh; email cần thêm hạ tầng gửi thư, ảnh hưởng effort | **TV1 chọn 21/10:** đề xuất trong ứng dụng là bắt buộc, email là Should; hỏi để xác nhận |
| 2 | Phạm vi tối thiểu thầy muốn thấy chạy được tại Progress Check 09/11, và thứ tự cắt (Could rồi Should) nếu không kịp | Chỉ có một Progress Check nên đây là mốc duy nhất | **Đã đến điều kiện gửi (21/10):** lịch A21 cho thấy 09/11 chưa có QR check-in (A37 xong 23–24/11) |
| 3 | ~~Cách thầy truy cập kho mã nguồn~~ | Đã chốt 13/10: nhóm mirror công khai và gửi link, không cần hỏi | — |

Các giá trị còn lại (quy mô sự kiện/người, cách mô phỏng tài khoản trường, mốc hiện trạng) thầy đã cho phép nhóm tự giả định (Q06, Q02, Q07), nên **ghi vào tài liệu là giả định của nhóm, không cần hỏi**. Đã chốt: ASM-02 (20 sự kiện/tháng, 100 người trung bình và 500 tối đa mỗi sự kiện, 50 check-in và 100 đăng ký đồng thời), ASM-06 (tài khoản mẫu có email trường), ASM-07 (15 giây/người, 20 phút/sự kiện) — xem báo cáo mục 1.2.

## Email v0.3 (gửi từ 22/10, trước họp A23 ngày 25/10)

> **AI hỗ trợ soạn (Claude Code, 21/10); chờ TV1 duyệt, sửa và tự gửi.** Ngày trong email lấy từ lịch dự kiến `../task2/2.11-schedule.md` v0.3 (TV1 chọn phương án, chưa được nhóm chốt tại A23). Không nêu số effort.

**Tiêu đề:** [CO3011 – Nhóm 9] Xin ý kiến về phạm vi Progress Check 09/11 và kênh thông báo

Kính gửi thầy,

Nhóm 9 (lớp L01) cảm ơn thầy đã phản hồi ngày 08/10. Nhóm dự kiến chốt Baseline V1.0 vào ngày 25/10. Theo P05, nhóm xin ý kiến thầy về hai điểm ảnh hưởng tới kế hoạch:

1. **Phạm vi tại Progress Check 09/11.** Theo lịch dự kiến sau khi cân đối thời gian của các thành viên, đến ngày 09/11 nhóm sẽ có: đăng nhập và phân quyền theo vai trò; tạo, duyệt, công bố sự kiện; đăng ký và hủy đăng ký theo hạn 24 giờ, có giới hạn số chỗ; danh sách chờ và tự chuyển người đang hoàn thiện (dự kiến xong 10/11); bản thử nghiệm quét QR. Điểm danh QR hoàn chỉnh (có nhập mã hoặc xác nhận thủ công) dự kiến xong 23–24/11; toàn bộ workflow gồm báo cáo và xuất file được nghiệm thu trong tuần 01–05/12.
   Thầy có đồng ý phạm vi trên là đủ cho Progress Check không ạ? Nếu thầy cần thấy điểm danh chạy được tại Progress Check, nhóm sẽ sắp xếp lại thứ tự công việc hoặc cắt yêu cầu mức Should, Could theo thứ tự đã thống nhất (không bỏ workflow cốt lõi Q08), rồi báo lại thầy lịch điều chỉnh.

2. **Kênh thông báo tối thiểu.** Theo Q14 và Q19, hệ thống phải thông báo cho sinh viên khi được chuyển từ danh sách chờ và khi sự kiện đổi thời gian, địa điểm hoặc bị hủy. Nhóm đề xuất thông báo **trong ứng dụng** là mức bắt buộc của MVP; gửi **email** là mức Should, chỉ làm nếu còn thời gian. Thầy có đồng ý không ạ?

Nếu đến ngày 24/10 nhóm chưa nhận được ý kiến, nhóm sẽ dùng hai phương án trên, ghi là giả định còn mở trong Baseline V1.0 và cập nhật khi thầy phản hồi.

Nhóm xin cảm ơn thầy.

Trân trọng,
Nguyễn Đức Nghĩa (TV1), thay mặt Nhóm 9, lớp L01

## Trước khi gửi

| # | Việc | Ai |
|---|---|---|
| 1 | Đọc lại hai câu hỏi, sửa câu chữ; kiểm ngày trong email khớp `2.11-schedule.md` | TV1 |
| 2 | Gửi email (từ 22/10); ghi giờ gửi | TV1 |
| 3 | Thêm dòng Client Log (câu hỏi A58, giờ gửi); khi có trả lời thì ghi trả lời, tác động, lưu ảnh chụp email lên Drive và ghi tên file vào cột Bằng chứng | TV1 (từ 18/10 TV1 phụ trách Client Log) |
| 4 | Nếu thầy trả lời: cập nhật tiêu chí CP4 trong `../task2/2.5-checkpoints.md`, báo cáo mục 2.5; nếu cần đổi thứ tự công việc thì chạy lại lịch bằng config mới trong `tools/schedule/` | TV1 |
| 5 | Nếu đến 24/10 chưa có trả lời: ghi hai phương án là giả định còn mở tại A23 | TV1 |

## Ghi chú nguồn

- Bảng "Đã được trả lời" trích từ `Phản hồi 8_10.txt` do nhóm cung cấp. Chưa thấy ảnh chụp email đi kèm.
- AI Log: 2026-10-12 · Claude Code · `A58-email-xac-nhan-scope.md` · soạn và viết lại bản nháp email · cột "Nhóm đã kiểm tra" điền sau khi PM sửa và gửi.
- AI Log: 2026-10-21 · Claude Code · `A58-email-xac-nhan-scope.md` v0.3 · soạn lại email theo lịch A21 (Progress Check, kênh notification) · cột "Nhóm đã kiểm tra" điền sau khi TV1 sửa và gửi.
