---
Nội dung: Việc Sprint 6–7 (22/10–03/11) của TV2 Ngô Thanh Hùng (Tester)
Người giao: TV1
Phiên bản: 0.3
Cập nhật: 22/10/2026
Trạng thái: AI hỗ trợ soạn (Claude Code, 22/10); TV1 duyệt 22/10; TV2 đọc, sửa phần [Đề xuất AI] và báo ý kiến trên chat trước tối 24/10
---

# TV2 · Ngô Thanh Hùng · Sprint 6–7

Bạn chỉ cần file này. Mọi quy tắc, dữ liệu và nội dung mẫu cần dùng đều đã chép vào đây.

Đầu vào của từng task có sẵn trong gói upload trên Drive, thư mục `4-tai-nguyen/<mã task>/`; mỗi thư mục có `DAU-VAO.md` ghi từng đầu vào lấy ở đâu (có sẵn, tab Sheet, hay chờ ai tạo). Tài liệu dùng chung (đề bài, Client Log, REQ, mục tiêu, giả định, PD-01…05, sơ đồ, mẫu ghi giờ hồi tưởng hạn 23/10) ở `4-tai-nguyen/chung/`; báo cáo PDF ở `3-bao-cao/`.

## Tóm tắt

| # | Task | Jira | Giờ còn lại | Ngày | Ngày xong | Găng |
|---|---|---|---:|---|---|---|
| 1 | A22 Write quality plan & test strategy | SCRUM-81 | 2,0 | 22/10 | **22/10** | không |
| 2 | A31 Write test cases for increment 1 | SCRUM-93 | 10,5 | 23–28/10 | **28/10** | không (chặn CP3) |
| 3 | A23 Họp chốt Baseline V1.0 | SCRUM-87 | 1,0 | 25/10 15h | 25/10 | |

Tổng: 13h trong Sprint 6 (22–27/10), 0,5h trong Sprint 7. Sprint 7 còn trống; TV1 sẽ báo nếu giao thêm.

## Kết quả của bạn dùng ở đâu trong bài nộp

Bạn không cần mở báo cáo. Báo cáo do TV1 soạn, đánh số đúng theo Task của đề: mục 3.5 của báo cáo là Task 3.5 của đề. Bạn chỉ cần để kết quả đúng nơi lưu dưới đây, TV1 đưa vào báo cáo.

| Kết quả | Nơi lưu | Dùng cho phần nào của bài nộp |
|---|---|---|
| Quality plan v0.2 (A22) | Drive `Sprint 6-7/A22/2.12-quality-plan.md` (TV1 đưa vào repo sau) | Baseline V1.0 (Task 2.12); Bằng chứng chất lượng (Task 3.5) |
| Bộ test case Increment 1 (A31) | Drive `Sprint 6-7/A31/test-cases.md` (TV1 đưa vào repo sau) | Bằng chứng chất lượng (Task 3.5); ma trận truy vết Objective → … → Test (bắt buộc trong đề) |
| Mã test theo REQ | Sheet, tab 6 Traceability | Ma trận truy vết |
| Ý kiến tại họp A23 | biên bản TV1 ghi ở Sheet, tab Biên bản CP | Baseline V1.0 (Task 2.12) |
| Log work Jira | Jira | So sánh kế hoạch và thực tế (Task 3.3); đóng góp cá nhân (Task 4.6). Thầy có thể hỏi khi viva |

## Cần có trước khi bắt đầu

Thiếu mục nào thì báo người cung cấp và TV1 ngay, đừng chờ.

| Cần có | Nội dung tối thiểu | Ai cung cấp | Cần trước |
|---|---|---|---|
| Thư mục Drive `Sprint 6-7/A22`, `Sprint 6-7/A31`, quyền Người chỉnh sửa | Thư mục trống | TV1 | 22/10 |
| Trình soạn thảo văn bản | Bất kỳ, ví dụ VS Code, Notepad++; lưu file `.md` mã hóa UTF-8 | bạn | 22/10 |
| Sheet Master quyền Editor | Tab 6 Traceability có sẵn các dòng REQ-01…09, 15, 21 và cột mã test | TV1 | 28/10 |
| Jira | Task SCRUM-81, SCRUM-93 giao cho bạn, có quyền log work | TV1 | 22/10 |
| API contract (A25) | Danh sách endpoint: method, đường dẫn, vai trò, các trường request/response, mã lỗi. Đủ cho đăng nhập, sự kiện, duyệt, đăng ký, hủy, waitlist, thông báo | TV3 | 23/10. Chưa có thì viết test case theo hành vi (cột Các bước tả thao tác trên màn hình), điền endpoint sau |
| Quyết định công cụ test | Frontend (TV4), database test (TV3, TV5) | TV4, TV3, TV5 | Không chặn: để nguyên chỗ **[Cần … quyết]** trong quality plan |

## Lịch theo ngày

| Ngày | Task | Giờ | Việc | Thực tế |
|---|---|---:|---|---|
| 20–21/10 | A22 | 4,0 | (đã qua) | |
| Thứ Năm 22/10 | A22 | 2,0 | Hoàn tất quality plan, gửi TV1 duyệt | |
| Thứ Sáu 23/10 | A31 | 2,0 | Viết T-AUTH-01…06 | |
| Thứ Bảy 24/10 | A31 | 2,0 | Viết T-EV-01…07 | |
| Chủ nhật 25/10 | A23 | 1,0 | Họp 15h | |
| Chủ nhật 25/10 | A31 | 2,0 | Viết T-REG-01…05 | |
| Thứ Hai 26/10 | A31 | 2,0 | Viết T-WL-01…04, T-DEP-01 | |
| Thứ Ba 27/10 | A31 | 2,0 | Dữ liệu test; gửi TV3, TV4 review | |
| Thứ Tư 28/10 | A31 | 0,5 | Sửa theo review; cập nhật tab Traceability | |

## Quy ước chung

- **[Đề xuất AI]**: nội dung AI gợi ý, bạn sửa theo ý mình. **[Cần X quyết]**: người được ghi tên quyết.
- Giờ theo lịch đã san tải (khoảng 2h/ngày) chỉ để định hướng; cái cần giữ là **ngày xong**.
- Log work trên Jira trong ngày làm, đúng mã SCRUM. Vượt quá 20% giờ hoặc thấy không kịp ngày xong: báo TV1 trên chat ngay trong ngày.
- Check-in 3 dòng trên chat thứ Tư 28/10 hoặc thứ Năm 29/10: đã làm, sẽ làm, vướng gì.
- **Tạm đến họp 25/10** (issue I03: GitLab tự host trên máy cá nhân, nhóm không truy cập được). Bạn không cần repo:
  - Tài liệu: file `.md` (lưu UTF-8), tải lên thư mục Drive `Sprint 6-7/<mã task>`. Sửa lại thì tải bản mới bằng **Quản lý phiên bản** của Drive (chuột phải vào file → Thông tin tệp → Quản lý phiên bản) để giữ cùng link và lịch sử. Người review gửi ý kiến trên chat nhóm.
  - TV1 đưa file vào repo chung sau họp.
- Review chéo trả lời trong 24 giờ.
- Hoàn thành = đúng yêu cầu task, đã review, file `.md` đã lên Drive, Jira Done, đã log work.

---

## 1. A22 · Write quality plan & test strategy

*Đầu vào có sẵn: `4-tai-nguyen/A22/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Chốt quality plan để cả nhóm kiểm thử theo một quy ước mã thống nhất với tab Traceability trên Sheet, có tiêu chí ra rõ cho từng checkpoint.

**Đầu vào:** stack React, Go, PostgreSQL; CI Jenkins (quyết định 21/10; có thể đổi ở họp 25/10 vì GitLab tự host không truy cập được). Log CI bị xoay vòng, nên bằng chứng phải được tải về repo. Mã test nhóm đang dùng ở Sheet và ma trận truy vết: T-AUTH, T-EV, T-REG, T-WL, T-CI, T-RP, T-UI, T-INT, T-DEP. Bản v0.1 cũ dùng mã T-AU, T-RG nên không dùng lại.

**Các bước:**

1. Tạo file `2.12-quality-plan.md` bằng trình soạn thảo, chép nguyên khối nội dung mẫu dưới đây vào, lưu UTF-8. Không cần bản cũ.
2. Sửa các chỗ **[Đề xuất AI]** theo ý bạn. Để nguyên chỗ **[Cần TV4 quyết]**, **[Cần TV3/TV5 quyết]** và hỏi người đó trên chat.
3. Tải lên Drive `Sprint 6-7/A22/`, nhắn TV1 duyệt trên chat trong ngày 22/10.

**Nội dung mẫu (chép nguyên khối):**

````markdown
---
Activity: A22
Chủ sở hữu: TV2 (thực hiện), TV1 (duyệt)
Phiên bản: 0.2
Cập nhật: 22/10/2026
Trạng thái: TV2 soạn, AI hỗ trợ đề xuất (Claude Code, 22/10); TV1 duyệt bản mẫu 22/10, duyệt lại sau khi TV2 sửa
---

# Quality plan và test strategy

## Mục tiêu

Tạo bằng chứng chất lượng mà đề yêu cầu (Task 3.5): chứng minh requirement và sản phẩm quan trọng đã được kiểm tra.

## Ranh giới test (PM chốt 20/10)

- Giờ của task lập trình đã gồm dev tự test, review, sửa lỗi của chính task đó.
- A31, A40: viết test case. A30, A39: chạy test, regression, demo. A53: sửa lỗi sau kiểm thử và triển khai.

## Các mức kiểm thử

| Mức | Phạm vi | Công cụ | Ai làm | Khi nào |
|---|---|---|---|---|
| Unit | Logic nghiệp vụ: số chỗ, trùng đăng ký, hạn hủy 24 giờ, FIFO waitlist, quyền | `go test` (backend); frontend [Cần TV4 quyết] | người viết code | mỗi Merge Request, chạy trên CI |
| Integration | API + PostgreSQL; đăng ký và tự chuyển waitlist đồng thời | `go test` với database test [Cần TV3/TV5 quyết] | TV3, TV5 | trong task lập trình |
| End-to-end | Đăng nhập → tạo sự kiện → duyệt → đăng ký → waitlist → điểm danh → báo cáo | thủ công theo test case | TV2 | CP3 (A30), A39, CP5 (A41) |
| Thiết bị thật | Quét QR trên điện thoại, mạng yếu | thủ công, ≥ 3 thiết bị | TV3, TV5 | A20, A33 |
| UAT | Workflow cốt lõi theo tiêu chí nghiệm thu của client | kịch bản UAT | TV2, TV1 | CP5 (A41) |

## Review tài liệu

| Loại | Người review | Checklist |
|---|---|---|
| Tài liệu Task 1, Task 2, Task 3 | một thành viên khác người soạn, trong 24 giờ | metadata đủ; mã tham chiếu tồn tại; không mâu thuẫn bảng khác |
| Toàn bộ trước checkpoint | TV1 (A57) | truy vết Objective → Product → Activity → Resource → Risk → Test → Checkpoint nhất quán |

## Quy ước mã test

Mã `T-<nhóm>-<số hai chữ số>`, luôn gắn với ít nhất một REQ.

| Mã | Nhóm | REQ |
|---|---|---|
| T-AUTH | Đăng nhập, phân quyền, quyền xem dữ liệu | REQ-01, 02, 04, 15 |
| T-EV | Quản lý sự kiện, duyệt, công bố, sửa/hủy sau công bố | REQ-03, 04, 21 |
| T-REG | Đăng ký, hủy, số chỗ, đăng ký đồng thời | REQ-05, 06 |
| T-WL | Waitlist, tự chuyển, thông báo | REQ-07, 08, 09 |
| T-CI | Điểm danh QR và dự phòng | REQ-10, 11 |
| T-RP | Danh sách, thống kê, xuất Excel/CSV | REQ-12, 13, 14 |
| T-UI | Giao diện responsive | phi chức năng |
| T-INT | Tích hợp luồng chính | cả luồng |
| T-DEP | Bản deploy | phi chức năng |

Trường của test case: mã, REQ, mức, điều kiện trước, các bước, dữ liệu, kết quả kỳ vọng (bắt buộc); kết quả thực tế, ngày chạy, người chạy (khi chạy).

## Mức lỗi

| Mức | Định nghĩa [Đề xuất AI] |
|---|---|
| Nghiêm trọng | Chặn luồng chính, hoặc sai dữ liệu đăng ký, số chỗ, waitlist, quyền truy cập |
| Cao | Chức năng Must sai nhưng có cách đi vòng |
| Trung bình | Chức năng Should/Could sai; hiển thị sai số liệu không quan trọng |
| Thấp | Giao diện, chính tả |

Lỗi ghi ở `docs/quality/defects.md` và tạo issue Jira gắn mã test.

## Tiêu chí ra

- **Increment (CP3, A39):** 100% test case Must đã chạy và pass; không còn lỗi nghiêm trọng.
- **UAT (CP5):** các luồng Must được xác nhận; lỗi còn lại được phân loại và ghi vào danh sách tồn đọng.

## Lưu bằng chứng

Trước mỗi checkpoint, tải artifact CI (`evidence/build-<số>.md`, file kết quả test JUnit) về `docs/quality/results/`, tên file kèm ngày và số build.
````

**Đầu ra:** file `2.12-quality-plan.md` v0.2 trên Drive `Sprint 6-7/A22/`.

**Hoàn thành khi:** mã test đúng bảng trên; mỗi mức kiểm thử có công cụ, người làm, thời điểm; có định nghĩa mức lỗi; TV1 duyệt.

**Phụ thuộc:** A31 dùng quy ước mã của task này.

---

## 2. A31 · Write test cases for increment 1

*Đầu vào có sẵn: `4-tai-nguyen/A31/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Mỗi yêu cầu Must của Increment 1 có test case với kết quả kỳ vọng đo được, sẵn sàng chạy ở A30 (CP3, 11–16/11).

**Yêu cầu trong Increment 1:**

| REQ | Nội dung | Mức |
|---|---|---|
| REQ-01 | Đăng nhập mô phỏng tài khoản trường (không SSO thật; tài khoản mẫu có email trường) | Must |
| REQ-02 | Truy cập và xem dữ liệu theo vai trò Student, Organizer, Admin | Must |
| REQ-03 | Tạo, chỉnh sửa sự kiện | Must |
| REQ-04 | Phê duyệt trước khi công bố; Admin duyệt; Organizer không tự duyệt sự kiện mình tạo | Must |
| REQ-05 | Giới hạn số lượng đăng ký (capacity) | Must |
| REQ-06 | Đăng ký, hủy đăng ký | Must |
| REQ-07 | Danh sách chờ (waitlist) | Must |
| REQ-08 | Tự động chuyển người đầu waitlist khi có chỗ trống | Must |
| REQ-09 | Thông báo cho người được chuyển từ waitlist | Must |
| REQ-15 | Bảo vệ dữ liệu cá nhân cơ bản (phần quyền xem dữ liệu) | Must |
| REQ-21 | Sửa, hủy sự kiện đã công bố; thông báo khi đổi thời gian/địa điểm; hủy sự kiện thì hủy đăng ký, đóng waitlist | Should (giữ) |

**Quy tắc thầy đã xác nhận (dùng để viết kết quả kỳ vọng):**

- Sinh viên tự hủy được đến **24 giờ trước giờ bắt đầu**; sau mốc đó phải liên hệ Organizer.
- Mỗi sinh viên chỉ có **một đăng ký còn hiệu lực** cho mỗi sự kiện. Hủy rồi được đăng ký lại; nếu sự kiện đầy thì vào **cuối** waitlist.
- Hết chỗ thì **vào waitlist**, không bị từ chối.
- Khi có chỗ trống, hệ thống **tự chuyển** người đầu waitlist thành đã đăng ký và gửi thông báo. Không cần ban tổ chức duyệt, **không có trạng thái chờ xác nhận**. Thông báo lỗi thì người đó vẫn tính là đã đăng ký.
- Organizer chỉ xem sự kiện của mình. Admin xem theo đơn vị được giao. Sinh viên chỉ xem dữ liệu của mình.
- Organizer được sửa hoặc hủy sự kiện đã công bố, không phải duyệt lại. Đổi thời gian hoặc địa điểm thì thông báo người đã đăng ký. Hủy sự kiện thì trạng thái Cancelled, hủy các đăng ký, đóng waitlist, gửi thông báo.
- Quy mô giả định: 100 lượt đăng ký đồng thời không được vượt số chỗ.

**Các bước:**

1. Tạo file `test-cases.md` với khung sau (lưu UTF-8), rồi điền từng test case. Bản cũ trong bộ khởi tạo chỉ có 6 dòng mẫu sai mã, không cần:

   ````markdown
   ---
   Activity: A31
   Chủ sở hữu: TV2
   Phiên bản: 0.1
   Cập nhật: <ngày>
   Trạng thái: TV2 soạn; chờ TV3, TV4 review
   ---

   # Test case Increment 1

   | Mã | REQ | Mức | Điều kiện trước | Các bước | Dữ liệu | Kết quả kỳ vọng | Kết quả thực tế | Ngày chạy | Người chạy |
   |---|---|---|---|---|---|---|---|---|---|
   ````

2. Viết test case theo danh sách dưới **[Đề xuất AI về cách chia mã; bạn chỉnh]**. Cột "Mức" ghi unit, integration hoặc e2e.

   | Mã | REQ | Kiểm gì | Kết quả kỳ vọng |
   |---|---|---|---|
   | T-AUTH-01 | 01 | Đăng nhập bằng 3 tài khoản mẫu (Student, Organizer, Admin) | Vào đúng trang chủ của vai trò; menu đúng vai trò |
   | T-AUTH-02 | 01 | Sai mật khẩu; email không phải email trường | Báo lỗi, không tạo phiên đăng nhập |
   | T-AUTH-03 | 02 | Gọi API khi chưa đăng nhập; Student gọi API duyệt sự kiện | 401 khi chưa đăng nhập; 403 khi sai vai trò; dữ liệu không đổi |
   | T-AUTH-04 | 04 | Organizer gọi duyệt sự kiện do mình tạo; Student xem sự kiện chưa duyệt | 403; Student không thấy sự kiện Draft, Pending |
   | T-AUTH-05 | 02, 15 | Organizer B xem danh sách đăng ký sự kiện của Organizer A | 403 |
   | T-AUTH-06 | 02, 15 | Admin xem dữ liệu đơn vị không được giao; Student xem đăng ký của người khác | 403 hoặc không thấy (viết sẵn, chạy ở CP5) |
   | T-EV-01 | 03 | Organizer tạo sự kiện hợp lệ | Lưu, trạng thái Draft |
   | T-EV-02 | 03 | Thiếu tên; giờ kết thúc trước giờ bắt đầu; số chỗ ≤ 0 | Báo lỗi đúng trường, không lưu |
   | T-EV-03 | 04 | Organizer gửi duyệt | Trạng thái Pending; hiện ở hàng chờ duyệt của Admin |
   | T-EV-04 | 04 | Admin duyệt; Admin từ chối | Duyệt: Published, Student thấy. Từ chối: không công bố, Organizer thấy lý do |
   | T-EV-05 | 03 | Organizer sửa sự kiện Draft và Published | Lưu; sự kiện Published không phải duyệt lại |
   | T-EV-06 | 21 | Đổi thời gian hoặc địa điểm sự kiện Published đã có người đăng ký | Mỗi người đăng ký nhận đúng 1 thông báo trong ứng dụng |
   | T-EV-07 | 21 | Hủy sự kiện có người đăng ký và người trong waitlist | Cancelled; mọi đăng ký bị hủy; waitlist đóng; tất cả nhận thông báo; không đăng ký mới được |
   | T-REG-01 | 05, 06 | Đăng ký sự kiện còn chỗ | Đã đăng ký; số chỗ còn lại giảm 1 |
   | T-REG-02 | 06 | Đăng ký lần hai khi đăng ký đầu còn hiệu lực | Bị từ chối; không có bản ghi mới |
   | T-REG-03 | 06 | Hủy khi còn hơn 24 giờ; khi còn dưới 24 giờ (thử biên 24h01 và 23h59 trước giờ bắt đầu) | Trước mốc: hủy được, chỗ trống tăng 1. Sau mốc: bị chặn, hiện hướng dẫn liên hệ Organizer |
   | T-REG-04 | 06, 07 | Hủy rồi đăng ký lại, khi còn chỗ và khi đầy | Còn chỗ: đã đăng ký. Đầy: vào cuối waitlist |
   | T-REG-05 | 05 | 100 lượt đăng ký đồng thời vào sự kiện N chỗ (ví dụ N = 20) | Đúng N người đã đăng ký, còn lại vào waitlist, không vượt chỗ |
   | T-WL-01 | 07 | Đăng ký khi sự kiện đầy | Vào waitlist, hiện vị trí trong hàng |
   | T-WL-02 | 08, 09 | Một người đã đăng ký hủy | Đúng người đầu waitlist thành đã đăng ký, nhận thông báo; người sau lên một vị trí |
   | T-WL-03 | 09 | Tạo thông báo bị lỗi (giả lập) khi chuyển | Người được chuyển vẫn là đã đăng ký |
   | T-WL-04 | 08 | Nhiều người hủy cùng lúc | Số người được chuyển bằng số chỗ trống, đúng thứ tự, không ai được chuyển hai lần |
   | T-DEP-01 | phi chức năng | Mở bản deploy qua HTTPS, gọi `/api/health`, đăng nhập bằng tài khoản demo | Tất cả thành công |

3. Dữ liệu test (ghi trong file, ghi rõ là dữ liệu mẫu):
   - 3 tài khoản mẫu: Student, Organizer gắn một đơn vị, Admin;
   - thêm Student thứ 2, thứ 3 và Organizer thứ 2 thuộc đơn vị khác, để thử quyền;
   - một sự kiện 2 chỗ, để thử waitlist;
   - một sự kiện bắt đầu sau khoảng 23 giờ và một sau khoảng 25 giờ, để thử hạn hủy.

   Tên endpoint và mã lỗi chính xác lấy theo API contract TV3 đưa lên Drive `Sprint 6-7/A25/`. Chưa có thì hỏi TV3.
4. Tải file lên Drive `Sprint 6-7/A31/`, nhắn TV3 (phần backend) và TV4 (phần màn hình) review trên chat, nhờ trả lời trong 24 giờ; sửa theo ý kiến, tải bản mới bằng Quản lý phiên bản.
5. Trên Sheet, tab 6 Traceability: điền mã test cho REQ-01…09, 15, 21.

**Đầu ra:** file `test-cases.md` trên Drive `Sprint 6-7/A31/` có bộ test Increment 1; tab Traceability có mã test.

**Hoàn thành khi:** 100% REQ Must của Increment 1 có ít nhất một test case; mọi test case có kết quả kỳ vọng đo được; TV3 hoặc TV4 đã review; mã test khớp quy ước của A22.

**Phụ thuộc:** cần API contract của TV3 (A25) và quy ước mã (A22). Task này chặn A30 (CP3).

---

## 3. A23 · Họp chốt Baseline V1.0 (15h Chủ nhật 25/10)

*Đầu vào có sẵn: `4-tai-nguyen/A23/` (xem `DAU-VAO.md`).*

Cả nhóm xác nhận kế hoạch Baseline V1.0, TV1 ký. Khoảng 1h. Các mục liên quan tới bạn, cần có ý kiến:

- **Repo và CI (mục 18):** GitLab tự host trên máy cá nhân, nhóm không truy cập được. Họp chọn nơi chứa repo chung (cũng là bản công khai gửi thầy) và nơi chạy CI. A24 cần repo ngày 26/10.
- **Phần việc TV2 làm thay TV1 (khoảng 19h):** A22 6h; A43 kế hoạch đóng dự án và bàn giao 5,2h (21–24/11); viết phần kiểm thử, chất lượng cho báo cáo cuối kỳ A45 5h (17–26/11; TV1 gửi danh sách nội dung cần viết khi tới lúc, bạn không cần mở báo cáo); phần chất lượng của phân tích kế hoạch so với thực tế A42 3h (10/11–02/12). Bạn đã đồng ý riêng với TV1, nay xác nhận trước cả nhóm.
- **Lịch kiểm thử:** CP3, chạy test và demo Increment 1 (A30): 11–16/11, trễ 15 ngày so với kế hoạch đầu 01/11. Test case Increment 2 (A40): 15–19/11. Test Increment 2 và regression (A39, cùng TV4): 25–27/11. UAT (A41, cùng TV1): 01–05/12. Không còn ngày dự trữ trước demo 07/12.
- **Mã test:** thống nhất T-REG (không dùng T-RG) và bảng mã ở A22.
