# Task 2 — Product-based Planning & Baseline

Task 2 là nội dung **Milestone 2 – Planning Baseline** theo bảng milestone của đề (products/activities, estimates, risks, resources, schedule, quality plan). Làm trong 06–12/10, nhóm tự chốt Baseline V1.0 trong tuần nghỉ. Ngày Milestone 2 chưa có — hỏi trong email vòng 2.
Baseline V1.0 do **nhóm tự chốt** trong tuần nghỉ, sớm nhất 15/10 (CP2, theo P05), sau đó đóng băng. Trước khi chốt, gửi email hỏi client các điểm ảnh hưởng scope (A58).

| File | Task | Activity | Chủ sở hữu |
|---|---|---|---|
| `2.1-pbs.md` | 2.1, 2.3 | A15 | TV3, TV5 |
| `2.2-product-descriptions.md` | 2.2 | A16 | TV2, TV4 |
| `2.4-activity-network.md` | 2.4, 2.7 | A17 | TV5, TV1 |
| `2.5-checkpoints.md` | 2.5 | A17 | TV5, TV1 |
| `2.6-estimates.md` | 2.6 | A18 | cả nhóm |
| `2.8-risk-register.md` | 2.8, 2.9 | A19 | TV5, TV4 |
| `2.10-resource-plan.md` | 2.10 | A50 | TV1 |
| `2.11-schedule.md` | 2.11 | A21 | TV1 (từ 18/10; trước đó TV3) |
| `2.12-quality-plan.md` | 2.12 | A22 | TV1 duyệt; TV2 thực hiện |

Lịch, Gantt và critical path tính bằng script `../../tools/schedule/` từ tab 10, 11 Sheet master (trang `../plan/index.html` cũ không còn trong repo); hình mạng activity, Gantt và sơ đồ kiến trúc cho báo cáo vẽ bằng `../../tools/diagrams/`. `2.11-schedule.md` ghi kết quả, cách tính và quyết định lập lịch.

## Nguyên tắc

- Mỗi product trong PBS phải có ít nhất một activity tạo ra nó.
- Mỗi activity phải tạo ra ít nhất một product.
- **Effort (person-hours) và elapsed time (ngày) ghi riêng** — đề chấm điểm này.
- Rủi ro exposure ≥ 12 phải có activity phản hồi trong kế hoạch (A20 spike, A38 reserve).
