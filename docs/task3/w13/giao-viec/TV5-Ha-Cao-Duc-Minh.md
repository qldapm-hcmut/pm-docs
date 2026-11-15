---
Nội dung: Giao việc W13–W14 (16–29/11) cho TV5
Người nhận: Hà Cao Đức Minh (TV5, Backend, DevOps)
Phiên bản: 0.1
Giờ: do TV5 ước lượng lại trước 20/11 (tham chiếu baseline V1.0: A24 8,9h; A20 5,7h; A53 12,6h chia chung)
Trạng thái: Nháp AI (Claude Code, 16/11); TV1 chốt phạm vi 16/11 (Docker local, không bắt buộc hosting); **bước kỹ thuật là đề xuất AI, chờ TV5 và TV3 duyệt**
---

# TV5: W13–W14

A24 và A20 đang quá hạn. Phạm vi A24 đã thu hẹp: **Docker chạy local + CI tối thiểu**; hosting không bắt buộc (làm nếu dư giờ).

## Task 1: Rebase và merge PR #28 (hạn 19/11)

**Mục tiêu:** PR #28 (demo auth, seed data, Docker, kiểm tra lịch sự kiện) vào `main`.

**Đầu vào:** PR #28 (+855/−78, 33 file) đang xung đột sau PR #30 (refactor).

**Các bước:**
1. Rebase lên `main`; giải xung đột, đặc biệt `internal/event/*`, `internal/db`, `db/queries`; chạy `make sqlc` nếu SQL đổi.
2. `make lint`, `make test`; `make test-int` nếu có `TEST_DATABASE_URL`.
3. Cập nhật mô tả PR: test đã chạy; nhờ TV3 review chéo.
4. Đăng nhập demo chỉ dùng cho local và demo (CR-03).

**Hoàn thành khi:** PR #28 merge sau review của TV3; tài khoản mẫu ba vai trò dùng được.

**Phụ thuộc:** TV3 review.

## Task 2: Docker local chạy từ `main` (A24, hạn 20/11)

**Mục tiêu:** một cách chạy lặp lại được cho cả bản demo và hồ sơ nộp ("link repo và hướng dẫn chạy").

**Đầu vào:** `compose.yaml` backend (hiện có Postgres); Dockerfile, `nginx.conf` trong PR #6 (frontend); Docker support trong PR #28.

**Các bước:** thống nhất cùng TV3, TV4 cách chạy toàn bộ (Postgres, migration, seed, API, worker, frontend); viết hướng dẫn từng lệnh trong README; thử từ máy sạch (không có sẵn môi trường của bạn); ghi các biến `.env` cần thiết (`DATABASE_URL`, `JWT_SECRET`, `QR_HMAC_SECRET`, `GOOGLE_CLIENT_ID`, `VITE_*`), không commit khóa thật.

**Đầu ra:** README có hướng dẫn chạy; checklist chạy thử.

**Hoàn thành khi:** thành viên khác (TV2 hoặc TV4) chạy được từ hướng dẫn mà không cần hỏi (T-DEP-01).

**Phụ thuộc:** merge PR #6, #28.

## Task 3: CI tối thiểu (A24, hạn 22/11)

**Mục tiêu:** có bằng chứng chất lượng tự động; không dựng hạ tầng riêng.

**Các bước (chờ TV3 đồng ý):** workflow GitHub Actions: backend `go vet ./...` và `go test -race ./...`; frontend `npm ci` và `npm run build`. Lưu log hoặc badge vào `docs/quality/` trước checkpoint (log CI có thể xoay vòng).

**Hoàn thành khi:** workflow chạy xanh trên `main` của hai repo; nếu cần cấu hình thêm thì ghi rõ giới hạn.

## Task 4: Kiểm chứng QR trên điện thoại (A20, R04; 19–22/11)

**Mục tiêu:** có kết quả thật về quét QR, kết thúc spike A20.

**Các bước:** cùng TV3, TV4: lấy QR từ "Đăng ký của tôi" (token dài khoảng 141 ký tự), quét bằng Organizer trên điện thoại; đo thời gian (mục tiêu median ≤ 5 giây, T-CI-01..03), thử QR trùng, nhập mã, xác nhận thủ công (T-CI-04..05). **Cần xác minh:** trình duyệt chỉ bật camera trên HTTPS hoặc `localhost`; ghi cách đã thử và kết quả, kể cả khi thất bại.

**Hoàn thành khi:** ghi kết quả (số lần thử, thời gian, thiết bị); Jira A20 đóng bằng kết quả này, hoặc ghi lý do nếu bỏ spike.

## Task 5: Release và video dự phòng (A53, 24–26/11)

- Gắn tag release trên hai repo, hướng dẫn chạy khớp tag.
- Quay video dự phòng chạy kịch bản: tạo sự kiện → duyệt → đăng ký → waitlist → hủy → tự chuyển → check-in → báo cáo; ghi rõ là bản ghi.
- Review chéo PR backend (R24): cùng TV3 nếu cần.

**Giờ thực tế:** điền tab 3 trước 19/11 (A24, A20, review PR #15…); log work Jira từ 16/11. Hosting free-tier chỉ làm khi mọi việc trên xong.
