---
Nội dung: Chỉ mục giao việc W13–W14 (16–29/11), mốc sẵn sàng 29/11
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11). TV1 chốt phạm vi và lịch (D1–D5); **bước kỹ thuật là đề xuất AI, chờ TV3 và TV5 duyệt trước khi giao**; giờ do chủ task ước lượng lại. Mỗi file độc lập, không cần file đính kèm.
---

# Giao việc W13–W14

**Mục tiêu:** đến 29/11 có bản chạy được bằng Docker local, test có kết quả, UAT nội bộ, V2.0 và hồ sơ nộp đủ.

**Đã chốt (TV1, 16/11):** giữ toàn bộ Must; không làm trang quản lý đơn vị và người dùng; Docker local kèm video dự phòng; merge PR #28, hoãn PR #31; CR-02, CR-03 duyệt phương án A; lập Baseline V2.0.

| Người | File | Việc chính |
|---|---|---|
| TV1 Nguyễn Đức Nghĩa | `TV1-Nguyen-Duc-Nghia.md` | V2.0, báo cáo, planned vs actual, UAT, nộp |
| TV2 Ngô Thanh Hùng | `TV2-Ngo-Thanh-Hung.md` | Test case, chạy test API, CP3, regression, UAT |
| TV3 Phan Huy Quang Minh | `TV3-Phan-Huy-Quang-Minh.md` | Môi trường test, review chéo, kiểm chứng end-to-end, sửa lỗi |
| TV4 Nguyễn Đắc Nghĩa | `TV4-Nguyen-Dac-Nghia.md` | Giao diện lên `main`, kiểm tra từng màn hình, điện thoại |
| TV5 Hà Cao Đức Minh | `TV5-Ha-Cao-Duc-Minh.md` | Rebase PR #28, Docker local, CI tối thiểu, QR trên điện thoại, video |

## Mốc chung

| Ngày | Mốc | Phụ thuộc |
|---|---|---|
| 17/11 | Mỗi người báo hiện trạng thật trên chat; TV3 gửi hướng dẫn môi trường test cho TV2 | — |
| 19/11 | Merge PR #6 (frontend) và PR #28 (demo auth) sau review chéo; hạn điền giờ thực tế 22/10–15/11 | TV5 rebase #28; TV3, TV4, TV5 review |
| 20/11 | CP3: luồng chính chạy end-to-end, có kết quả test | Merge 19/11 |
| 22/11 | Kiểm chứng QR và CSV xong, Jira cập nhật | TV2, TV3, TV5 |
| 23–24/11 | Tích hợp và regression | CP3 |
| 24–26/11 | Sửa lỗi, đóng gói release, quay video dự phòng | Danh sách lỗi của TV2 |
| 26–27/11 | UAT nội bộ | Release |
| 28/11 | Tổng duyệt demo và viva | — |
| 29/11 | Nộp; mốc sẵn sàng | — |

## Quy tắc

- Log work Jira ngay khi làm, ghi giờ thật. Giờ hồi tưởng 22/10–15/11 ghi rõ "hồi tưởng", tự điền.
- Code qua PR; review bởi người khác tác giả trong 24h; mô tả PR nêu test đã chạy.
- Blocker báo trên chat trong ngày.
- Ghi kết quả kiểm thử đúng sự thật: đạt, không đạt, chưa chạy; nêu rõ bằng gì (thật hay mock).
- Không thêm tính năng sau 24/11; 30/11–06/12 chỉ sửa lỗi.

## Năng lực

Mỗi người khoảng 14h/tuần, tức khoảng 28h trong 16–29/11. Nếu phần việc của bạn vượt mức này, báo TV1 trong ngày 17/11 để cắt theo thứ tự Could rồi Should. TV1 có phần việc báo cáo và V2.0 nặng (R19): phần nháp có AI hỗ trợ, TV1 duyệt.
