---
Nội dung: Việc Sprint 6–7 (22/10–03/11) của TV4 Nguyễn Đắc Nghĩa (Frontend)
Người giao: TV1
Phiên bản: 0.3
Cập nhật: 22/10/2026
Trạng thái: AI hỗ trợ soạn (Claude Code, 22/10); TV1 duyệt 22/10; TV4 duyệt bước frontend và báo ý kiến trên chat trước tối 24/10
---

# TV4 · Nguyễn Đắc Nghĩa · Sprint 6–7

Bạn chỉ cần file này. Mọi quy tắc, phân công và nội dung cần duyệt đều đã chép vào đây.

Đầu vào của từng task có sẵn trong gói upload trên Drive, thư mục `4-tai-nguyen/<mã task>/`; mỗi thư mục có `DAU-VAO.md` ghi từng đầu vào lấy ở đâu (có sẵn, tab Sheet, hay chờ ai tạo). Tài liệu dùng chung (đề bài, Client Log, REQ, mục tiêu, giả định, PD-01…05, sơ đồ, mẫu ghi giờ hồi tưởng hạn 23/10) ở `4-tai-nguyen/chung/`; báo cáo PDF ở `3-bao-cao/`.

## Tóm tắt

| # | Task | Jira | Giờ của bạn | Ngày | Ngày xong | Găng |
|---|---|---|---:|---|---|---|
| 1 | A24 Codebase, CI & deployment, phần frontend | SCRUM-88 | 4,45 | 22/10 (khung React), 26–28/10 | **28/10** | **có** |
| 2 | A28 UI layout & shared components | SCRUM-92 | 10,5 (còn 8,5) | 21–26/10 | **26/10** | **có** |
| 3 | A23 Họp chốt Baseline V1.0 | SCRUM-87 | 1,0 | 25/10 15h | 25/10 | |
| 4 | Việc duyệt trước họp A23 | | | 22–24/10 | **tối 24/10** | |
| 5 | A26 Authentication & roles, phần màn hình | SCRUM-91 | 3,5 | 29–30/10 | **30/10** | **có** |
| 6 | A27 Event management, phần màn hình | SCRUM-94 | 8,4 | 31/10–04/11 | **04/11** | **có** |

Tổng: 13h trong Sprint 6 (22–27/10), 12,5h trong Sprint 7.

## Kết quả của bạn dùng ở đâu trong bài nộp

Bạn không cần mở báo cáo. Báo cáo do TV1 soạn, đánh số đúng theo Task của đề: mục 3.5 của báo cáo là Task 3.5 của đề. Bạn chỉ cần để kết quả đúng nơi lưu dưới đây, TV1 đưa vào báo cáo.

| Kết quả | Nơi lưu | Dùng cho phần nào của bài nộp |
|---|---|---|
| Code frontend A24, A28, A26, A27 và Merge Request đã review | git local, đẩy lên repo chung sau họp 25/10 | Hiện thực phần mềm (Task 3.1) |
| README phần frontend | repo chung | Hướng dẫn chạy (đề bắt buộc nộp link repo kèm hướng dẫn chạy) |
| Ảnh chụp màn hình trên điện thoại và desktop (A28) | Drive `Sprint 6-7/A28/`; đính vào Merge Request khi có repo chung | Bằng chứng chất lượng (Task 3.5); rủi ro R21 (Task 3.4) |
| Ý kiến duyệt, ý kiến tại họp A23 | chat nhóm; biên bản TV1 ghi ở Sheet, tab Biên bản CP | Baseline V1.0 (Task 2.12) |
| Log work Jira, lịch sử commit | Jira, git (repo chung) | So sánh kế hoạch và thực tế (Task 3.3); đóng góp cá nhân (Task 4.6). Thầy có thể hỏi khi viva |

**Bạn có tải liên tục nhất trên đường găng đến 04/11** (A28 → A24 → A26 → A27). Trễ một ngày ở A28 hoặc A24 là trễ A26, A27 và demo. Vướng thì báo TV1 trong ngày.

## Cần có trước khi bắt đầu

Thiếu mục nào thì báo người cung cấp và TV1 ngay, đừng chờ. Bạn đang trên đường găng, một ngày chờ là một ngày trễ demo.

| Cần có | Nội dung tối thiểu | Ai cung cấp | Cần trước |
|---|---|---|---|
| Quyền trên repo chung | Tạo nhánh, push, mở và review Merge Request | người tạo repo (họp 25/10 chọn) | 26/10 |
| Thư mục Drive `Sprint 6-7/A28`, quyền Người chỉnh sửa | Để nộp ảnh chụp giao diện | TV1 | 26/10 |
| Cấu trúc thư mục thống nhất với TV5 | Ví dụ `src/frontend/`, `src/backend/`, để ghép vào repo chung không phải sửa | TV5 | **sáng 22/10** |
| Git, Node.js (bản LTS), npm trên máy bạn | Repo git local cho frontend | bạn | 22/10 |
| API contract (A25) | Các trường request/response của sự kiện, đăng ký, waitlist, thông báo, `/api/me`; một định dạng lỗi chung (lỗi theo trường cho 400); mã 401, 403; giá trị trạng thái; cách phân trang | TV3 | 23/10. Chưa có thì dựng component bằng mock, đặt tên trường tạm, sửa khi có contract |
| Cơ chế phiên đăng nhập | Cookie hay token, để làm lớp gọi API | TV5, TV3 | 25/10. Chưa có thì để lớp gọi API một chỗ duy nhất, đổi sau |
| Backend chạy `/api/health` | Local hoặc trên bản deploy | TV5 | 27/10, sau khi có repo chung (trước đó gọi mock) |
| Hosting frontend, biến môi trường deploy | Nơi deploy, URL backend | TV5 | 27/10 |
| Điện thoại thật | Kiểm layout ngoài chế độ giả lập của trình duyệt | bạn | 26/10 |
| Jira | SCRUM-88, 91, 92, 94 có tên bạn, có quyền log work | TV1 | 22/10 |
| Tài khoản demo 3 vai trò | Email, mật khẩu (gửi riêng, không qua repo) | TV5, TV3 | 29/10 (A26) |

## Lịch theo ngày

| Ngày | Task | Giờ | Việc | Thực tế |
|---|---|---:|---|---|
| 21/10 | A28 | 2,0 | (đã qua) | |
| Thứ Năm 22/10 | A24, A28 | 2,0 | Khung React trước (mục 1 bước 1); chọn thư viện component | |
| Thứ Sáu 23/10 | A28 | 2,0 | Layout chung, điều hướng theo vai trò | |
| Thứ Bảy 24/10 | A28 | 2,0 | Component dùng chung; gửi ý kiến duyệt (mục 4) | |
| Chủ nhật 25/10 | A23 | 1,0 | Họp 15h | |
| Chủ nhật 25/10 | A28 | 2,0 | Lớp gọi API, dữ liệu mock | |
| Thứ Hai 26/10 | A28, A24 | 2,0 | Kiểm layout điện thoại; Merge Request A28 | |
| Thứ Ba 27/10 | A24 | 2,0 | Nối frontend vào CI và bản deploy cùng TV5 | |
| Thứ Tư 28/10 | A24 | 1,0 | README phần frontend; Merge Request A24; review test case A31 | |
| 29–30/10 | A26 | 3,5 | Màn hình đăng nhập, điều hướng theo vai trò | |
| 31/10–03/11 | A27 | 8,0 | Màn hình sự kiện, duyệt, thông báo | |
| Thứ Tư 04/11 | A27 | 0,4 | (Sprint 8) phần còn lại | |

## Quy ước chung

- **[Đề xuất AI]**: tên màn hình, component, thư viện, endpoint do AI gợi ý. API contract TV3 chốt (A25) là nguồn chính; khác thì theo contract và báo TV1 sửa. **[Cần X quyết]**: người được ghi tên quyết, ghi quyết định lên chat nhóm (khi có repo chung thì ghi cả vào mô tả Merge Request).
- Giờ theo lịch đã san tải (khoảng 2h/ngày) chỉ để định hướng; cái cần giữ là **ngày xong**. Giờ lập trình **đã gồm** tự test, review, sửa lỗi.
- Log work trên Jira trong ngày làm. Vượt quá 20% giờ hoặc thấy không kịp ngày xong: báo TV1 ngay trong ngày.
- Check-in 3 dòng trên chat thứ Tư 28/10 hoặc thứ Năm 29/10.
- **Tạm đến họp 25/10** (issue I03: GitLab tự host trên máy cá nhân, nhóm không truy cập được; họp 25/10 chọn nơi chứa repo chung và CI):
  - Code: dùng git trên máy bạn (`git init`), commit thường xuyên, đặt `git config user.name` và `user.email` đúng tên thật. Lịch sử commit là bằng chứng đóng góp và được giữ nguyên khi đẩy lên repo chung.
  - Tài liệu: file `.md` (lưu UTF-8), tải lên thư mục Drive `Sprint 6-7/<mã task>`. Sửa lại thì tải bản mới bằng **Quản lý phiên bản** của Drive (chuột phải vào file → Thông tin tệp → Quản lý phiên bản) để giữ cùng link và lịch sử. Người review gửi ý kiến trên chat nhóm.
  - Merge Request có review, CI, deploy: làm từ 26/10, khi có repo chung.
- Khi có repo chung: mỗi việc một nhánh; Merge Request ghi mã activity, nội dung, cách kiểm tra; ít nhất một người khác review; review chéo trả lời trong 24 giờ. Không đưa secret hay `.env` vào repo.
- Hoàn thành = chạy được, đúng yêu cầu, đã review, đã merge vào repo chung (trước 26/10: đã commit trên git local), Jira Done, đã log work.

## Quy tắc nghiệp vụ cần thể hiện trên giao diện

- 3 vai trò: Student; Organizer (thuộc một đơn vị: Khoa, CLB/Đội/Nhóm, phòng ban); Admin (duyệt sự kiện, xem theo đơn vị được giao).
- Đăng nhập bằng tài khoản mẫu có email trường, không SSO thật.
- Web responsive là đủ, không làm app mobile; thiết kế mobile-first.
- Sự kiện phải được duyệt trước khi công bố. Organizer không tự duyệt sự kiện mình tạo. Sau công bố, Organizer vẫn sửa hoặc hủy được, không phải duyệt lại.
- Hủy sự kiện thì các đăng ký bị hủy và waitlist đóng, nên phải có bước xác nhận.
- Sinh viên tự hủy đăng ký được đến 24 giờ trước giờ bắt đầu; sau đó liên hệ Organizer. Hết chỗ thì vào waitlist.
- Thông báo trong ứng dụng là bắt buộc (chuông thông báo); email là Should.
- Rủi ro R21 (bạn là owner): giao diện quét QR hoặc form vỡ layout trên điện thoại nhỏ (P 3, I 4). Dự phòng: giao diện HTML rút gọn.

---

## 1. A24 · Codebase, CI & deployment (găng), phần frontend

*Đầu vào có sẵn: `4-tai-nguyen/A24/` (xem `DAU-VAO.md`).*

**Mục tiêu chung của A24:** Có repo chạy được frontend React, backend Go, PostgreSQL ở máy dev và trên bản deploy, CI chạy build và test ở mỗi Merge Request, để từ A26 chỉ cần viết tính năng.

**Phân công:** TV5 làm cấu trúc repo, backend khung, database, CI, deploy. Bạn làm phần frontend. Lịch chia 4,45h/người.

**Các bước:**
1. **Làm trước tiên (22/10)**, vì A28 dựng trên khung này. Tạo dự án React trong repo git local của bạn, theo cấu trúc thư mục thống nhất với TV5 (đề xuất `src/frontend/`) để ghép vào repo chung sau:
   - công cụ build **[Đề xuất AI: Vite; Cần TV4 quyết]**;
   - router (ví dụ React Router);
   - base URL của API đọc từ biến môi trường build (ví dụ `VITE_API_BASE_URL`); thêm `.env.example`.
2. Một trang trống gọi `GET /api/health` và hiển thị kết quả, để kiểm frontend nói chuyện được với backend.
3. 27/10, cùng TV5, khi đã có repo chung (họp 25/10 chọn):
   - thêm bước build frontend vào CI (cài thư viện bằng `npm ci`, `npm run build`, test frontend nếu có);
   - deploy frontend lên hosting TV5 chọn;
   - xử lý CORS hoặc proxy giữa frontend và backend.
4. 28/10: viết phần frontend trong README: cài, cấu hình biến môi trường, chạy local, build. Mục tiêu: người ngoài nhóm dựng lại cả hệ thống trong dưới 30 phút.
5. Đẩy code lên repo chung, mở Merge Request, nhờ TV5 review.

**Hoàn thành khi:** trang React trên bản deploy gọi được `/api/health`; CI build frontend thành công ở Merge Request; README đủ để chạy local.

**Phụ thuộc:** chờ contract của TV3 (A25) và cấu trúc thư mục của TV5. Bước 3–5 cần repo chung (họp 25/10). A24 kết thúc khi phần của bạn xong (28/10) và chặn A26.

---

## 2. A28 · UI layout & shared components (găng)

*Đầu vào có sẵn: `4-tai-nguyen/A28/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Có khung giao diện responsive và bộ component dùng chung, để A26, A27 và các task sau chỉ ghép màn hình, không dựng lại.

**Đầu vào:**
- Khung React (mục 1 bước 1).
- API contract của TV3 (bạn review phần request/response).
- Nguyên tắc: không tự xây component khi đã có thư viện.

**Các bước:**
1. Chọn thư viện component **[Cần TV4 quyết, TV3 đồng ý; ví dụ MUI, Ant Design, Mantine]**. Tiêu chí: có sẵn bảng phân trang, form kiểm dữ liệu, hộp thoại, dùng tốt trên màn hình nhỏ.
2. Layout chung:
   - Thanh điều hướng theo vai trò:

     | Vai trò | Mục điều hướng |
     |---|---|
     | Student | Sự kiện, Đăng ký của tôi, Thông báo |
     | Organizer | Sự kiện của tôi, Tạo sự kiện, Thông báo |
     | Admin | Hàng chờ duyệt, Sự kiện |

   - Vùng nội dung.
   - Trang 404; trang "không có quyền" (403); hiển thị lỗi API chung.
3. Component dùng chung **[Đề xuất AI]**:
   - thẻ sự kiện (tên, thời gian, địa điểm, số chỗ còn lại);
   - bảng danh sách có phân trang;
   - form kiểm dữ liệu, hiện lỗi theo từng trường;
   - hộp xác nhận (hủy đăng ký, hủy sự kiện);
   - nhãn trạng thái sự kiện: Draft, Pending, Published, Rejected, Cancelled;
   - nhãn trạng thái đăng ký: đã đăng ký, waitlist kèm vị trí, đã hủy;
   - chuông thông báo có số chưa đọc.
4. Lớp gọi API dùng chung:
   - gửi kèm thông tin đăng nhập theo cơ chế TV5 chọn (cookie hoặc token);
   - 401 thì chuyển về trang đăng nhập; 403 thì hiện trang không có quyền; 400 thì hiện lỗi theo trường của form;
   - backend chưa có API thì dùng dữ liệu mock đúng theo contract.
5. Kiểm ở chiều rộng điện thoại nhỏ (khoảng 360px) và desktop (khoảng 1280px): không cuộn ngang, chữ đọc được, nút đủ lớn.
6. 26/10: đẩy lên repo chung, mở Merge Request, nhờ TV3 hoặc TV5 review. Trước đó gửi ảnh chụp màn hình lên Drive `Sprint 6-7/A28/` và chat để mọi người xem sớm. Nếu 26/10 vẫn chưa có repo chung thì review bằng ảnh chụp và chạy thử trên máy bạn, báo TV1.

**Hoàn thành khi:** màn hình mẫu hiển thị đúng trên điện thoại và desktop, không cuộn ngang; mỗi component dùng ở ít nhất một màn hình mẫu; Merge Request đã review.

**Phụ thuộc:** chờ A25. Chặn A27.

---

## 3. A23 · Họp chốt Baseline V1.0 (15h Chủ nhật 25/10)

*Đầu vào có sẵn: `4-tai-nguyen/A23/` (xem `DAU-VAO.md`).*

Cả nhóm xác nhận kế hoạch Baseline V1.0, TV1 ký. Khoảng 1h. Các mục cần ý kiến của bạn:

- **Repo và CI (mục 18):** GitLab tự host trên máy cá nhân, nhóm không truy cập được. Họp chọn nơi chứa repo chung (cũng là bản công khai gửi thầy) và nơi chạy CI. A24 cần repo ngày 26/10.
- **Bạn làm chung A39 với TV2:** test Increment 2 và regression, 25–27/11, 5,25h mỗi người. Bạn đã đồng ý riêng với TV1, nay xác nhận trước cả nhóm.
- **Lịch frontend của bạn:**

  | Task | Ngày | Giờ |
  |---|---|---|
  | A28 | 21–26/10 | |
  | A24 | đến 28/10 | |
  | A26 | 29–30/10 | |
  | A27 | 31/10–04/11 | |
  | A29 đăng ký và hủy | 05–07/11 | |
  | A62 waitlist | 08–10/11 | |
  | A35 màn hình check-in và báo cáo | 15–22/11 | 14,8h, task găng dài nhất của bạn |
  | A37 tích hợp | 23–24/11 | |
  | A39 | 25–27/11 | |
  | A53 sửa lỗi | 28–30/11 | |

- **Chia giờ A26, A24 (mục 17):** lịch hiện tại chia A26 đều 3 người, nên A26 phải chờ bạn xong A24 ngày 28/10, trong khi TV3, TV5 trống 24–28/10. Hai phương án khác:
  - **V1:** A26 không có phần của bạn (TV3 5,5h, TV5 5h); màn hình đăng nhập do TV5 làm hoặc bạn gộp vào A28. Nộp bài xong 06/12, dự trữ 1 ngày.
  - **V2:** V1, thêm phần A24 của bạn chỉ còn khung React 2h, TV5 làm phần còn lại 6,9h. Xong 05/12, dự trữ 2 ngày.

  Hãy cho biết 2h có đủ cho khung React không.

---

## 4. Việc duyệt trước họp A23 (hạn tối 24/10)

1. Đọc và duyệt các bước ở mục 1, 2, 5, 6 của file này: màn hình, component, số giờ (nhất là 4,45h cho phần A24). Ghi ý kiến lên chat nhóm.
2. Hướng màn hình của hai task sau (giao chi tiết ở sprint sau), cho ý kiến:
   - **A29 đăng ký và hủy** (05–07/11):
     - nút đăng ký và hủy ở chi tiết sự kiện, hiện số chỗ còn lại;
     - sau mốc 24 giờ thì ẩn nút hủy và hiện hướng dẫn liên hệ Organizer;
     - trang "đăng ký của tôi";
     - Organizer xem danh sách người đăng ký sự kiện của mình.
   - **A62 waitlist** (08–10/11):
     - hiện "đang ở waitlist, vị trí N";
     - thông báo khi được chuyển;
     - Organizer xem waitlist.
3. **Từ 27/10:** review test case A31 phần màn hình khi TV2 gửi, trả lời trong 24 giờ.

---

## 5. A26 · Authentication & roles (găng), phần màn hình

*Đầu vào có sẵn: `4-tai-nguyen/A26-A27/` (xem `DAU-VAO.md`).*

**Mục tiêu chung:** Người dùng đăng nhập bằng tài khoản mẫu có email trường và chỉ thấy, chỉ làm được phần của vai trò mình. Quyền thật do backend chặn.

**Phân công:**
- TV3: API đăng nhập và phân quyền backend.
- TV5: cơ chế phiên đăng nhập, seed tài khoản, deploy.
- Bạn: màn hình.

Lịch chia 3,5h/người. Đề xuất của TV3 ngày 14/10 không có phần của bạn, nên ba người thống nhất khi nhận task.

**Các bước:**
1. Màn hình đăng nhập: email, mật khẩu; báo lỗi khi sai hoặc khi email không phải email trường; trạng thái đang tải.
2. Sau đăng nhập gọi `GET /api/me` **[Đề xuất AI]** (trả họ tên, vai trò, đơn vị) rồi điều hướng:
   - Student → danh sách sự kiện;
   - Organizer → sự kiện của tôi;
   - Admin → hàng chờ duyệt.
3. Ẩn menu và route không thuộc vai trò (chỉ để dễ dùng; backend vẫn chặn).
4. Đăng xuất; hết phiên thì quay về trang đăng nhập.
5. Kiểm trên điện thoại và desktop; Merge Request nhờ TV3 review.

**Hoàn thành khi:** trên bản deploy, đăng nhập được bằng 3 tài khoản demo và vào đúng trang theo vai trò; sai mật khẩu báo lỗi đúng (test T-AUTH-01, 02).

**Phụ thuộc:** chờ A24 (28/10). Chặn A27.

---

## 6. A27 · Event management (găng), phần màn hình

*Đầu vào có sẵn: `4-tai-nguyen/A26-A27/` (xem `DAU-VAO.md`).*

**Mục tiêu chung:** Organizer tạo, sửa, gửi duyệt, sửa hoặc hủy sự kiện; Admin duyệt trước khi công bố; Student chỉ thấy sự kiện đã công bố.

**Phân công:**
- TV3: API sự kiện và luồng duyệt.
- TV5: API thông báo.
- Bạn: màn hình.

Lịch chia khoảng 8,4h/người.

**Các bước:**
1. **Student:**
   - danh sách sự kiện đã công bố (thẻ sự kiện, phân trang);
   - trang chi tiết sự kiện; nút đăng ký để chỗ sẵn, nối API ở A29.
2. **Organizer:**
   - "sự kiện của tôi" kèm nhãn trạng thái;
   - form tạo, sửa (tên, mô tả, địa điểm, giờ bắt đầu, giờ kết thúc, số chỗ), hiện lỗi theo trường;
   - nút gửi duyệt;
   - nút hủy sự kiện, có hộp xác nhận ghi rõ các đăng ký sẽ bị hủy;
   - hiện lý do khi bị từ chối.
3. **Admin:**
   - hàng chờ duyệt (lọc theo đơn vị được giao);
   - xem chi tiết; duyệt; từ chối kèm ô lý do;
   - không hiện nút duyệt cho sự kiện do chính người đó tạo.
4. **Chuông thông báo:** số chưa đọc, danh sách thông báo, đánh dấu đã đọc (API của TV5).
5. Kiểm trên điện thoại và desktop; Merge Request nhờ TV3 review.

**Hoàn thành khi:** trên bản deploy chạy được:
- tạo, sửa, gửi duyệt, duyệt, từ chối, công bố;
- Student không thấy sự kiện chưa duyệt;
- Organizer không có nút duyệt;
- chuông hiện thông báo.

(Tương ứng test T-EV-01…05, T-AUTH-04.)

**Phụ thuộc:** chờ A26, A28 và họp A23. Chặn A29.
