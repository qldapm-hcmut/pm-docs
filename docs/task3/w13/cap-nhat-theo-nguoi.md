---
Nội dung: Việc từng thành viên cần cập nhật (Jira, Time Tracking, PR) trong W13
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11) để TV1 gửi nhóm sau khi duyệt `lich-rut-gon.md`. Chỉ nêu việc đã thấy trên GitHub, Jira, Sheet; không ghi ai làm việc gì khi chưa có xác nhận. Bước kỹ thuật chờ TV3, TV5 duyệt.
---

# Việc cần cập nhật theo người

**Quy tắc chung:** log work Jira ngay khi làm, ghi giờ thật (kể cả phần đã làm). Code đẩy qua PR, review bởi người khác tác giả. Blocker báo trên chat trong ngày. Hạn thu giờ thực tế 22/10–15/11: **19/11**. Xác nhận tài khoản GitHub của mình: `minhphan-hcmut`, `DucMinh2211`, `InterValiCanis` [mỗi người tự nhận tài khoản của mình].

## TV1 Nguyễn Đức Nghĩa (PM)

- Duyệt D1–D12 trong `README.md`; gửi gói này cho nhóm.
- Sheet: dán `2-weekly-log-W11-W13.tsv`, `9-ai-log-16-11.tsv`; thêm câu SỬA 16/11 vào CP4 (`cap-nhat-16-11.md`); duyệt R23, R24, đóng R11, chấm R15, R25, R26.
- Jira: A51 sang Done sau khi ghi CP4; xóa tay SCRUM-115 đến 119 (sub-task tạo nhầm); dời hạn theo mục 4 `lich-rut-gon.md`; log work A36, A51, A57.
- Giới hạn quyền Sheet và Drive (R20); xuất Jira CSV (cột Log Work) mỗi Chủ nhật vào tab Time Tracking.
- Đưa `docs/` mới và `v1.0.pdf` kèm tag `baseline-v1.0` vào `pm-docs` bằng PR riêng.
- Báo cáo: viết các phần chờ số liệu (xem `bao-cao-hoan-thien.md`).

## TV2 Ngô Thanh Hùng (Tester)

- Jira: A22 (quá hạn 22/10), A31 (28/10), A40, A30: cập nhật trạng thái thật.
- Chạy test API đã merge theo từng luồng (đăng nhập, sự kiện và duyệt, đăng ký, waitlist, hủy, check-in, báo cáo): lưu kết quả vào `docs/quality/results/`, kèm mã test T-…, đạt hay không, bằng gì (thật hay mock).
- Hoàn thiện quality plan (A22); test case Increment 1 và 2.
- Time Tracking: giờ A22, A31 (22/10–15/11).
- Chuẩn bị UAT 26–27/11 (A41).

## TV3 Phan Huy Quang Minh (Tech Lead, backend)

- Jira: A26, A27, A29, A62 (In Review), A33, A34 (Backlog): chuyển trạng thái thật; Done chỉ khi TV2 có kết quả test.
- Time Tracking: tự điền giờ các dòng "[TV3 chọn]" (skeleton, thông báo, review, hỗ trợ frontend, đăng nhập demo, họp) và PR #23–#30.
- Quyết định PR #28 (demo auth, validation lịch) và PR #31 (import sinh viên, admin CLI, email Mailpit): phạm vi so với baseline, effort, có cần CR không (D4).
- CR-02, CR-03: gửi effort, lịch, cách demo để TV1 duyệt.
- Kiểm chứng end-to-end bằng kịch bản D1 và gửi xác nhận; cập nhật README (tên repo mới `-be`, `-fe`).
- Bật branch protection (chủ repo) hoặc báo chủ repo; yêu cầu 1 review trước merge (R24).

## TV4 Nguyễn Đắc Nghĩa (Frontend)

- Hiện trạng: PR #1–#5 (02/11) merge vào nhánh xếp chồng nên chưa vào `main`; PR #6 đang mở. Xác nhận phần nào của PR #6 là của mình, phần nào còn thiếu.
- Jira: A28 (Backlog), A35, giao diện A26, A27, A29: cập nhật theo thực tế.
- Kiểm tra giao diện trên điện thoại nhỏ (R21) và luồng QR của sinh viên và Organizer.
- Time Tracking: giờ A28 và giao diện (02/11–15/11).
- Tham gia A39 cùng TV2.

## TV5 Hà Cao Đức Minh (Backend, DevOps)

- Jira: A24 (Backlog), A20 (In Review): cập nhật; đóng A20 bằng kết quả kiểm chứng QR hoặc ghi lý do bỏ spike.
- Phối hợp review chéo PR #6, #28, #31; chốt Docker local chạy được từ `main`.
- Quyết định hosting hay Docker local (D3) cùng TV1; thêm workflow CI tối thiểu (test + build) nếu TV3 đồng ý bước kỹ thuật. Giờ: [TV5 ước lượng].
- Time Tracking: giờ A24, A20 và các PR của mình.
- Chuẩn bị video demo dự phòng (24–26/11).
