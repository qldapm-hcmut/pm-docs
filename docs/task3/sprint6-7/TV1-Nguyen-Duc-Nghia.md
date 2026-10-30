---
Nội dung: Việc Sprint 6–7 (22/10–03/11) của TV1 Nguyễn Đức Nghĩa (PM)
Người giao: TV1
Phiên bản: 0.3
Cập nhật: 22/10/2026
Trạng thái: AI hỗ trợ soạn (Claude Code, 22/10); TV1 duyệt 22/10
---

# TV1 · Nguyễn Đức Nghĩa · Sprint 6–7

Đầu vào của từng task có sẵn trong gói upload trên Drive, thư mục `4-tai-nguyen/<mã task>/`; mỗi thư mục có `DAU-VAO.md` ghi từng đầu vào lấy ở đâu (có sẵn, tab Sheet, hay chờ ai tạo). Tài liệu dùng chung (đề bài, Client Log, REQ, mục tiêu, giả định, PD-01…05, sơ đồ, mẫu ghi giờ hồi tưởng hạn 23/10) ở `4-tai-nguyen/chung/`; báo cáo PDF ở `3-bao-cao/`.

## Tóm tắt

| # | Task | Jira | Giờ | Ngày | Ngày xong |
|---|---|---|---:|---|---|
| 1 | Giao việc Sprint 6–7 | | | 22/10 | **22/10** |
| 2 | A58 Confirm scope-affecting points with client | SCRUM-86 | 2,1 | 22–23/10 (đợi trả lời đến 24/10) | **24/10** |
| 3 | A23 Approve Project Baseline V1.0 (chủ trì) | SCRUM-87 | 1,0 (cả nhóm 5,2) | 25/10 15h | 25/10, sau họp: PDF và tag |
| 4 | A36, A57 Theo dõi tiến độ, rà truy vết (hammock) | | 9,5 | từ 25/10 | hằng tuần |

Tổng: 6,0h trong Sprint 6 (22–27/10), 6,6h trong Sprint 7.

## Lịch theo ngày

| Ngày | Task | Giờ | Việc | Thực tế |
|---|---|---:|---|---|
| Thứ Năm 22/10 | Giao việc | | Gửi file của từng người; dán vào mô tả Jira | |
| Thứ Năm 22/10 | A58 | 2,0 | Đọc lại, gửi email; ghi Client Log | |
| Thứ Sáu 23/10 | A58 | 0,1 | Theo dõi trả lời; nhắc nộp giờ hồi tưởng (hạn hôm nay) | |
| Thứ Bảy 24/10 | A58 | | Chưa có trả lời thì chốt hai giả định còn mở; kiểm điều kiện họp | |
| Chủ nhật 25/10 | A23 | 1,0 | Chủ trì họp 15h, ký biên bản | |
| 25–27/10 | A36, A57 | 2,9 | Weekly Log W9; các bước sau họp | |
| 28/10–03/11 | A36, A57 | 6,6 | Xuất PDF baseline, tag; Weekly Log W10 (01/11); rà log work, truy vết | |

---

## 1. Giao việc Sprint 6–7

**Chuẩn bị trước khi gửi (hôm nay 22/10).** Mỗi file của TV2–TV5 có bảng "Cần có trước khi bắt đầu"; các mục do bạn cung cấp gom ở đây.

| # | Việc | Vì sao | Ai chờ |
|---|---|---|---|
**Phương án tạm đến họp 25/10 (issue I03: nhóm không truy cập được GitLab tự host).**
- Tài liệu: file `.md` trong thư mục Drive `Sprint 6-7/`; sửa lại thì tải bản mới bằng Quản lý phiên bản của Drive (giữ cùng link, lịch sử); review bằng ý kiến trên chat. Bạn đưa vào repo sau họp.
- Code: git trên máy từng người, đẩy lên repo chung sau.
- CI, deploy, Merge Request: dời sang 26–28/10, sau khi họp chọn nền tảng (mục 18 họp A23).

| # | Việc | Vì sao | Ai chờ |
|---|---|---|---|
| 1 | Tạo thư mục Drive `Sprint 6-7/`, bên trong có 5 thư mục con: `A20`, `A22`, `A25`, `A28`, `A31`. Chia quyền (cách làm ở dưới) | TV2, TV3 nộp tài liệu, TV4 nộp ảnh chụp giao diện vào đây | TV2, TV3, TV4 |
| 2 | Kiểm cả 5 người là Editor của Sheet Master; Jira giao đúng người, ai cũng log work được | Mọi task đều cần | Tất cả |
| 3 | Kiểm Sheet: tab 6 có dòng REQ-01…09, 15, 21 và cột mã test; tab 7 dòng PD-02 có phần bổ sung 20/10; tab Risk Register có R04, R09, R17, R18, R20, R21 | TV2 điền tab 6; TV3 xác nhận tab 7; TV3, TV5 cập nhật rủi ro | TV2, TV3, TV5 |
| 4 | Hỏi nhóm ai có iPhone hoặc máy Android đời cũ cho TV3 mượn đo QR 23–24/10 | Spike cần ≥ 3 thiết bị | TV3 |
| 5 | Nhắc TV3: API contract tối thiểu phải lên Drive trước 23/10 (danh sách nội dung có trong file của TV3) | TV4 (A28) và TV2 (A31) chờ | TV4, TV2 |
| 6 | Ghi issue I03 lên Sheet và Weekly Log W9 (dòng dán sẵn: `docs/sheet-import/2-weekly-log-W9-I03.tsv`; nội dung issue ở `docs/task3/issues.md`) | Bằng chứng xử lý vấn đề (Task 3.4) | |
| 7 | Chuẩn bị mục 18 cho họp A23: chọn nơi chứa repo và CI, ai tạo, ai có quyền quản trị | A24 (găng) cần repo ngày 26/10 | TV5, TV4 |

**Cách chia quyền thư mục Drive (việc 1):**
1. Trên Google Drive, bấm chuột phải vào thư mục `Sprint 6-7`, chọn **Chia sẻ**.
2. Nhập email Google của TV2, TV3, TV4, TV5. Chọn vai trò **Người chỉnh sửa** (Editor), để họ tạo và sửa file, thêm comment.
3. Bỏ chọn gửi thông báo nếu không cần, rồi bấm **Gửi**. Thư mục con và file tạo bên trong sẽ có cùng quyền.
4. Nếu thư mục nằm trong thư mục chung của nhóm đã được chia sẻ sẵn thì bỏ qua bước này; chỉ cần kiểm mỗi người mở được.
5. Gửi link thư mục lên chat nhóm.

Chia quyền Sheet làm tương tự: bấm **Chia sẻ** ở góc phải Sheet, thêm email, chọn **Người chỉnh sửa**.

Mật khẩu, khóa, tài khoản demo chỉ trao đổi riêng, không gửi qua chat chung hay Jira.

1. Gửi mỗi người đúng một file trong thư mục này. Không cần gửi kèm file nào khác; mọi nội dung cần dùng đã chép vào file của từng người.
   - TV2: `TV2-Ngo-Thanh-Hung.md`
   - TV3: `TV3-Phan-Huy-Quang-Minh.md`
   - TV4: `TV4-Nguyen-Dac-Nghia.md`
   - TV5: `TV5-Ha-Cao-Duc-Minh.md`
2. Trên Jira, dán mục của task tương ứng vào phần mô tả của task: SCRUM-81 A22, SCRUM-82 A25, SCRUM-84 A20, SCRUM-88 A24, SCRUM-91 A26, SCRUM-92 A28, SCRUM-93 A31, SCRUM-94 A27. Task làm chung thì dán phần của từng người, mỗi phần có tiêu đề tên người.
3. Nhắn nhóm: đọc file, gửi ý kiến duyệt lên chat trước tối 24/10. Bước kỹ thuật do AI soạn được coi là giao chính thức sau khi TV3 (backend, database) và TV5 (repo, CI, deploy, QR) đồng ý.

---

## 2. A58 · Confirm scope-affecting points with client

*Đầu vào có sẵn: `4-tai-nguyen/A58/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Trước họp A23, có ý kiến của thầy (hoặc ghi rõ giả định còn mở) về hai điểm: phạm vi demo tại Progress Check 09/11, và kênh thông báo tối thiểu.

**Đầu vào:**
- Lịch Baseline V1.0, tính đến 09/11:
  - đã có: đăng nhập và phân quyền; tạo, duyệt, công bố sự kiện; đăng ký và hủy theo hạn 24 giờ, có giới hạn số chỗ; bản thử QR;
  - đang làm: waitlist và tự chuyển, xong 10/11;
  - **chưa có QR check-in hoàn chỉnh**: luồng chính có QR xong 23–24/11; UAT 01–05/12.
- Ý kiến thầy ngày 08/10: chỉ có một Progress Check; điểm nào ảnh hưởng đáng kể tới scope hoặc planning thì hỏi trước khi chốt (P05). Q14, Q19 bắt buộc có thông báo nhưng không nêu kênh.
- Đề xuất của nhóm (bạn chọn 21/10): thông báo trong ứng dụng là bắt buộc; email là Should.

**Các bước:**
1. Đọc lại email dưới đây, sửa câu chữ nếu cần. Kiểm các ngày: 25/10, 09/11, 10/11, 23–24/11, 01–05/12.
2. Gửi cho thầy Nguyễn Minh Tâm, ghi giờ gửi.
3. Thêm vào tab Client Log hai câu hỏi: A58-1 (phạm vi Progress Check), A58-2 (kênh thông báo). Ghi ngày giờ gửi, để trống cột trả lời.
4. Khi thầy trả lời:
   - ghi nguyên văn trả lời, giờ trả lời, tác động tới dự án;
   - chụp email, lưu lên Drive nhóm (ví dụ `A58-2026-10-xx-email-tra-loi.png`), ghi tên file vào cột Bằng chứng;
   - sửa tiêu chí CP4 trong `docs/task2/2.5-checkpoints.md` và báo cáo mục 2.5.
5. Nếu thầy đòi có QR check-in tại 09/11: báo nhóm, chạy lại lịch với thứ tự mới và đưa ra họp A23.
6. Nếu tối 24/10 chưa có trả lời:
   - ghi vào Client Log "chưa có trả lời tại thời điểm chốt baseline";
   - tại họp A23, ghi hai giả định còn mở: (1) Progress Check demo đến đăng ký, hủy, waitlist và spike QR; (2) thông báo trong ứng dụng là bắt buộc, email là Should.
7. Tab AI Log: cột "Nhóm đã kiểm tra" của dòng bản nháp email ghi "TV1 đã sửa và gửi ngày …".

**Nội dung email (AI hỗ trợ soạn 21/10; bạn sửa và tự gửi):**

> **Tiêu đề:** [CO3011 – Nhóm 9] Xin ý kiến về phạm vi Progress Check 09/11 và kênh thông báo
>
> Kính gửi thầy,
>
> Nhóm 9 (lớp L01) cảm ơn thầy đã phản hồi ngày 08/10. Nhóm dự kiến chốt Baseline V1.0 vào ngày 25/10. Theo P05, nhóm xin ý kiến thầy về hai điểm ảnh hưởng tới kế hoạch:
>
> 1. **Phạm vi tại Progress Check 09/11.** Theo lịch dự kiến sau khi cân đối thời gian của các thành viên, đến ngày 09/11 nhóm sẽ có: đăng nhập và phân quyền theo vai trò; tạo, duyệt, công bố sự kiện; đăng ký và hủy đăng ký theo hạn 24 giờ, có giới hạn số chỗ; danh sách chờ và tự chuyển người đang hoàn thiện (dự kiến xong 10/11); bản thử nghiệm quét QR. Điểm danh QR hoàn chỉnh (có nhập mã hoặc xác nhận thủ công) dự kiến xong 23–24/11; toàn bộ workflow gồm báo cáo và xuất file được nghiệm thu trong tuần 01–05/12.
>    Thầy có đồng ý phạm vi trên là đủ cho Progress Check không ạ? Nếu thầy cần thấy điểm danh chạy được tại Progress Check, nhóm sẽ sắp xếp lại thứ tự công việc hoặc cắt yêu cầu mức Should, Could theo thứ tự đã thống nhất (không bỏ workflow cốt lõi Q08), rồi báo lại thầy lịch điều chỉnh.
>
> 2. **Kênh thông báo tối thiểu.** Theo Q14 và Q19, hệ thống phải thông báo cho sinh viên khi được chuyển từ danh sách chờ và khi sự kiện đổi thời gian, địa điểm hoặc bị hủy. Nhóm đề xuất thông báo **trong ứng dụng** là mức bắt buộc của MVP; gửi **email** là mức Should, chỉ làm nếu còn thời gian. Thầy có đồng ý không ạ?
>
> Nếu đến ngày 24/10 nhóm chưa nhận được ý kiến, nhóm sẽ dùng hai phương án trên, ghi là giả định còn mở trong Baseline V1.0 và cập nhật khi thầy phản hồi.
>
> Nhóm xin cảm ơn thầy.
>
> Trân trọng,
> Nguyễn Đức Nghĩa (TV1), thay mặt Nhóm 9, lớp L01

**Hoàn thành khi:** Client Log có câu hỏi, giờ gửi, và trả lời hoặc ghi chú "chưa có trả lời, dùng giả định".

---

## 3. A23 · Approve Project Baseline V1.0 (15h Chủ nhật 25/10)

*Đầu vào có sẵn: `4-tai-nguyen/A23/` (xem `DAU-VAO.md`).*

**Mục tiêu:** Cả nhóm xác nhận Baseline V1.0, bạn ký; có biên bản; sau họp xuất PDF và gắn tag để baseline không bị sửa.

**Điều kiện trước họp (hạn tối 24/10):**

| # | Việc | Ai | Trạng thái 22/10 |
|---|---|---|---|
| 1 | Lịch, Gantt, cost baseline, san tải | TV1 | Xong 20–21/10 |
| 2 | Quality plan v0.2 (A22) trên Drive, có quy ước mã test thống nhất | TV2 làm, TV1 duyệt | Lịch xong 22/10 |
| 3 | TV3 xác nhận phần bổ sung thiết kế database; API contract trên Drive | TV3 | Jira In Review 21/10 |
| 4 | Email A58 đã gửi, đã ghi Client Log | TV1 | Chưa gửi |
| 5 | Ba bảng dán Sheet (Activity, Weekly Log W9–W10, AI Log) | TV1 | Đã dán |
| 6 | Giờ hồi tưởng đến 20/10 của cả nhóm (hạn 23/10) | Cả nhóm | Đang thu |
| 7 | TV2–TV5 đã đọc file của mình, gửi ý kiến duyệt lên chat | TV2–TV5 | Gửi 22/10 |
| 8 | Biên dịch lại báo cáo (`latexmk -pdf main.tex` trong `report/`) | TV1 | Đã biên dịch 21/10 |

**Các mục nhóm xác nhận tại họp.** Ghi từng dòng: Đồng ý / Sửa (ghi nội dung) / Không đồng ý (lý do, ai xử lý, hạn).

| # | Mục | Nội dung |
|---|---|---|
| 1 | L8 | Làm gối đầu Increment 1: A24, A28, A31 bắt đầu sau A25; A26 sau A24; A27 chờ A23 |
| 2 | L9 | TV1 là owner và người duyệt; TV2 làm thay khoảng 19h (A22 6h, A43 5,2h, phần chất lượng A45 5h, A42 3h); TV5 làm chung A34 với TV3; TV4 làm chung A39 với TV2 |
| 3 | L10 | Việc đóng dự án bắt đầu sớm: A42 sau A51; A43, A45 sau A30; A44 sau A39; A46, A47, A54 theo mạng activity |
| 4 | L11 | A32 (lập kế hoạch Increment 2) sau A62, song song A30 |
| 5 | REQ-21 | Giữ REQ-21 (sửa, hủy sự kiện đã công bố; Should); nếu A27 trễ quá 1 ngày so với 04/11 thì TV1 xem xét cắt (khoảng 8h, 1–2 ngày) |
| 6 | Năng lực | 14h/tuần mỗi người, cao điểm 16h |
| 7 | Estimate | Giữ số PM chốt 20/10; implement và test còn ý kiến trái chiều, theo dõi qua R02 và Time Tracking; chưa có ước lượng chéo độc lập (báo cáo ghi trung thực) |
| 8 | Cost baseline | 364,2 person-hours + quỹ dự phòng A38 30h = 394,2 person-hours |
| 9 | Lịch và mốc | A23 25/10; CP3 11–16/11 (trễ 15 ngày so với 01/11); Progress Check 09/11 chưa có QR check-in; luồng chính có QR 23–24/11; UAT 01–05/12 (trễ 11 ngày); nộp bài 06–07/12; 0 ngày dự trữ trước demo 07/12 |
| 10 | Đường găng | A24 → A26 → A27 → A29 → A62 → A32 → A35 → A37 → A39 → A53 → A41 → A47 → A54 |
| 11 | CP4 | Theo trả lời A58; chưa có thì giả định demo đến đăng ký, hủy, waitlist và spike QR |
| 12 | Thông báo | Trong ứng dụng là bắt buộc, email là Should (chờ A58) |
| 13 | A38 | Quỹ 30h ngoài chuỗi, dùng giờ dư TV2–TV5; nếu change event rơi vào chuỗi găng thì cắt Could rồi Should, hoặc lập Baseline V2.0 |
| 14 | Rủi ro | R15 (lịch vượt mốc) đã cập nhật 21/10; mọi rủi ro cấp activity có owner |
| 15 | Truy vết | Objective → Product → Activity → Resource → Risk → Test → Checkpoint không mâu thuẫn giữa báo cáo, Sheet, repo |
| 16 | Task Increment 1 | TV2–TV5 đã duyệt phần của mình (ý kiến trên chat) |
| 17 | Chia giờ A26, A24 | V0 (giữ lịch): A26 chia đều 3 người, chờ TV4 xong A24 ngày 28/10, TV3, TV5 trống 24–28/10. V1: A26 theo đề xuất TV3 14/10 (TV3 5,5h, TV5 5h, TV4 0h; màn hình đăng nhập do TV5 làm hoặc gộp vào A28), nộp bài xong 06/12, dự trữ 1 ngày. V2: V1 cộng A24 TV5 6,9h, TV4 2h (khung React), xong 05/12, dự trữ 2 ngày. Mô hình chạy thử 22/10 (AI hỗ trợ). Nhóm chọn |
| 18 | Repo và CI (I03) | GitLab tự host trên máy cá nhân, nhóm không truy cập được. Chọn nơi chứa repo chung (cũng là bản công khai gửi thầy) và nơi chạy CI; ai tạo, ai quản trị. A24 (găng) cần repo ngày 26/10. Nếu đổi khỏi Jenkins: ghi đính chính quyết định "CI dùng Jenkins" (21/10), viết lại kiểm tra `Baseline frozen` cho nền tảng mới. Sau họp: TV1 đưa bộ khởi tạo `docs/` (quét secret, không đưa `Link.txt`, file `.xlsx`) và tài liệu trên Drive vào repo |

Không chốt nếu mục 8, 9, 15 hoặc 18 chưa được đồng ý. Mục khác không đạt: sửa ngay trong họp, hoặc chốt có điều kiện kèm hạn.

**Biên bản:** ghi vào tab Biên bản CP, mục CP2 (bổ sung cho biên bản 18/10). Nội dung: ngày giờ, người dự, kết quả từng mục, mục đã sửa, hành động kèm người và hạn, kết luận (đạt / đạt có điều kiện), TV1 ký.

**Sau họp:**
1. Sửa trạng thái từ "chờ nhóm xác nhận tại A23" thành "nhóm xác nhận tại A23 ngày 25/10", ghi kèm mục nào đã sửa trong họp:
   - trong repo: `docs/task2/2.4`, `2.5`, `2.6`, `2.10`, `2.11`, `docs/baseline/README.md`;
   - trong báo cáo: mục 2.4, 2.5, 2.6, 2.10, 2.11, 2.12, và ngày chốt ở Phụ lục C.
2. Nếu nhóm chọn V1 hoặc V2: tạo config mới trong `tools/schedule/` (không sửa config V1.0), chạy lại lịch, cập nhật ngày trên Jira và các file giao việc.
3. Biên dịch báo cáo, chép `report/main.pdf` thành `docs/baseline/v1.0.pdf` (hoặc chỉ chương 1–2 và Phụ lục C; bạn quyết).
4. Trong repo chung họp chọn (mục 18): tạo nhánh, đưa các file đã sửa và `v1.0.pdf` vào. Mở **một Merge Request (hoặc Pull Request) riêng** cho `v1.0.pdf`. Kiểm tra `Baseline frozen` chỉ chặn sửa hoặc xóa file `v*.pdf` đã có, nên thêm `v1.0.pdf` lần đầu không bị chặn. Repo chưa sẵn sàng thì lưu `v1.0.pdf` lên Drive kèm ngày, gắn tag khi có repo.
5. Sau khi merge, gắn tag:
   ```bash
   git tag -a baseline-v1.0 -m "Baseline V1.0 approved 25/10/2026"
   git push origin baseline-v1.0
   ```

**Hoàn thành khi:** mục 8, 9, 15, 18 được đồng ý; bạn đã ký; `v1.0.pdf` đã lưu; tag đã đẩy lên repo chung khi có.

---

## 4. A36, A57 · Theo dõi tiến độ, rà truy vết

**Mục tiêu:** Weekly Log đúng hạn và truy vết nhất quán, làm bằng chứng quản lý cho Task 3.

**Các bước:**
1. **Chủ nhật 25/10 (sau họp):** chốt Weekly Log W9 trên tab 2:
   - công việc kế hoạch và thực tế;
   - effort kế hoạch và thực tế, độ lệch;
   - hành động quản lý: chốt Baseline V1.0, gửi A58;
   - issue và rủi ro thay đổi.

   Cột "Người cập nhật" ghi người thực sự cập nhật.
2. **Chủ nhật 01/11 (họp định kỳ):**
   - xuất Jira CSV (all fields, có cột Log Work), chuyển thành dòng tab 3 Time Tracking;
   - so thực tế với kế hoạch: A24 8,9h, A28 10,5h, A31 10,5h, A20 5,7h, A26 10,5h;
   - task găng lệch trên 20%: ghi deviation và hành động;
   - chốt Weekly Log W10.
3. **Trước mỗi checkpoint và sau mỗi thay đổi kế hoạch:** rà chuỗi Objective → Product → Activity → Resource → Risk → Test → Checkpoint giữa báo cáo, Sheet và repo. Ví dụ: `docs/traceability.md` cũ còn mã T-RG, đúng là T-REG.
4. Ghi AI Log cho mọi lần dùng AI trong tuần.
