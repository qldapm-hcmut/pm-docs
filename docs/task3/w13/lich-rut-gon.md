---
Nội dung: Lịch rút gọn về mốc sẵn sàng 29/11 và điều chỉnh task
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11). Ngày và giờ là đề xuất, chưa phải lịch của nhóm. Bước kỹ thuật chờ TV3, TV5 duyệt; TV2, TV4 xác nhận phần của mình. TV1 chưa duyệt.
---

# Lịch rút gọn

## 1. Cơ sở

- Baseline V1.0: A41 UAT 01–05/12, A47 nộp 06–07/12, demo 07/12, 0 ngày dự trữ. Giữ nguyên V1.0 làm tham chiếu.
- Thầy thông báo hai tuần cuối các nhóm demo và viva; TV1 muốn chừa 1 tuần. Mốc nộp 06/12 lùi 7 ngày thành **29/11 (Chủ nhật)**; 30/11 đến 06/12 là tuần dự trữ trước slot demo. Ngày của nhóm: [chờ thầy xếp].
- Còn 14 ngày (16–29/11). Năng lực mỗi người khoảng 14h/tuần (E01), tức khoảng 28h trong 2 tuần.
- Phần còn lại theo bằng chứng 16/11:
  - Backend đã có code trên `main` cho hầu hết Must, **chưa có kết quả kiểm thử nào** trong `docs/quality/results/` (chưa kiểm chứng ở 16/11; TV2 xác nhận).
  - Frontend: có trên nhánh, chưa vào `main`.
  - Chưa có CI, deploy, test case, quality plan.
  - Báo cáo: 49 `\todo` (xem `bao-cao-hoan-thien.md`).

Effort tham chiếu của baseline cho phần còn mở (không phải số còn lại thật; backend đã làm phần lớn nên owner phải tự ước lượng lại):

| Nhóm việc | Activity | Effort baseline (h) |
|---|---|---:|
| Frontend | A28, A35 (chưa tính phần FE nằm trong A26, A27, A29) | 25,3 |
| Hạ tầng | A24, A20 | 14,6 |
| Kiểm thử (tổng activity, chia chung nhiều người) | A22, A31, A40, A30, A39, A41 | 52,5 |
| Tích hợp và sửa lỗi | A37, A53 | 21,0 |

Nút thắt lớn nhất là **kiểm thử** và **merge frontend**, không phải backend.

## 2. Phương án

**TV1 chốt 16/11: P-A, kèm bỏ UI quản trị đơn vị và người dùng** (thiết lập bằng seed hoặc admin CLI; PR #6 hiện không có trang này). Mốc sẵn sàng 29/11 (D1).

| Phương án | Nội dung | Đánh đổi |
|---|---|---|
| **P-A (AI khuyến nghị)** | Giữ toàn bộ Must; mốc sẵn sàng 29/11; email và phần Should chưa xong thì cắt; triển khai = Docker local kèm video dự phòng, hosting chỉ làm nếu dư giờ | Giảm phạm vi Should; cần TV2 tham gia từ tuần này |
| P-B | Như P-A, nhưng màn hình quản trị (đơn vị, người dùng) chỉ demo bằng API, UI chỉ làm 3 vai trò luồng chính | Mất UI phần quản trị; giảm tải TV4 |
| P-C | Giữ lịch gốc 07/12, không chừa tuần dự trữ | Trái thông báo của thầy; 0 ngày dự trữ; **không khuyến nghị** |

Quy tắc cắt giữ nguyên baseline: cắt Could rồi Should; không bỏ luồng cốt lõi (tạo sự kiện → duyệt → đăng ký/hủy → capacity + waitlist + tự chuyển → QR check-in → báo cáo/CSV, Q08, Q10). Quỹ A38 (30h) giữ nguyên cho change event Q17; dùng cho việc khác phải ghi quyết định.

## 3. Mốc theo P-A

| Ngày | Mốc | Người chính | Điều kiện hoàn thành |
|---|---|---|---|
| 16–17/11 | TV1 chốt D1–D3; Jira đồng bộ; mỗi người báo hiện trạng thật (code ở máy riêng, giờ) | TV1, cả nhóm | Thread chat có đủ 5 người |
| 19/11 (Thứ Năm) | Merge FE PR #6 và BE PR #28 vào `main` sau review chéo | TV3, TV4, TV5 | Có approve của người khác tác giả; Docker chạy được luồng chính từ `main` |
| 19/11 | Thu xong giờ thực tế 22/10–15/11 | Cả nhóm; TV1 tổng hợp | Time Tracking có dòng của 5 người |
| 20/11 (Thứ Sáu) | **A30/CP3: Increment 1 chạy end-to-end** (kịch bản D1 + UI) | TV2 chủ trì | Kết quả test lưu `docs/quality/results/`; ghi deviation so với 16/11 |
| 16–22/11 | A31, A40 viết và chạy test case trên API đã merge (không chờ UI) | TV2 | Test case có mã T-…, kết quả đạt/không đạt |
| 22/11 | A33, A34 kiểm chứng (QR, CSV) và đóng trên Jira | TV3, TV2 | Có kết quả test; nếu chưa kiểm chứng thì không ghi Done |
| 23–24/11 | A37 tích hợp luồng chính; A39 regression | TV3, TV4, TV2 | Luồng chính đạt trên bản `main` |
| 24–26/11 | A53 sửa lỗi, đóng gói bản release; quay video dự phòng | TV3, TV5, TV4 | Tag bản release; video quay xong |
| 26–27/11 | A41 UAT nội bộ theo tiêu chí PD | TV2, TV1 | Biên bản UAT; có mời thầy hay không: [TV1 quyết] |
| 28/11 | A46 tổng duyệt demo và viva (ai cũng có thể bị hỏi) | Cả nhóm | Mỗi người trả lời được estimate, rủi ro, thay đổi lịch, client, scope |
| **29/11** | **A47 nộp: báo cáo PDF, link repo và hướng dẫn chạy, V1.0 và bản sửa, logs, khai báo AI** | TV1 | Checklist nộp đủ |
| 30/11–06/12 | Dự trữ: chỉ sửa lỗi; chờ slot demo | Cả nhóm | Không thêm tính năng |

Chạy song song: A45 báo cáo 17–27/11; A42 (planned vs actual) 20–25/11 sau khi có giờ; A43 (closure) 23–25/11; A44 (retrospective) 26/11; A36, A57 liên tục đến nộp.

## 4. Task điều chỉnh

| Activity | Tình trạng 16/11 | Điều chỉnh đề xuất |
|---|---|---|
| A30 CP3 | Hạn 16/11, Jira Backlog | Dời 20/11; đổi tiêu chí thành "luồng chính chạy end-to-end, có test" |
| A32 Plan increment 2 | Backend increment 2 đã có code | Đóng; thay bằng tài liệu này |
| A33, A34 | Code đã merge, Jira còn Backlog | Chuyển In Review; đóng sau khi TV2 có kết quả test |
| A24 | Chưa có CI, deploy | Thu hẹp: Docker local + một workflow chạy test và build làm bằng chứng chất lượng; hosting là Could. Giờ: [TV5 ước lượng] |
| A20 Spike QR | PR #15 QR đã merge | Đóng bằng kết quả kiểm chứng QR trên điện thoại (R04); nếu bỏ spike phải ghi lý do |
| A35 Check-in và report UI | Có trên nhánh | Gộp vào PR #6; hoàn thành khi chạy trên `main` |
| A39 + A53 | Hạn 27/11, 30/11 | Dời lên 23–26/11, chồng nhau |
| A41 | 01–05/12 | Dời 26–27/11 |
| A42, A43, A44, A45, A46, A47 | Hạn cuối 26/11–07/12 | Dời theo mục 3; A47 = 29/11 |
| A38 | Chưa dùng | Giữ 30h cho Q17 |
| Thêm mới | — | Nếu D4 chọn "lập CR" thì thêm activity xử lý CR; không tự thêm khi TV1 chưa duyệt |

## 5. Rủi ro và điều kiện

- Lịch không còn dự trữ trong 16–29/11; chuỗi găng: merge FE → kiểm thử → sửa lỗi → UAT → nộp. Nếu PR #6 chưa merge trước 20/11 thì chuyển sang P-B.
- Một người viết toàn bộ backend (R24): review chéo bắt buộc trước khi merge để có bằng chứng chất lượng.
- Time Tracking còn thiếu: chưa có độ lệch effort tin cậy; không báo tỷ lệ hoàn thành từ số giờ hiện có.
- Q17: thầy có thể đưa change event muộn; với mốc 29/11, phần xử lý phải nằm trong A38.
