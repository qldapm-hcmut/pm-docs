---
Mã: CR-02
Ngày nhận: 01/11/2026
Người yêu cầu: TV1 (phát hiện khi đối chiếu hợp đồng API với Client Log)
Người phân tích: TV1, TV3
Trạng thái: đã duyệt phương án A (TV1, 16/11/2026); effort lấy từ log work TV3
---

# CR-02 — Phạm vi xem dữ liệu rộng hơn Q20

AI hỗ trợ soạn; đã bổ sung phản hồi của TV3 (TV1 chuyển 01/11/2026); còn thiếu effort và ảnh hưởng lịch, chưa duyệt.

## Mô tả thay đổi và lý do

| Vai trò | Thầy đã đồng ý (Q20, 08/10) | Hợp đồng API hiện tại |
|---|---|---|
| Organizer | Chỉ xem sự kiện của mình | Mọi sự kiện thuộc đơn vị được gán |
| Admin | Xem theo đơn vị được giao | Xem và duyệt toàn trường |

Lý do ghi trong hợp đồng API: ngày sự kiện cần nhiều người cùng check-in và có người làm thay khi người tạo vắng; Admin là quản trị viên cấp trường.

TV3 đề xuất giữ Organizer theo đơn vị và Admin toàn trường, ghi rõ là nhóm tự quyết định.

Nhóm không hỏi thầy về thay đổi này (TV1 chốt 01/11). Báo cáo phải ghi đây là quyết định của nhóm, không ghi là client đồng ý.

## Phân tích tác động

| Hạng mục | Tác động | Chi tiết |
|---|---|---|
| Requirements / products | Có | Quyền xem dữ liệu ở PD-01 và các mục dẫn Q20; [TV1 rà khi duyệt] |
| Activities (thêm, bỏ, sửa) | [TV3 xác nhận] | |
| Effort (h) | Chưa xác nhận | TV3 còn rà effort tài liệu và test; [TV3 điền số giờ] |
| Resources | Không | |
| Risks | Có | Nhiều người xem được dữ liệu cá nhân hơn (Q09); hợp đồng API giảm bớt bằng cách chỉ gán Organizer cho người cần |
| Schedule, critical path | Chưa xác nhận | TV3 chưa khẳng định không ảnh hưởng lịch |
| Cost | [TV3 xác nhận] | |
| Quality, test | Có | [TV2 bổ sung ca kiểm tra quyền xem theo đơn vị] |

## Phương án

| Phương án | Mô tả | Ưu | Nhược | Effort | Ảnh hưởng mốc |
|---|---|---|---|---|---|
| A | Giữ theo hợp đồng API, ghi là quyết định của nhóm | Không đổi thiết kế; nhiều người cùng quét được | Khác nội dung đã thống nhất với client | [TV3] | [TV3] |
| B | Sửa code về đúng Q20 | Khớp nội dung client đã đồng ý | Cần cách giao người trực check-in và Admin theo đơn vị | [TV3] | [TV3] |

## Quyết định

**Phương án chọn:** TV1 định hướng A ngày 01/11, TV3 cùng đề xuất A; chốt sau khi TV3 xác nhận effort và lịch.

**SỬA 16/11/2026:** TV1 duyệt phương án A. Đây là quyết định của nhóm, không ghi là client đồng ý. Code (quản trị đơn vị, PR #23, merge 09/11, và phạm vi xem theo đơn vị) được làm trước khi có CR; CR này ghi nhận sau. Effort: chưa có, lấy từ log work của TV3, không ước đoán.

**Lý do:** [TV1 điền]

**Người duyệt và ngày duyệt:** TV1, 16/11/2026

**Có cần Baseline V2.0 không:** Có, đưa vào danh sách thay đổi của Baseline V2.0 (TV1 chốt 16/11).
