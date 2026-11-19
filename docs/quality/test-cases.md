---
Activity: A31, A40
Chủ sở hữu: TV2
Trạng thái: Chờ TV3 rà các ca API và TV4 rà các ca UI
---

# Test cases

Mã ca theo [tab 6 Traceability đã export](../sheet-import/6-traceability.tsv). Tiêu chí nghiệp vụ lấy từ [scope và MoE](../task1/1.4-scope-objectives-moe.md), [Product Descriptions](../task2/2.2-product-descriptions.md) và CR-01–03. Khi gọi API, thêm tiền tố `/api/v1` cho các đường dẫn nghiệp vụ. Đối chiếu status và payload với `ticket-system-uni-be/api/openapi.yaml` của commit đang chạy.

Dùng tài khoản thử Student (S1, S2…), Organizer của đơn vị sự kiện (O), Organizer đơn vị khác (O2) và Admin (A). Với ca liên quan thời gian, lấy mốc tương đối so với đồng hồ server. Ghi ngày, commit, vai trò, kết quả và bằng chứng trong [results](results/).

## Increment 1

| Mã | Requirement | Vai trò và tiền điều kiện | Bước | Kết quả kỳ vọng |
|---|---|---|---|---|
| T-AUTH-01 | REQ-01, CR-03 | Tài khoản mẫu qua Google OIDC, backend ở chế độ Google | Gọi `POST /auth/google` với ID token hợp lệ của tài khoản trường. Thử lại với tài khoản sai domain hoặc token hết hạn | Token trường hợp hợp lệ trả 200 và có access token, refresh token. Trường hợp sai bị từ chối 401 |
| T-AUTH-02 | REQ-01 | Đã có refresh token của hệ thống | Gọi `POST /auth/refresh`, gọi `GET /me` bằng access token mới, rồi thử dùng lại refresh token cũ | 200 cấp token mới kèm hồ sơ hiện tại. Refresh token cũ trả 401 |
| T-AUTH-03 | REQ-02 | Có access token demo của S1, O, A | Gọi `GET /me` bằng từng vai trò rồi gọi không kèm token | 200 cho cả ba token. Hồ sơ có STUDENT, ORGANIZER của đơn vị được gán, hoặc ADMIN tương ứng. Thiếu token trả 401 |
| T-AUTH-04 | REQ-04, Q12 | O tạo sự kiện và gửi duyệt. Có thêm fixture người tạo kiêm Admin | S1 xem nháp và sự kiện chờ duyệt. O và chính người tạo kiêm Admin thử `POST /events/{id}/approve` | S1 nhận 404 ở cả hai trạng thái. Cả hai lần tự duyệt bị chặn 403. Hợp đồng API quy định `SELF_APPROVAL_NOT_ALLOWED` khi người tạo kiêm Admin, sự kiện vẫn chờ duyệt |
| T-AUTH-05 | REQ-15 | S1 đã đăng ký, S2 là Student độc lập | S1 và S2 gọi `GET /registrations/{id}` của S1. S2 gọi danh sách đăng ký của sự kiện | S1 đọc được đăng ký của mình. S2 nhận 404 cho cả hai tài nguyên |
| T-AUTH-06 | REQ-15, CR-02 | Sự kiện có đăng ký, O không nhất thiết là người tạo, O2 ngoài đơn vị, A cấp trường | Gọi `GET /events/{id}/registrations` theo từng vai trò | O cùng đơn vị và A nhận 200. O2 nhận 404. Danh sách quản lý không chứa QR token hoặc mã check-in |
| T-EV-01 | REQ-03 | O có quyền trên đơn vị, giờ bắt đầu và hạn đăng ký trong tương lai | `POST /events`, rồi `GET /manage/events?status=DRAFT` | 201 trả DRAFT. Danh sách quản lý chứa đúng ID vừa tạo |
| T-EV-02 | REQ-03 | O có nháp, biết version | `PATCH /events/{id}` đổi địa điểm với `If-Match` hiện hành. Gửi lại với version cũ | 200, địa điểm đổi và version tăng. Version cũ trả 409 `VERSION_CONFLICT` |
| T-EV-03 | REQ-03, REQ-04 | O có nháp hợp lệ. A không phải người tạo | O gọi `POST /events/{id}/submit`. A mở `GET /approvals/pending`, sau đó duyệt. S1 mở danh mục và chi tiết | Sự kiện xuất hiện trong danh sách chờ duyệt. Sau khi A duyệt trả PUBLISHED và S1 thấy sự kiện |
| T-EV-04 | REQ-03, REQ-04 | O và A có sự kiện chờ duyệt | A gọi `POST /events/{id}/reject` kèm lý do, O chỉnh sửa và gửi duyệt lại. A xem approval log | REJECTED, log ghi lý do. Gửi duyệt lại đưa sự kiện về PENDING_APPROVAL |
| T-EV-05 | REQ-03 | O có sự kiện chờ duyệt | Tạo sự kiện có `endAt = startAt`. Thử sửa địa điểm của sự kiện đang chờ duyệt | Tạo lỗi lịch trả 400 `VALIDATION_ERROR`. Sửa khi chờ duyệt trả 409 `INVALID_STATE_TRANSITION` |
| T-EV-06 | REQ-21, Q19 | O, sự kiện PUBLISHED còn hơn 60 phút, có Student đã đăng ký và chờ | `PATCH /events/{id}` đổi địa điểm; đọc `GET /me/notifications` theo Student | Vẫn PUBLISHED, địa điểm cập nhật và cả hai nhóm nhận `EVENT_CHANGED` |
| T-EV-07 | REQ-21, Q19 | Sự kiện PUBLISHED có đăng ký và waitlist | O gọi `POST /events/{id}/cancel` kèm lý do, đọc lại trạng thái và thông báo | CANCELLED. Các đăng ký đang hiệu lực chuyển `CANCELLED_BY_EVENT`, waitlist đóng, mỗi người bị ảnh hưởng có `EVENT_CANCELLED` |
| T-REG-01 | REQ-05, REQ-06 | Student, sự kiện đã công bố, còn chỗ và đang mở đăng ký | `POST /events/{id}/registrations`, rồi đọc chi tiết sự kiện | 201 REGISTERED, có mã check-in. Số đăng ký tăng một và số chỗ trống giảm một |
| T-REG-02 | REQ-05, Q15 | Một Student và sự kiện còn chỗ | Đăng ký hai lần liên tiếp. Với sự kiện mới gửi đồng thời hai request cùng Student | Chỉ một bản ghi còn hiệu lực. Lần trùng trả 409 `ALREADY_REGISTERED` |
| T-REG-03 | REQ-05, PD-02 | Hai Student, sự kiện còn một chỗ và tắt waitlist. Fixture bổ sung có 100 Student, sức chứa 3, giới hạn chờ 5 | Gửi hai POST đăng ký cùng lúc. Chạy ca tích hợp dịch vụ/DB với 100 lượt đồng thời | Ở HTTP có một 201, một 409 `EVENT_FULL`. Ở fixture 100 lượt có 3 REGISTERED, 5 WAITLISTED, 92 bị từ chối vì đầy |
| T-REG-04 | REQ-06, Q13 | Chủ đăng ký REGISTERED, sự kiện còn hơn 24 giờ | `POST /registrations/{id}/cancel`, đọc lại đăng ký | 200 CANCELLED, `cancelledBy=STUDENT`. Nếu có waitlist thì xử lý theo T-WL-02 |
| T-REG-05 | REQ-06, Q13 | Sự kiện chưa bắt đầu, còn dưới 24 giờ, không có ngoại lệ hủy. Có Student đã đăng ký và Student đang chờ | Mỗi Student tự hủy đăng ký của mình | REGISTERED bị chặn với 422 `CANCEL_DEADLINE_PASSED`. WAITLISTED có thể rời hàng, trả 200 CANCELLED |
| T-WL-01 | REQ-07 | Sự kiện hết chỗ, waitlist tối đa hai người | S2 rồi S3 đăng ký. S4 đăng ký khi waitlist đã đầy | S2 và S3 nhận 201 WAITLISTED, vị trí 1 và 2, không có mã check-in. S4 nhận 409 `EVENT_FULL` |
| T-WL-02 | REQ-08, REQ-09, Q14 | Một chỗ đã có S1 và hàng chờ S2 trước S3. Sự kiện còn hơn 24 giờ | S1 hủy; đọc đăng ký của S2/S3 và thông báo của S2 | Chỉ S2 chuyển REGISTERED, có đúng một thông báo `PROMOTED`. S3 vẫn WAITLISTED, lên vị trí 1 |
| T-WL-03 | REQ-09, Q14 | Fixture như T-WL-02. Mô phỏng lỗi lưu `PROMOTED` trong DB kiểm thử riêng | S1 hủy, đọc lại trạng thái S2 | Theo Q14, S2 vẫn là REGISTERED khi thông báo lỗi, không có bước chờ xác nhận. Ghi riêng response của thao tác hủy |
| T-WL-04 | REQ-07, Q15 | S1 đã hủy, S2 đã thế chỗ, S3 đứng đầu waitlist | S1 đăng ký lại | Tạo ID mới. S1 vào cuối hàng sau S3, không có hai đăng ký còn hiệu lực |

## Increment 2 và tích hợp

| Mã | Requirement | Vai trò và tiền điều kiện | Bước | Kết quả kỳ vọng |
|---|---|---|---|---|
| T-CI-01 | REQ-10, PD-03 | Student có REGISTERED và đang trong cửa sổ check-in. O thuộc đơn vị | Student lấy QR từ `GET /registrations/{id}`. O gửi mã QR bằng `POST /events/{id}/check-ins` | 201 với `method=QR`, đúng ID đăng ký và có thời điểm check-in |
| T-CI-02 | REQ-10 | T-CI-01 đã thành công | O gửi lại cùng QR và đọc `GET /events/{id}/check-ins?method=QR` | 409 `ALREADY_CHECKED_IN`, có thời điểm lần trước. Chỉ một lượt điểm danh |
| T-CI-03 | REQ-10, O2, PD-03 | Ít nhất một thiết bị thật (nên dùng nhiều thiết bị nếu có), camera hoạt động, QR hợp lệ, mỗi lượt một Student riêng | Đo thời gian từ lúc quét đến xác nhận UI qua ít nhất 5 lượt độc lập. Ghi thiết bị, số lượt và mạng | Trung vị ≤ 5 giây. Kiểm tra tiêu chí PD-03 mỗi lượt < 10 giây |
| T-CI-04 | REQ-11 | Student REGISTERED chưa check-in, O thuộc đơn vị | O gửi `method=CODE` với mã viết thường và bỏ dấu gạch. Student đọc lại đăng ký | 201, `method=CODE`; trạng thái điểm danh cập nhật như khi quét QR |
| T-CI-05 | REQ-11, CR-01 | Student REGISTERED chưa check-in, O thuộc đơn vị, A không kiêm O | A thử xác nhận thủ công. O gửi `method=MANUAL` thiếu ghi chú, rồi thử với ghi chú hợp lệ. Đọc lại đăng ký và audit | A bị chặn và không tạo check-in. Thiếu ghi chú trả 400. O nhận 201, lưu `method=MANUAL` và đúng một audit `MANUAL_CHECKIN` |
| T-RP-01 | REQ-12 | Có đăng ký đang hiệu lực, lượt đã điểm danh và đăng ký đã hủy | O mở danh sách đăng ký và check-in, đối chiếu ID và trạng thái | Danh sách điểm danh khớp các ID đã check-in và không tính đăng ký đã hủy chưa điểm danh |
| T-RP-02 | REQ-13 | Có dữ liệu QR, CODE, MANUAL và một đăng ký đã hủy | A gọi `GET /events/{id}/reports/summary`, đối chiếu với danh sách nguồn | Số đăng ký, đã hủy, check-in theo phương thức và tỷ lệ tham dự khớp toàn bộ dữ liệu nguồn |
| T-RP-03 | REQ-14, O3 | Sự kiện thử có 500 đăng ký, 250 đã điểm danh, danh sách MSSV dự kiến | O lấy summary và xuất `/events/{id}/exports/registrations?format=csv` và `attendance?format=csv`. Đo tổng thời gian, đếm dòng và so mã nguồn | Tổng ≤ 30 giây, summary 500/250, CSV có 500/250 dòng dữ liệu tương ứng, đúng tất cả MSSV nguồn |
| T-UI-01 | REQ-10, S36 | Bản frontend tích hợp, Organizer dùng điện thoại có camera | Mở màn hình check-in, cấp quyền camera, quét QR; thử chuyển sang nhập mã | Bố cục thao tác được trên điện thoại, có phản hồi rõ, chuyển được sang nhập mã khi không quét được |
| T-INT-01 | S42, O1/O4 | Có bản tích hợp, một sự kiện thử và các vai trò | O tạo, gửi duyệt; A duyệt; Student đăng ký đến hết chỗ, thêm người chờ; Student đang giữ chỗ hủy | Sự kiện công bố sau duyệt; đúng một người đầu hàng được chuyển; trạng thái nhất quán xuyên luồng |
| T-INT-02 | S42, O2 | Tiếp tục trên sự kiện T-INT-01, trong cửa sổ check-in | O check-in các Student đã đăng ký, gồm người vừa được chuyển. Thử QR, CODE và MANUAL | Mỗi người được điểm danh đúng một lần trên cùng sự kiện, trạng thái cập nhật đúng |
| T-INT-03 | S42, O3 | Tiếp tục với dữ liệu T-INT-02 | O mở báo cáo và xuất hai CSV, đối chiếu số liệu với lượt đăng ký/check-in vừa thực hiện | Summary và CSV khớp dữ liệu vừa tạo |
| T-DEP-01 | S51, PD-05 | Máy sạch có Docker và hai repo ở commit chuẩn bị demo | Dựng bằng hướng dẫn README, kiểm tra health, đăng nhập và chạy T-INT-01–03 | Người khác trong nhóm dựng được, cả frontend và API sẵn sàng, luồng chính chạy được từ đầu đến cuối |
