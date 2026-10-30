# Baseline

**Baseline đã duyệt là bất biến.** Repo này không có CI tự động chặn sửa file; bất biến được giữ bằng review pull request: PR sửa, xóa hoặc đổi tên file `v*.pdf` đã có trong thư mục này bị từ chối, chỉ thêm file mới (`v2.0.pdf`) và sửa README, checklist. Nhóm không dựng CI riêng cho repo tài liệu (TV1 chốt 30/10), nên stage `Baseline frozen` của quyết định 21/10 không còn áp dụng.

| File | Ngày duyệt | Người duyệt | Git tag |
|---|---|---|---|
| `v1.0.pdf` | 25/10/2026 (họp A23; CP2 18/10 đạt có điều kiện; `v1.0.pdf` chưa xuất, chờ repo chung) | Cả nhóm, TV1 ký | `baseline-v1.0` |
| `v2.0.pdf` | sau change event | | `baseline-v2.0` |

## Quy trình tạo baseline

1. Rà traceability (A57).
2. Xuất PDF báo cáo (chương 1–2 là nội dung baseline; trang plan cũ không còn trong repo). Checklist họp và các bước chi tiết: `A23-checklist.md`.
3. Đã rà các điểm ảnh hưởng scope (A58); chỉ gửi email hỏi client nếu còn điểm ảnh hưởng đáng kể chưa rõ (P05), việc gửi do TV1 quyết. Cả nhóm xác nhận, TV1 ký; ghi biên bản ở `../checkpoints/`. Client không duyệt toàn bộ baseline (P05).
4. Commit PDF vào thư mục này **bằng một pull request riêng**, được TV1 duyệt.
5. Gắn tag: `git tag -a baseline-v1.0 -m "Baseline V1.0 approved <ngày>" && git push origin baseline-v1.0`

Baseline V2.0 chỉ được tạo sau khi có Change Request đã duyệt trong `../change/`. Thêm file mới, không sửa V1.0.

> Đưa `v1.0.pdf` vào lần đầu là thêm file mới. Mọi thay đổi về sau phải là file mới. Nếu sau này muốn kiểm tự động thì thêm workflow so sánh `docs/baseline/v*.pdf` giữa nhánh PR và `main`; chưa làm.
