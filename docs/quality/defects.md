# Defects

| Mã | Ngày | Mô tả | Mức độ (nghiêm trọng / cao / trung bình / thấp) | Test liên quan | Người sửa | Trạng thái |
|---|---|---|---|---|---|---|
| D01 | 18/11/2026 | Khi lưu thông báo in-app `PROMOTED` thất bại, API hủy đăng ký trả 500 và transaction hoàn tác cả hủy lẫn chuyển người đầu hàng. Theo Q14, lỗi thông báo vẫn tính là đã đăng ký đối với người được chuyển. Quan sát khi chủ động mô phỏng lỗi lưu thông báo trên DB kiểm thử. | Cao | T-WL-03 | TV3, phối hợp TV5 (đề xuất) | Mở, chờ đối chiếu Q14 |
| D02 | 18/11/2026 | Người tạo sự kiện kiêm Admin bị chặn tự duyệt đúng quy tắc. HTTP trả 403 `FORBIDDEN` thay cho `SELF_APPROVAL_NOT_ALLOWED` theo hợp đồng, nên client không phân biệt được trường hợp tự duyệt và thiếu vai trò. | Thấp | T-AUTH-04 | TV3 (đề xuất) | Mở, chờ rà hợp đồng |

Bằng chứng: [kết quả CP3 và log HTTP](results/cp3-2026-11-20.md).
