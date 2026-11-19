# Kết quả kiểm thử hồi quy A39 (20/11/2026)

- **Ngày chạy:** 20/11/2026. Người phụ trách: TV2. Hai lượt độc lập chạy bằng Claude Code và Codex (ghi trong [AI log](../../ai-usage.md)), cùng một bản, môi trường Docker tách riêng, sau đó đối chiếu kết quả.
- **Bản kiểm thử (bản demo):** backend `main` tại `a964e194165e9f1f559b55918941596441c0b375` (đã có PR #28, #33). Frontend `main` tại `b4847e9` ghép PR #6 (`feat/local-demo-integration`, `84c38cb`) trên máy, merge sạch, chưa merge trên GitHub. Theo D4 (TV1, 16/11), PR #31 backend hoãn nên không thuộc bản này.
- **Môi trường:** Go 1.27.4, PostgreSQL 16 (client `psql` 18.1 cho integration test), Node 24.11.1, `AUTH_MODE=local`, tài khoản demo và dữ liệu tổng hợp. Lượt 1 dùng Docker Compose của backend (postgres, migrate, api, worker, web nginx) và Google Chrome 157 headless qua Playwright 1.65.1 (Node). Lượt 2 dựng từng container bằng `docker run` (postgres, api, web nginx) và Chromium 156 headless qua Playwright cho Python.
- **Bằng chứng (lượt 1):** [log HTTP bộ API, đã ẩn token và mã check-in](regression-2026-11-20-api.ndjson); [kết quả E2E](regression-2026-11-20-e2e/results.json), [ảnh từng bước](regression-2026-11-20-e2e/shots/), [log mạng E2E đã ẩn mã](regression-2026-11-20-e2e/network.ndjson), [script E2E](regression-2026-11-20-e2e/cp3-ui.mjs). Ảnh chụp có QR và mã check-in của dữ liệu thử trên máy, cơ sở dữ liệu đã xóa sau lượt chạy.

## Tóm tắt

**Toàn bộ test đã chạy đều đạt, trừ hai defect đã biết D01 và D02.** Hai lượt độc lập cho cùng số liệu.

| Phần | Lượt 1 (Claude Code) | Lượt 2 (Codex) | So với CP3 18/11 |
|---|---|---|---|
| Go build, vet | Đạt | Đạt | CP3 không ghi riêng |
| Go integration (`go test -count=1 -tags integration ./...`) | 29 package, 605 test/subtest đạt, 0 lỗi | 29 package, 605 đạt, 0 lỗi | Như cũ |
| Bộ API CP3 (114 request) | 28/30 nhóm đạt | 28/30 nhóm đạt | Như cũ |
| Frontend `npm ci`, `npm run build`, unit test | Đạt, 5/5 test | Đạt, 5/5 test | Mới (lần đầu chạy trên bản ghép) |
| E2E trình duyệt: 10 bước CP3 + 3 ca lỗi | 12/13 đạt, ca tự duyệt không đạt (D02) | 12/13 đạt, ca tự duyệt không đạt (D02). Bước 6 lượt 2 ghi "một phần" vì UI không hiện thông báo | Mới, tự động hóa lượt UI 19/11 |

## E2E trên giao diện

Mỗi vai một phiên trình duyệt riêng: Organizer, Admin, Student A, Student B, đăng nhập bằng cách dán token demo (`cmd/dev-token`) vào trang đăng nhập local. Mọi thao tác ghi dữ liệu đều đi qua UI, ngoại trừ: tạo hai Student bằng cách đổi email user demo; ca C2 công bố sự kiện phụ trực tiếp trong DB để bỏ bước duyệt; ca C3 nâng tạm quyền Admin cho Organizer trong DB rồi trả lại. Script đọc DB để đối chiếu (trạng thái đăng ký, thông báo, mã check-in) nhưng không sửa dữ liệu ở các bước chính. Bảng dưới là quan sát của lượt 1; lượt 2 cho cùng kết quả.

| Bước | Kết quả | Quan sát (lượt 1) | Ảnh |
|---|---|---|---|
| 1. Organizer tạo sự kiện (sức chứa 1, hàng chờ 2), gửi duyệt | Đạt | POST 201, submit 200 | [01](regression-2026-11-20-e2e/shots/01-organizer-gui-duyet.png) |
| 2. Admin duyệt và công bố | Đạt | approve 200, PUBLISHED | [02](regression-2026-11-20-e2e/shots/02-admin-duyet.png) |
| 3. Student A đăng ký | Đạt | 201 REGISTERED | [03](regression-2026-11-20-e2e/shots/03-studentA-dang-ky.png) |
| 4. Student B vào hàng chờ | Đạt | 201 WAITLISTED, vị trí 1 | [04](regression-2026-11-20-e2e/shots/04-studentB-hang-cho.png) |
| 5. Student A hủy khi còn hơn 24 giờ | Đạt | 200 CANCELLED | [05](regression-2026-11-20-e2e/shots/05-studentA-huy.png) |
| 6. Student B tự lên chỗ | Đạt | B thành REGISTERED trên UI và trong DB, có đúng 1 thông báo `PROMOTED` trong DB. FE chưa có màn hình xem thông báo (xem mục Quan sát) | [06](regression-2026-11-20-e2e/shots/06-studentB-len-cho.png) |
| 7. Organizer dời giờ bắt đầu về khoảng 30 phút tới | Đạt | PATCH 200. Hạn đóng đăng ký dời về 20 phút tới để lịch hợp lệ | [07](regression-2026-11-20-e2e/shots/07-organizer-doi-gio.png) |
| 8. Student B mở vé | Đạt | Có QR và mã check-in đúng | [08](regression-2026-11-20-e2e/shots/08-studentB-qr.png) |
| 9. Organizer check-in B bằng tab Nhập mã, rồi nhập lại | Đạt | 201 `CODE`; lần hai 409 `ALREADY_CHECKED_IN` | [lần 1](regression-2026-11-20-e2e/shots/09-checkin-lan1.png), [lần 2](regression-2026-11-20-e2e/shots/09-checkin-lan2.png) |
| 10. Organizer xem thống kê và tải CSV | Đạt | 1 đăng ký, 1 check-in, 100%; CSV tải được | [10](regression-2026-11-20-e2e/shots/10-bao-cao-csv.png) |
| C1. Student hủy khi còn dưới 24 giờ (mã `7b` trong results.json) | Đạt | 422 `CANCEL_DEADLINE_PASSED`, UI báo "Đã quá hạn hủy đăng ký" | [7b](regression-2026-11-20-e2e/shots/07b-huy-qua-han.png) |
| C2. Check-in ngoài khung giờ | Đạt | 422 `CHECKIN_WINDOW_CLOSED`, UI báo ngoài khung giờ | [C2](regression-2026-11-20-e2e/shots/C2-checkin-ngoai-gio.png) |
| C3. Organizer kiêm Admin tự duyệt | Không đạt mã lỗi (D02) | Bị chặn 403 nhưng trả `FORBIDDEN`; UI báo "Bạn không có quyền thực hiện thao tác này" | [C3](regression-2026-11-20-e2e/shots/C3-tu-duyet.png) |

## Bộ API

Chạy lại script CP3 18/11, chỉ đổi tên container. 28/30 nhóm đạt, hai nhóm không đạt giống CP3:

- **T-WL-03 (D01):** khi cố ý làm lỗi bước ghi thông báo `PROMOTED`, hủy đăng ký trả 500 `INTERNAL_ERROR`, Student A vẫn REGISTERED và Student B vẫn WAITLISTED. Lệch Q14.
- **T-AUTH-04 (D02):** người tạo kiêm Admin tự duyệt bị chặn 403 nhưng nhận `FORBIDDEN` thay cho `SELF_APPROVAL_NOT_ALLOWED`.

Trạng thái hai defect giữ nguyên trong [defects.md](../defects.md).

## Chưa kiểm

| Mã | Lý do |
|---|---|
| T-AUTH-01 (đăng nhập Google OIDC) | Nhóm chưa có `GOOGLE_CLIENT_ID`; `.env` để trống nên FE không hiện nút Google. Code đăng nhập Google đã có ở cả backend và frontend. Demo dùng tài khoản mẫu theo CR-03. Chạy bổ sung khi TV3 cung cấp Client ID |
| Quét QR bằng camera | Trình duyệt tự động không có camera; check-in trong E2E dùng tab Nhập mã. Đã quét QR thật bằng điện thoại ngày 19/11 (xem [cp3-2026-11-20.md](cp3-2026-11-20.md), T-CI-03) |

## Quan sát ngoài bộ test case

Các điểm dưới đây không thuộc ca test nào nên không tính là không đạt. Ghi lại để nhóm quyết định:

- Frontend không gọi `GET /me/notifications`, chưa có màn hình xem thông báo; backend đã tạo thông báo (Q22: thông báo in-app là Must).
- Khi check-in trùng, banner hiển thị UUID người check-in thay vì tên (`CheckinResultBanner.jsx`).
- Event trả về không có `rejectReason`, nên form sửa không hiện lý do từ chối (lịch sử duyệt vẫn có).
- Backend bỏ qua `comment` khi duyệt; danh sách chờ duyệt sắp theo giờ bắt đầu sự kiện, trong khi mô tả API ghi "gửi duyệt cũ nhất trước".

## Ghi chú

- Bản demo là bản ghép PR #6 trên máy. Khi PR #6 được merge trên GitHub, chạy lại bộ API và script E2E để xác nhận `main` khớp với kết quả này. Điều kiện và biến môi trường để chạy script E2E ghi ở đầu file `cp3-ui.mjs`.
- Lượt 2 (Codex) có báo cáo chi tiết hơn về đối chiếu hợp đồng FE ↔ BE (26 cặp method/path), lưu trong thư mục làm việc của TV2, không đưa vào repo.
