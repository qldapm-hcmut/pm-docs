# Bằng chứng chất lượng (Task 3.5)

| Thư mục / file | Nội dung |
|---|---|
| `test-cases.md` | Bộ test case có mã, gắn requirement |
| `results/` | Kết quả chạy test theo mốc: `cp3-YYYY-MM-DD.md`, export JUnit từ CI |
| `defects.md` | Danh sách defect, mức độ, trạng thái |
| `uat/` | Kịch bản và biên bản UAT |

**Log CI có thể bị xoay vòng.** Trước mỗi checkpoint: tải artifact `evidence/` của build tương ứng và commit vào `results/`, ghi số build và commit hash.
