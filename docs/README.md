# docs/ — Tài liệu quản lý dự án

Nơi lưu mọi thứ đề CO3011 yêu cầu nộp hoặc giữ lại. Mỗi thư mục có README riêng nói rõ chứa gì, ai sở hữu, hạn khi nào.

## Bản đồ nhanh

| Thư mục | Chứa | Đề yêu cầu ở | Chủ sở hữu |
|---|---|---|---|
| `plan/` | Trang kế hoạch dự án (HTML tự chứa, mở trực tiếp bằng trình duyệt) | Submission (lịch, Gantt) | TV1 |
| `client/` | Client Interaction Log + bằng chứng (email, ảnh chụp) | Task 1.1, Submission | TV2 |
| `task1/` | Bối cảnh, business case, scope, objectives & MoE, authority, stakeholders, standards, lifecycle | Task 1 Expected outputs | TV2, TV4, TV5 |
| `task2/` | PBS, Product Descriptions, PFD, activity network, checkpoints, estimates, cost, risk register, resource plan, Gantt, quality plan | Task 2 Expected outputs | TV3, TV5, TV2 |
| `task3/` | Dữ liệu planned vs actual, risk/issue cập nhật, lower-level plans | Task 3 Expected outputs | TV1 |
| `task4/` | So sánh baseline, đánh giá hiệu quả, closure plan, lessons learned | Task 4 Expected outputs | TV1, TV5 |
| `baseline/` | Baseline V1.0 và V2.0, giữ nguyên để so sánh | Submission, Task 3.7 | TV1 |
| `logs/` | Weekly project log | Task 3.2, Submission | TV1 |
| `checkpoints/` | Biên bản CP1–CP5 | Task 2.5 | TV1 |
| `change/` | Change Request và phân tích tác động | Task 3.6, 3.7 | TV1 |
| `quality/` | Test case, kết quả test, export từ CI của repo code | Task 3.5 | TV2 |
| `reflection/` | Contribution và reflection từng cá nhân | Task 4.6 | từng người |
| `traceability.md` | Bảng nối Objective → Product → Activity → Resource → Risk → Test → Checkpoint | Mandatory Traceability | TV1 |
| `ai-usage.md` | Nhật ký dùng công cụ AI | Use of Generative AI | TV1 |
| `report/` | Báo cáo cuối (PDF) và các bản nộp milestone | Submission | TV1 |

## Quy ước

**Mã ID dùng chung toàn dự án.** Mọi tài liệu, Jira issue và commit đều tham chiếu các mã này:

| Tiền tố | Nghĩa | Ví dụ |
|---|---|---|
| `O#` | Objective | O1 |
| `P#` | Product | P3 |
| `A##` | Activity | A27 |
| `R##` | Risk | R04 |
| `T-XX-##` | Test case | T-CI-01 |
| `CP#` | Checkpoint | CP2 |
| `Q##` / `P##` | Câu hỏi client (yêu cầu / quy trình) | Q03 |

**Đặt tên file:** chữ thường, nối bằng gạch ngang, có ngày khi tài liệu lặp lại.
`week-03.md`, `cp2-baseline-approval.md`, `cr-01-change-event.md`

**Mỗi tài liệu mở đầu bằng khối metadata:**

```markdown
---
Activity: A19
Chủ sở hữu: TV5
Phiên bản: 1.0
Cập nhật: 2026-10-08
Trạng thái: nháp | đã review | đã duyệt
---
```

## Nguyên tắc một nguồn sự thật

Số liệu chỉ tồn tại ở **một** nơi. Nơi khác tham chiếu chứ không chép lại.

| Số liệu | Nguồn duy nhất |
|---|---|
| Estimate kế hoạch (effort, duration) | Sheet master, tab Estimates |
| Actual effort | Jira worklog → tổng hợp vào Sheet master, tab Time Tracking |
| Risk (P, I, exposure, owner) | Sheet master, tab Risk Register |
| Trạng thái công việc | Jira |
| Lịch và dependencies | `plan/index.html` (mảng `ACT`) |
| Câu trả lời của client | Sheet master, tab Client Log |

Trước mỗi checkpoint, TV1 chạy activity A57: rà toàn bộ các bảng xem có mâu thuẫn không.

## Trước mỗi lần nộp

1. Export Sheet master và Jira ra PDF/CSV, đặt vào thư mục tương ứng — bài nộp phải tự đọc được, giảng viên không truy cập Jira hay Sheet master của nhóm.
2. Chạy A57 rà traceability.
3. Kiểm tra mọi sơ đồ và bảng đọc được khi in.
4. Cập nhật `ai-usage.md`.
5. Gắn tag Git: `m1-submission`, `baseline-v1.0`, `final`.
