# Client Interaction Log

Đề CO3011 yêu cầu log có tối thiểu: Date, Team Question, Client Response, **Impact on Project**.
Cột Impact là cột được chấm: nó phải trỏ tới một requirement, risk, estimate hoặc quyết định cụ thể.

## Quy tắc

- Ghi log **trong 24 giờ** sau mỗi lần trao đổi, khi còn nhớ nguyên văn.
- Ghi đúng ý client nói, không diễn giải. Phần suy luận của nhóm thuộc về assumptions (`task1/`).
- Mỗi câu trả lời quan trọng phải có **bằng chứng** trong `evidence/`: email, ảnh chụp tin nhắn LMS, hoặc biên bản có xác nhận.
- Sau mỗi buổi, gửi email tóm tắt cho client để xin xác nhận; lưu email đó làm bằng chứng.
- Đề cảnh báo: **tương tác client bịa đặt có thể bị xử lý như vi phạm liêm chính học thuật.** Không điền câu trả lời mà nhóm đoán.

## Mã câu hỏi

| Tiền tố | Loại |
|---|---|
| `P##` | Câu hỏi về quy trình: ai là client, kênh liên lạc, hạn nộp, dạng bằng chứng |
| `Q##` | Câu hỏi về yêu cầu dự án |

## Đặt tên bằng chứng

`evidence/<mã>-<ngày>-<mô-tả>.png`
Ví dụ: `evidence/Q03-2026-09-28-tra-loi-checkin.png`

## Nguồn dữ liệu

Bản làm việc nằm ở Sheet master, tab **Client Log**. File `client-interaction-log.md` ở đây là bản export để commit vào repo — cập nhật trước mỗi lần nộp.
