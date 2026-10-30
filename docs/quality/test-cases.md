---
Activity: A31, A40
Chủ sở hữu: TV2
Trạng thái: nháp
---

# Test cases

| Mã | Requirement | Tiền điều kiện | Các bước | Kết quả kỳ vọng | Kết quả thực tế | Ngày | Người chạy |
|---|---|---|---|---|---|---|---|
| T-RG-01 | Đăng ký sự kiện | Sự kiện còn chỗ, SV đã đăng nhập | Bấm Đăng ký | Đăng ký thành công, số chỗ còn lại giảm 1 | | | |
| T-RG-02 | Giới hạn số chỗ | Sự kiện đã hết chỗ | Bấm Đăng ký | Bị từ chối, thông báo hết chỗ | | | |
| T-RG-03 | Chống đăng ký trùng | SV đã đăng ký sự kiện | Đăng ký lần nữa | Bị từ chối, không tạo bản ghi mới | | | |
| T-CI-01 | Check-in bằng QR | SV đã đăng ký | Ban tổ chức quét mã | Ghi nhận tham dự, có thời điểm | | | |
| T-CI-02 | Chống check-in trùng | SV đã check-in | Quét lại | Báo đã check-in, không tạo bản ghi mới | | | |
| T-CI-03 | Nhập mã thủ công | Camera không quét được | Nhập mã | Check-in thành công | | | |
