---
Mã: CR-01
Ngày nhận: 01/11/2026
Người yêu cầu: TV1 (phát hiện khi đối chiếu PD-03 với hợp đồng API)
Người phân tích: TV1
Trạng thái: đã duyệt
---

# CR-01 — Chỉ Organizer được điểm danh

AI hỗ trợ soạn; TV1 duyệt ngày 01/11/2026.

## Mô tả thay đổi và lý do

PD-03 ghi "chỉ Organizer của sự kiện hoặc Admin được điểm danh (Q20)". Hợp đồng API (`docs/db-schema-and-api-contract.md`, `api/openapi.yaml` của repo `ticket-system-uni`) ghi vai trò Admin không cho quyền check-in.

Sửa PD-03 theo hợp đồng API. Lý do: Admin đã phụ trách duyệt sự kiện, không cần thêm quyền ghi nhận tham dự. Q20 quy định quyền xem dữ liệu, không quy định quyền điểm danh, nên không phải căn cứ cho câu cũ.

## Phân tích tác động

| Hạng mục | Tác động | Chi tiết |
|---|---|---|
| Requirements / products | Có | PD-03 (S34): sửa tiêu chí chất lượng. REQ-10, REQ-11 không đổi |
| Activities (thêm, bỏ, sửa) | Không | A33, A35 giữ nguyên |
| Effort (h) | Không đáng kể | Hợp đồng API đã theo hướng này; chỉ thêm test case |
| Resources | Không | |
| Risks | Không | |
| Schedule, critical path | Không | |
| Cost | Không | |
| Quality, test | Có | TV2 thêm ca: Admin không phải Organizer bị từ chối; Organizer không tự điểm danh cho đăng ký của mình |

## Phương án

| Phương án | Mô tả | Ưu | Nhược | Effort | Ảnh hưởng mốc |
|---|---|---|---|---|---|
| A | Sửa PD-03 theo hợp đồng API | Không đổi code; quyền rõ ràng | Sửa nội dung PD đã duyệt | Không đáng kể | Không |
| B | Sửa code cho Admin được điểm danh | Giữ nguyên PD-03 | Đổi hợp đồng API và kiểm thử quyền | [TV3 ước lượng nếu chọn] | Có thể ảnh hưởng A33 |

## Quyết định

**Phương án chọn:** A.

**Lý do:** không phát sinh việc code, và câu cũ dựa trên Q20 không đúng phạm vi.

**Người duyệt và ngày duyệt:** TV1, 01/11/2026.

**Có cần Baseline V2.0 không:** không cần riêng cho CR này; nếu sau này lập Baseline V2.0 thì liệt kê CR-01 trong các mục thay đổi so với V1.0.
