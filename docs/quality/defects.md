# Defects

| Mã | Ngày | Mô tả | Mức độ (nghiêm trọng / cao / trung bình / thấp) | Test liên quan | Người sửa | Trạng thái |
|---|---|---|---|---|---|---|
| D01 | 18/11/2026 | Khi lưu thông báo in-app `PROMOTED` thất bại, API hủy đăng ký trả 500 và transaction hoàn tác cả hủy lẫn chuyển người đầu hàng. Theo Q14, lỗi thông báo vẫn tính là đã đăng ký đối với người được chuyển. Quan sát khi chủ động mô phỏng lỗi lưu thông báo trên DB kiểm thử. | Cao | T-WL-03 | TV3, phối hợp TV5 (đề xuất) | Đã sửa (PR #35), kiểm lại 27/11 trên main 24e08ce: T-WL-03 đạt |
| D02 | 18/11/2026 | Người tạo sự kiện kiêm Admin bị chặn tự duyệt đúng quy tắc. HTTP trả 403 `FORBIDDEN` thay cho `SELF_APPROVAL_NOT_ALLOWED` theo hợp đồng, nên client không phân biệt được trường hợp tự duyệt và thiếu vai trò. | Thấp | T-AUTH-04 | TV3 (đề xuất) | Đã sửa (PR #34), kiểm lại 27/11 trên main 24e08ce: T-AUTH-04 đạt |
| D03 | 27/11/2026 | Màn check-in mở mặc định ở Quét QR. Khi camera không khởi động được, chuyển sang Nhập mã hoặc tab khác làm trắng toàn trang. Organizer mất cả nhập mã và xác nhận thủ công. | Cao | CP3 bước 9, C2, U2 | TV4 (đề xuất) | Đã sửa (FE PR #12), kiểm lại 27/11 trên FE main ff9ea2d: CP3 bước 9, C2, U2 đạt |

D01 và D02 có bằng chứng ban đầu từ [kết quả CP3 và log HTTP](results/cp3-2026-11-20.md). Bằng chứng kiểm lại ở [kết quả API ngày 27/11](results/main-2026-11-27.md#bộ-api).

## D03 · Trang check-in trắng khi rời tab Quét QR

Tái hiện trên Chrome headless không có camera. Mở màn check-in, đợi thông báo không mở được camera rồi rời tab Quét QR bằng cách chọn Nhập mã hoặc Danh sách. Trang trắng với lỗi JavaScript `Cannot stop, scanner is not running or paused.`. Chưa thử trên trình duyệt thật bị từ chối quyền camera. [Báo cáo ngày 27/11](results/main-2026-11-27.md#e2e-trên-giao-diện), [log mạng bước 9](results/main-2026-11-27-e2e/network.ndjson#L41), [log mạng C2](results/main-2026-11-27-e2e/network.ndjson#L58), [log mạng U2](results/main-2026-11-27-e2e/network.ndjson#L77), [ảnh trang trắng](results/main-2026-11-27-e2e/shots/FAIL-9-organizer.png)

Khi rời tab, `QrScanner.jsx` gọi `scanner.stop()` trước khi scanner chạy. `html5-qrcode` ném lỗi đồng bộ trước khi tạo Promise nên `.catch()` không bắt được. Hồi quy trên `main` qua PR #11: bản `QrScanner.jsx` của nhánh TV4 (từ `614a5c3`, 02/11) chưa có bước chờ khởi động và kiểm tra `isScanning` trước khi dừng, trong khi bản của PR #6 trên `main` đã có. Khi merge `main` vào nhánh TV4 (`e43c46a`, 26/11), bản của TV4 được giữ nên mất bước bảo vệ; PR #11 đưa bản này vào `main`. Bước 9 và C2 đều đạt ở A39 ngày 20/11 trước PR #11. [Commit merge](https://github.com/qldapm-hcmut/ticket-system-uni-fe/commit/e43c46a), [kết quả A39](results/regression-2026-11-20.md#e2e-trên-giao-diện)

**Kiểm lại sau PR #12.** Trên FE main `ff9ea2d`, CP3 bước 9, C2 và U2 đều đạt với Chrome headless mặc định. Cả bốn tình huống camera đều chuyển được sang Nhập mã. Camfast còn một cảnh báo phát video. [Kết quả từng ca](results/main-2026-11-27-e2e/sau-pr12/results.json), [nhật ký camera](results/main-2026-11-27-e2e/sau-pr12/d03-report.json), [ảnh nhập mã](results/main-2026-11-27-e2e/sau-pr12/U2-nhap-ma.png).
