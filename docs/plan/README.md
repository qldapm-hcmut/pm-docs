# Trang kế hoạch dự án

`index.html` — một file HTML tự chứa, mở trực tiếp bằng trình duyệt (không cần server).

## Sửa ở đâu

| Muốn sửa | Tìm trong `<script>` |
|---|---|
| Activity, effort, thời lượng, phụ thuộc, owner | mảng `ACT` |
| Nội dung chi tiết từng activity | object `DETAILS` |
| Ngày bắt đầu dự án | `DEFAULT_START` |
| Tuần nghỉ | `BREAK` |
| Đường mốc trên Gantt | `COURSE_MARKS` |
| Risk register đề xuất | mảng `RISKS` |
| Câu hỏi client | `QUESTIONS`, `PQUESTIONS` |

CPM, Gantt, bảng phân tích mạng và bảng tải tự tính lại khi `ACT` thay đổi.

Khi Baseline V1.0 đã duyệt, mọi thay đổi `ACT` phải đi kèm Change Request.
