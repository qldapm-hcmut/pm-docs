---
Thành viên: TV2, Ngô Thanh Hùng (2311289)
Vai trò: Kiểm thử (Tester)
---

# Contribution & reflection — Ngô Thanh Hùng

## Thẻ bằng chứng

Tổng giờ trên Jira: 28,0 giờ (giờ từng việc xem worklog Jira).

| Activity | Việc đã làm | Effort TT (h) | Sản phẩm tạo ra | Quyết định của tôi và lý do | Bằng chứng (commit / MR / tài liệu) |
|---|---|---|---|---|---|
| A22 | Viết quality plan, chốt v1.0 ngày 19/11 | | Quality plan v1.0 | Tiêu chí đạt của increment: mọi ca Must đã chạy đều đạt và không còn defect nghiêm trọng đang mở | [2.12-quality-plan.md](../task2/2.12-quality-plan.md) |
| A31, A40 | Viết 35 test case có mã T-…, khớp bảng truy vết | | Bộ test case Increment 1, 2 | Viết theo API đã merge vì lúc đó frontend chưa lên `main` | [test-cases.md](../quality/test-cases.md) |
| A30 | Kiểm thử API trước CP3 (18/11), quét QR bằng điện thoại thật (19/11) | | Kết quả CP3, D01, D02 | T-CI-03 ghi theo số đo thật từ log máy chủ, không ghi đạt khi chưa đủ ba thiết bị | [results/](../quality/results/), [defects.md](../quality/defects.md) |
| A39 | Hồi quy ngày 20/11: hai lượt độc lập (Go, API, build FE, E2E 13 ca) | | Báo cáo hồi quy | Chọn bản kiểm thử theo D4 (bỏ PR #31 BE); chạy hai lượt để đối chiếu | [regression-2026-11-20.md](../quality/results/regression-2026-11-20.md) |
| A41 | UAT nội bộ: tự đi tay toàn bộ luồng ngày 24/11, E2E trên `main` ngày 27/11 | | Kịch bản UAT-01..15, biên bản 27/11 | Dùng E2E trên `main` thay cho đi tay lại; kết luận chờ TV1 xác nhận | [uat/](../quality/uat/), pm-docs PR #14 |
| Kiểm thử lại 27/11 | API 30/30 nhóm, Go 606/606, FE 5/5, E2E 11/13 rồi 13/13 sau PR #12 | | Kết quả trên `main`; D01, D02 đóng; D03 mới | Truy nguồn gốc D03 và so sánh bản gốc với bản sửa trước khi merge | [main-2026-11-27.md](../quality/results/main-2026-11-27.md) |
| Sửa D03 | Trang check-in trắng khi không có camera: chờ camera khởi động xong mới tắt | | FE PR #12 (merge 27/11, `ff9ea2d`) | Chỉ sửa `QrScanner.jsx`; kiểm bốn tình huống camera | ticket-system-uni-fe PR #12 |
| A43 | Soạn bản nháp kế hoạch đóng dự án và bàn giao | | Bản nháp 4.4 | Các mục export, quyền Sheet, người nhận bàn giao để TV1 chốt | [4.4-closure-handover.md](../task4/4.4-closure-handover.md) |

## Contribution statement

Tôi chịu trách nhiệm chính phần kiểm thử của dự án: quality plan, bộ 35 test case, các lượt kiểm thử ngày 18–20/11 và 27/11, sổ defect D01 đến D03, UAT nội bộ (A41) và bản nháp kế hoạch bàn giao (A43). Tôi sửa D03 ở frontend (PR #12). D01 và D02 do TV3 sửa (PR #35, #34); phần của tôi là phát hiện hai lỗi này và kiểm lại.

## Reflection

### Điều tôi học được về quản lý dự án

Kiểm thử là một việc trên đường găng chứ không phải bước cuối. Khi frontend chưa lên `main`, tôi kiểm thử thẳng trên API đã merge, nên nhóm có kết quả từ 18/11. Ghi đúng số đo cũng quan trọng ngang kết quả đạt: T-CI-03 mới có một thiết bị, và tôi ghi rõ như vậy thay vì ghi đạt. Chạy lại toàn bộ trên `main` sau mỗi đợt merge là cần thiết: lượt 27/11 tìm ra D03 và sửa xong trong ngày, trước demo.

### Một quyết định tôi sẽ làm khác nếu làm lại, và vì sao

Tôi sẽ đề xuất CI chạy test backend và E2E cho mỗi PR ngay từ đầu. Đến 23/11 cả hai repo vẫn chưa có workflow CI, nên test chỉ chạy khi tôi tự chạy trên máy mình, theo từng đợt, chứ không tự chạy sau mỗi PR. Tôi cũng sẽ viết test case ngay khi chốt yêu cầu.

### Artifact của người khác mà tôi đã nắm được (chuẩn bị viva)

- Hợp đồng API và backend của TV3 (`api/openapi.yaml`, waitlist FIFO, quy tắc tự duyệt), vì bộ API test dựa trên chúng.
- Luồng check-in QR và giao diện của TV4 (A35), qua lúc truy và sửa D03.
- PR #6 của TV5 (tích hợp luồng, Docker), bản tôi ghép để chạy hồi quy A39.
- Baseline V2.0 và D-list của TV1, dùng để chọn bản kiểm thử (D4).
