---
Nội dung: Tin nhắn báo nhóm các quyết định của TV1 ngày 16/11
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 16/11/2026
Trạng thái: Nháp AI (Claude Code, 16/11) để TV1 sửa rồi tự gửi lên chat nhóm. Chỉ nêu việc đã quyết hoặc đã có bằng chứng; chỗ [ngoặc vuông] TV1 điền.
---

# Tin nhắn gửi nhóm (bản chat)

**[Cập nhật tiến độ và lịch 16/11]**

Mình đã rà Sheet, Jira, GitHub sau Progress Check. Tóm tắt để cả nhóm nắm:

**1. Tình hình**
- Progress Check 09/11: nhóm mình không được thầy gọi, không có nhận xét.
- Thầy thông báo 2 tuần cuối các nhóm demo và viva. Chưa biết ngày của nhóm mình, nên mình chừa 1 tuần: **mốc sẵn sàng là Chủ nhật 29/11**.
- Backend trên `main` đã có luồng chính (đăng nhập Google, tạo và duyệt sự kiện, đăng ký, waitlist, hủy và tự chuyển, check-in QR/mã/thủ công, thống kê, CSV, thông báo in-app). Email chưa nằm trên `main`.
- Frontend `main` mới có scaffold; các màn hình nằm ở PR #6 (đang mở). Chưa có kết quả test nào trong repo, chưa có CI.

**2. Mình đã quyết (TV1, 16/11)**
- Giữ toàn bộ Must. Không làm trang quản lý đơn vị/người dùng; thiết lập bằng seed hoặc admin CLI.
- Demo bằng Docker chạy local + video dự phòng. Hosting chỉ làm nếu dư giờ.
- Merge PR #28 (demo auth) trước 19/11; hoãn PR #31 (import, admin CLI, email), xét lại sau regression.
- Duyệt phương án A cho CR-02 (phạm vi xem dữ liệu) và CR-03 (đăng nhập Google). Đây là quyết định của nhóm, không phải thầy đồng ý.
- Lập Baseline V2.0 (giữ V1.0). Mình chốt nội dung rồi gửi lại cho cả nhóm.
- Giữ nguyên quyền Sheet master như hiện tại (ai có link đều sửa được); mình chấp nhận rủi ro này. Ai thấy không ổn thì nói.
- Owner rủi ro mới: R23 giao diện lên main: TV4; R24 backend phụ thuộc một người: TV2.

**3. Lịch (bản đề xuất, chi tiết trong `docs/task3/w13/`)**
- **17/11:** mỗi người báo hiện trạng thật (code ở máy riêng, việc đang làm).
- **19/11:** merge PR #6 và PR #28 sau review chéo; **hạn điền giờ thực tế 22/10–15/11** vào tab 3 (giờ hồi tưởng ghi rõ "hồi tưởng", tự điền, không ai điền thay).
- **20/11:** CP3: luồng chính chạy end-to-end, có kết quả test.
- **23–26/11:** tích hợp, regression, sửa lỗi, quay video dự phòng.
- **26–27/11:** UAT nội bộ. **28/11:** tổng duyệt demo và viva. **29/11:** nộp.
- 30/11–06/12: chỉ sửa lỗi, chờ slot demo.

**4. Việc của từng người**
- **TV2:** chạy test API đã merge từ hôm nay, lưu kết quả vào `docs/quality/results/`; hoàn thiện quality plan và test case.
- **TV3:** hướng dẫn môi trường và tài khoản mẫu cho TV2 ngay đầu tuần; review chéo PR #28 và #6; kiểm chứng kịch bản demo end-to-end.
- **TV4:** xác nhận phần nào của giao diện đã xong; cùng TV5 đưa PR #6 vào `main` trước 19/11; thử trên điện thoại.
- **TV5:** rebase PR #28 lên `main` (đang xung đột); Docker chạy local từ `main`; CI tối thiểu nếu TV3 đồng ý; kiểm chứng QR trên điện thoại.
- **Cả nhóm:** log work trên Jira từ hôm nay; review chéo trong 24h; mỗi người tự viết phần cá nhân cuối báo cáo.

**5. Cần mọi người phản hồi trong 24h (đến [giờ] 17/11):**
- Có chỗ nào trong lịch hoặc phạm vi không khả thi với phần của bạn không? Nếu có, nói rõ chỗ nào và cần gì.
- Ai không phản hồi sau 24h thì mình coi là đồng ý (theo quy ước review chéo của nhóm).
- Mỗi người xác nhận tài khoản GitHub của mình và việc mình đã làm mà chưa có trên repo.

Chi tiết từng người: `docs/task3/w13/giao-viec/` (file riêng cho từng thành viên, [đã gửi hay sẽ gửi: TV1 điền]). Bước kỹ thuật là đề xuất, TV3 và TV5 xem và chỉnh trước.
