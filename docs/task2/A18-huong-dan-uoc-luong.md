---
Activity: A18
Chủ sở hữu: TV1 (gửi), TV3 (tổng hợp)
Phiên bản: 0.1
Cập nhật: 12/10/2026
Trạng thái: sẵn sàng gửi (hạn chót tối 14/10/2026)
---

# A18 — Hướng dẫn ước lượng effort từ dưới lên

Bản này để gửi nhóm. Kết quả điền vào Sheet master, tab **Estimates**; khung bảng ở [2.6-estimates.md](2.6-estimates.md).

## Tin nhắn gửi nhóm

> **A18 — ước lượng effort (hạn: tối 14/10).**
> A17 đã có bản nháp (2.4, 2.5 trong repo); TV2 kiểm giúp mình. Mạng đã chỉnh 4 điểm (PM chốt 12–13/10): tách A29 thành A29 + A62 (danh sách chờ); A53 gộp việc triển khai; **A34 làm gối đầu A33** (bắt đầu sau A25 và A32 trên schema dữ liệu, tích hợp ở A39; **TV3 xác nhận khả thi**); **A38 là quỹ dự phòng 30h không nằm trong chuỗi phụ thuộc**. Số ước lượng của các bạn quyết định lịch có kịp Progress Check 09/11 không (xem "Ghi chú nguồn quyết định" trong 2.4). Hãy ước lượng elapsed thật cho A33 và A34; TV3 cho biết A34 có bắt đầu được ngay sau A25 không.
> Việc cần làm, mỗi người **độc lập**:
> 1. Mở tab Estimates, ước lượng 3 điểm (O/M/P, giờ người) cho activity của mình, kèm số ngày lịch (elapsed). **Chưa xem số của nhau và chưa xem số effort trong trang plan.**
> 2. Ước lượng độc lập lại cho người kế tiếp theo vòng: TV1→TV2→TV3→TV4→TV5→TV1.
> 3. Lệch >50% thì hai người giải thích và thống nhất, ghi lý do.
> 4. Ghi giả định năng lực nếu khác E01/E02 (lịch thi, tuần nghỉ).
> 5. Ghi thời gian bạn bỏ ra vào Jira worklog hoặc tab Time Tracking.
> TV3 tổng hợp PERT sau khi mọi người xong.

## Giả định nền (E01–E05)

| Mã | Giả định |
|---|---|
| E01 | TV2–TV5 ~12h/tuần (cao điểm ~16h); TV1 ~7h/tuần |
| E02 | Tuần nghỉ 12–18/10 ~6h/người |
| E03 | Không tính thời gian học lý thuyết |
| E04 | Không quy đổi VND: chi phí nhân công tính bằng person-hours |
| E05 | Dùng thư viện có sẵn, không tự xây component |

## Cách ước lượng

- **O** lạc quan, **M** khả dĩ nhất, **P** bi quan, tính theo giờ người. `E = (O + 4M + P) / 6`.
- **Elapsed**: số ngày lịch từ lúc bắt đầu đến lúc xong, có tính giờ rảnh của chính bạn.
- Activity có nhiều owner: ước lượng tổng giờ của cả nhóm cho activity đó, ghi rõ bạn chiếm bao nhiêu.
- Phản hồi của thầy 08/10 thêm yêu cầu: sửa/hủy sự kiện đã công bố và thông báo người đã đăng ký (Q19, ảnh hưởng **A27**, **A29**); notification khi chuyển từ waitlist (Q14, **A62**). Hãy tính vào ước lượng; số nháp trong plan chưa tính đủ.
- Activity mới cần ước lượng lại do chỉnh mạng: **A29** (chỉ đăng ký, hủy), **A62** (danh sách chờ), **A53** (sửa lỗi và triển khai). Số trong plan chỉ là nháp, đừng dùng làm mốc.

## Vòng ước lượng chéo

| Người ước lượng lại | Cho activity của |
|---|---|
| TV1 | TV2 |
| TV2 | TV3 |
| TV3 | TV4 |
| TV4 | TV5 |
| TV5 | TV1 |

## Bàn giao

- Mỗi người: điền Estimates xong → báo trong chat.
- TV3: tổng hợp PERT, xử lý chỗ lệch, bàn giao bảng cho A21 (lịch, Gantt).
- TV1: duyệt tổng effort so với năng lực (E01/E02) và quyết định cách thu hồi lịch (A33 + A34).
