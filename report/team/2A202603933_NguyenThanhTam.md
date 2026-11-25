# Báo cáo cá nhân — Nguyễn Thành Tâm - 2A202603933

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thành Tâm
- MSSV: 2A202603933
- Email: ngthanhtamtb@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người kiểm số 1 (Nhiệm vụ A, B) → Người viết code 2 (Nhiệm vụ D, E)

## 2. Phần việc phụ trách

- Thực hiện vai trò **Người kiểm số 1** ở Giai đoạn 1 (CP1 & CP2): tính tay đối chiếu độc lập các phép tính mẫu ở từng bảng A1–A4, B1–B4 để kiểm chứng code của TV1, điền số liệu chuẩn, gắn nhãn `simulated` và viết các câu trả lời nhận xét vào `report/team/bang_chi_phi.md`.
- Chuyển vai sau giờ giải lao sang **Người viết code 2** ở Giai đoạn 2 (CP4 & CP5): lập trình tiếp vào `src/lab13.py` phần tính 5 câu cỡ mẫu D1, hệ số thiết kế `DE`, giới hạn cỡ mẫu hiệu dụng `c / ICC`, `power` thực tế ở mức +5 điểm khi chọn `mde = 0.06`, tỉ lệ `mo_lai_trong_7_ngay` hiện tại và tính thử 3 chỉ số E1.
- Điền lời giải D1 (a–e), D2 (1–5), đánh đổi đã chấp nhận và các trường thông số kỹ thuật (`owner`, `scope`, `assignment`, `rollout`, `primary_metric`, `identifiability`, `interim_looks`, `rollback`, `decision_date`, `simulated_inputs`) vào `report/team/pilot_plan.yaml`.

## 3. Đóng góp cụ thể

- Tính tay kiểm chứng toàn bộ bảng chi phí A1–A4 và bảng độ nhạy B1–B4:
  - Kiểm tra 3 phép thử A1 với `p = 0,8`: `E[chạy, k=2] = (1 - 0,2²) / 0,8 = 1,20`; `E[chạy, k=∞] = 1 / 0,8 = 1,25`; hệ số CPS `= 1 / p = 1,25`.
  - Kiểm tra A2 trên 1.200 yêu cầu (1.624 lần chạy): hoá đơn kỹ thuật `(245.585 + 84.000) / 1.200 = 274,7 đ/YC`; cộng nhân công xem lại (`1.780.000 đ`, `simulated`) và làm lại (`2.264.000 đ`, `simulated`) ra tổng `4.373.585 đ`, chia `978` việc thành công đạt CPS `4.472 đ` (`simulated`, gấp `16,3 lần` hoá đơn); chi phí cả hệ thống `(4.373.585 + 222 × 12.000) / 1.200 = 5.865 đ/YC` (`0,49×` của `12.000 đ`, `simulated`).
  - Kiểm tra A3 & A4: xác nhận `quoc_te` tốn `22.515 đ/việc` (`1,88×`, `simulated`, thành công `27,3%`) không đáng chạy; phân bổ chi phí cố định `40 triệu đ/tháng` cho phạm vi `noi_dia + hang_nang` (`33.750` việc/tháng ở quy mô `45.000 YC/tháng`) là `1.185 đ/việc`, nâng CPS lên `4.599 đ` (`0,38×`, `simulated`) và `5.784 đ` (`0,48×`, `simulated`) ở một nửa khối lượng.
  - Kiểm tra tính tuyến tính B1–B2 (`+5,6% + 40,7% = +46,3%`, `6.543 đ`), chi phí cả hệ thống B3 (giới hạn 2 lần chạy rẻ nhất: `4.093.220 + 234 × 12.000 = 6.901.220 đ`, `simulated`), và kịch bản xem lại 100% ở B4 (`11.743 đ = 0,98×` với 9 phút làm lại; `11.173.313,27 / 900 = 12.414,79 đ ≈ 12.414–12.415 đ = 1,03×` với 15,3 phút làm lại, `simulated`).
- Biên soạn đầy đủ bảng số liệu và câu trả lời (đảm bảo `≤ 3 dòng/câu`, có số liệu và đủ nhãn `simulated`) trong `report/team/bang_chi_phi.md`.
- Viết các hàm `co_mau()`, `he_so_thiet_ke()`, `co_mau_hieu_dung_toi_da()` và khối lệnh tính D1, E1 ở cuối `src/lab13.py` (dùng `NormalDist`, `proportion_effectsize`, `NormalIndPower`).
- Hoàn thiện phần chú thích D1–D2 và cấu hình kỹ thuật trong `report/team/pilot_plan.yaml`, đồng bộ (rebase) với bộ 4 luật dừng của TV3 và kiểm tra đạt `yaml.safe_load`.

## 4. Bằng chứng

- Commit hoàn thiện bảng chi phí CP1–CP2: `1157ccd` (`docs(cp1-cp2): TV2 kiểm số và hoàn thiện bảng chi phí A1-A4, B1-B4` — file `report/team/bang_chi_phi.md`).
- Commit code D1, E1 và kế hoạch pilot CP4–CP5: `b746be4` (`cp4,5: Viết tiếp lab13.py, Điền D1, D2` — file `src/lab13.py` dòng 89–106, 212–252 và `report/team/pilot_plan.yaml`).
- Các con số D1 & E1 do code của tôi tính và in ra từ `src/lab13.py`:
  - D1a (chia theo yêu cầu, `+5 điểm`): `1.251` yêu cầu/nhóm.
  - D1b (theo nhân viên, `m = 75`, `DE = 2,48`): `3.103` yêu cầu/nhóm (~`42` NV/nhóm, tổng `84 > 40` → không đủ người).
  - D1c (20 NV/nhóm): trần hiệu dụng `c / ICC = 20 / 0,02 = 1.000 < 1.251` → không đạt cho `+5 điểm`.
  - D1d (6 depot/nhóm): trần hiệu dụng `6 / 0,02 = 300 < 1.251` → không đạt.
  - D1e (`+6 điểm`, `859` YC/nhóm, 20 NV/nhóm): cần `m ≥ 299` YC/nhân viên (`DE = 6,96`); `power` thực tế ở mức `+5 điểm` giảm còn `0,64`.
  - Tỉ lệ `mo_lai_trong_7_ngay` hiện tại: `4,25%` (`51/1.200` toàn mẫu) và `3,97%` (`39/982` trong `noi_dia + hang_nang`).
  - Ba chỉ số E1: Chỉ số chính `82,83%` (`994/1.200`), Chỉ số dùng `27,12%` (`48/177`), Chỉ số an toàn `4,25%` (`51/1.200`).

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity (Gemini) hỗ trợ kiểm tra nhanh công thức cỡ mẫu 2 tỉ lệ độc lập, cú pháp `NormalIndPower().power()` của `statsmodels` và rà soát quy định định dạng file Markdown/YAML.
- Cách tự kiểm tra: Tự tính tay đối chiếu từng công thức mẫu ở A1–A4, B1–B4 và giải tay bất phương trình `20m / (1 + 0,02(m - 1)) ≥ 859` để kiểm chứng kết quả `m ≥ 299`; chạy trực tiếp `python lab13.py` trong `src/` và kiểm tra `yaml.safe_load(open('../report/team/pilot_plan.yaml'))` cùng lệnh `grep` quét sạch dấu `?` và từ ngữ bị cấm theo quy tắc lab.

## 6. Tự đánh giá

- Đã hoàn thành đầy đủ, chính xác và đúng tiến độ cả hai vai trò được phân công trong nhóm: kiểm số độc lập & hoàn thiện `report/team/bang_chi_phi.md` ở Giai đoạn 1, và trực tiếp viết code D1, E1 trong `src/lab13.py` cùng cấu hình kỹ thuật `report/team/pilot_plan.yaml` ở Giai đoạn 2.
