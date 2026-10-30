# Cấu hình GitHub, CI, Jira

Hạ tầng đã dựng. File này ghi **cấu hình nội dung** để các công cụ phục vụ đúng yêu cầu của môn học, và là bằng chứng cho Task 1.7.

> Điền URL thật và đánh dấu từng mục khi xong. Ghi ngày và người làm.
> Cập nhật 30/10/2026: nhóm đã chuyển từ GitLab tự host sang GitHub; phần GitLab và Jenkins của bản cũ đã được thay bằng mục 1 và 2.

---

## 1. GitHub

**Tổ chức:** `qldapm-hcmut` · **Người phụ trách:** TV1 (quản trị tổ chức), TV3 (repo code)

| Repo | Nội dung | Chế độ |
|---|---|---|
| `ticket-system-uni` | Mã nguồn sản phẩm (Go, PostgreSQL) | public |
| `pm-docs` | Hồ sơ quản lý dự án (`docs/`, `tools/`, `report/`) | private |

### Repository
- [ ] Mời đủ 5 thành viên vào tổ chức; quyền **Write** cho cả hai repo; TV1 và chủ repo code quyền **Admin**
- [ ] Settings → Branches (hoặc Rules → Rulesets): bảo vệ `main` ở cả hai repo — yêu cầu pull request, ít nhất 1 approval, cấm force-push
- [ ] Settings → General → Pull Requests: bật *Automatically delete head branches*
- [ ] Mỗi PR một mục đích; tiêu đề PR nêu activity ID khi liên quan

### Labels (Issues → Labels)
`TV1` … `TV5` · `task1` … `task4` · `docs` · `code` · `test` · `risk` · `change-request`

### Truy cập của giảng viên — quan trọng
Repo `pm-docs` là private. Khi nộp bài chọn một:
- [ ] Mời tài khoản GitHub của giảng viên làm collaborator quyền Read, **hoặc**
- [ ] Chuyển `pm-docs` sang public sau khi quét dữ liệu cá nhân (họ tên, MSSV, email) và secret (rủi ro **R20**)

### Backup
- [ ] Mỗi thành viên giữ một bản clone; export bản zip của `pm-docs` trước mỗi lần nộp

---

## 2. CI/CD

CI/CD của repo code (`ticket-system-uni`) do người dựng repo đó thiết lập và quản lý. Nhóm không dựng CI riêng (Jenkins hay GitHub Actions) cho `pm-docs` (TV1 chốt 30/10).

- [ ] Ghi vào đây tên workflow, nơi xem kết quả và cách tải log khi biết cấu hình (TV3 hoặc TV5 điền)

Hệ quả cho tài liệu: không còn kiểm tự động `Baseline frozen` và cấu trúc `docs/`; bất biến của baseline giữ bằng review pull request (xem `docs/baseline/README.md`).

### Bằng chứng cho Task 3.5
Log CI có thể bị xoay vòng. **Trước mỗi checkpoint**: tải kết quả chạy test từ CI của repo code → commit vào `docs/quality/results/` kèm mã lần chạy và commit hash.

---

## 3. Jira

**URL:** 
**Người phụ trách:** TV1 (cấu hình), cả nhóm (sử dụng)

### Project
- [ ] Tạo project kiểu *Kanban* (không dùng Scrum — dự án theo incremental delivery với baseline cố định, không chạy sprint)
- [ ] Key gợi ý: `EVR`

### Workflow
`To Do` → `In Progress` → `In Review` → `Done`
- `Done` chỉ khi đạt Definition of Done (`docs/task1/1.7-standards-communication.md`)

### Trường
- [ ] Bật *Time tracking* (Original estimate, Time spent) — Settings → Issues → Time tracking
- [ ] Bật *Start date*, *Due date*
- [ ] Đơn vị thời gian: giờ; 1 ngày làm việc = 8h (chỉ để Jira tính, không phải năng lực thật)

### Nhập dữ liệu (quyền thành viên, không cần admin)
`docs/jira-import.csv` đã soạn cho chế độ import của thành viên: 57 task, Original Estimate tính bằng **giây**, mỗi nhãn một cột `Labels`, không có epic.

- [ ] **Filters → Search work items → ••• → Import work items from CSV**
- [ ] Encoding UTF-8, delimiter dấu phẩy; Date format `yyyy-MM-dd`
- [ ] Map: Summary → Summary · Issue Type → Work type · Labels → Labels · Original Estimate → Original estimate · Start date → Start date · Due date → Due date · Description → Description
- [ ] **Validate** trước, kiểm tra A01 hiện 6h và nhãn tách riêng (`A01`, `P0`, `TV3`, `TV5`), rồi **Begin import**
- [ ] Tạo tay 8 epic theo giai đoạn
- [ ] Gắn task vào epic: JQL `labels = P1` → ••• → Bulk change → Edit fields → Parent (lặp cho P0–P7)
- [ ] Gán Assignee: JQL `labels = TV5` → Bulk change → Assignee; làm theo thứ tự TV5 → TV1 để người chịu trách nhiệm chính được gán sau cùng

| Label | Epic |
|---|---|
| P0 | Khởi động |
| P1 | Task 1 – Initiation & Definition |
| P2 | Task 2 – Baseline draft & Milestone 1 |
| P3 | Nghỉ giữa kỳ & Baseline V1.0 |
| P4 | Task 3 – Increment 1 |
| P5 | Task 3 – Increment 2 & Progress Check |
| P6 | Task 3 – Change & Test |
| P7 | Task 4 – Delivery & Closure |

### Quy ước dùng
- Mỗi người **log work** trên issue khi làm — đây là nguồn actual effort duy nhất
- Branch và commit chứa activity ID; nếu dùng tích hợp GitHub–Jira thì ghi thêm issue key (`SCRUM-27`) để tự liên kết
- **Không sửa Original Estimate** sau khi Baseline V1.0 duyệt. Thay đổi đi qua Change Request.

### Tích hợp GitHub
- [ ] Cài app *GitHub for Jira* từ Jira, kết nối tổ chức `qldapm-hcmut`
- [ ] Commit có issue key sẽ tự hiện trên Jira — tăng bằng chứng traceability

### Export trước mỗi lần nộp
Giảng viên không truy cập Jira. Trước Milestone 1, Progress Check và báo cáo cuối:
- [ ] Export toàn bộ issue kèm worklog ra CSV → `docs/task3/`
- [ ] Chụp màn hình board → đưa vào báo cáo

---

## Phân vai dữ liệu giữa các công cụ

Một số liệu chỉ có một nguồn. Đề phạt nặng việc các bảng mâu thuẫn nhau.

| Dữ liệu | Nguồn duy nhất | Nơi khác |
|---|---|---|
| Danh sách activity, phụ thuộc, lịch | `docs/plan/index.html` | Jira import từ đây |
| Estimate kế hoạch | Baseline (Sheet master → plan) | Jira Original Estimate, chỉ đọc |
| Actual effort | **Jira worklog** | tổng hợp vào `docs/task3/planned-vs-actual.md` |
| Trạng thái công việc | Jira | — |
| Risk | Sheet master / `docs/task2/2.8-risk-register.md` | — |
| Client log | Sheet master / `docs/client/` | — |
| Kết quả test | CI của repo code → `docs/quality/results/` | — |
