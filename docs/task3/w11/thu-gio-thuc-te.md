---
Nội dung: Thu giờ thực tế 22/10–08/11 (đóng I02 cho giai đoạn Increment 1)
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 08/11/2026
Trạng thái: Nháp AI (Claude Code, 08/11). TV1 duyệt trước khi gửi nhóm.
---

# Thu giờ thực tế 22/10–08/11

## Vì sao cần

- Time Tracking trong Sheet mới 52,5h, dừng ở 22/10; Jira có 9h, chỉ của TV1.
- Progress Check cần actual effort và lịch so với V1.0. Không có giờ thật thì không có độ lệch.
- Chỉ ghi giờ **thật**. Không ước cho đủ; không điền hộ người khác.

## Tin nhắn gửi nhóm (chat)

> Mọi người ghi lại giờ làm thật từ 22/10 đến hết 08/11 cho từng activity (A20, A22, A24, A25, A26, A27, A28, A29, A31, A33, A62, A34, A36, A51...). Trả lời theo mẫu: `Ngày | Activity | Số giờ | Link (PR/tài liệu) | Ghi chú`. Chỉ ghi việc đã làm; chưa làm thì ghi 0 hoặc bỏ trống, đừng ước. Giờ hồi tưởng ghi rõ "ước tính hồi tưởng". Hạn: [TV1 điền, đề xuất trước 15h Chủ nhật 08/11 để rà ở họp]. Từ nay log work trên Jira ngay khi làm.

## Mẫu dán vào tab 3

`sheet-import/3-time-tracking-22-10-08-11-mau.tsv`: mỗi dòng đã có người, activity, link PR (nếu là PR của TV3). **Cột Giờ để trống**, người làm tự điền.

## Sửa lỗi định dạng tab 3 (hai ô)

- `E5` (TV3, A02) và `E16` (TV3, A09) đang là **ngày** (1 tháng 5), vì nhập "1.5" trong Sheet đặt ngôn ngữ vi_VN. Hậu quả: tab 11 hiện Effort TT của A02 là 46144,0 và A09 là 46144,5.
- Cách sửa: nhập `1,5` (dấu phẩy) và đặt định dạng ô là số. Sau đó tab 11: A02 phải còn 2,5 và A09 phải còn 3,0 (nếu TV2 đã nhập 1 và 1,5). Kiểm lại sau khi sửa.
- Chưa sửa trực tiếp trên Sheet.

## Quy trình rà

1. Nhóm gửi giờ qua chat.
2. TV1 chuyển thành dòng tab 3 (cột Ghi chú: nguồn, hồi tưởng hay log Jira).
3. Điền cột Effort TT (G) và Chênh lệch (H) của Weekly Log W10, W11; cập nhật `task3/planned-vs-actual.md`.
4. Từ W12: mỗi Chủ nhật xuất Jira CSV (all fields, cột Log Work) để cộng.
