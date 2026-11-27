# P1 · Kiểm thử lại main ngày 27/11/2026

> Bản lưu báo cáo P1. Đường dẫn bằng chứng đã đổi theo vị trí trong repo. Các log văn bản đổi đuôi thành `.txt`. Tên đường dẫn trong lệnh và nội dung dưới đây chỉ vị trí lúc chạy P1. Báo cáo kết quả chính thức diễn giải U3 là **đạt một phần** và giữ nguyên kết quả máy.

- Backend `24e08ce36dabd3a07ae6f38e31d3d28bb4ab22e0`, gồm PR #34 và #35. Frontend `58a81b8f2b314687fe0c9f68a55f5d3ac069c31f`, gồm PR #6 và #11. Hai worktree detached đặt ở `../wt-be` và `../wt-fe`. Ba checkout chính đều sạch trên `main` sau kiểm thử. PR #31 backend ngoài phạm vi theo D4.
- API đạt **30/30 nhóm có bản ghi kết quả**, gồm D01 và D02. Go đạt **606/606 test và subtest**. Frontend đạt **5/5 test validation**.
- Playwright mặc định **11/13 ca chính, 1/3 ca PR #11**. Bật camera giả để chẩn đoán đạt **13/13 ca chính, 2/3 ca PR #11**. Lượt mặc định ghi nhận màn hình check-in bị trắng khi chuyển từ tab quét chưa mở được camera. U3 trượt ở cả hai lượt vì form báo lỗi bằng toast, trường tương ứng không có thông báo riêng.
- Stack chạy trên **http://127.0.0.1:5178/login**. Web, API readiness và hồ sơ của cả ba vai demo đều trả HTTP 200. [Bằng chứng kiểm tra stack](stack-smoke.txt)

## Môi trường và lệnh đã chạy

Windows/amd64, múi giờ UTC+7. Git 2.49.0.windows.1, Docker Engine/CLI 29.0.1, Compose v2.40.3-desktop.1, PostgreSQL 16.14, nginx 1.28.3, Go 1.27.4, Node.js 24.11.1, npm 11.6.2, Vite 6.4.5, Python 3.12.0, Playwright Node 1.65.1 và Chrome 158.0.8127.38 headless, viewport 1280×900. Playwright dùng bản cài A39 qua junction `../node_modules` nằm ngoài thư mục bằng chứng.

| Nơi chạy | Lệnh | Mã thoát và kết quả |
| --- | --- | --- |
| Gốc workspace | `git -C ticket-system-uni-be worktree add --detach ../.scratch/orca/main-retest-2026-11-27/wt-be 24e08ce` | 0 |
| Gốc workspace | `git -C ticket-system-uni-fe worktree add --detach ../.scratch/orca/main-retest-2026-11-27/wt-fe 58a81b8` | 0 |
| `wt-be` | `docker compose -p qldapm-m27 -f compose.yaml -f compose.host.yaml -f compose.a39.yaml config --quiet` | 0 |
| `wt-be` | Cùng tùy chọn Compose, `up -d --build --wait postgres migrate api worker web` | 0. Migration exit 0, Postgres/API/web healthy. [Log Compose](compose-up.txt) |
| `wt-be` | Cùng tùy chọn Compose, `up -d tools` | 0. Kiểm binary với `docker exec qldapm-m27-tools-1 /tmp/dev-token -h` và file seed với `docker exec qldapm-m27-tools-1 test -r /db/seed/demo.sql`, cả hai exit 0 |
| `wt-be` | `go build ./...` | 0. Không lỗi. [Log build](go-build.txt) |
| `wt-be` | `go vet ./...` | 0. Không lỗi. [Log vet](go-vet.txt) |
| `wt-be` | `go list -tags integration ./...` | 0. 34 package. [Danh sách package](go-packages.txt) |
| `wt-be` | `go test -json -count=1 -tags integration ./...` | 0. 29 package có test đạt, 5 package không có test, 101 test cấp cao nhất, 606 test/subtest tính cả cấp con, 0 lỗi/skip ở cấp test. [Log Go JSON](go-integration.ndjson) |
| `wt-fe` | `npm.cmd ci` | 0. 113 package được cài. [Log cài](npm-ci.txt) |
| `wt-fe` | `npm.cmd run build` | 0. 1.782 module. [Log build](npm-build.txt) |
| `wt-fe` | `node --test src/features/events/eventValidation.test.js` | 0. 5 đạt, 0 trượt, 0 bỏ qua. [Log test FE](node-test.txt) |

Integration dùng `TEST_DATABASE_URL` lấy từ `DATABASE_URL` của `wt-be/.env`, trỏ Postgres công bố ở `127.0.0.1:55436`. Role `ticket` tạo và xóa các database test riêng. Cổng API `53006` và web `5178` cũng bind vào loopback. Tools dùng chung network namespace với Postgres và mount binary `../tools/dev-token` cùng `db/seed/demo.sql` ở chế độ chỉ đọc. Phạm vi thao tác Docker giới hạn trong `qldapm-m27`.

## API

Chạy `python -X utf8 fixture.py` từ `main-retest-2026-11-27`. Script gọi `python run/verify_api_uat.py` hai lượt với UTF-8 rồi đưa DB về dữ liệu demo sạch. Trước mỗi lượt, script xóa dữ liệu ứng dụng trong DB thử của `qldapm-m27` bằng `TRUNCATE … RESTART IDENTITY CASCADE`, giữ bảng migration, nạp lại demo và đối chiếu baseline. Hai baseline khớp hoàn toàn về số dòng từng bảng, ba vai demo và membership `DEMO/ORGANIZER`. ID và timestamp sinh mới theo từng lượt. [Script đã chạy](verify_api_uat.py), [baseline lượt 1](baseline-run1.txt), [baseline lượt 2](baseline-run2.txt)

| Lượt | Cấu hình | Request | Nhóm có kết quả | Mã thoát |
| --- | --- | --- | --- | --- |
| 1 | Chạy đủ nhánh, có T-WL-03 | 51, gồm 50 phản hồi đúng kỳ vọng tại điểm chạy và 1 phản hồi sau khi fixture đã đổi trạng thái | 12 đạt. T-REG-04 ngắt khi hủy lần hai, nên T-WL-02 và 16 nhóm tiếp theo chưa tới | 1. [HTTP NDJSON](../../main-2026-11-27-api-run1.ndjson), [stderr](api-run1.txt) |
| 2 | `SKIP_WL03=1`, fixture demo mới | 111, tất cả qua kiểm tra của script | 29 đạt, 0 trượt, bỏ qua đúng T-WL-03 | 0. [HTTP NDJSON](../../main-2026-11-27-api-run2.ndjson), [stderr](api-run2.txt) |
| Tổng hợp | Lượt 1 lấy T-WL-03; lượt 2 lấy 29 nhóm còn lại | 114 request làm bằng chứng, gồm toàn bộ 111 request lượt 2 và 3 request T-WL-03 lượt 1 | 30/30 nhóm có bản ghi `result` đạt | |

Hai health check và T-AUTH-02 có kiểm trong cả hai lượt, đã tính trong số request. T-AUTH-02 gửi refresh token giả và kiểm `401 UNAUTHENTICATED`, nằm ở dòng 3 của cả hai log. Script gốc chỉ dùng assert cho T-AUTH-02 nên ca này không nằm trong mẫu số 30 theo các bản ghi `result`. T-RP-03 lượt 2 trả CSV 500 đăng ký và 250 điểm danh, tổng thời gian lấy thống kê và hai CSV là 0,060 giây. [Log lượt 2](../../main-2026-11-27-api-run2.ndjson)

- **D01 · T-WL-03 đạt.** Sau khi trigger thử nghiệm từ chối ghi `PROMOTED`, `POST /registrations/{id}/cancel` của S1 trả **200**, trạng thái `CANCELLED`, có đăng ký được đôn lên và không có mã lỗi. `GET /registrations/{id}` của S2 trả **200 REGISTERED**. Đọc lại S1 trả **200 CANCELLED**. Log container xác nhận backend bỏ qua ghi thông báo khi PostgreSQL trả `P0001`. Tại bước kế tiếp của lượt 1, hủy lại chính đăng ký S1 nhận **409 INVALID_STATE_TRANSITION**, làm dừng nhóm T-REG-04/T-WL-02. Lượt 2 cho cả hai nhóm đạt với dữ liệu đầu tương đương và không chạy trigger. [Lượt 1 dòng 59–64](../../main-2026-11-27-api-run1.ndjson#L59), [cảnh báo backend dòng 1](d01-api-container.txt)
- **D02 · T-AUTH-04 đạt ở cả hai lượt.** Student nhận **404 NOT_FOUND** ở cả trạng thái nháp và chờ duyệt. Organizer chỉ có vai gốc nhận **403 FORBIDDEN**. Chính người tạo sau khi được cấp thêm vai Admin nhận **403 SELF_APPROVAL_NOT_ALLOWED** khi gọi `POST /events/{id}/approve`. Đọc lại trả **200 PENDING_APPROVAL**. Phép thử trả lại quyền Organizer trong `finally`. [Lượt 2 dòng 15–21](../../main-2026-11-27-api-run2.ndjson#L15), [lượt 1 dòng 15–21](../../main-2026-11-27-api-run1.ndjson#L15)

Script API giữ nguyên assertions nghiệp vụ, đổi container sang project mới, đọc cấu hình DB từ container API thay cho mật khẩu ghi cứng và chuyển cùng refresh token giả thành biến cục bộ. Lỗi môi trường lúc chuẩn bị là truy vấn baseline dùng nhầm cột membership, đã sửa sang `member_role` trước lượt lấy bằng chứng.

## Playwright CP3 và PR #11

Đặt `BE_ENV` đến `wt-be/.env`, `OUT_DIR` đến thư mục chạy bên ngoài `run`, rồi chạy `node run/e2e/cp3-ui.mjs`. Dùng cùng script cho cả hai lượt, đặt `FAKE_CAMERA=1` ở lượt chẩn đoán và chờ video giả sẵn sàng trước khi rời tab quét. Mỗi lượt đặt lại DB demo trước khi chạy. Cả hai exit **1** do các ca trượt được ghi trong `results.json`. [Script CP3](../cp3-ui.mjs), [script U1–U3](../pr11-ui.mjs), [log mặc định](../run.txt), [log camera giả](../fake-camera/run.txt)

Điều chỉnh CP3 theo giao diện PR #11 gồm mở panel dev trước khi chọn dán token, tìm ô sự kiện theo nhãn vì ID cũ đã bỏ, chọn tên nút đăng ký/hàng chờ, hủy, nhập mã và tải CSV hiện hành. Bước 10 đọc thanh thống kê qua ARIA. C3 nhận thêm nguyên văn thông báo tự duyệt mới. Kỳ vọng trạng thái, HTTP và mã lỗi của 13 ca giữ theo bản trước. C1 dùng mã bước 7b của script gốc. Script ghi lỗi JavaScript, ẩn thông tin xác thực trước khi ghi mạng và trả exit 1 nếu còn ca trượt.

| Ca | Headless mặc định | Camera giả | Bằng chứng nghiệp vụ |
| --- | --- | --- | --- |
| 1 · Tạo và gửi duyệt | Đạt | Đạt | 201 tạo, 200 gửi duyệt, sức chứa 1, hàng chờ 2 |
| 2 · Admin duyệt | Đạt | Đạt | 200 `PUBLISHED` |
| 3 · A đăng ký | Đạt | Đạt | 201 `REGISTERED` |
| 4 · B chờ | Đạt | Đạt | 201 `WAITLISTED`, vị trí 1 |
| 5 · A hủy ngoài hạn 24 giờ | Đạt | Đạt | 200 `CANCELLED` |
| 6 · B lên chỗ | Đạt | Đạt | DB `REGISTERED`, 1 thông báo `PROMOTED`, UI hiện Đã đăng ký |
| 7 · Dời giờ sự kiện | Đạt | Đạt | PATCH 200 |
| 8 · Vé của B | Đạt | Đạt | Có QR canvas, mã trùng DB |
| 9 · Check-in mã rồi làm trùng | Trượt | Đạt | Trang trắng sau chuyển tab ở lượt mặc định. Lượt chẩn đoán trả 201 `CODE`, rồi 409 `ALREADY_CHECKED_IN` |
| 10 · Thống kê và xuất CSV | Đạt | Đạt | Tệp 3 dòng. Tỉ lệ 0% lượt mặc định sau ca 9 trượt và 100% khi ca 9 đạt |
| C1 · Hủy quá hạn (7b) | Đạt | Đạt | 422 `CANCEL_DEADLINE_PASSED`, UI hiện thông báo |
| C2 · Check-in ngoài giờ | Trượt | Đạt | Trang trắng sau chuyển tab ở lượt mặc định. Lượt chẩn đoán trả 422 `CHECKIN_WINDOW_CLOSED` và UI báo ngoài khung giờ |
| C3 · Tự duyệt | Đạt | Đạt | 403 `SELF_APPROVAL_NOT_ALLOWED`, UI báo “Bạn không thể tự duyệt sự kiện do chính mình tạo.” |
| **Tổng ca chính** | **11/13** | **13/13** | |

| Ca bổ sung | Mặc định | Camera giả | Kiểm tra thành phần |
| --- | --- | --- | --- |
| U1 · Vé/QR | Đạt 4/4 | Đạt 4/4 | Tab Sắp tới hiện REGISTERED và WAITLISTED đúng dữ liệu. Tab Tất cả hiện thêm CANCELLED. Tab Đã hủy chỉ hiện CANCELLED. Chi tiết vẽ QR, mã UI và API khớp DB |
| U2 · Check-in | Trượt 2/7 | Đạt 7/7 | Mặc định xác nhận thống kê ban đầu và mở tab Quét QR. Trang trắng khi chuyển Nhập mã làm chặn các thành phần còn lại. Lượt camera giả xác nhận đủ ba tab, mã sai trả 404 `NOT_FOUND` và UI báo lỗi, MANUAL bắt buộc ghi chú rồi trả 201, DB có `MANUAL` và một audit. Thống kê UI khớp DB từ 0/1 (0%) lên 1/1 (100%) |
| U3 · Form sự kiện | Trượt 2/6 | Trượt 2/6 | Tạo hợp lệ 201 `DRAFT`; sửa 200, tải lại và đọc DB đều thấy địa điểm mới. 4 phép thử thiếu tiêu đề và sai thứ tự lịch trên cả form tạo và sửa đều chặn request, nhưng lỗi chỉ xuất hiện trong toast |
| **Tổng ca bổ sung** | **1/3, 8/17 thành phần** | **2/3, 13/17 thành phần** | 0 ca không áp dụng |

- **Trang trắng khi camera không chạy.** Lượt mặc định ghi đúng lỗi JavaScript `Cannot stop, scanner is not running or paused.` ở ca 9, C2 và U2. `QrScanner.jsx` gọi `scanner.stop().then(…).catch(…)` khi rời tab. Thư viện html5-qrcode ném lỗi đồng bộ nếu scanner chưa chạy, trước khi chuỗi Promise được tạo. Chrome fake media làm scanner hoạt động, xác nhận các luồng nhập mã, check-in ngoài giờ và thủ công khi chuyển tab thành công. [Mạng mặc định dòng 41–42, 58–59, 77–78](../network.ndjson#L41), [ảnh ca 9](../shots/FAIL-9-organizer.png), [ảnh U2 lúc chuyển tab](../shots/U2-nhap-ma.png)
- **Form báo lỗi ở toast.** Điều kiện U3 yêu cầu thông báo ngay tại trường nhập. Với cả bốn thao tác không hợp lệ, ứng dụng không gửi POST/PATCH và toast hiện đúng nội dung, nhưng vùng của Tiêu đề/Kết thúc không có lỗi. [Ảnh thiếu tiêu đề](../shots/U3-tao-thieu-tieu-de.png), [ảnh tạo sai lịch](../shots/U3-tao-sai-lich.png), [ảnh sửa thiếu tiêu đề](../shots/U3-sua-thieu-tieu-de.png), [ảnh sửa sai lịch](../shots/U3-sua-sai-lich.png)

Quan sát ngoài ca kiểm thử. FE main chưa có màn hình thông báo in-app. `rg -n '/me/notifications|/notifications' ../wt-fe/src` trả exit 1 và 0 dòng. Hai log trình duyệt không có request này, dù API kiểm được thông báo. Banner check-in trùng vẫn hiện UUID người check-in. Bước 9 lượt camera giả đối chiếu UUID trên banner với `checked_in_by` trong DB. [Mạng camera giả dòng 44](../fake-camera/network.ndjson#L44), [ảnh banner](../fake-camera/shots/09-checkin-lan2.png)

## Bằng chứng và quét dữ liệu

- `e2e/results.json`, `e2e/network.ndjson`, `e2e/run.log`, `e2e/registrations.csv` và `e2e/shots/` là lượt mặc định, có 86 dòng mạng và 36 ảnh.
- `e2e/fake-camera/` có cùng cấu trúc cho lượt chẩn đoán, 92 dòng mạng và 31 ảnh. Lượt có QR giữ ảnh dữ liệu demo cục bộ theo phạm vi giao việc. [Kết quả mặc định](../results.json), [kết quả camera giả](../fake-camera/results.json)
- `api-run{1,2}.ndjson`, `api-run{1,2}.log`, `baseline-run{1,2}.txt`, `d01-api-container.log`, các log Go/npm và `stack-smoke.log` là bằng chứng máy chủ, build và test. Các script và báo cáo đều nằm trong phạm vi thư mục lượt chạy.

Từ `main-retest-2026-11-27`, chạy `python -X utf8 collect_evidence.py` để chuẩn hóa UTF-8, ẩn JWT, thông tin xác thực HTTP, giá trị các trường token/mã check-in, khóa và mã lấy từ DB thử. Sau khi ghi báo cáo, chạy `python -X utf8 collect_evidence.py --scan-only`. Lệnh grep bên trong là `rg --pcre2 --count --no-heading -f - -g '!*.png' <đường dẫn run>`. Mẫu được chuyển qua stdin từ dữ liệu cục bộ, không ghi giá trị trong lệnh hay báo cáo. Kết quả `rg exit=1, matches=0`, tức **0 dòng khớp** trên toàn bộ tệp chữ trong `run/`. `.env`, giá trị kiểm tra chính xác và log thô chỉ nằm ngoài `run/`.

## Stack bàn giao

Mở http://127.0.0.1:5178/login. Từ `wt-be`, nạp môi trường của lượt thử và tạo token demo ngay tại máy bằng PowerShell. Mỗi vai dùng tab riêng tư hoặc đăng xuất trước khi đổi vai. Token demo có hạn 8 giờ.

```powershell
Get-Content .env | ForEach-Object {
    if ($_ -match '^(AUTH_MODE|HTTP_ADDR|DATABASE_URL|JWT_SECRET)=(.*)$') {
        [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2], 'Process')
    }
}
go run ./cmd/dev-token -role organizer | Set-Clipboard
go run ./cmd/dev-token -role admin | Set-Clipboard
go run ./cmd/dev-token -role student | Set-Clipboard
```

Chạy lệnh của vai cần đăng nhập rồi dán clipboard vào **Dán access token để test → Dán token trực tiếp → Access token → Vào hệ thống**. Bỏ trống Refresh token. Đơn vị của Organizer là `DEMO`. DB đã trở về trạng thái demo sạch sau các phép thử.

Lệnh tắt từ `wt-be`.

```powershell
docker compose -p qldapm-m27 -f compose.yaml -f compose.host.yaml -f compose.a39.yaml down
```

T-AUTH-01 chưa chạy vì chưa có `GOOGLE_CLIENT_ID`. T-CI-03 giữ mốc 1 thiết bị từ lượt trước. Lượt này không đo camera/thiết bị thật. U1–U3 Playwright thay phần TV2 đi tay theo cập nhật của lead. Hai kết quả sản phẩm còn mở là chuyển tab check-in khi camera chưa chạy và lỗi form chưa hiện bên cạnh trường.
