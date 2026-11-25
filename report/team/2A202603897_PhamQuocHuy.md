# Báo cáo cá nhân — Phạm Quốc Huy - 2A202603897

## 1. Thông tin thành viên

- Họ tên: Phạm Quốc Huy
- MSSV: 2A202603897
- Email: huymix2k4@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code 1 (Nhiệm vụ A, B) → Người kiểm số 2 (Nhiệm vụ D, E) kiêm QA kỹ thuật

## 2. Phần việc phụ trách

- Thiết lập môi trường ảo Python (`.venv`) và cài đặt các hàm tính toán cho Nhiệm vụ A (A1–A4) và Nhiệm vụ B (B1–B4) trong `src/lab13.py`.
- Chuyển vai sau giờ giải lao sang Người kiểm số 2: tính tay đối chiếu độc lập các câu cỡ mẫu D1 (a–e), tỉ lệ mở lại an toàn và 3 chỉ số E1 do TV2 lập trình.
- Thực hiện QA kỹ thuật trên toàn bộ kho lưu trữ trước Gate 2a (kiểm thử thực thi `lab13.py`, cú pháp `pilot_plan.yaml`, rà soát nhãn `simulated`, dấu `?` và các từ khoá bị cấm theo quy tắc lab).

## 3. Đóng góp cụ thể

- Viết 3 hàm xác suất chạy lại ở A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), vượt qua cả 3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`).
- Xây dựng hàm tổng quát `mo_hinh()` trong `src/lab13.py` tính chi phí từ trace cho toàn mẫu 1.200 yêu cầu (A2), tách theo 4 loại yêu cầu kèm bảng tỉ lệ `ok` theo `attempt` (A3), tính phân bổ chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang` (A4).
- Lập trình trong `src/lab13.py` cho 9 kịch bản độ nhạy đơn lẻ (B1), kịch bản cặp tuyến tính và xếp hạng 3 yếu tố nhạy nhất (B2), so sánh chi phí toàn hệ thống khi giới hạn 1–2–3 lần chạy (B3), và tính chi phí + điểm hoà vốn khi xem lại 100% (B4).
- Tính tay kiểm chứng độc lập kết quả D1 & E1 của TV2: kiểm tra `DE = 1 + 74 × 0,02 = 2,48` (`3.103` YC/nhóm → `42` NV/nhóm), trần `c / ICC` (`1.000` với 20 NV, `300` với 6 depot), giải bất phương trình `20m / (1 + 0,02(m - 1)) ≥ 859 ⇔ 2,82m ≥ 841,82 ⇒ m ≥ 299` (`DE = 6,96`), và kiểm đếm 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`).
- Chạy bộ lệnh QA xác nhận `yaml.safe_load` đọc thành công `report/team/pilot_plan.yaml`, sạch dấu `?` ngoài chú thích và không vi phạm quy tắc từ ngữ cấm trong toàn bộ hồ sơ.

## 4. Bằng chứng

- Commit code Nhiệm vụ A & B: `bc6cffb` (`src/lab13.py`, dòng 16–85 và 108–210) và commit điều phối `243b27e`.
- Kết quả chạy `src/lab13.py` do tôi cài đặt:
  - A2: Token `245.585 đ`, Tool `84.000 đ` (lần chạy 2 & 3: `93.804 đ`), Xem lại `1.780.000 đ` (`simulated`), Làm lại `2.264.000 đ` (`simulated`), Tổng `4.373.585 đ`, `978` việc thành công → CPS `4.472 đ` (`simulated`, gấp `16,3×` hoá đơn `274,7 đ`); cả hệ thống `5.865 đ/YC` (`0,49×` mức `12.000 đ`, `simulated`).
  - A3 & A4: `noi_dia` `2.696 đ` (`0,22×`), `hang_nang` `8.221 đ` (`0,69×`), `quoc_te` `22.515 đ` (`1,88×`), `doi_tac` `10.215 đ` (`0,85×`); cộng cố định phạm vi pilot đạt `4.599 đ` (`0,38×`) ở `45.000 YC/tháng` và `5.784 đ` (`0,48×`) ở nửa khối lượng (`simulated`).
  - B1–B4: Làm lại `×2` lên `6.787 đ` (`+51,8%`), Xem lại `×2` lên `6.292 đ` (`+40,7%`), Cặp B2 `6.543 đ` (`+46,3%`), Giới hạn 2 lần rẻ nhất toàn hệ thống (`6.901.220 đ`), Xem lại 100% tốn `11.743 đ` (`0,98×` với 9 phút) hoặc `12.415 đ` (`1,03×` với 15,3 phút) (`simulated`).
- Bằng chứng kiểm số D1 & QA: Đối chiếu khớp 100% với commit `b746be4` (`src/lab13.py` dòng 89–106, 212–252) và xác thực `report/team/pilot_plan.yaml` hợp lệ.

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity (Gemini) hỗ trợ giải thích bản chất công thức Cost-of-Pass, gợi ý cấu trúc hàm `mo_hinh()` trong `src/lab13.py` và viết lệnh PowerShell kiểm tra cú pháp YAML / rà soát quy định định dạng.
- Cách tự kiểm tra: Chạy trực tiếp `python lab13.py` trên dữ liệu `logix_runs.csv` và `logix_requests.csv` (`keep_default_na=False`), kiểm tra 3 assert ở A1 đạt sai số `< 1e-9`, kiểm chứng tính tuyến tính ở B1/B2 (mức giảm nửa bằng đúng nửa mức tăng gấp đôi; tác động cặp `+46,3% = +5,6% + 40,7%`), và tự giải tay bất phương trình cỡ mẫu cụm D1e để đối chiếu chéo.

## 6. Tự đánh giá

- Đã hoàn thành đầy đủ và đúng hạn vai trò Người viết code 1 ở Giai đoạn 1 (Nhiệm vụ A, B), bàn giao code rõ ràng cho TV2 phát triển tiếp phần D, E, đồng thời thực hiện nghiêm túc vai trò Kiểm số D/E và QA kỹ thuật toàn bộ hồ sơ trước phiên duyệt chéo Gate 2a.
