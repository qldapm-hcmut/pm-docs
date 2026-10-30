---
Nội dung: Mô tả cụ thể task Increment 1 (A24, A28, A31, A20, A26, A27, A29, A62, A30)
Chủ sở hữu: TV1 (giao việc); TV3, TV5 duyệt bước kỹ thuật
Phiên bản: 0.1
Cập nhật: 21/10/2026
Trạng thái: AI hỗ trợ soạn (Claude Code, 21/10); chờ TV3 duyệt bước backend/database, TV5 duyệt bước CI/deploy/QR, TV4 duyệt bước frontend, TV2 duyệt mã test; TV1 duyệt trước khi giao
---

# Increment 1: mô tả task cho nhóm kỹ thuật

Khung theo CLAUDE.md mục 0: Mục tiêu · Đầu vào · Các bước theo stack · Đầu ra · Hoàn thành khi · Người làm, giờ, phụ thuộc.

## Nguồn

- Giờ, ngày, owner, phụ thuộc: `../task2/2.11-schedule.md` v0.3 (lịch đã san tải, A23 họp 25/10). Ngày là ngày dự kiến, không phải hạn cứng; trễ trên đường găng (đánh dấu **găng**) làm trễ demo vì lịch không còn ngày dự trữ.
- Phạm vi và phân rã giờ: `../../../TV3-checklist-baseline.md` (TV3 xác nhận 14/10).
- Quy tắc nghiệp vụ: PD-01, PD-02, PD-03 (báo cáo mục 2.2), Client Log Q01–Q20, REQ-01…21 (báo cáo mục 1.4).
- Mã test: ma trận truy vết (báo cáo chương 5). Mã chính thức chốt ở A22 (TV2).

## Quy ước khi đọc

- **[Đề xuất AI]** đánh dấu tên endpoint, tên migration, tên màn hình. Đây chỉ là gợi ý để ước lượng phạm vi; **API contract và schema của A25 là nguồn chính**. Nếu khác A25 thì theo A25 và sửa file này.
- **[Cần TV3/TV5 quyết]** đánh dấu điểm kỹ thuật chưa được quyết định trong tài liệu nhóm.
- Effort đã gồm phần dev tự test, review, sửa lỗi (E06). Không cộng thêm giờ test vào activity lập trình.
- Log work trên Jira khi làm (I02). Vượt 20% effort thì báo TV1 trong check-in thứ 4/5.

## Tổng quan

| ID | Jira | Activity | Owner | Effort (h) | Ngày dự kiến | Phụ thuộc | Găng |
|---|---|---|---|---:|---|---|---|
| A24 | SCRUM-88 | Set up codebase, CI & deployment | TV5, TV4 | 8,9 | 21–28/10 | A25 | **có** |
| A28 | SCRUM-92 | Build UI layout & shared components | TV4 | 10,5 | 21–26/10 | A25 | |
| A31 | SCRUM-93 | Write test cases for increment 1 | TV2 | 10,5 | 23–28/10 | A25 | |
| A20 | SCRUM-84 | Prototype QR check-in (spike) | TV3, TV5 | 5,7 | 22–24/10 | A21 (đã xong) | |
| A26 | SCRUM-91 | Implement authentication & roles | TV3, TV5, TV4 | 10,5 | 29–30/10 | A24 | **có** |
| A27 | SCRUM-94 | Implement event management | TV3, TV5, TV4 | 25,3 | 31/10–04/11 | A26, A28, A23 | **có** |
| A29 | SCRUM-95 | Implement event registration & cancellation | TV3, TV5, TV4 | 12,6 | 05–07/11 | A27 | **có** |
| A62 | SCRUM-72 | Implement waitlist & auto-promotion | TV3, TV5, TV4 | 13,4 | 08–10/11 | A29 | **có** |
| A30 | SCRUM-96 | Test & demo increment 1 | TV2 chủ trì, cả nhóm | 10,5 | 11–16/11 | A62, A31 | (CP3) |

Lịch chia đều effort cho các owner khi chưa có phân chia riêng. Phân chia đề xuất của TV3 (14/10) ghi ở từng task; TV3, TV4, TV5 thống nhất phần của mình khi nhận task và báo TV1 nếu khác lịch.

Progress Check 09/11 rơi giữa A62: theo lịch, lúc đó có đăng nhập, quản lý sự kiện, đăng ký/hủy; waitlist đang làm; chưa có QR check-in. Phạm vi demo chờ thầy trả lời A58.

---

## A24: Set up codebase, CI & deployment (găng)

**Mục tiêu:** Có repo chạy được frontend React, backend Go, PostgreSQL ở máy dev và trên môi trường deploy, có CI chạy build và test ở mỗi Merge Request, để A26 trở đi chỉ cần viết tính năng.

**Đầu vào:** A25 (stack, cấu trúc module, API contract bản đầu); quy ước Git ở báo cáo mục 1.7 (nhánh riêng, Merge Request có review); R20 (không đưa secret vào repo).

**Các bước:**

1. TV5: tạo cấu trúc repo trên GitLab nhóm, ví dụ `frontend/` (React), `backend/` (Go), `backend/migrations/`, `docs/`. **[Cần TV3/TV5 quyết]** monorepo hay hai repo; tên thư mục.
2. TV5: backend Go khung: điểm vào HTTP server, đọc cấu hình từ biến môi trường, kết nối PostgreSQL, endpoint kiểm tra sống `GET /api/health` **[Đề xuất AI]**, lệnh chạy migration. **[Cần TV3/TV5 quyết]** thư viện router và công cụ migration.
3. TV5: migration `0001` rỗng hoặc tạo bảng nền theo A25 (users, roles, units) để kiểm luồng migration; bảng nghiệp vụ thêm ở A26–A62.
4. TV4: frontend React khung (công cụ build, router, gọi API qua biến môi trường base URL), chạy được trang trống gọi `/api/health`.
5. TV5: môi trường dev local cho PostgreSQL (ví dụ container hoặc cài trực tiếp), file `.env.example` không chứa giá trị thật; `.gitignore` loại `.env`.
6. TV5: thêm vào `Jenkinsfile` các bước build frontend, build và `go test` backend, chạy ở mỗi Merge Request (**CI dùng Jenkins**, TV1 báo 21/10). Kiểm Jenkins nhận được sự kiện Merge Request từ GitLab.
7. TV5: deploy bản khung lên hosting free-tier (ASM-05); ghi URL vào README. **[Cần TV5 quyết]** nền tảng hosting.
8. TV5, TV4: README hướng dẫn chạy local (PD-05: người ngoài nhóm dựng lại được trong dưới 30 phút; đo lại ở A53).

**Đầu ra:** repo khung; pipeline CI chạy được; URL deploy bản khung; README; `.env.example`.

**Hoàn thành khi:** một Merge Request mẫu chạy CI pass và có người review; `GET /api/health` trả về thành công trên bản deploy và trang React gọi được nó; repo không chứa secret (quét trước khi mirror, R20); T-DEP-01 (TV2 đặc tả ở A31) có thể chạy trên bản deploy.

**Người làm, giờ, phụ thuộc:** TV5 chủ trì, TV4 phần frontend; 8,9h (lịch chia 4,45h/người); 21–28/10 (kéo dài vì TV4 làm song song A28). Phụ thuộc A25. Chặn A26.

---

## A28: Build UI layout & shared components

**Mục tiêu:** Có khung giao diện responsive và bộ component dùng chung để A26, A27, A29, A62 chỉ ghép màn hình, không dựng lại từ đầu.

**Đầu vào:** A25 (danh sách màn hình, request/response mẫu; TV4 đã review 2h theo checklist TV3); PD-03 tiêu chuẩn mobile-first; R21 (vỡ layout trên điện thoại nhỏ).

**Các bước:**

1. Chọn thư viện component có sẵn (E05: không tự xây component). **[Cần TV4 quyết, TV3 đồng ý]** tên thư viện.
2. Layout chung: thanh điều hướng theo vai trò (Student, Organizer, Admin), vùng nội dung, trang lỗi/không có quyền, hiển thị thông báo lỗi API.
3. Component dùng chung **[Đề xuất AI]**: thẻ sự kiện, bảng danh sách có phân trang, form có kiểm tra dữ liệu, hộp xác nhận (hủy đăng ký, hủy sự kiện), nhãn trạng thái (Draft, Pending, Published, Cancelled; Registered, Waitlisted, Cancelled), biểu tượng chuông thông báo.
4. Lớp gọi API dùng chung (gắn thông tin đăng nhập, xử lý 401/403) theo API contract A25; dùng dữ liệu mock khi API chưa có.
5. Kiểm layout trên màn hình điện thoại nhỏ và desktop.

**Đầu ra:** layout và component trong `frontend/`; trang demo component hoặc màn hình mẫu dùng mock.

**Hoàn thành khi:** các màn hình mẫu hiển thị đúng ở chiều rộng điện thoại và desktop, không cuộn ngang; component được dùng ít nhất ở một màn hình mẫu; Merge Request đã review. Chưa có mã test riêng: TV2 thêm test case giao diện chung ở A31 nếu cần (ví dụ T-UI-02).

**Người làm, giờ, phụ thuộc:** TV4; 10,5h; 21–26/10. Phụ thuộc A25. Chặn A27.

---

## A31: Write test cases for increment 1

**Mục tiêu:** Mỗi yêu cầu Must của Increment 1 có test case với kết quả kỳ vọng đo được, sẵn sàng chạy ở A30 (CP3).

**Đầu vào:** A22 (quality plan, quy ước mã T-nhóm-số); PD-01 (REQ và quy tắc nghiệp vụ), PD-02 (ràng buộc dữ liệu), PD-04; ma trận truy vết chương 5; checklist TV3 mục 5.

**Các bước:**

1. Lập danh sách yêu cầu trong Increment 1: REQ-01, 02, 03, 04, 05, 06, 07, 08, 09, phần quyền xem dữ liệu của REQ-15, REQ-21 (Should, còn giữ).
2. Viết test case theo nhóm mã đang có trong ma trận truy vết:
   - T-AUTH-01…03: đăng nhập tài khoản mẫu, phân quyền theo vai trò (REQ-01, 02). T-AUTH-04: sự kiện chưa duyệt không được công bố; Organizer không tự duyệt sự kiện mình tạo (REQ-04, Q12). T-AUTH-05…06: quyền xem dữ liệu theo vai trò và đơn vị (REQ-15, Q20; kiểm ở CP5 nhưng viết sẵn).
   - T-EV-01…05: tạo, sửa, gửi duyệt, duyệt/từ chối, công bố (REQ-03). T-EV-06…07: đổi thời gian/địa điểm có thông báo; hủy sự kiện thì hủy đăng ký, đóng waitlist, thông báo (REQ-21, Q19).
   - T-REG-01…05: không đăng ký trùng; không vượt số chỗ; hủy được đến 24 giờ trước giờ bắt đầu, sau đó bị chặn; đăng ký lại sau khi hủy; đăng ký đồng thời (REQ-05, 06, Q13, Q15; PD-02: 100 lượt đồng thời không vượt chỗ).
   - T-WL-01…04: vào waitlist khi đầy; tự chuyển đúng một người đầu hàng (FIFO) khi có chỗ; thông báo lỗi vẫn giữ trạng thái đã đăng ký; đăng ký lại vào cuối hàng (REQ-07, 08, 09, Q14, Q15).
   - T-DEP-01: bản deploy chạy được (A24).
3. Mỗi test case ghi: mã, REQ, điều kiện trước, bước, dữ liệu, kết quả kỳ vọng, mức (unit/integration/e2e theo A22).
4. Chuẩn bị dữ liệu test: tài khoản mẫu cho 3 vai trò (ASM-06), sự kiện có số chỗ nhỏ (ví dụ 2 chỗ) để kiểm waitlist.
5. Gửi TV3 (backend) và TV4 (frontend) review chéo; cập nhật cột mã test trong tab Traceability.

**Đầu ra:** file test case Increment 1 trong `docs/quality/` (PD-04); cột mã test trong tab 6 Sheet.

**Hoàn thành khi:** 100% REQ Must của Increment 1 có ít nhất một test case; mỗi test case có kết quả kỳ vọng đo được; TV3 hoặc TV4 đã review; mã test khớp chương 5. Lưu ý: `docs/traceability.md` cũ dùng mã T-RG; báo cáo và Sheet dùng T-REG, giữ T-REG.

**Người làm, giờ, phụ thuộc:** TV2; 10,5h; 23–28/10. Phụ thuộc A25 (và A22 cho quy ước mã). Chặn A30.

---

## A20: Prototype QR check-in (spike)

**Mục tiêu:** Trả lời trong timebox 6h: quét QR trên trình duyệt điện thoại có dùng được không, mất bao lâu, cần phương án dự phòng thế nào, để A33 làm đúng ngay từ đầu (R04).

**Đầu vào:** PD-03 (QR, nhập mã, xác nhận thủ công, không check-out; median ≤ 5 giây trong môi trường test, O2); Q03; A21 đã xong.

**Các bước:**

1. TV5 (tối đa 3h): prototype trang web quét QR bằng camera điện thoại và ô nhập mã dự phòng; sinh vài mã QR mẫu. **[Cần TV5 quyết]** thư viện quét QR.
2. TV3 (3h): thử trên ít nhất 3 thiết bị/trình duyệt khác nhau, mạng yếu; đo thời gian từ mở trang đến ghi nhận; ghi lỗi gặp phải (quyền camera, HTTPS bắt buộc cho camera, ánh sáng).
3. Ghi kết luận: dùng được hay không, thời gian đo được, nội dung mã QR nên chứa gì (mã đăng ký, không chứa dữ liệu cá nhân), điểm còn chưa rõ chuyển vào A33.
4. Cập nhật R04 trong Risk Register theo kết quả.

**Đầu ra:** ghi chú kết quả spike trong `docs/` (kèm số đo thật); code prototype (không merge vào nhánh chính nếu không dùng lại).

**Hoàn thành khi:** có kết luận và số đo trên ≥ 3 thiết bị; điểm chưa rõ đã ghi sang A33; R04 đã cập nhật. Hết 6h thì dừng và ghi lại, không kéo dài (timebox TV3 đề xuất, PM áp dụng 20/10).

**Người làm, giờ, phụ thuộc:** TV5 (prototype ≤ 3h), TV3 (thử và đo 3h); 5,7h PERT; 22–24/10. Phụ thuộc A21 (đã xong). Đầu vào của A33 (L7). Không nằm trên đường găng (float 9 ngày).

---

## A26: Implement authentication & roles (găng)

**Mục tiêu:** Người dùng đăng nhập bằng tài khoản mẫu có email trường và chỉ làm/xem được đúng phần vai trò và đơn vị của mình cho phép.

**Đầu vào:** A24 (repo, CI, deploy); A25 (bảng users, roles, units; API contract); Q02 (không SSO thật, mô phỏng bằng email trường/tài khoản mẫu), ASM-06, Q12 (Admin duyệt), Q20 (quyền xem dữ liệu).

**Các bước:**

1. TV5: cấu hình đăng nhập và thư viện xác thực (TV3 đề xuất phần TV5 khoảng 5h, chờ TV5 xác nhận). **[Cần TV3/TV5 quyết]** cơ chế phiên đăng nhập (session hay token).
2. TV3, TV5: migration bảng users, roles, units theo A25; seed tài khoản mẫu cho Student, Organizer (gắn đơn vị), Admin (PD-05: 3 tài khoản demo). Không lưu mật khẩu dạng rõ.
3. TV3: endpoint **[Đề xuất AI]** `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/me` (trả về vai trò, đơn vị).
4. TV3: middleware phân quyền dùng chung cho mọi API: kiểm vai trò; kiểm đơn vị cho Organizer/Admin (Q20); trả 401 khi chưa đăng nhập, 403 khi không có quyền.
5. TV4: màn hình đăng nhập; điều hướng sau đăng nhập theo vai trò; ẩn menu không có quyền (không thay cho kiểm quyền ở backend).
6. Test do dev tự viết (E06) cho middleware phân quyền.

**Đầu ra:** đăng nhập chạy trên bản deploy; middleware phân quyền; seed tài khoản mẫu.

**Hoàn thành khi:** T-AUTH-01…03 pass trên bản deploy; gọi API của vai trò khác bị chặn ở backend (không chỉ ẩn nút); không có mật khẩu dạng rõ trong database hay repo. T-AUTH-05…06 kiểm ở CP5 nhưng middleware phải hỗ trợ đơn vị từ bây giờ.

**Người làm, giờ, phụ thuộc:** TV3, TV5, TV4; 10,5h (lịch chia 3,5h/người; TV3 đề xuất 14/10: TV3 5,5h, TV5 5h; TV4 phần màn hình đăng nhập: cần thống nhất); 29–30/10. Phụ thuộc A24 (L8). Chặn A27.

---

## A27: Implement event management (găng)

**Mục tiêu:** Organizer tạo, sửa, gửi duyệt, sửa/hủy sự kiện; Admin duyệt trước khi công bố; Student xem danh sách sự kiện đã công bố.

**Đầu vào:** A26 (đăng nhập, phân quyền); A28 (layout, component); A23 (Baseline V1.0 đã chốt); A25 (bảng events, notifications); Q01, Q12, Q19; REQ-03, 04, 21.

**Các bước (phân rã TV3 14/10):**

1. TV3 (CRUD, kiểm dữ liệu 3h): migration bảng events (thông tin, đơn vị tổ chức, số chỗ, thời gian, địa điểm, trạng thái). Endpoint **[Đề xuất AI]** `POST /api/events`, `PUT /api/events/{id}`, `GET /api/events` (Student: chỉ Published), `GET /api/events/{id}`, `GET /api/organizer/events` (sự kiện của mình, Q20).
2. TV3 (duyệt, công bố, quyền 2h): trạng thái Draft → Pending → Published hoặc bị từ chối; endpoint `POST /api/events/{id}/submit`, `/approve`, `/reject` **[Đề xuất AI]**; Organizer không duyệt sự kiện mình tạo, chỉ Admin duyệt (Q12).
3. TV3 (hủy sự kiện 3h): `POST /api/events/{id}/cancel` **[Đề xuất AI]** chuyển Cancelled, hủy các đăng ký, đóng waitlist, tạo thông báo cho người liên quan (Q19). Phần này chạm bảng registrations/waitlist: thống nhất với A29, A62, không làm trùng (R14).
4. TV5 (thông báo dùng chung): migration bảng notifications; hàm tạo thông báo trong ứng dụng dùng chung cho A27, A62; endpoint `GET /api/me/notifications`, đánh dấu đã đọc **[Đề xuất AI]**. Kênh tối thiểu là trong ứng dụng; email là Should, chờ A58.
5. TV3 (tích hợp thông báo 1h): đổi thời gian/địa điểm sự kiện đã công bố thì thông báo người đã đăng ký (Q19, REQ-21).
6. TV4: màn hình danh sách và chi tiết sự kiện (Student); form tạo/sửa, danh sách sự kiện của tôi (Organizer); hàng chờ duyệt (Admin); chuông thông báo.
7. Dev tự test, review, sửa (3h, E06).

**Đầu ra:** module sự kiện và thông báo trong ứng dụng, chạy trên bản deploy.

**Hoàn thành khi:** T-EV-01…05 và T-AUTH-04 pass; T-EV-06…07 pass (REQ-21, Should, PM giữ 20/10); sự kiện chưa duyệt không hiện cho Student. Nếu trễ quá 1 ngày so với 04/11, báo TV1 xem xét cắt REQ-21 (rút khoảng 8h, 1–2 ngày) theo thứ tự Could rồi Should.

**Người làm, giờ, phụ thuộc:** TV3 (TV3 đề xuất 12h), TV5 (thông báo dùng chung), TV4 (frontend); 25,3h (lịch chia khoảng 8,4h/người); 31/10–04/11. Phụ thuộc A26, A28, A23 (L8). Chặn A29.

---

## A29: Implement event registration & cancellation (găng)

**Mục tiêu:** Student đăng ký và hủy đăng ký sự kiện đúng quy tắc: không trùng, không vượt số chỗ, hủy đến 24 giờ trước giờ bắt đầu.

**Đầu vào:** A27 (sự kiện đã công bố, số chỗ); A25 (bảng registrations); Q13 (hạn hủy 24 giờ, sau đó liên hệ Organizer), Q15 (một đăng ký còn hiệu lực/sinh viên/sự kiện, đăng ký lại được); REQ-05, 06.

**Các bước (phân rã TV3 14/10):**

1. TV3 (API đăng ký/hủy, hạn 24 giờ 2h): migration bảng registrations (trạng thái, thời điểm đăng ký, thời điểm hủy). Endpoint **[Đề xuất AI]** `POST /api/events/{id}/registrations`, `DELETE /api/registrations/{id}` (chặn khi còn dưới 24 giờ), `GET /api/me/registrations`.
2. TV3 (chống trùng, đăng ký lại 1h): ràng buộc ở mức database chỉ một đăng ký còn hiệu lực cho mỗi cặp sinh viên–sự kiện (PD-02); đã hủy thì đăng ký lại được.
3. TV3 (transaction chống vượt chỗ 2h): đếm chỗ và tạo đăng ký trong cùng transaction hoặc khóa phù hợp. **[Cần TV3 quyết]** cách khóa. Khi đầy thì trả kết quả "đầy" để A62 xử lý waitlist (không làm waitlist ở đây).
4. TV4: nút đăng ký/hủy ở chi tiết sự kiện (hiện số chỗ còn lại, ẩn nút hủy sau mốc 24 giờ và hướng dẫn liên hệ Organizer); trang "đăng ký của tôi"; Organizer xem danh sách người đăng ký sự kiện của mình.
5. Test đồng thời (TV3/TV5): 100 lượt đăng ký cùng lúc không vượt chỗ (PD-02, ASM-02). Dev tự test, review 2h.

**Đầu ra:** module đăng ký/hủy trên bản deploy.

**Hoàn thành khi:** T-REG-01…05 pass, gồm test đồng thời; hủy sự kiện ở A27 đã hủy đúng các đăng ký (không làm lại ở A29).

**Người làm, giờ, phụ thuộc:** TV3 (TV3 đề xuất 7h), TV5, TV4; 12,6h (lịch chia 4,2h/người); 05–07/11. Phụ thuộc A27. Chặn A62.

---

## A62: Implement waitlist & auto-promotion (găng)

**Mục tiêu:** Khi sự kiện đầy, Student vào waitlist; khi có chỗ trống, hệ thống tự chuyển người đầu waitlist thành đã đăng ký và gửi thông báo, không cần BTC duyệt, không có trạng thái "chờ xác nhận".

**Đầu vào:** A29 (đăng ký, transaction chống vượt chỗ); thông báo dùng chung (A27, TV5); A25 (bảng waitlist); Q04, Q14, Q15; REQ-07, 08, 09; R17 (tranh chấp waitlist).

**Các bước (phân rã TV3 14/10):**

1. TV3 (FIFO 2h): migration bảng waitlist (thứ tự theo thời điểm vào hàng). Đăng ký khi đầy thì vào cuối waitlist; hủy rồi đăng ký lại thì vào cuối hàng (Q15). Endpoint **[Đề xuất AI]** `GET /api/events/{id}/waitlist` (Organizer của sự kiện), vị trí của tôi trong hàng ở `GET /api/me/registrations`.
2. TV3 (tự chuyển, chống chuyển trùng 2h): khi một đăng ký bị hủy, trong cùng transaction lấy đúng một người đầu hàng, chuyển thành đã đăng ký; chặn chuyển trùng khi nhiều lượt hủy cùng lúc (R17).
3. TV3/TV5 (thông báo 1h): tạo thông báo cho người được chuyển bằng hàm dùng chung. Thông báo lỗi **không** rollback việc chuyển: người đó vẫn là đã đăng ký (Q14).
4. TV4: hiển thị "đang ở waitlist, vị trí N"; thông báo được chuyển; Organizer xem waitlist.
5. Test và sửa (2h): FIFO, đồng thời, thông báo lỗi.

**Đầu ra:** waitlist và tự chuyển trên bản deploy.

**Hoàn thành khi:** T-WL-01…04 pass; test đồng thời không chuyển trùng; hủy sự kiện (A27) đóng waitlist đúng. Không dùng xác nhận thủ công để thay cho tự chuyển (checklist TV3 mục 4).

**Người làm, giờ, phụ thuộc:** TV3 (TV3 đề xuất 7h), TV5, TV4; 13,4h (lịch chia khoảng 4,5h/người); 08–10/11 (đang làm lúc Progress Check 09/11). Phụ thuộc A29. Chặn A30 và A32 (L11).

---

## A30: Test & demo increment 1 (CP3)

**Mục tiêu:** Chạy toàn bộ test case Increment 1 trên bản deploy, ghi kết quả làm bằng chứng chất lượng, demo nội bộ và kết luận CP3.

**Đầu vào:** A62 xong (toàn bộ tính năng Increment 1); A31 (test case); tiêu chí CP3 ở `../task2/2.5-checkpoints.md`.

**Các bước:**

1. TV2: chạy T-AUTH-01…04, T-EV-01…07, T-REG-01…05, T-WL-01…04, T-DEP-01 trên bản deploy; ghi pass/fail, ngày, người chạy, bằng chứng (ảnh chụp hoặc log CI).
2. Lỗi tìm thấy: ghi issue trên Jira gắn mã test; dev sửa trong quỹ giờ của activity gốc (E06); lỗi chặn luồng báo TV1 ngay.
3. Chạy lại test của các lỗi đã sửa.
4. Cả nhóm: demo nội bộ luồng đăng nhập → tạo sự kiện → duyệt → công bố → đăng ký/hủy → đầy → waitlist → tự chuyển và thông báo.
5. TV2 kết luận CP3 (đạt / đạt có điều kiện / không đạt), ghi biên bản ở tab Biên bản CP; TV1 ghi deviation vào Weekly Log.

**Đầu ra:** kết quả chạy test trong `docs/quality/`; biên bản CP3; danh sách lỗi còn mở.

**Hoàn thành khi:** 100% test case Must của Increment 1 đã chạy và ghi kết quả; không còn lỗi nghiêm trọng ở đăng ký, waitlist, phân quyền; biên bản CP3 có người duyệt (TV2).

**Người làm, giờ, phụ thuộc:** TV2 chủ trì, cả nhóm demo; 10,5h; 11–16/11 (CP3, trễ 15 ngày so với kế hoạch ban đầu 01/11). Phụ thuộc A62, A31. A32 chạy song song (L11). Chặn A43, A45.

---

## Việc cần duyệt trước khi giao

| Người duyệt | Nội dung |
|---|---|
| TV3 | Bước backend và database của A26, A27, A29, A62: tên endpoint, migration, cách khóa transaction, phân chia giờ với TV5, TV4 |
| TV5 | Bước A24 (cấu trúc repo, CI, hosting), A20 (thư viện QR), phần thông báo dùng chung trong A27 |
| TV4 | Bước frontend và màn hình của A28, A26, A27, A29, A62 |
| TV2 | Danh sách mã test của A31 và A30; quy ước T-REG thay cho T-RG trong file traceability cũ |
| TV1 | Duyệt cả file rồi giao trên Jira (gắn link vào mô tả từng task). Đã chọn Jenkins cho CI (21/10) |
