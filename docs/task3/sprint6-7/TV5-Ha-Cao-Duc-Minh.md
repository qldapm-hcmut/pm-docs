---
Nội dung: Việc Sprint 6–7 (22/10–03/11) của TV5 Hà Cao Đức Minh (Backend, DevOps)
Người giao: TV1
Phiên bản: 0.3
Cập nhật: 22/10/2026
Trạng thái: AI hỗ trợ soạn (Claude Code, 22/10); TV1 duyệt 22/10; TV5 duyệt bước repo, CI, deploy, QR và báo ý kiến trên chat trước tối 24/10
---

# TV5 · Hà Cao Đức Minh · Sprint 6–7

Bạn chỉ cần file này. Mọi quy tắc, phân công và đoạn code Jenkins cần dùng đều đã chép vào đây.

Đầu vào của từng task có sẵn trong gói upload trên Drive, thư mục `4-tai-nguyen/<mã task>/`; mỗi thư mục có `DAU-VAO.md` ghi từng đầu vào lấy ở đâu (có sẵn, tab Sheet, hay chờ ai tạo). Tài liệu dùng chung (đề bài, Client Log, REQ, mục tiêu, giả định, PD-01…05, sơ đồ, mẫu ghi giờ hồi tưởng hạn 23/10) ở `4-tai-nguyen/chung/`; báo cáo PDF ở `3-bao-cao/`.

## Tóm tắt

| # | Task | Jira | Giờ của bạn | Ngày | Ngày xong | Găng |
|---|---|---|---:|---|---|---|
| 1 | A24 Codebase, CI & deployment, phần repo, backend, CI, deploy | SCRUM-88 | 4,45 | 21–23/10 phần trên máy; 26–28/10 CI, deploy (sau họp) | **28/10** | **có** |
| 2 | A20 Prototype QR check-in (spike), phần prototype | SCRUM-84 | 2,85 | 23–24/10 | **24/10** | không |
| 3 | A23 Họp chốt Baseline V1.0 | SCRUM-87 | 1,0 | 25/10 15h | 25/10 | |
| 4 | Việc trước họp A23: ý kiến chọn repo và CI, duyệt bước; sau họp: kiểm `Baseline frozen` | | | 22–24/10; 26–28/10 | **tối 24/10**; 28/10 | |
| 5 | A26 Authentication & roles, phần phiên đăng nhập, seed, deploy | SCRUM-91 | 3,5 | 29–30/10 | **30/10** | **có** |
| 6 | A27 Event management, phần thông báo dùng chung | SCRUM-94 | 8,4 | 31/10–04/11 | **04/11** | **có** |

Tổng: 6,3h trong Sprint 6 (22–27/10), 11,5h trong Sprint 7. Lịch trống 26–28/10. Phần A24 của bạn nhiều việc hơn 4,45h; nếu vượt, dùng giờ trống này. Việc đó không ảnh hưởng đường găng, vì A24 vẫn chờ TV4 đến 28/10. Phần CI, deploy, Merge Request của A24 dời vào 26–28/10 vì chưa có repo chung (GitLab tự host không truy cập được, họp 25/10 chọn). **Họp chưa chốt được thì A24 (găng) trễ theo.**

## Kết quả của bạn dùng ở đâu trong bài nộp

Bạn không cần mở báo cáo. Báo cáo do TV1 soạn, đánh số đúng theo Task của đề: mục 3.5 của báo cáo là Task 3.5 của đề. Bạn chỉ cần để kết quả đúng nơi lưu dưới đây, TV1 đưa vào báo cáo.

| Kết quả | Nơi lưu | Dùng cho phần nào của bài nộp |
|---|---|---|
| Repo khung, code A26, A27 và Merge Request đã review | git local, đẩy lên repo chung sau họp 25/10 | Hiện thực phần mềm (Task 3.1) |
| README, URL deploy | repo chung | Hướng dẫn chạy (đề bắt buộc nộp link repo kèm hướng dẫn chạy) |
| Pipeline CI, artifact build (`evidence/`, kết quả test) | CI (nền tảng họp 25/10 chọn); tải về `docs/quality/results/` trước mỗi checkpoint | Bằng chứng chất lượng (Task 3.5) |
| Kết quả kiểm stage `Baseline frozen` | báo TV1 trên chat | Baseline V1.0 (Task 2.12): chứng minh baseline đã duyệt không bị sửa |
| Thư viện QR, cách mở camera (A20) | gửi TV3 ghi vào kết quả spike | Bằng chứng chất lượng (Task 3.5) |
| R20, R09, R18 nếu có thay đổi | Sheet, tab Risk Register và Risk History | Cập nhật rủi ro và vấn đề (Task 3.4) |
| Log work Jira, lịch sử commit | Jira, git (repo chung) | So sánh kế hoạch và thực tế (Task 3.3); đóng góp cá nhân (Task 4.6). Thầy có thể hỏi khi viva |

## Cần có trước khi bắt đầu

Thiếu mục nào thì báo người cung cấp và TV1 ngay, đừng chờ. Mật khẩu và khóa chỉ trao đổi riêng, không ghi vào repo, Jira hay chat chung.

| Cần có | Nội dung tối thiểu | Ai cung cấp | Cần trước |
|---|---|---|---|
| Git, Go, PostgreSQL (cài trực tiếp hoặc container) trên máy | Repo git local cho backend | bạn | **22/10** |
| Cấu trúc thư mục thống nhất với TV4 | Ví dụ `src/frontend/`, `src/backend/` | bạn báo TV4 | **sáng 22/10** |
| Repo chung và quyền quản trị | Tạo nhánh, bảo vệ nhánh chính, cấu hình webhook | họp 25/10 chọn | 26/10 |
| **Bộ khởi tạo `docs/` trong repo chung** | Đủ 12 thư mục `docs/plan`, `client`, `task1`…`task4`, `baseline`, `logs`, `checkpoints`, `change`, `quality`, `reflection` (thư mục trống cần file `.gitkeep`). Nếu giữ Jenkins: thiếu một thư mục là stage `Docs structure` làm fail mọi build | TV1 đưa vào sau họp | 26/10, trước khi bật CI |
| CI chạy được | Giữ Jenkins: quyền quản trị Jenkins, plugin nhận Merge Request, credential truy cập repo, Go và Node trên agent, `Jenkinsfile` có stage `Baseline frozen` (đoạn code ở mục 4). Đổi nền tảng: CI của nền tảng mới | họp 25/10 chọn | 26/10 |
| Tài khoản hosting free-tier | Backend, PostgreSQL, frontend; có HTTPS; biến môi trường cấu hình được trên hosting | bạn tạo (dùng email nhóm nếu có) | 26–28/10 |
| API contract, schema (A25) | Bảng nền (units, users) để viết migration `0001`; định dạng lỗi chung | TV3 | 22/10 (migration có thể làm sau, khung server không chờ) |
| Công cụ quét secret | Ví dụ gitleaks | bạn | trước khi mirror công khai |
| Thư viện QR; đường hầm HTTPS tạm hoặc dịch vụ host tĩnh | Camera điện thoại chỉ mở trên HTTPS; chưa có bản deploy trước 26/10 | bạn | 23/10 |
| Jira | SCRUM-84, 88, 91, 94 có tên bạn, có quyền log work | TV1 | 22/10 |

## Lịch theo ngày

| Ngày | Task | Giờ | Việc | Thực tế |
|---|---|---:|---|---|
| 21/10 | A24 | 2,0 | (đã qua) | |
| Thứ Năm 22/10 | A24 | 2,0 | Cấu trúc repo (báo TV4 ngay); backend khung; PostgreSQL local; migration | |
| Thứ Sáu 23/10 | A24 | 0,5 | `.env.example`, `.gitignore`, README chạy local | |
| Thứ Sáu 23/10 | A20 | 1,6 | Prototype quét QR, ô nhập mã | |
| Thứ Bảy 24/10 | A20 | 1,3 | Hoàn tất prototype qua HTTPS, gửi TV3 đo; gửi ý kiến duyệt | |
| Chủ nhật 25/10 | A23 | 1,0 | Họp 15h | |
| 26–28/10 | A24 (dời từ trước họp) | | Đẩy code lên repo chung; CI, deploy, Merge Request; nối frontend cùng TV4 (27/10); kiểm `Baseline frozen` | |
| Thứ Năm 29/10 | A26 | 2,0 | Cơ chế phiên đăng nhập; seed tài khoản | |
| Thứ Sáu 30/10 | A26 | 1,5 | Deploy A26; tự chạy test đăng nhập | |
| 31/10–03/11 | A27 | 8,0 | Thông báo dùng chung | |
| Thứ Tư 04/11 | A27 | 0,4 | (Sprint 8) phần còn lại | |

## Quy ước chung

- **[Đề xuất AI]**: tên thư mục, biến môi trường, bảng, endpoint, thư viện, đoạn code do AI gợi ý. Schema và API contract TV3 chốt (A25) là nguồn chính. **[Cần X quyết]**: người được ghi tên quyết, ghi quyết định lên chat nhóm (khi có repo chung thì ghi cả vào mô tả Merge Request).
- **Găng:** lịch không còn ngày dự trữ trước demo 07/12, trễ một ngày ở task găng là trễ demo một ngày.
- Giờ theo lịch đã san tải (khoảng 2h/ngày) chỉ để định hướng; cái cần giữ là **ngày xong**. Giờ lập trình **đã gồm** tự test, review, sửa lỗi.
- Log work trên Jira trong ngày làm. Vượt quá 20% giờ hoặc thấy không kịp ngày xong: báo TV1 ngay trong ngày.
- Check-in 3 dòng trên chat thứ Tư 28/10 hoặc thứ Năm 29/10.
- **Tạm đến họp 25/10** (issue I03: GitLab tự host trên máy cá nhân, nhóm không truy cập được; họp 25/10 chọn nơi chứa repo chung và CI):
  - Code: dùng git trên máy bạn (`git init`), commit thường xuyên, đặt `git config user.name` và `user.email` đúng tên thật. Lịch sử commit là bằng chứng đóng góp và được giữ nguyên khi đẩy lên repo chung.
  - Tài liệu: file `.md` (lưu UTF-8), tải lên thư mục Drive `Sprint 6-7/<mã task>`. Sửa lại thì tải bản mới bằng **Quản lý phiên bản** của Drive (chuột phải vào file → Thông tin tệp → Quản lý phiên bản) để giữ cùng link và lịch sử. Người review gửi ý kiến trên chat nhóm.
  - Merge Request có review, CI, deploy: làm từ 26/10, khi có repo chung.
- Khi có repo chung: mỗi việc một nhánh; Merge Request ghi mã activity, nội dung, cách kiểm tra; ít nhất một người khác review; review chéo trả lời trong 24 giờ.
- Hoàn thành = chạy được, đúng yêu cầu, đã review, đã merge vào repo chung (trước 26/10: đã commit trên git local), Jira Done, đã log work.

## Quy tắc và ràng buộc liên quan tới bạn

- Stack: React, Go, PostgreSQL. CI: Jenkins (nhóm chọn 21/10; có thể đổi ở họp 25/10 vì GitLab tự host không truy cập được). Hosting: free-tier, chi phí 0 VND.
- Repo của nhóm sẽ có bản công khai cho thầy xem. Rủi ro R20 (bạn là owner): lộ thông tin xác thực khi mirror (P 2, I 5). Không đưa secret vào repo; quét trước khi mirror; mật khẩu nào từng nằm trong file thì phải đổi.
- Rủi ro R09 (bạn là owner): hosting lỗi trước demo. Giảm thiểu: deploy sớm, kiểm tra trước demo 2 ngày.
- Đăng nhập: không SSO thật, tài khoản mẫu có email trường; 3 tài khoản demo Student, Organizer, Admin.
- Thông báo trong ứng dụng là bắt buộc; email là Should (đang chờ thầy xác nhận). Rủi ro R18 (bạn là owner): thông báo thất bại. Thông báo lỗi **không** được hoàn tác thao tác chính; người được chuyển từ waitlist vẫn là đã đăng ký.
- Điểm danh: median ≤ 5 giây; chạy trên trình duyệt điện thoại, không cài ứng dụng; có nhập mã hoặc xác nhận thủ công; không check-out. Camera trên trình duyệt chỉ mở được trên HTTPS hoặc localhost.

---

## 1. A24 · Codebase, CI & deployment (găng), phần của bạn

*Đầu vào có sẵn: `4-tai-nguyen/A24/` (xem `DAU-VAO.md`).*

**Mục tiêu chung:** Có repo chạy được frontend React, backend Go, PostgreSQL ở máy dev và trên bản deploy, CI chạy build và test ở mỗi Merge Request, để từ A26 chỉ cần viết tính năng.

**Hiện trạng bộ khởi tạo (đang ở máy TV1, đưa vào repo chung sau họp 25/10):**
- `docs/` bắt buộc phải có: stage `Docs structure` kiểm đủ các thư mục con plan, client, task1–task4, baseline, logs, checkpoints, change, quality, reflection.
- `src/` đang trống.
- `Jenkinsfile` có các stage Checkout, Baseline frozen, Docs structure, Build & test, Thu thập bằng chứng. Stage `Build & test` hiện chỉ chạy `npm ci` và `npm test` trong `src/` khi có `src/package.json`, nên **chưa build được Go**.

**Phân công:** bạn làm phần dưới. TV4 làm khung React, đưa frontend lên CI và deploy, viết README frontend.

**Các bước:**
1. **Cấu trúc repo [Cần TV3/TV5 quyết]**. Đề xuất AI: một repo, giữ `docs/`, code trong `src/frontend/` (React) và `src/backend/` (Go), migration trong `src/backend/migrations/`. **Báo TV4 đường dẫn ngay trong 22/10**, vì TV4 tạo khung React đầu tiên. Trước 26/10, mỗi người làm trong repo git local theo cấu trúc này.
2. **Backend Go khung:**
   - điểm vào HTTP server;
   - đọc cấu hình từ biến môi trường **[Đề xuất AI]**: `DATABASE_URL`, `PORT`, `APP_ENV`, `FRONTEND_ORIGIN` (CORS), `SESSION_SECRET`;
   - kết nối PostgreSQL;
   - `GET /api/health` trả trạng thái server và database;
   - lệnh chạy migration.

   **[Cần TV3/TV5 quyết]**: router (ví dụ `net/http` chuẩn, chi, gin), driver (ví dụ pgx), công cụ migration (ví dụ golang-migrate, goose).
3. Migration `0001` tạo bảng nền theo A25 (ví dụ units, users) để kiểm luồng migration. Bảng nghiệp vụ thêm dần ở các task sau.
4. **Môi trường local:**
   - PostgreSQL chạy bằng container hoặc cài trực tiếp, ghi cả hai cách vào README;
   - `.env.example` chỉ có tên biến và giá trị giả;
   - `.gitignore` loại `.env`, thư mục build, `node_modules`.
5. **CI (26–28/10, sau họp).** Nếu họp giữ Jenkins: thay stage `Build & test` bằng đoạn dưới **[Đề xuất AI; cần Go và Node trên agent Jenkins]**, giữ nguyên các stage khác. Nếu đổi nền tảng: viết bước tương đương (go vet, go test xuất JUnit, npm ci, npm run build) trên CI mới.

   ```groovy
   stage('Build & test') {
     steps {
       script {
         if (fileExists('src/backend/go.mod')) {
           dir('src/backend') {
             sh 'go vet ./...'
             sh 'go run gotest.tools/gotestsum@latest --junitfile junit-backend.xml ./...'
           }
         }
         if (fileExists('src/frontend/package.json')) {
           dir('src/frontend') {
             sh 'npm ci'
             sh 'npm run build'
           }
         }
       }
     }
     post {
       always {
         junit allowEmptyResults: true, testResults: 'src/**/junit*.xml'
       }
     }
   }
   ```

   File `junit-backend.xml` nằm ở `src/backend/`, nên stage `Thu thập bằng chứng` (lệnh `cp src/**/junit*.xml`) vẫn thu được. Không thêm `|| true` vào lệnh test, để test lỗi thì build fail.
6. Kiểm CI chạy ở mỗi Merge Request của repo chung và báo trạng thái build lên Merge Request.
7. **Deploy (26–28/10, sau khi có repo chung):**
   - chọn hosting free-tier **[Cần TV5 quyết; kiểm điều kiện free-tier hiện tại. Ví dụ: Render, Railway, Fly.io cho backend; Neon, Supabase cho PostgreSQL]**;
   - **bắt buộc HTTPS** (camera trên điện thoại cần HTTPS cho QR);
   - ghi URL vào README;
   - free-tier hay ngủ khi không có truy cập, nên ghi cách đánh thức trước demo.
8. Quét secret trước khi đẩy lên repo sẽ mirror (ví dụ gitleaks, **[Đề xuất AI]**). Mật khẩu nào từng có trong lịch sử commit thì đổi.
9. README phần backend, database, deploy. Mục tiêu: người ngoài nhóm dựng lại cả hệ thống trong dưới 30 phút. Đẩy lên repo chung, mở Merge Request, nhờ TV3 review.

**Hoàn thành khi:**
- một Merge Request mẫu chạy CI pass và có người review;
- `GET /api/health` trả thành công trên bản deploy qua HTTPS;
- repo không chứa secret;
- sau khi TV4 xong: mở bản deploy, gọi health, đăng nhập được (test T-DEP-01).

**Phụ thuộc:** chờ contract của TV3 (A25). Bước 5–7 cần repo chung (họp 25/10). Chặn A26.

---

## 2. A20 · Prototype QR check-in (spike), phần prototype

*Đầu vào có sẵn: `4-tai-nguyen/A20/` (xem `DAU-VAO.md`).*

**Mục tiêu chung:** Trong timebox 6h cho cả task, trả lời: quét QR bằng trình duyệt điện thoại có dùng được không, mất bao lâu, cần dự phòng thế nào. Kết quả dùng để làm đúng A33 (điểm danh, 15–19/11, bạn chủ trì cùng TV3).

**Phân công:** bạn làm prototype, tối đa 3h. TV3 thử và đo trên ≥ 3 thiết bị (23–24/10).

**Các bước:**
1. 22/10: cùng TV3 chọn thư viện quét QR trên trình duyệt **[Cần TV5 quyết; ví dụ html5-qrcode, @zxing/browser]**.
2. Làm một trang web đơn giản:
   - mở camera sau, quét mã, hiện nội dung mã và thời điểm quét;
   - ô nhập mã dự phòng;
   - hiện thời gian xử lý trên màn hình để TV3 đo.
3. Sinh 5–10 mã QR mẫu chứa mã ngẫu nhiên kiểu mã đăng ký, không chứa họ tên, MSSV hay email.
4. Chạy prototype qua HTTPS (chưa có bản deploy trước 26/10): một đường hầm HTTPS tạm từ máy bạn (ví dụ cloudflared, ngrok) hoặc dịch vụ host tĩnh kéo-thả không cần git (ví dụ Netlify Drop) **[Đề xuất AI; Cần TV5 quyết]**. Gửi link cho TV3 trong ngày 23/10.
5. Lưu code prototype trong repo git local (thư mục hoặc nhánh riêng); không đưa vào nhánh chính của repo chung nếu A33 không dùng lại. Ghi tên thư viện đã chọn và lý do cho TV3 đưa vào ghi chú kết quả spike.

**Hoàn thành khi:** TV3 đo được trên ≥ 3 thiết bị; thư viện và cách mở camera đã được ghi lại cho A33.

---

## 3. A23 · Họp chốt Baseline V1.0 (15h Chủ nhật 25/10)

*Đầu vào có sẵn: `4-tai-nguyen/A23/` (xem `DAU-VAO.md`).*

Cả nhóm xác nhận kế hoạch Baseline V1.0, TV1 ký. Khoảng 1h. Các mục cần ý kiến của bạn:

- **Bạn làm chung A34 với TV3:** báo cáo và xuất Excel/CSV, 19–24/11, 7,4h mỗi người. Bạn đã đồng ý riêng với TV1, nay xác nhận trước cả nhóm.
- **Lịch của bạn:**

  | Task | Ngày |
  |---|---|
  | A26 | 29–30/10 |
  | A27 | 31/10–04/11 |
  | A29 | 05–07/11 |
  | A62 | 08–10/11 |
  | A33 điểm danh QR, chủ trì | 15–19/11 |
  | A34 | 19–24/11 |
  | A37 tích hợp | 23–24/11 |
  | A53 sửa lỗi và deploy bản release | 28–30/11 |

- **Chia giờ A26, A24 (mục 17):** lịch hiện tại chia A26 đều 3 người, nên A26 phải chờ TV4 xong A24 ngày 28/10, trong khi bạn và TV3 trống 24–28/10. Hai phương án khác:
  - **V1:** A26 theo đề xuất của TV3 ngày 14/10 (TV3 5,5h, bạn 5h, TV4 0h; màn hình đăng nhập do bạn làm hoặc TV4 gộp vào A28). Nộp bài xong 06/12, dự trữ 1 ngày.
  - **V2:** V1, thêm bạn nhận 6,9h của A24 (TV4 chỉ làm khung React 2h). Xong 05/12, dự trữ 2 ngày.

  Hãy cho biết bạn có nhận thêm giờ được không.
- **Repo và CI (mục 18):** GitLab tự host không truy cập được; họp chọn nơi chứa repo chung và CI. Bạn phụ trách CI, deploy nên chuẩn bị ý kiến (mục 4 bước 1).

---

## 4. Việc trước họp A23 (hạn tối 24/10) và kiểm `Baseline frozen` (sau họp)

1. **Ý kiến cho mục 18 họp A23 (chọn repo và CI).** Ghi lên chat trước tối 24/10: mỗi phương án cần gì, ai tạo, mất bao lâu. Các hướng thường gặp **[Đề xuất AI, nhóm quyết]**:
   - repo trên GitHub, CI GitHub Actions;
   - repo trên GitLab.com, CI GitLab CI;
   - giữ Jenkins trên máy cá nhân, nhận webhook từ repo công khai: máy phải bật và truy cập được từ Internet khi có Merge Request, chỉ chủ máy xem log.
2. **Kiểm tra `Baseline frozen` (26–28/10, sau họp).** Nếu họp giữ Jenkins thì kiểm stage dưới chạy với Merge Request trên Jenkins thật; nếu đổi nền tảng thì viết kiểm tra tương đương trên CI mới với cùng quy tắc.
   - Stage chặn Merge Request sửa, xóa hoặc đổi tên file `docs/baseline/v*.pdf` đã có, nhưng cho thêm file mới.
   - Logic `git diff` đã thử trên repo giả lập, chưa chạy trên Jenkins.
   - Cần plugin nhận Merge Request (biến `CHANGE_TARGET` hoặc `gitlabTargetBranch`) và quyền `git fetch` nhánh đích.
   - Đoạn stage (nếu giữ Jenkins, chép vào `Jenkinsfile` ngay sau stage `Checkout`):

   ```groovy
   // Chỉ chạy với Merge Request: chặn sửa/xóa baseline đã duyệt (docs/baseline/v*.pdf), cho phép thêm bản mới.
   stage('Baseline frozen') {
     when { expression { env.CHANGE_TARGET || env.gitlabTargetBranch } }
     steps {
       sh '''
         set -e
         TARGET="${CHANGE_TARGET:-$gitlabTargetBranch}"
         git fetch --no-tags origin "+refs/heads/$TARGET:refs/remotes/origin/$TARGET"
         CHANGED=$(git diff --name-only --diff-filter=MDR "origin/$TARGET"...HEAD -- 'docs/baseline/v*.pdf')
         if [ -n "$CHANGED" ]; then
           echo "MR sửa hoặc xóa baseline đã duyệt:"; echo "$CHANGED"
           echo "Baseline đã duyệt là bất biến. Thêm file mới (vd v2.0.pdf) kèm Change Request trong docs/change/."
           exit 1
         fi
         echo "Không sửa baseline đã duyệt."
       '''
     }
   }
   ```

   Cách thử: tạo nhánh thêm một file PDF giả `docs/baseline/v0.9-test.pdf`, mở Merge Request; kết quả mong đợi là pass. Merge vào nhánh thử, rồi mở Merge Request khác sửa file đó; kết quả mong đợi là fail. Xong thì xóa nhánh thử. Báo kết quả cho TV1.
3. **Duyệt các bước ở mục 1, 2, 5, 6** của file này (cấu trúc repo, CI, hosting, thư viện QR, phiên đăng nhập, thông báo). Ghi ý kiến lên chat nhóm trước tối 24/10.

---

## 5. A26 · Authentication & roles (găng), phần phiên đăng nhập, seed, deploy

*Đầu vào có sẵn: `4-tai-nguyen/A26-A27/` (xem `DAU-VAO.md`).*

**Mục tiêu chung:** Người dùng đăng nhập bằng tài khoản mẫu có email trường và chỉ làm, chỉ xem được phần vai trò và đơn vị của mình cho phép.

**Phân công:**
- TV3: migration users, roles, units; API đăng nhập; middleware phân quyền.
- Bạn: phần dưới.
- TV4: màn hình.

Lịch chia 3,5h/người (đề xuất của TV3 ngày 14/10: phần bạn 5h). Ba người thống nhất khi nhận task.

**Các bước:**
1. Chọn cơ chế phiên đăng nhập **[Cần TV3/TV5 quyết]**:
   - (a) session lưu ở server, cookie HttpOnly: dễ đăng xuất, cần nơi lưu session;
   - (b) token ký (ví dụ JWT) trong cookie HttpOnly: không cần lưu phiên, khó thu hồi trước hạn.

   Báo TV4 để lớp gọi API làm đúng.
2. Cấu hình thư viện xác thực, băm mật khẩu, thời hạn phiên, cookie Secure trên HTTPS.
3. Cùng TV3 viết seed:
   - tài khoản demo Student, Organizer, Admin;
   - tài khoản test quyền: Student thứ 2, Organizer thuộc đơn vị khác.

   Mật khẩu seed đọc từ biến môi trường của bản deploy, không ghi vào repo.
4. Deploy A26. Tự chạy trên bản deploy trước khi chuyển Done: đăng nhập 3 vai trò; sai mật khẩu bị từ chối; gọi API vai trò khác bị 401/403 (T-AUTH-01…03).

**Hoàn thành khi:** các kiểm tra ở bước 4 đạt; không có mật khẩu dạng rõ trong database hay repo.

**Phụ thuộc:** chờ A24 (28/10). Chặn A27.

---

## 6. A27 · Event management (găng), phần thông báo dùng chung

*Đầu vào có sẵn: `4-tai-nguyen/A26-A27/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Có cơ chế thông báo trong ứng dụng dùng chung cho A27 (duyệt, từ chối, đổi hoặc hủy sự kiện) và A62 (được chuyển từ waitlist, 08–10/11).

**Phân công:**
- TV3: sự kiện và luồng duyệt.
- Bạn: thông báo.
- TV4: màn hình (có chuông thông báo).

Lịch chia khoảng 8,4h/người.

**Các bước:**
1. Migration `notifications` **[Đề xuất AI]**:
   - cột: id, user_id, type, event_id, message, is_read, created_at;
   - type nhận các giá trị: event_changed, event_cancelled, promoted_from_waitlist, event_approved, event_rejected.
2. Hàm tạo thông báo dùng chung trong backend, nhận danh sách người nhận và nội dung. Lỗi thì ghi log và trả về bình thường, **không** rollback giao dịch chính.
3. Endpoint **[Đề xuất AI]**:
   - `GET /api/me/notifications`: mới nhất trước, kèm số chưa đọc;
   - `POST /api/me/notifications/{id}/read`;
   - `POST /api/me/notifications/read-all`.

   Người dùng chỉ đọc được thông báo của mình.
4. Bàn với TV3 chỗ gọi hàm:
   - Admin duyệt hoặc từ chối: báo Organizer;
   - đổi thời gian hoặc địa điểm: báo người đã đăng ký;
   - hủy sự kiện: báo người đã đăng ký và người trong waitlist;
   - để sẵn cho A62 gọi khi chuyển từ waitlist.
5. Unit test:
   - tạo thông báo đúng người nhận;
   - lỗi khi tạo không làm hỏng thao tác chính;
   - không đọc được thông báo của người khác.
6. Merge Request nhờ TV3 review.

**Hoàn thành khi:** chuông thông báo của TV4 hiện đúng thông báo trên bản deploy; test lỗi thông báo không ảnh hưởng thao tác chính.

**Phụ thuộc:** chờ A26, A28 và họp A23. Chặn A29.
