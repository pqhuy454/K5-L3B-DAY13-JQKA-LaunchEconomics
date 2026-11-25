# Team

## Thông tin nhóm

- Tên nhóm: JQKA
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-JQKA-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/pqhuy454/K5-L3B-DAY13-JQKA-LaunchEconomics` · nhánh `main` · commit chốt: *(cập nhật sau commit cuối)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Phạm Quốc Huy | 2A202603897 | huymix2k4@gmail.com | pqhuy454 | Viết code A/B → kiểm số D/E, QA kỹ thuật |
| 2 | Nguyễn Thành Tâm | 2A202603933 | ngthanhtamtb@gmail.com | ngthanhtamtb | Kiểm số A/B → viết code D/E |
| 3 | Trịnh Gia Huy | 2A202603924 | trgyahuy1710@gmail.com | TrGiaHuy1710-valid | Gắn nhãn 1, điều phối, event và báo cáo nhóm |
| 4 | Đặng Đức Minh | 2A202603886 | ddminh1102@gmail.com | DMinh1102 | Gắn nhãn 2, giữ hồ sơ launch, chủ trì Gate 2a |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Phân công và bằng chứng TV4

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Nguyễn Thành Tâm - 2A202603933

### Phần việc phụ trách

- **Giai đoạn 1 (CP1–CP2 — Người kiểm số 1):** Tính tay kiểm số độc lập cho các bảng A1–A4, B1–B4 để đối chiếu với code của TV1; trực tiếp điền bảng số liệu, gắn nhãn `simulated` và viết các câu trả lời nhận xét trong [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md).
- **Giai đoạn 2 (CP4–CP5 — Người viết code 2):** Viết tiếp vào [src/lab13.py](src/lab13.py) phần tính 5 câu cỡ mẫu D1 (`NormalDist` / `statsmodels`), tính `power` thực tế ở mức +5 điểm khi chọn `mde = 0.06` (`0,64`), tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu, `3,97%` phạm vi) và tính thử 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`); điền lời giải chú thích D1–D2 và các trường thông số kỹ thuật vào [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml).

### Đóng góp cụ thể

- Tính tay kiểm chứng các bẫy kinh tế ở A2 (gấp `16,3 lần` hoá đơn token `274,7 đ`; chi phí cả hệ thống `5.865 đ/YC = 0,49×`), A3 (loại `quoc_te` `22.515 đ = 1,88×` và `doi_tac` `10.215 đ = 0,85×`), A4 (cố định `1.185 đ/việc` → `4.599 đ = 0,38×` ở `45.000 YC/tháng`), tính tuyến tính B1–B2 (`+46,3%`), giới hạn 2 lần chạy rẻ nhất toàn hệ thống ở B3 (`6.901.220 đ`), và chi phí xem lại 100% ở B4 (`11.743 đ = 0,98×` với 9 phút; `12.414,79 đ ≈ 12.414–12.415 đ = 1,03×` với 15,3 phút làm lại) (`simulated`).
- Lập trình các hàm `co_mau()`, `he_so_thiet_ke()`, `co_mau_hieu_dung_toi_da()` và đoạn script in kết quả D1 (`1.251`, `3.103`, `1.000`, `300`, `m >= 299` với `DE = 6,96`, `power = 0,64`) cùng 3 chỉ số E1 ở cuối [src/lab13.py](src/lab13.py).
- Điền hoàn chỉnh phần giải thích D1, D2, đánh đổi MDE 6 điểm và các trường cấu hình kỹ thuật trong [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml), gộp (rebase) cùng bộ luật dừng của TV3 và xác thực `yaml.safe_load` hợp lệ.

### Bằng chứng

- Commit `1157ccd`: hoàn thiện toàn bộ bảng và câu trả lời A1–A4, B1–B4 trong [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md).
- Commit `b746be4`: viết code D1, E1 trong [src/lab13.py](src/lab13.py) (dòng 89–106, 212–252) và cập nhật D1, D2 cùng thông số kỹ thuật trong [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml).
- Báo cáo cá nhân: [report/team/2A202603933_NguyenThanhTam.md](report/team/2A202603933_NguyenThanhTam.md).

## HoVaTen-MSSV

### Phần việc phụ trách

-

### Đóng góp cụ thể

-

### Bằng chứng

-
