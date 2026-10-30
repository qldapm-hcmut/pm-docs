# CO3011 – University Event Registration System · Hồ sơ quản lý dự án

Dự án môn Software Project Management (CO3011), học kỳ 2026–2027, lớp L01, nhóm 9 (5 thành viên).
Hệ thống hỗ trợ tổ chức sự kiện, đăng ký tham dự, quản lý người tham gia và theo dõi điểm danh cho trường đại học.

> Môn học chấm chủ yếu phần **quản lý dự án** (code chiếm 20%). Repo này là nơi lưu bằng chứng quản lý. **Mã nguồn sản phẩm nằm ở repo riêng** [`qldapm-hcmut/ticket-system-uni`](https://github.com/qldapm-hcmut/ticket-system-uni) (cách cài đặt và chạy xem README của repo đó).

## Mốc chính

Ngày dự kiến theo lịch Baseline V1.0 (họp A23 ngày 25/10/2026).

| Mốc | Ngày |
|---|---|
| Trình bày Milestone 1 (trên lớp) | 05/10/2026 |
| Nhóm chốt Baseline V1.0 (họp A23) | 25/10/2026 |
| Progress Check (CP4) | 09/11/2026 |
| Increment 1 chạy end-to-end (CP3) | 11–16/11/2026 |
| UAT (CP5) | 01–05/12/2026 |
| Demo & viva | 07/12/2026 |

## Cấu trúc repo

```
docs/     Toàn bộ tài liệu quản lý dự án (xem docs/README.md)
tools/    Script tính lịch (CPM) và vẽ sơ đồ cho báo cáo
report/   Mã nguồn LaTeX của báo cáo (biên dịch bằng latexmk -pdf main.tex)
```

Trang kế hoạch dự án: mở thẳng `docs/plan/index.html` bằng trình duyệt (file HTML tự chứa).

## Quy ước làm việc

- **Activity ID** (`A01`–`A62`) là khóa nối giữa kế hoạch, Jira và Git. Branch, commit và pull request liên quan activity nào thì mang ID đó.
- Branch: `docs/<mô-tả>`, `feature/<mô-tả>`; mỗi branch một mục đích.
- Pull request: nêu rõ mục đích và activity ID liên quan; ít nhất một người review trong 24 giờ.
- Mọi thay đổi vào `main` đi qua pull request. Branch protection do chủ repo bật.
- Baseline đã duyệt thì **không sửa**. Thay đổi đi qua Change Request (`docs/change/`) và tạo baseline mới.
- Repo ở chế độ public (TV1 chuyển ngày 30/10/2026, sau khi quét secret; TV1 xác nhận việc lộ họ tên và MSSV không phải vấn đề). Không đưa secret, `Link.txt`, file `.xlsx` vào repo; quét lại trước khi thêm file có link nội bộ hoặc dữ liệu cá nhân mới.

## Phân công

| Mã | Vai trò | Sở hữu |
|---|---|---|
| TV1 | PM — Nguyễn Đức Nghĩa | Toàn bộ sản phẩm quản trị và báo cáo: authority, Client Log, scope/MoE, PBS/PFD, PD, estimate, lịch/Gantt, resource plan, risk register, quality plan, baseline, weekly log, traceability, change request, AI log, báo cáo |
| TV2 | Tester — Ngô Thanh Hùng | Test case, chạy kiểm thử, regression, UAT |
| TV3 | Tech Lead, Backend — Phan Huy Quang Minh | Backend (Go), database (PostgreSQL), API, quyết định kỹ thuật |
| TV4 | Frontend — Nguyễn Đắc Nghĩa | Frontend (React) |
| TV5 | Backend, DevOps — Hà Cao Đức Minh | Backend (Go), codebase, CI/CD, deploy, check-in QR |

Phân vai chốt ngày 18/10/2026; việc làm trước ngày đó ghi đúng người đã làm.

## Nhịp làm việc

- Báo tiến độ bất đồng bộ qua chat: check-in 3 dòng (đã xong gì kèm activity ID, đang làm gì, vướng gì) vào thứ 4 hoặc 5.
- Họp định kỳ **15h Chủ nhật hằng tuần**: rà time tracking, chốt weekly log, review chéo tài liệu, chuẩn bị viva.
- Họp bất thường khi gặp 1 trong 6 điều kiện: quyết định cần từ 3 người mà chat chưa xong; trước checkpoint hoặc nộp milestone; có change event; deviation vượt 20% ở activity găng; rủi ro exposure ≥ 12 xảy ra; từ 2 người báo blocker cùng đợt.

## Công cụ

| Công cụ | Dùng để | Không dùng để |
|---|---|---|
| GitHub (org `qldapm-hcmut`) | Mã nguồn (`ticket-system-uni`), tài liệu quản lý (repo này), lịch sử thay đổi, review bằng pull request | Theo dõi trạng thái công việc |
| CI/CD của repo code | Build, test, bằng chứng chất lượng | Lưu trữ lâu dài (log CI có thể bị xoay vòng — export vào `docs/quality/` trước mỗi checkpoint) |
| Jira | Trạng thái công việc, worklog (actual effort) | Lưu estimate kế hoạch, risk register |
| Sheet master | Estimate, risk register, traceability, client log, time tracking | Trạng thái công việc |

Một số liệu chỉ có **một** nguồn. Đề phạt nặng việc các bảng mâu thuẫn nhau.

## Khai báo AI

Nhóm có dùng công cụ AI hỗ trợ. Nhật ký tại `docs/ai-usage.md`, và sẽ được khai báo trong báo cáo cuối theo yêu cầu của đề.
