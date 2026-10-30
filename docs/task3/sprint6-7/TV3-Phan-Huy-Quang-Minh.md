---
Nội dung: Việc Sprint 6–7 (22/10–03/11) của TV3 Phan Huy Quang Minh (Tech Lead, Backend)
Người giao: TV1
Phiên bản: 0.3
Cập nhật: 22/10/2026
Trạng thái: AI hỗ trợ soạn (Claude Code, 22/10); TV1 duyệt 22/10; TV3 duyệt bước backend, database và báo ý kiến trên chat trước tối 24/10
---

# TV3 · Phan Huy Quang Minh · Sprint 6–7

Bạn chỉ cần file này. Mọi quy tắc nghiệp vụ, phân công và nội dung cần duyệt đều đã chép vào đây.

Đầu vào của từng task có sẵn trong gói upload trên Drive, thư mục `4-tai-nguyen/<mã task>/`; mỗi thư mục có `DAU-VAO.md` ghi từng đầu vào lấy ở đâu (có sẵn, tab Sheet, hay chờ ai tạo). Tài liệu dùng chung (đề bài, Client Log, REQ, mục tiêu, giả định, PD-01…05, sơ đồ, mẫu ghi giờ hồi tưởng hạn 23/10) ở `4-tai-nguyen/chung/`; báo cáo PDF ở `3-bao-cao/`.

## Tóm tắt

| # | Task | Jira | Giờ của bạn | Ngày | Ngày xong | Găng |
|---|---|---|---:|---|---|---|
| 1 | A25 Database schema & API contract (phần còn lại) | SCRUM-82 | 1,0 | 20/10 (nếu chưa xong: làm đầu tiên) | ngay | chặn 2 task găng |
| 2 | A20 Prototype QR check-in (spike), phần thử và đo | SCRUM-84 | 2,9 | 22–24/10 | **24/10** | không |
| 3 | A23 Họp chốt Baseline V1.0 | SCRUM-87 | 1,0 | 25/10 15h | 25/10 | |
| 4 | Việc duyệt trước họp A23 | | | 22–24/10 | **tối 24/10** | |
| 5 | A26 Authentication & roles, phần backend | SCRUM-91 | 3,5 | 29–30/10 | **30/10** | **có** |
| 6 | A27 Event management, phần sự kiện và duyệt | SCRUM-94 | 8,4 | 31/10–04/11 | **04/11** | **có** |

Tổng: 3,9h trong Sprint 6 (22–27/10), 11,5h trong Sprint 7. Lịch trống 24–28/10, dùng cho mục 4 và review test case của TV2.

## Kết quả của bạn dùng ở đâu trong bài nộp

Bạn không cần mở báo cáo. Báo cáo do TV1 soạn, đánh số đúng theo Task của đề: mục 3.5 của báo cáo là Task 3.5 của đề. Bạn chỉ cần để kết quả đúng nơi lưu dưới đây, TV1 đưa vào báo cáo.

| Kết quả | Nơi lưu | Dùng cho phần nào của bài nộp |
|---|---|---|
| Xác nhận thiết kế database (A25) | Sheet, tab 7 Product Description, dòng PD-02 | Product Descriptions (Task 2.2) |
| ERD, API contract (A25) | Drive `Sprint 6-7/A25/` (contract là file `.md`, ERD là ảnh hoặc file xuất); TV1 đưa vào repo sau | Hiện thực phần mềm (Task 3.1) |
| Kết quả spike QR có số đo (A20) | Drive `Sprint 6-7/A20/A20-spike-qr.md` | Bằng chứng chất lượng (Task 3.5); lower-level plan Increment 2 (Task 3.8) |
| R04 cập nhật | Sheet, tab Risk Register và Risk History | Cập nhật rủi ro và vấn đề (Task 3.4) |
| Ý kiến duyệt sơ đồ kiến trúc | chat nhóm | Hạ tầng dự án (Task 1.7) |
| Code A26, A27 và Merge Request đã review | git local, đẩy lên repo chung sau họp 25/10 | Hiện thực phần mềm (Task 3.1); hướng dẫn chạy (phụ lục repository) |
| Ý kiến tại họp A23 | biên bản TV1 ghi ở Sheet, tab Biên bản CP | Baseline V1.0 (Task 2.12) |
| Log work Jira, lịch sử commit | Jira, git (repo chung) | So sánh kế hoạch và thực tế (Task 3.3); đóng góp cá nhân (Task 4.6). Thầy có thể hỏi khi viva |

## Cần có trước khi bắt đầu

Thiếu mục nào thì báo người cung cấp và TV1 ngay, đừng chờ.

| Cần có | Nội dung tối thiểu | Ai cung cấp | Cần trước |
|---|---|---|---|
| Thư mục Drive `Sprint 6-7/A20`, `Sprint 6-7/A25`, quyền Người chỉnh sửa | Thư mục trống | TV1 | 22/10 |
| Quyền trên repo chung | Tạo nhánh, push, mở và review Merge Request | người tạo repo (họp 25/10 chọn) | 26/10 |
| Sheet Master quyền Editor | Tab 7 có dòng PD-02 với phần bổ sung 20/10 (units, notifications, migration PostgreSQL); tab Risk Register có R04, R17 | TV1 | 22/10 |
| Jira | SCRUM-82, 84, 91, 94 có tên bạn, có quyền log work | TV1 | 22/10 |
| Công cụ vẽ ERD | Bất kỳ công cụ nào xuất được ảnh hoặc file văn bản đưa vào repo (ví dụ dbdiagram, draw.io) | bạn chọn | A25 |
| Link prototype QR qua HTTPS | Trang quét QR, ô nhập mã, 5–10 mã QR mẫu | TV5 | 23/10 |
| ≥ 3 điện thoại, trình duyệt khác nhau | Ít nhất một Android, một iPhone nếu nhóm có | hỏi cả nhóm trên chat ngày 22/10 | 23/10. Không có iPhone thì ghi rõ trong kết luận spike |
| Repo khung (A24) trên repo chung | Go module, server, đọc cấu hình, kết nối PostgreSQL, công cụ migration đã chọn với migration `0001`, `/api/health`, CI chạy được, README chạy local | TV5, TV4 | 29/10 (A26) |
| Môi trường dev | Git, Go, PostgreSQL (cài trực tiếp hoặc container) trên máy bạn; giá trị `.env` local do TV5 gửi riêng, **không** qua repo | bạn, TV5 | 29/10 |
| Cơ chế phiên đăng nhập | Session hay token (quyết cùng TV5) | TV3, TV5 | 29/10 |

**API contract của bạn (A25) là đầu vào của TV4 (A28, 21–26/10) và TV2 (A31, 23–28/10).** Trước 23/10, tải lên Drive `Sprint 6-7/A25/` một contract tối thiểu có:
- danh sách endpoint của đăng nhập, `/api/me`, sự kiện, duyệt, hủy sự kiện, đăng ký, hủy đăng ký, waitlist, thông báo; mỗi endpoint ghi method, đường dẫn, vai trò được gọi, các trường request và response;
- một định dạng lỗi chung (ví dụ JSON có mã lỗi, thông điệp, lỗi theo từng trường cho 400) và các mã 400, 401, 403, 404, 409;
- giá trị trạng thái: sự kiện (draft, pending, published, rejected, cancelled), đăng ký (đã đăng ký, waitlist, đã hủy);
- cách phân trang danh sách.

## Lịch theo ngày

| Ngày | Task | Giờ | Việc | Thực tế |
|---|---|---:|---|---|
| 20/10 | A25 | 1,0 | (đã qua) Xác nhận thiết kế database, đưa contract vào repo | |
| Thứ Năm 22/10 | A20 | 2,0 | Chuẩn bị đo; cùng TV5 chọn thư viện QR | |
| Thứ Sáu 23/10 | A20 | 0,9 | Thử prototype, ghi số đo | |
| Thứ Bảy 24/10 | A20 | | Kết luận spike, cập nhật R04; gửi ý kiến duyệt (mục 4) | |
| Chủ nhật 25/10 | A23 | 1,0 | Họp 15h | |
| 26–28/10 | (trống) | | Review test case A31 khi TV2 gửi (27/10) | |
| Thứ Năm 29/10 | A26 | 2,0 | Migration users, roles, units; seed; API đăng nhập | |
| Thứ Sáu 30/10 | A26 | 1,5 | Middleware phân quyền; test | |
| 31/10–03/11 | A27 | 8,0 | Bảng events; CRUD; duyệt, công bố; hủy; thông báo khi đổi | |
| Thứ Tư 04/11 | A27 | 0,4 | (Sprint 8) phần còn lại | |

## Quy ước chung

- **[Đề xuất AI]**: tên bảng, cột, endpoint, thư viện do AI gợi ý để hình dung phạm vi. Schema và API contract bạn chốt ở A25 là nguồn chính; khác thì làm theo A25 và báo TV1 sửa. **[Cần X quyết]**: người được ghi tên quyết, ghi quyết định lên chat nhóm (khi có repo chung thì ghi cả vào mô tả Merge Request).
- **Găng:** lịch không còn ngày dự trữ trước demo 07/12, trễ một ngày ở task găng là trễ demo một ngày.
- Giờ theo lịch đã san tải (khoảng 2h/ngày) chỉ để định hướng; cái cần giữ là **ngày xong**. Giờ lập trình **đã gồm** tự test, review, sửa lỗi của chính task.
- Log work trên Jira trong ngày làm. Vượt quá 20% giờ hoặc thấy không kịp ngày xong: báo TV1 ngay trong ngày.
- Check-in 3 dòng trên chat thứ Tư 28/10 hoặc thứ Năm 29/10.
- **Tạm đến họp 25/10** (issue I03: GitLab tự host trên máy cá nhân, nhóm không truy cập được; họp 25/10 chọn nơi chứa repo chung và CI):
  - Code: dùng git trên máy bạn (`git init`), commit thường xuyên, đặt `git config user.name` và `user.email` đúng tên thật. Lịch sử commit là bằng chứng đóng góp và được giữ nguyên khi đẩy lên repo chung.
  - Tài liệu: file `.md` (lưu UTF-8), tải lên thư mục Drive `Sprint 6-7/<mã task>`. Sửa lại thì tải bản mới bằng **Quản lý phiên bản** của Drive (chuột phải vào file → Thông tin tệp → Quản lý phiên bản) để giữ cùng link và lịch sử. Người review gửi ý kiến trên chat nhóm.
  - Merge Request có review, CI, deploy: làm từ 26/10, khi có repo chung.
- Khi có repo chung: mỗi việc một nhánh; Merge Request ghi mã activity, nội dung, cách kiểm tra; ít nhất một người khác review; review chéo trả lời trong 24 giờ. Không đưa secret (mật khẩu, khóa, chuỗi kết nối thật, `.env`) vào repo, vì repo sẽ mirror công khai.
- Hoàn thành = chạy được, đúng yêu cầu, đã review, đã merge vào repo chung (trước 26/10: đã commit trên git local), Jira Done, đã log work.

## Quy tắc nghiệp vụ thầy đã xác nhận

- 3 vai trò: Student; Organizer (thuộc một đơn vị: Khoa, CLB/Đội/Nhóm, phòng ban); Admin (duyệt sự kiện, xem theo đơn vị được giao). Không làm role duyệt riêng.
- Đăng nhập: không SSO thật, mô phỏng bằng tài khoản mẫu có email trường.
- Quyền xem: Organizer chỉ xem sự kiện của mình; Admin theo đơn vị được giao; sinh viên chỉ xem dữ liệu của mình.
- Sự kiện phải được duyệt trước khi công bố. Organizer không tự duyệt sự kiện mình tạo.
- Sau công bố, Organizer được sửa hoặc hủy, không phải duyệt lại. Đổi thời gian hoặc địa điểm thì thông báo người đã đăng ký. Hủy sự kiện thì trạng thái Cancelled, hủy các đăng ký, đóng waitlist, thông báo.
- Hạn hủy đăng ký: đến 24 giờ trước giờ bắt đầu. Một đăng ký còn hiệu lực cho mỗi sinh viên và sự kiện; hủy rồi được đăng ký lại, nếu đầy thì vào cuối waitlist.
- Waitlist tự chuyển người đầu hàng, không có trạng thái chờ xác nhận. Thông báo lỗi vẫn tính là đã đăng ký.
- Thông báo trong ứng dụng là bắt buộc; email là Should (đang chờ thầy xác nhận).
- Quy mô giả định: 100 lượt đăng ký đồng thời không vượt chỗ; dữ liệu mẫu 500 lượt đăng ký.

---

## 1. A25 · Database schema & API contract (phần còn lại)

*Đầu vào có sẵn: `4-tai-nguyen/A25/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Có schema và API contract đã chốt, trên Drive nhóm, để TV5 dựng khung (A24), TV4 dựng component và lớp gọi API (A28), TV2 viết test case (A31) mà không phải đoán.

**Đầu vào:**
- Thiết kế database nhóm đã đồng ý 14/10: bảng users, roles, events, registrations, waitlist, attendance.
- Bổ sung ngày 20/10, chờ bạn xác nhận:
  - bảng **units** (đơn vị tổ chức, dùng cho quyền xem theo đơn vị);
  - bảng **notifications** (thông báo trong ứng dụng);
  - migration SQL cho PostgreSQL nằm trong mã nguồn Go.
- Ràng buộc:
  - không đăng ký trùng và không vượt số chỗ phải thực thi ở mức database;
  - tự chuyển đầu waitlist đúng một lần;
  - không tạo điểm danh trùng;
  - tên `snake_case`; 3NF trừ khi ghi lý do;
  - trạng thái sự kiện có Cancelled.

**Các bước:**
1. Xác nhận phần bổ sung trên Sheet, tab 7 Product Description, dòng PD-02: ghi tên và ngày.
2. Viết API contract thành file `.md` (ví dụ `api-contract.md`), xuất ERD ra ảnh hoặc file, ghi số phiên bản, tải lên Drive `Sprint 6-7/A25/`. Mỗi endpoint ghi:
   - method, đường dẫn, vai trò được gọi;
   - request, response;
   - mã lỗi (400, 401, 403, 404, 409).
3. Nhờ TV4 xác nhận phần request/response mà màn hình cần.
4. Báo TV1 để chuyển SCRUM-82 sang Done; báo TV5, TV4, TV2 đường dẫn contract.

**Hoàn thành khi:** tab 7 có xác nhận của bạn; TV4 xác nhận contract; contract có trên Drive.

**Phụ thuộc:** A24, A28 (găng) và A31 đều chờ task này. Chưa xong thì làm ngay đầu Sprint.

---

## 2. A20 · Prototype QR check-in (spike), phần thử và đo

*Đầu vào có sẵn: `4-tai-nguyen/A20/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Trong timebox 6h cho cả task, trả lời ba câu: quét QR bằng trình duyệt điện thoại có dùng được không, mất bao lâu, cần dự phòng thế nào. Kết quả dùng để làm đúng A33 (điểm danh, 15–19/11) ngay từ đầu.

**Phân công:** TV5 làm prototype (tối đa 3h, xong 23–24/10). Bạn thử và đo (khoảng 3h).

**Yêu cầu sản phẩm điểm danh:**
- median thời gian điểm danh ≤ 5 giây trong môi trường test của nhóm;
- không check-out;
- có nhập mã hoặc xác nhận thủ công khi QR không dùng được;
- chạy trên trình duyệt điện thoại, không cài ứng dụng;
- chỉ Organizer của sự kiện hoặc Admin được điểm danh.

Rủi ro R04 (QR chạy kém trên điện thoại hoặc mạng yếu): P 3, I 4.

**Các bước:**
1. **22/10, chuẩn bị:**
   - Chọn ≥ 3 tổ hợp thiết bị và trình duyệt trong nhóm. Ví dụ: Android + Chrome, iPhone + Safari, một máy Android đời cũ.
   - Định nghĩa cách đo: từ lúc đưa mã QR vào khung camera đến lúc màn hình báo đã ghi nhận. Mỗi thiết bị đo ≥ 10 lần, lấy median.
   - Chọn điều kiện đo: đủ sáng; thiếu sáng; mã hiển thị trên màn hình một điện thoại khác; mạng yếu.
   - Lập bảng kết quả với các cột: thiết bị, trình duyệt, điều kiện, 10 lần đo, median, lỗi gặp.
   - Cùng TV5 chọn thư viện quét QR.
2. **23–24/10, đo:**
   - Thử theo bảng đã lập.
   - Ghi riêng các lỗi gặp: quyền camera; camera chỉ mở trên HTTPS hoặc localhost (prototype phải chạy qua HTTPS); camera trước/sau; lấy nét.
   - Thử ô nhập mã dự phòng, đo thời gian nhập.
3. **Kết luận**, gồm:
   - dùng được hay không;
   - median trên từng thiết bị;
   - mã QR nên chứa gì: mã đăng ký ngẫu nhiên, không chứa họ tên, MSSV hay email;
   - những điểm A33 phải xử lý.
4. Ghi kết luận và số đo thật vào file `A20-spike-qr.md`, tải lên Drive `Sprint 6-7/A20/`.
5. Trên Sheet, tab Risk Register: cập nhật R04 (P, I, trạng thái, ghi chú). Thêm một dòng ở tab Risk History.
6. Hết 6h cho cả A20 thì dừng, ghi lại những gì đã biết, không kéo dài.

**Hoàn thành khi:** có kết luận và median trên ≥ 3 thiết bị; điểm chưa rõ đã ghi cho A33; R04 đã cập nhật.

---

## 3. A23 · Họp chốt Baseline V1.0 (15h Chủ nhật 25/10)

*Đầu vào có sẵn: `4-tai-nguyen/A23/` (xem `DAU-VAO.md`).*

Cả nhóm xác nhận kế hoạch Baseline V1.0, TV1 ký. Khoảng 1h. Các mục cần ý kiến của bạn:

- **Repo và CI (mục 18):** GitLab tự host trên máy cá nhân, nhóm không truy cập được. Họp chọn nơi chứa repo chung (cũng là bản công khai gửi thầy) và nơi chạy CI. A24 cần repo ngày 26/10.
- **Đường găng:** A24 → A26 → A27 → A29 → A62 → A32 → A35 → A37 → A39 → A53 → A41 → A47 → A54. Không còn ngày dự trữ trước demo 07/12.
- **Lịch backend của bạn:**

  | Task | Ngày |
  |---|---|
  | A26 | 29–30/10 |
  | A27 | 31/10–04/11 |
  | A29 đăng ký và hủy | 05–07/11 |
  | A62 waitlist | 08–10/11 (đang làm lúc Progress Check 09/11) |
  | A33 điểm danh, cùng TV5 | 15–19/11 |
  | A34 báo cáo, cùng TV5 | 19–24/11 |
  | A37 tích hợp | 23–24/11 |
  | A53 sửa lỗi và deploy | 28–30/11 |

- **Estimate:** giữ số PM chốt 20/10. Ý kiến trái chiều về giờ implement và test được theo dõi qua rủi ro R02 (bạn là owner) và Time Tracking.
- **Chia giờ A26, A24 (mục 17):** lịch hiện tại chia A26 đều 3 người (3,5h/người), nên A26 phải chờ TV4 xong A24 ngày 28/10, trong khi bạn và TV5 trống 24–28/10. Hai phương án khác:
  - **V1:** A26 theo đề xuất của bạn ngày 14/10 (TV3 5,5h, TV5 5h, TV4 0h; màn hình đăng nhập do TV5 làm hoặc gộp vào A28). Nộp bài xong 06/12, dự trữ 1 ngày.
  - **V2:** V1, thêm A24 TV5 làm 6,9h, TV4 chỉ làm khung React 2h. Xong 05/12, dự trữ 2 ngày.

  Nhóm chọn V0 (giữ), V1 hoặc V2.

---

## 4. Việc duyệt trước họp A23 (hạn tối 24/10)

Ghi ý kiến lên chat nhóm.

1. **Bước backend của A26, A27** (mục 5, 6 của file này): tên bảng, cột, endpoint, phân chia giờ với TV5, TV4. Sửa thẳng nếu khác contract A25.
2. **Bước backend của A29, A62 sắp tới** (giao chi tiết ở sprint sau), duyệt hướng:
   - **A29 đăng ký và hủy** (05–07/11, 12,6h, lịch chia 4,2h/người; đề xuất của bạn 7h):
     - bảng registrations (trạng thái, thời điểm đăng ký, thời điểm hủy);
     - ràng buộc ở database: một đăng ký còn hiệu lực cho mỗi sinh viên–sự kiện;
     - đếm chỗ và tạo đăng ký trong cùng transaction, **[Cần TV3 quyết]** cách khóa (ví dụ `SELECT … FOR UPDATE` trên dòng sự kiện, hoặc cập nhật có điều kiện);
     - chặn hủy khi còn dưới 24 giờ;
     - test 100 lượt đồng thời.
   - **A62 waitlist** (08–10/11, 13,4h, lịch chia khoảng 4,5h/người; đề xuất của bạn 7h):
     - bảng waitlist có thứ tự theo thời điểm vào hàng;
     - khi một đăng ký bị hủy, trong cùng transaction lấy đúng một người đầu hàng và chuyển thành đã đăng ký;
     - chặn chuyển trùng khi nhiều lượt hủy cùng lúc (rủi ro R17, bạn là owner);
     - thông báo lỗi không rollback việc chuyển.
3. **Sơ đồ kiến trúc** (AI vẽ 21/10, TV1 đưa vào báo cáo phần hạ tầng dự án, Task 1.7). Nội dung sơ đồ chép dưới đây; xác nhận đúng hay sửa:
   - Người dùng dùng trình duyệt web: Sinh viên, Organizer (Khoa, CLB/Đội/Nhóm, phòng ban), Admin duyệt sự kiện. Web responsive, không native mobile.
   - **Frontend React** (SPA, responsive): đăng nhập; tạo, sửa, duyệt, công bố sự kiện; đăng ký, hủy, waitlist; check-in (quét QR, nhập mã, xác nhận thủ công); báo cáo, xuất file. TV4 làm, gồm A28 layout và component, A35 màn hình check-in và báo cáo.
   - Frontend gọi backend qua HTTP API theo contract A25.
   - **Backend Go** (TV3, TV5). Các module:
     - xác thực, phân quyền (A26);
     - sự kiện, duyệt, công bố, sửa/hủy (A27);
     - đăng ký, hủy hạn 24 giờ (A29);
     - waitlist FIFO, tự chuyển (A62);
     - điểm danh QR và dự phòng (A33);
     - báo cáo, xuất CSV (A34);
     - thông báo trong ứng dụng dùng chung.

     Quyền xem theo vai trò và đơn vị; đăng nhập bằng tài khoản mẫu có email trường, không SSO thật.
   - **PostgreSQL**: users, roles, units, events, registrations, waitlist, attendance, notifications. Migration SQL nằm trong mã nguồn backend; ràng buộc một đăng ký còn hiệu lực cho mỗi sự kiện; không tạo điểm danh trùng.
   - **Mã nguồn, CI, triển khai** (TV5): repo GitLab của nhóm (mirror công khai để nộp; đang tự host, nhóm chưa truy cập được, họp 25/10 chọn lại); CI Jenkins (có thể đổi theo họp); hosting free-tier (nền tảng chưa chốt).
   - **Kênh thông báo:** trong ứng dụng là tối thiểu; email là Should.
4. **Từ 27/10:** review test case A31 phần backend khi TV2 gửi, trả lời trong 24 giờ.

---

## 5. A26 · Authentication & roles (găng), phần backend

*Đầu vào có sẵn: `4-tai-nguyen/A26-A27/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Người dùng đăng nhập bằng tài khoản mẫu có email trường và chỉ làm, chỉ xem được phần vai trò và đơn vị của mình cho phép. Phân quyền chặn ở backend, không chỉ ẩn nút.

**Đầu vào:**
- Repo chung, CI, deploy từ A24 (TV5, TV4; xong 28/10, sau khi họp 25/10 chọn nền tảng).
- Schema và contract A25.

**Phân công:**
- Bạn: migration, API đăng nhập, middleware phân quyền.
- TV5: cơ chế phiên đăng nhập, thư viện xác thực, seed, deploy.
- TV4: màn hình đăng nhập, điều hướng.

Lịch chia 3,5h/người; đề xuất của bạn 14/10 là TV3 5,5h, TV5 5h. Ba người thống nhất khi nhận task, khác lịch thì báo TV1.

**Các bước:**
1. Migration **[Đề xuất AI, theo A25]**:
   - `units` (id, name, type: faculty/club/office);
   - `users` (id, email duy nhất, password_hash, full_name, role: student/organizer/admin, unit_id cho Organizer);
   - gán Admin với các đơn vị được giao: bảng riêng hoặc cột tương đương, **[Cần TV3 quyết]**.

   Không lưu mật khẩu dạng rõ (bcrypt hoặc tương đương).
2. Seed cùng TV5:
   - tài khoản demo Student, Organizer, Admin;
   - tài khoản để test quyền: Student thứ 2, Organizer thuộc đơn vị khác.

   Mật khẩu seed lấy từ biến môi trường, không ghi vào repo.
3. Endpoint **[Đề xuất AI]**:
   - `POST /api/auth/login`: email, mật khẩu; chỉ nhận email đuôi trường; sai thì 401;
   - `POST /api/auth/logout`;
   - `GET /api/me`: id, họ tên, vai trò, đơn vị.
4. Middleware phân quyền dùng chung cho mọi API:
   - chưa đăng nhập thì 401; sai vai trò thì 403;
   - Organizer: kiểm sự kiện thuộc người đó;
   - Admin: kiểm đơn vị được giao.

   Viết sẵn hàm kiểm để A27, A29, A62 gọi lại.
5. Unit test middleware: 3 vai trò × có quyền/không quyền, và trường hợp chưa đăng nhập.

**Hoàn thành khi:**
- trên bản deploy, đăng nhập được bằng 3 tài khoản và vào đúng vai trò; sai mật khẩu bị từ chối; gọi API vai trò khác bị 401/403 (test T-AUTH-01…03);
- không có mật khẩu dạng rõ trong database hay repo;
- middleware kiểm được theo đơn vị.

**Phụ thuộc:** chờ A24 (28/10). Chặn A27.

---

## 6. A27 · Event management (găng), phần sự kiện và duyệt

*Đầu vào có sẵn: `4-tai-nguyen/A26-A27/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Organizer tạo, sửa, gửi duyệt, sửa hoặc hủy sự kiện; Admin duyệt trước khi công bố; Student chỉ thấy sự kiện đã công bố.

**Đầu vào:**
- A26 (đăng nhập, middleware).
- A28 (giao diện của TV4).
- Baseline V1.0 đã chốt (họp 25/10).

**Phân công:**
- Bạn: sự kiện và luồng duyệt.
- TV5: thông báo dùng chung (bảng notifications, hàm tạo thông báo, API xem/đánh dấu đã đọc).
- TV4: màn hình.

Lịch chia khoảng 8,4h/người (đề xuất của bạn 14/10: phần TV3 12h). Phân rã của bạn 14/10: CRUD và kiểm dữ liệu 3h; duyệt/công bố/quyền 2h; hủy sự kiện 3h; tích hợp thông báo 1h; tự test và sửa 3h.

**Các bước:**
1. Migration `events` **[Đề xuất AI]**:
   - cột: id, title, description, unit_id, organizer_id, location, start_at, end_at, capacity, status, reject_reason, created_at, updated_at;
   - status nhận các giá trị: draft, pending, published, rejected, cancelled;
   - kiểm dữ liệu: title bắt buộc, end_at sau start_at, capacity > 0.
2. Endpoint **[Đề xuất AI]**:
   - `POST /api/events`: Organizer, tạo Draft;
   - `PUT /api/events/{id}`: Organizer chủ sự kiện; Published sửa không phải duyệt lại;
   - `GET /api/events`: Student chỉ thấy published;
   - `GET /api/events/{id}`;
   - `GET /api/organizer/events`: sự kiện của mình.
3. Luồng duyệt:
   - `POST /api/events/{id}/submit`: Draft → Pending;
   - `POST /api/events/{id}/approve`: Admin, Pending → Published;
   - `POST /api/events/{id}/reject`: Admin, kèm lý do;
   - Organizer gọi approve sự kiện của chính mình phải nhận 403;
   - `GET /api/admin/events?status=pending`: hàng chờ duyệt, lọc theo đơn vị được giao.
4. Hủy sự kiện: `POST /api/events/{id}/cancel` chuyển sang Cancelled. Phần hủy đăng ký và đóng waitlist chạm bảng registrations, waitlist (A29, A62 tạo). **[Cần TV3 quyết]**, ghi lại để không làm trùng hay sót:
   - (a) tạo sẵn hai bảng này theo A25 ngay ở A27;
   - (b) A27 chỉ đổi trạng thái và gửi thông báo; hủy đăng ký và đóng waitlist làm ở A29, A62.
5. Đổi thời gian hoặc địa điểm sự kiện Published: gọi hàm thông báo dùng chung của TV5 cho từng người đã đăng ký (khi A29 có dữ liệu đăng ký). Khi Admin duyệt hoặc từ chối: thông báo Organizer.
6. Tự test luồng trạng thái và quyền. Review Merge Request phần thông báo của TV5.

**Hoàn thành khi:**
- trên bản deploy chạy đúng: tạo Draft; lỗi dữ liệu báo đúng trường; gửi duyệt vào hàng chờ; duyệt thành Published, từ chối kèm lý do; sửa sự kiện; Organizer không tự duyệt được; Student không thấy sự kiện chưa duyệt (test T-EV-01…05, T-AUTH-04);
- thông báo khi đổi hoặc hủy chạy khi có dữ liệu đăng ký (T-EV-06, 07).

Nếu trễ quá 1 ngày so với 04/11: báo TV1 xem xét cắt phần sửa/hủy sau công bố (REQ-21, mức Should, khoảng 8h).

**Phụ thuộc:** chờ A26, A28 và họp A23. Chặn A29 (05–07/11).
