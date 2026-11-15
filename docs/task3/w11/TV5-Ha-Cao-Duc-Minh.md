---
Nội dung: Giao việc W11 (02–08/11) cho TV5
Người nhận: Hà Cao Đức Minh (TV5, Backend, DevOps)
Phiên bản: 0.3 (02/11: cập nhật theo PR #15 đang mở)
Giờ đề xuất: 14h (A24 8h, A20 6h, gồm review PR #15)
Trạng thái: AI hỗ trợ soạn (Claude Code, 01–02/11); TV1 duyệt hướng làm 01/11, đồng ý cập nhật 02/11; số giờ và bước kỹ thuật là đề xuất AI, chờ TV3, TV5 duyệt
---

# TV5: W11

Trên Jira, A24 và A20 đang Backlog (hạn 28/10, 24/10). A20 chưa làm (TV1 xác nhận 01/11). Nếu A24 đã làm phần nào, đẩy lên, cập nhật trạng thái và log giờ thật.

## A24 CI và deploy (8h)

**Mục tiêu:** mỗi PR tự chạy kiểm tra; có link deploy để demo 09/11.

**Đầu vào:** repo `ticket-system-uni` (đã có `compose.yaml`, `Makefile` với `lint`, `test`, `test-int`, `migrate-up`, `seed`); chưa có workflow CI và Dockerfile.

**Các bước:**
1. **[Cần TV5 quyết]** hosting free-tier cho API và PostgreSQL (ASM-05), có HTTPS vì camera trên trình duyệt cần HTTPS.
2. Thêm CI chạy `make lint`, `make test`, và `make test-int` nếu dựng được PostgreSQL trên CI.
3. Đóng gói và deploy API, worker, chạy migration và seed tài khoản mẫu. Sau khi PR #15 merge, API cần thêm `QR_HMAC_SECRET` (ít nhất 32 byte, khác `JWT_SECRET`).
4. Deploy frontend khi TV4 có bản chạy được.
5. Điền thông tin CI vào `docs/setup-tools.md` mục 2 của `pm-docs`. Secret để trong biến môi trường, không commit.

**Đầu ra:** CI chạy trên PR; link deploy; hướng dẫn trong README.

**Hoàn thành khi:** PR mẫu có kết quả CI; `GET /health/ready` trên link deploy trả về thành công; TV2 test được trên deploy trước 05/11.

## A20 Spike QR (timebox 6h, cùng TV3)

**Mục tiêu:** trả lời quét QR trên trình duyệt điện thoại có dùng được không, mất bao lâu, cần dự phòng thế nào, theo mô hình Organizer quét QR trên điện thoại sinh viên.

**Lý do làm ngay:** backend QR đã có ở PR #15 nhưng chưa ai đo việc quét trên điện thoại. Kết quả spike cần có trước khi chốt PR #15 và màn hình quét ở A35.

**Các bước:**
1. Review PR #15. Cùng TV3 chọn thư viện quét QR trên trình duyệt.
2. Chạy prototype qua HTTPS trên ≥ 3 thiết bị thật, mỗi thiết bị ≥ 10 lần, lấy median. Dùng mã có độ dài như token thật của PR #15, khoảng 141 ký tự.
3. Ghi lỗi gặp phải (quyền camera, lấy nét) và thử nhập mã dự phòng.
4. Không chứa họ tên, MSSV, email trong mã QR.

**Đầu ra:** `A20-spike-qr.md` có số đo thật, nộp vào thư mục W11 trên Drive; cập nhật R04 và Jira.

**Hoàn thành khi:** có kết luận và median trên ≥ 3 thiết bị. Hết 6h thì dừng, ghi lại những gì đã biết.

## Hỗ trợ frontend

TV3 nhận phần hỗ trợ chính. TV5 chỉ nhận thêm khi A24, A20 xong trước hạn và còn giờ trong mức 14–16h/tuần.
