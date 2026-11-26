---
Nội dung: Đề xuất cập nhật Sheet master theo rà tiến độ 23/11 (chưa dán)
Chủ sở hữu: TV1
Phiên bản: 0.1
Cập nhật: 23/11/2026
Trạng thái: TV1 duyệt 23/11; AI kiểm tra lại trên Sheet rồi ghi mục 1, 2, 3 cùng ngày (tab 2 dòng 85–89, tab 8 dòng CP3, tab 6 ô G7:G9; đã đọc lại khớp). Mục 4 không đổi. Mục 5 (tab 9) xem PROGRESS.md.
---

# Cập nhật Sheet 23/11

## 1. Tab 2 Weekly Log: dòng W13 (17–22/11)

Tab hiện dừng ở dòng W13 ngày 16/11. Dán sau dòng đó (cột A–K, phân tách bằng tab; cột Effort để trống/"—" vì chưa có giờ thực tế).

```
W13	16/11 – 22/11	A30, A31, A40	TV2: kiểm thử API và CP3, hồi quy A39	18/11: chạy bộ API 114 request (28/30 nhóm assertion đạt). 19/11: chạy giao diện 10 bước và quét QR thật trên điện thoại Android, nhánh PR #6 ghép với backend main. 20/11: hồi quy A39, hai lượt độc lập (12/13 ca E2E đạt). Kết quả trong docs/quality/results/ (pm-docs PR #11, merge 22/11). Jira chưa cập nhật	—			35 ca: 32 đạt, 2 không đạt, 1 chưa chạy. D01 (cao): lỗi lưu thông báo PROMOTED làm hủy đăng ký trả 500, trái Q14. D02 (thấp): mã lỗi tự duyệt. T-AUTH-01 chưa chạy (chưa có Google Client ID). Bản kiểm thử là bản ghép trên máy, chưa phải main frontend	TV3 đối chiếu D01 với Q14; chạy lại bộ API và E2E khi PR #6 merge; chuyển Jira A30, A31, A39 theo kết quả	Đức Nghĩa
W13	16/11 – 22/11	A22	TV2: chốt quality plan	Quality plan v1.0 chốt 19/11 (TV2), 35 test case có mã T-… khớp ma trận truy vết	—			Trễ so với hạn 22/10	Đối chiếu Traceability sau khi TV1 sửa cột Checkpoint	Đức Nghĩa
W13	16/11 – 22/11	A28, A35, A24	TV4, TV5: merge frontend, Docker, CI	PR #6 (frontend) vẫn mở, mergeable, chưa có approve của người; PR #28 (backend) đã merge 15/11. Chưa có workflow CI ở cả hai repo; Jira A24 Backlog	—			PR #6 trễ hạn merge 19/11 trong lịch rút gọn (R23); frontend main vẫn chỉ có khung	Review chéo và merge PR #6; nếu chưa merge thì quyết phương án P-B theo lich-rut-gon.md	Đức Nghĩa
W13	16/11 – 22/11	A26, A27, A29, A33, A34	TV3: sửa lỗi hợp đồng API	PR #33 (16/11, hợp đồng phản hồi duyệt sự kiện), PR #34 (22/11, mã lỗi SELF_APPROVAL_NOT_ALLOWED). PR #31 (import, admin CLI, email) vẫn mở, hoãn theo D4	—			PR #34 chưa được TV2 chạy lại; D01 chưa sửa; chưa thấy review của người khác trên PR backend (R24)	TV2 chạy lại T-AUTH-04 sau PR #34; cập nhật defects.md	Đức Nghĩa
W13	16/11 – 22/11	A36	Theo dõi tiến độ, thu giờ thực tế	23/11: hạn thu giờ 19/11 đã qua; tab 3 chưa có giờ 22/10–15/11 của TV1, TV3, TV4, TV5 (TV2 có A22, A31 mỗi dòng 1,0 giờ); Jira worklog chỉ 9 giờ (A21, A50, A58), đều của TV1; Jira không issue nào cập nhật từ 16/11	—			I02 còn mở; không so sánh được effort kế hoạch và thực tế (R02)	Nhắc từng thành viên nhập giờ vào tab 3; quyết có giữ cột Effort TT trống ở báo cáo nếu hết hạn nộp vẫn thiếu	Đức Nghĩa
```

(Thay "Đức Nghĩa" nếu TV1 không phải người dán.)

## 2. Tab 8 Biên bản CP: dòng CP3

Ô hiện ghi "Chưa diễn ra (dự kiến 11–16/11)" và kết quả "Chưa đánh giá". Đề xuất **nối thêm** (không xóa nội dung cũ, theo quy tắc nhật ký):

- Cột B (Ngày thực tế): `SỬA 23/11: kiểm thử API 18/11, giao diện 19/11 (nhánh PR #6), hồi quy 20/11 (TV2).`
- Cột D (Kết quả): `SỬA 23/11: chưa đạt tiêu chí "test case đạt". 35 ca: 32 đạt, 2 không đạt (T-AUTH-04, T-WL-03; D02, D01), 1 chưa chạy (T-AUTH-01). Luồng đăng nhập (bản demo), tạo, duyệt, đăng ký, hủy, danh sách chờ, check-in QR, báo cáo chạy xuyên suốt trên bản ghép backend main và frontend PR #6; chưa chạy trên main frontend. Chi tiết: pm-docs docs/quality/results/cp3-2026-11-20.md.`
- Cột F (Hành động): `Sửa D01 (TV3), chạy lại sau khi PR #6 merge; UAT 26–27/11 (A41).`

TV2 xác nhận phần kết luận "chưa đạt" trước khi dán (tiêu chí đạt do TV2 và TV1 chốt).

## 3. Tab 6 Traceability: cột Checkpoint

Ba dòng điểm danh ghi CP4 trong khi báo cáo và Q21 ghi CP5 (REQ-10 QR, REQ-11 nhập mã/thủ công, REQ-10 giao diện mobile-first, cột G dòng 7–9). Đề xuất sửa `CP4` thành `CP5` ở ba ô này. Đây là chỗ lệch giữa Sheet và báo cáo; đề phạt nặng bảng mâu thuẫn nhau.

## 4. Tab 3 Time Tracking

Không đề xuất điền thay. Chỉ nhắc: hạn 19/11 đã qua. Theo quy tắc liêm chính dữ liệu, nếu thành viên không nhập, báo cáo ghi trống và nêu giới hạn.

## 5. Tab 9 AI Log

Dán `9-ai-log-23-11.tsv`. Hai dòng của TV2 (18/11, 20/11) đã có ở `docs/ai-usage.md` trong pm-docs; kiểm tra tab 9 có đủ chưa.
