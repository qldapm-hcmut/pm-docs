---
Nội dung: Giao việc W13–W14 (16–29/11) cho TV2
Người nhận: Ngô Thanh Hùng (TV2, Tester)
Phiên bản: 0.1
Giờ: do TV2 ước lượng lại trước 20/11 (tham chiếu baseline V1.0: A22 6,3h; A31 10,5h; A40 8,4h; A30 10,5h chia chung; A39 10,5h chia chung; A41 6,3h chia chung)
Trạng thái: Nháp AI (Claude Code, 16/11); TV1 chốt phạm vi 16/11; bước kỹ thuật là đề xuất AI, chờ TV3, TV5 duyệt
---

# TV2: W13–W14

Hiện chưa có kết quả test nào trong repo (R26, owner TV2). Việc quan trọng nhất là có **bằng chứng kiểm thử thật** ngay cả khi frontend chưa lên `main`: kiểm thử trên API đã merge.

## Task 1: Test case theo mã (A31, A40, hạn 18/11)

**Mục tiêu:** có bộ test case Increment 1 và 2 trong `docs/quality/test-cases.md`, mỗi ca có mã T-… khớp bảng truy vết.

**Đầu vào:** mô tả sản phẩm PD-01..05; `api/openapi.yaml` của repo backend (`ticket-system-uni-be`); Sheet tab 6 Traceability.

**Các bước:** viết theo nhóm mã sau, mỗi ca gồm tiền điều kiện, bước, kết quả mong đợi, vai trò:
- T-AUTH-01..03 đăng nhập và phân quyền (`POST /auth/google`, `/auth/refresh`, `/me`); T-AUTH-04 không công bố khi chưa duyệt, Organizer không tự duyệt sự kiện của mình; T-AUTH-05..06 quyền xem dữ liệu theo vai trò.
- T-EV-01..05 tạo, sửa sự kiện (`/manage/events`, `/events/{id}/submit`, `/approvals/pending`, `/events/{id}/approve`, `/events/{id}/reject`); T-EV-06..07 sửa, hủy sự kiện đã công bố.
- T-REG-01..05 đăng ký và hủy (`/events/{id}/registrations`, `/registrations/{id}/cancel`): không trùng, không vượt chỗ, hủy đến 24 giờ trước giờ bắt đầu.
- T-WL-01..04 waitlist FIFO, tự chuyển, thông báo lỗi vẫn đăng ký, đăng ký lại.
- T-CI-01..05 check-in QR, trùng, mã nhập tay, xác nhận thủ công (`/registrations/{id}/check-in`, `/events/{id}/check-ins`); chỉ Organizer được điểm danh (CR-01): thêm ca Admin bị từ chối.
- T-RP-01..03 thống kê và xuất CSV (`/events/{id}/reports/summary`, `/events/{id}/exports/{kind}`), có ca 500 lượt đăng ký trong 30 giây.
- T-UI-01 giao diện check-in trên điện thoại; T-INT-01..03 luồng end-to-end; T-DEP-01 chạy bản Docker.

**Đầu ra:** `docs/quality/test-cases.md` đã cập nhật.

**Hoàn thành khi:** mọi mã trên có ít nhất một ca; TV3 xem lướt phần API.

**Người làm, phụ thuộc:** TV2; TV3 giải đáp API.

## Task 2: Chạy test API đã merge (A31, từ 17/11, kết quả đầu tiên 20/11)

**Mục tiêu:** có kết quả chạy thật cho các ca không cần giao diện.

**Đầu vào:** hướng dẫn môi trường của TV3 (17/11): `.env` (`DATABASE_URL`, `JWT_SECRET`, `QR_HMAC_SECRET`), `make db-up`, `make migrate-up`, `make seed ADMIN_EMAIL=<email>`, `make run`; tài khoản mẫu ba vai trò sau khi PR #28 merge.

**Các bước:**
1. Chạy môi trường theo hướng dẫn; nếu vướng, báo TV3 trong ngày.
2. Gọi API bằng Postman, Swagger hoặc curl theo từng ca; ghi request, response, đạt hay không.
3. Với ca đồng thời (đăng ký đồng thời, FIFO), ghi cách thực hiện và số lượt.
4. Lỗi tìm được: ghi vào `docs/quality/defects.md` (mã lỗi, ca gây ra, mức nghiêm trọng, người nhận).

**Đầu ra:** `docs/quality/results/cp3-2026-11-20.md` (bảng mã T-… · đạt/không đạt/chưa chạy · bằng chứng: ảnh, log, link) và danh sách lỗi.

**Hoàn thành khi:** có kết quả cho ít nhất T-REG, T-WL, T-CI-04..05, T-AUTH-01..04; ca chưa chạy ghi "chưa chạy" kèm lý do. Không ghi "đạt" khi chưa chạy.

**Người làm, phụ thuộc:** TV2; TV3 môi trường (17/11); merge PR #28 (19/11) cho tài khoản mẫu.

## Task 3: CP3, regression, UAT (A30, A39, A41)

- **A30 (CP3) 20/11:** chủ trì buổi chạy kịch bản end-to-end: tạo sự kiện → duyệt → đăng ký → đầy chỗ → waitlist → hủy → tự chuyển → check-in → báo cáo. Ghi deviation so với kế hoạch.
- **A39 regression 23–24/11:** chạy lại bộ test sau khi các PR cuối merge; cập nhật results.
- **A41 UAT 26–27/11 (cùng TV1):** chạy kịch bản người dùng theo tiêu chí trong PD; biên bản UAT: ca, kết quả, lỗi còn lại. Có mời thầy hay không: TV1 quyết.

**Hoàn thành khi:** có file kết quả cho từng mốc (`cp3-…`, `regression-…`, `uat-…`) trong `docs/quality/results/`.

## Task 4: Quality plan và giờ thực tế (A22, hạn 22/11)

Hoàn thiện `docs/task2/2.12-quality-plan.md` theo thực tế (chiến lược test, môi trường, tiêu chí đạt). Điền giờ thực tế 22/10–15/11 vào tab 3 Sheet trước 19/11; log work Jira từ 16/11.

**Rủi ro của bạn:** R26 (chưa có bằng chứng kiểm thử, owner TV2), R24 (backend phụ thuộc một người: yêu cầu review chéo trước merge). Nếu không chạy được ca nào, báo TV1 sớm.
