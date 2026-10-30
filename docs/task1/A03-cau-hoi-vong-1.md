# Danh sách câu hỏi yêu cầu dự án (Client - Vòng 1)

---

## Mức ưu tiên 1: Tác động cực lớn đến Scope và Rủi ro (Q08, Q03, Q04)

**1. Tiêu chí nghiệm thu là gì? Nếu thiếu thời gian thì ưu tiên chức năng nào? (Q08)**
*   **Phân tích tác động:** Nếu thầy yêu cầu phải xong toàn bộ mới được nghiệm thu, rủi ro (R02, R05) sẽ cực cao. Câu trả lời giúp chốt chính xác danh sách Must-have và Should-have.
*   **Câu hỏi Follow-up:** "Nếu dự án làm không kịp tính năng thông báo/nhắc lịch thì có ảnh hưởng đến điểm qua môn không thưa thầy?"

**2. Điểm danh (check-in) nên làm thế nào (QR, mã, danh sách)? Có cần check-out không? Mạng yếu tại hội trường thì xử lý ra sao? (Q03)**
*   **Phân tích tác động:** Nếu thầy bắt buộc phải quét QR bằng thiết bị của trường hoặc yêu cầu chế độ offline, effort cho spike (A20) và code module điểm danh (A33) sẽ tăng đột biến.
*   **Câu hỏi Follow-up:** "Nếu bắt buộc dùng QR, nhóm xin phép làm thêm tính năng fallback là nhập mã số tay (khi mạng lag) có được không thầy?"

**3. Sự kiện có giới hạn số chỗ không? Khi hết chỗ có danh sách chờ (waitlist) không? Có hạn chót hủy đăng ký không? (Q04)**
*   **Phân tích tác động:** Nếu có danh sách chờ, logic database xử lý đồng thời (concurrent) khi người dùng hủy/đăng ký ở A29 sẽ rất phức tạp và tốn thêm effort code.
*   **Câu hỏi Follow-up:** "Danh sách chờ sẽ tự động đẩy người lên khi có người đăng ký hủy, hay ban tổ chức phải duyệt tay ạ?"

---

## Mức ưu tiên 2: Tác động lớn đến luồng dữ liệu và thiết kế (Q01, Q02, Q05)

**4. Ai được tạo sự kiện (khoa, CLB, Phòng CTSV)? Sự kiện có cần qua bước duyệt không? (Q01)**
*   **Phân tích tác động:** Nếu cần duyệt, nhóm phải vẽ thêm một luồng quy trình (approval flow) và thêm màn hình quản lý cho Admin, làm tăng scope của A27.
*   **Câu hỏi Follow-up:** "Admin (trường) duyệt hay các Khoa/CLB tự duyệt sự kiện của mình thưa thầy?"

**5. Người dùng đăng nhập bằng gì: tài khoản trường, email trường hay tự đăng ký? (Q02)**
*   **Phân tích tác động:** Nếu thầy bắt buộc tích hợp SSO thật của trường, effort kỹ thuật sẽ cực kỳ lớn. Đăng nhập qua email là dễ nhất.
*   **Câu hỏi Follow-up:** "Nhóm có thể giả lập đăng nhập bằng email Google (@hcmut.edu.vn) thay vì kết nối hệ thống SSO thật của trường không ạ?"

**6. Sau sự kiện cần báo cáo gì, theo định dạng nào? Có liên quan tới điểm rèn luyện không? (Q05)**
*   **Phân tích tác động:** Nếu bắt buộc liên kết API với hệ thống điểm rèn luyện thật, đây là rủi ro scope phình to. Nếu chỉ xuất file CSV/Excel thì effort ở mức vừa phải cho A34.
*   **Câu hỏi Follow-up:** "Nếu không kết nối API thật, nhóm thiết kế chức năng xuất file Excel theo format chuẩn của trường để nộp tay có được chấp nhận không?"

---

## Mức ưu tiên 3: Tác động đến thông số giả định và đo lường (Q06, Q09, Q07)

**7. Quy mô: bao nhiêu sự kiện mỗi tháng, bao nhiêu người mỗi sự kiện, lúc cao điểm check-in bao nhiêu người cùng lúc? (Q06)**
*   **Phân tích tác động:** Số liệu này quyết định việc thiết kế tải (load design) cho Database và API (A25). 

**8. Có ràng buộc gì về dữ liệu cá nhân sinh viên, hosting hay nền tảng (web hay mobile)? (Q09)**
*   **Phân tích tác động:** Nếu thầy yêu cầu hosting máy chủ riêng hoặc không dùng free-tier, nhóm phải cập nhật giới hạn (constraints) vào Task 1.

**9. Hiện nay đang dùng công cụ gì, và việc tổng hợp mất bao lâu? (Q07)**
*   **Phân tích tác động:** Không ảnh hưởng code nhưng cung cấp mốc thời gian gốc (baseline metrics) để thiết lập Measures of Effectiveness (MoE) cho A07 và tính toán Business Case A06.