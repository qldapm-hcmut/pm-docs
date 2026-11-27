---
Activity: A41
Chủ sở hữu: TV2
Trạng thái: bản nháp
---

# Biên bản UAT A41 (27/11/2026)

## 1. TV2 đi tay độc lập ngày 24/11/2026

- **Người chạy và môi trường** TV2, trên máy TV2.
- **Bản kiểm** BE `main` lúc đó tại `a964e194165e9f1f559b55918941596441c0b375`. FE nhánh `feat/local-demo-integration` của PR #6 trước merge tại `84c38cb38802971e81c8460d9c9c79aabcae4037`.
- **Kết quả theo xác nhận của TV2** TV2 tự đi toàn bộ luồng chức năng theo PD trên giao diện và báo tất cả đạt; buổi này không rà tài liệu PD-01, PD-02, PD-04. Không có ảnh chụp, bản ghi assertion từng ca hoặc người thứ hai xác nhận. Chi tiết trong kịch bản giữ nguyên phạm vi lời xác nhận. [Kịch bản UAT](uat-kich-ban.md)
- **Nguồn đối chiếu** API và E2E tự động ngày 24/11 chạy riêng trên BE `24e08ce` và FE ghép `7ff51eb`. [Bảng so sánh các bản](../results/main-2026-11-27.md#tóm-tắt)

## 2. Bằng chứng tự động P1 trên main ngày 27/11/2026 (trước PR #12)

BE `24e08ce36dabd3a07ae6f38e31d3d28bb4ab22e0`, FE `58a81b8f2b314687fe0c9f68a55f5d3ac069c31f`. P1 chạy stack Docker local, Playwright/Chrome headless, tài khoản demo. TV2 không đi tay lại ngày 27/11. TV1 xác nhận qua review PR **đang chờ**. [Báo cáo P1](../results/main-2026-11-27-e2e/p1/report.md), [môi trường và kết quả chi tiết](../results/main-2026-11-27.md)

Playwright mặc định là kết quả chính. Ca chính **11 đạt, 2 trượt, 0 không áp dụng**. Ca U **1 đạt đủ, 1 trượt, 1 đạt một phần, 0 không áp dụng**. Camera giả dùng chẩn đoán, đạt **13/13 ca chính và 2/3 ca U**. [Kết quả máy mặc định](../results/main-2026-11-27-e2e/results.json), [kết quả máy camera giả](../results/main-2026-11-27-e2e/fake-camera/results.json)

### Ca chính

Mỗi dòng lấy từ mã ca tương ứng trong `results.json` mặc định. C1 được ghi dưới mã `7b`.

| Mã · Thao tác | Kết quả mặc định | Assertion và ảnh |
|---|---|---|
| 1 · Organizer tạo và gửi duyệt | Đạt | Tạo 201, gửi duyệt 200. [Ảnh](../results/main-2026-11-27-e2e/shots/01-organizer-gui-duyet.png) |
| 2 · Admin duyệt | Đạt | 200 `PUBLISHED`. [Ảnh](../results/main-2026-11-27-e2e/shots/02-admin-duyet.png) |
| 3 · Student A đăng ký | Đạt | 201 `REGISTERED`. [Ảnh](../results/main-2026-11-27-e2e/shots/03-studentA-dang-ky.png) |
| 4 · Student B vào hàng chờ | Đạt | 201 `WAITLISTED`, vị trí 1. [Ảnh](../results/main-2026-11-27-e2e/shots/04-studentB-hang-cho.png) |
| 5 · Student A hủy trước hạn | Đạt | 200 `CANCELLED`. [Ảnh](../results/main-2026-11-27-e2e/shots/05-studentA-huy.png) |
| 6 · Student B được đôn lên | Đạt | UI và DB `REGISTERED`, DB có 1 `PROMOTED`. [Ảnh](../results/main-2026-11-27-e2e/shots/06-studentB-len-cho.png) |
| 7 · Organizer dời giờ | Đạt | PATCH 200. [Ảnh](../results/main-2026-11-27-e2e/shots/07-organizer-doi-gio.png) |
| 8 · Student B mở vé | Đạt | QR có trên canvas, mã hiển thị khớp DB. [Ảnh](../results/main-2026-11-27-e2e/shots/08-studentB-qr.png) |
| 9 · Check-in bằng mã và thử trùng | Trượt · D03 | Trang trắng khi chuyển tab, không nhập được mã. Camera giả cho 201 `CODE`, lần sau 409 `ALREADY_CHECKED_IN`. [Ảnh mặc định](../results/main-2026-11-27-e2e/shots/FAIL-9-organizer.png), [ảnh camera giả lần 1](../results/main-2026-11-27-e2e/fake-camera/shots/09-checkin-lan1.png), [lần 2](../results/main-2026-11-27-e2e/fake-camera/shots/09-checkin-lan2.png) |
| 10 · Thống kê và CSV | Đạt | Tải CSV 3 dòng. Tỉ lệ 0% sau bước 9 trượt. Camera giả đạt 100% sau check-in. [Ảnh mặc định](../results/main-2026-11-27-e2e/shots/10-bao-cao-csv.png), [ảnh camera giả](../results/main-2026-11-27-e2e/fake-camera/shots/10-bao-cao-csv.png) |
| C1 · Hủy quá hạn | Đạt | 422 `CANCEL_DEADLINE_PASSED` và UI báo quá hạn. [Ảnh](../results/main-2026-11-27-e2e/shots/07b-huy-qua-han.png) |
| C2 · Check-in ngoài khung giờ | Trượt · D03 | Trang trắng khi chuyển tab. Camera giả nhận 422 `CHECKIN_WINDOW_CLOSED` và UI báo ngoài giờ. [Ảnh mặc định](../results/main-2026-11-27-e2e/shots/FAIL-C2-organizer.png), [ảnh camera giả](../results/main-2026-11-27-e2e/fake-camera/shots/C2-checkin-ngoai-gio.png) |
| C3 · Người tạo kiêm Admin tự duyệt | Đạt | 403 `SELF_APPROVAL_NOT_ALLOWED`, có thông báo tự duyệt trên UI. [Ảnh](../results/main-2026-11-27-e2e/shots/C3-tu-duyet.png) |

### Ca bổ sung U1–U3

| Ca | Kết quả mặc định | Assertion và ảnh |
|---|---|---|
| U1 · Vé của tôi và QR | Đạt 4/4 | Sắp tới, Tất cả và Đã hủy lọc đúng trạng thái. QR được vẽ, mã hiển thị và API khớp DB. [Sắp tới](../results/main-2026-11-27-e2e/shots/U1-sap-toi.png), [Tất cả](../results/main-2026-11-27-e2e/shots/U1-tat-ca.png), [Đã hủy](../results/main-2026-11-27-e2e/shots/U1-da-huy.png), [QR](../results/main-2026-11-27-e2e/shots/U1-qr.png) |
| U2 · Check-in | Trượt, 2/7 | Thống kê đầu khớp DB, mở được tab Quét QR. D03 làm trắng trang khi chuyển Nhập mã, chặn thử mã sai, Danh sách, thủ công và thống kê sau. Camera giả đạt 7/7, có MANUAL 201, một audit và thống kê sau khớp DB. [Thống kê đầu](../results/main-2026-11-27-e2e/shots/U2-thong-ke-truoc.png), [Quét QR](../results/main-2026-11-27-e2e/shots/U2-quet-qr.png), [trang trắng](../results/main-2026-11-27-e2e/shots/U2-nhap-ma.png), [thủ công với camera giả](../results/main-2026-11-27-e2e/fake-camera/shots/U2-thu-cong.png) |
| U3 · Form tạo và sửa sự kiện | Đạt một phần, 2/6 | Tạo hợp lệ 201, sửa hợp lệ 200 và tải lại đúng dữ liệu. Cả bốn thao tác sai đều bị chặn trước request, có toast. Thiếu lỗi tại riêng từng trường theo kỳ vọng bổ sung của U3. Kết quả máy ghi `ok: false` ở cả hai lượt, không tính U3 là đạt đủ. [Tạo hợp lệ](../results/main-2026-11-27-e2e/shots/U3-tao-hop-le.png), [sửa hợp lệ](../results/main-2026-11-27-e2e/shots/U3-sua-hop-le.png), [thiếu tiêu đề tạo](../results/main-2026-11-27-e2e/shots/U3-tao-thieu-tieu-de.png), [sai lịch tạo](../results/main-2026-11-27-e2e/shots/U3-tao-sai-lich.png), [thiếu tiêu đề sửa](../results/main-2026-11-27-e2e/shots/U3-sua-thieu-tieu-de.png), [sai lịch sửa](../results/main-2026-11-27-e2e/shots/U3-sua-sai-lich.png) |

## 3. Kiểm lại trên FE main `ff9ea2d`

| Ca UAT | Kết quả sau PR #12 |
|---|---|
| UAT-08 | Bước 9 nhận 201 khi nhập mã hợp lệ rồi 409 ALREADY_CHECKED_IN khi nhập lại. |
| UAT-09 | Tab Nhập mã mở được khi camera không chạy. Mã sai trả 404, mã đúng trong giờ trả 201, ngoài giờ trả 422. |
| UAT-10 | Danh sách mở được. MANUAL trả 201, có một audit và thống kê khớp DB. |
| UAT-14 | Luồng mặc định đạt 13/13 ca, tỉ lệ sau check-in là 100%, CSV có 3 dòng. |

[Kiểm lại sau PR #12](../results/main-2026-11-27.md#kiểm-lại-sau-pr-12), [log mạng](../results/main-2026-11-27-e2e/sau-pr12/network.ndjson).

### Điểm còn lại

- **D03 đã sửa ở PR #12 và kiểm lại đạt trên FE main `ff9ea2d`.** Lượt mặc định đạt 13/13 ca chính. U1 và U2 đạt đủ, U3 đạt một phần. Bốn tình huống camera đều chuyển được về Nhập mã. D01/D02 đã kiểm lại đạt ở lượt API trước đó. [Kiểm lại sau PR #12](../results/main-2026-11-27.md#kiểm-lại-sau-pr-12), [Defects](../defects.md).
- **T-AUTH-01 chưa kiểm** vì chưa có `GOOGLE_CLIENT_ID`. P1 xác nhận stack chạy với auth demo. [Phạm vi chưa kiểm](../results/main-2026-11-27.md#chưa-kiểm)
- **T-CI-03 mới có một thiết bị** từ lượt 19/11, thiếu so với ≥3 thiết bị của PD-03. P1 chưa quét QR thật trên main. [Bằng chứng thiết bị thật](../results/cp3-2026-11-20.md)
- **PD-05 chưa có bằng chứng người ngoài nhóm dựng theo README.** P1 dựng stack nội bộ bằng cấu hình thử riêng. Chưa có bằng chứng lượt dựng độc lập trên máy sạch của người ngoài. [Báo cáo dựng stack P1](../results/main-2026-11-27-e2e/p1/report.md#môi-trường-và-lệnh-đã-chạy)
- **Quan sát** FE chưa có màn thông báo in-app. Banner khi check-in trùng vẫn hiện UUID. U3 không mở defect. Các đối chiếu tài liệu PD-01, PD-02 và PD-04 còn thiếu bằng chứng như ghi trong kịch bản. [Quan sát P1](../results/main-2026-11-27.md#quan-sát-ngoài-bộ-test-case), [kịch bản UAT](uat-kich-ban.md)

**Kết luận A41** chờ TV2/TV1 xác nhận.
