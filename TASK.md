# PHÂN CÔNG CÔNG VIỆC NHÓM 4 NGƯỜI (TASK ALLOCATION)
**Dự án:** Lab 13 — Định giá Agent & Lập kế hoạch Pilot (LogiX-VN, Gate 2a)  
**Nhóm:** `JQKA` · **Lớp:** `L3B` · **Repo:** `K5-L3B-DAY13-JQKA-LaunchEconomics`

> Phân công này bám sát quy định tổ chức nhóm 4 người của Lab 13 (`TEAM.md` & `CHECKPOINTS.md`), bao gồm quy tắc **hoán đổi người viết code sau giờ giải lao** (để ít nhất 2 thành viên trực tiếp code và tính được mô hình) và **gắn nhãn độc lập 2 người ở Nhiệm vụ C**.

---

## 1. Bảng Định danh 4 Vai trò Chính

| Mã TV | Họ tên & MSSV | Vai trò Giai đoạn 1 (CP1–CP2: Trước giải lao) | Vai trò Giai đoạn 2 (CP3–CP5: Sau giải lao) | File phụ trách chính |
| :---: | --- | --- | --- | --- |
| **TV1** | *Phạm Quốc Huy* | **Người viết code 1** (`src/lab13.py`: A1, A2, A3, A4, B1–B4) | **Người kiểm số 2 & Kỹ thuật QA** (Kiểm số D1, E1; kiểm định YAML & script cuối buổi) | `src/lab13.py` (phần A, B), đồng phụ trách `bang_chi_phi.md` |
| **TV2** | *Nguyễn Thành Tâm* | **Người kiểm số 1** (Tính tay đối chiếu A1–A4, B3–B4; điền bảng & câu trả lời `bang_chi_phi.md`) | **Người viết code 2** (`src/lab13.py`: D1 cỡ mẫu, E1 chỉ số; điền số kỹ thuật `pilot_plan.yaml`) | `report/team/bang_chi_phi.md`, `src/lab13.py` (phần D, E), `pilot_plan.yaml` |
| **TV3** | *Trịnh Gia Huy* | **Người gắn nhãn 1 & Điều phối chất lượng ("Xong khi")** (Canh giờ, soát quy tắc lab cho A & B) | **Người gắn nhãn 1 & Thiết kế Vận hành/Event** (Gắn nhãn 20 ca; soạn `stop_rules` D3, events E1, `group_report.md`) | `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/group_report.md` |
| **TV4** | *Đặng Đức Minh* | **Người gắn nhãn 2 kiêm Giữ Hồ sơ Launch** (Khởi tạo `TEAM.md`, điền cuốn chiếu mục 1–3 vào `ho_so_launch_v0.md`) | **Người gắn nhãn 2 & Chủ trì Gate 2a** (Gắn nhãn 20 ca; chốt `ho_so_launch_v0.md` 7 mục + đề xuất; trình bày & ghi `phieu_cham.md`) | `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/phieu_cham.md`, `TEAM.md` |

---

## 2. Chi tiết Công việc của Từng Thành viên

### 👤 Thành viên 1 (TV1): Người viết code 1 → Người kiểm số 2
1. **Khởi tạo & Nhiệm vụ A (CP1):**
   - Cài đặt `.venv` trong `src/`, cài `requirements.txt`, kiểm tra môi trường.
   - Viết 3 hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`) trong `src/lab13.py`, đảm bảo pass `kiem_tra_dap_an_biet_truoc()` (`1,20 · 1,25 · 1,25`).
   - Viết hàm tổng quát `mo_hinh(runs, reqs, ...)` cho A2, chạy vòng lặp tách theo `loai` cho A3 (kèm phân tích tỉ lệ `ok` theo `attempt` 1, 2, 3) và tính chi phí cố định A4.
2. **Nhiệm vụ B (CP2 + 8 phút đầu CP3):**
   - Viết code trong `src/lab13.py` chạy 9 kịch bản đơn lẻ (B1), kịch bản cặp (B2), chi phí cả hệ thống ở giới hạn 1–2–3 lần chạy (B3), và kịch bản xem lại 100% cho `noi_dia + hang_nang` (B4).
   - Bàn giao code sạch và giải thích cấu trúc `lab13.py` cho **TV2** vào giờ giải lao.
3. **Nhiệm vụ D & E (CP4–CP5 — Vai Kiểm số & QA kỹ thuật):**
   - Tính tay công thức cỡ mẫu, hệ số thiết kế `DE = 1 + (m - 1) * ICC` và bất phương trình câu D1e (`m >= 299`) để đối chiếu độc lập với code của TV2.
   - Chạy bộ lệnh kiểm tra cuối cùng: `python lab13.py`, `yaml.safe_load` cho `pilot_plan.yaml`, quét dấu `?` còn sót và quét từ cấm `"production"`.
4. **Cá nhân:** Tạo `report/team/<MSSV_TV1>_<HoTen>.md` và điền mục đóng góp của TV1 trong `TEAM.md`.

---

### 👤 Thành viên 2 (TV2): Người kiểm số 1 → Người viết code 2
1. **Nhiệm vụ A & B (CP1–CP2 + 8 phút đầu CP3 — Vai Kiểm số):**
   - Tính tay ít nhất 1 phép tính mẫu ở mỗi bảng (A2, A3, A4, B3, B4) để kiểm chứng code của TV1 không dính bẫy (quên chia 1.000 token, quên cộng lần chạy lỗi, quên cộng `12.000 đ × ca không thành công`).
   - Trực tiếp điền số liệu chuẩn vào `report/team/bang_chi_phi.md`, gắn đầy đủ nhãn `simulated`, và viết các câu trả lời nhận xét (đảm bảo **≤ 3 dòng/câu** và **có ít nhất 1 con số**).
2. **Nhiệm vụ D & E (CP4–CP5 — Nhận vai Viết code):**
   - Viết tiếp vào `src/lab13.py` phần tính 5 câu cỡ mẫu D1 (`statsmodels` / `NormalDist`), tính `power` thực tế ở mức 5 điểm khi chọn `mde = 0.06` (`~0,64`), tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%`), và tính thử 3 chỉ số E1 (`82,83%`, `27,12%`, `4,25%`).
   - Điền lời giải D1, D2 (trong phần `#` đầu file) và các trường thông số kỹ thuật (`primary_metric`, `assignment`, `rollout`, `simulated_inputs`) vào `report/team/pilot_plan.yaml`.
3. **Cá nhân:** Tạo `report/team/<MSSV_TV2>_<HoTen>.md` và điền mục đóng góp của TV2 trong `TEAM.md`.

---

### 👤 Thành viên 3 (TV3): Người gắn nhãn 1 & Điều phối Chất lượng / Event
1. **Xuyên suốt buổi Lab (Vai Điều phối & Kiểm soát Rubric):**
   - Đọc kỹ đề gốc `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, canh mốc thời gian các Checkpoint, rà soát điều kiện **"Xong khi"** của từng nhiệm vụ trước khi chốt.
   - Soát lỗi quy tắc trên mọi file `.md`/`.yaml`: không dùng `"production"`, không ghi `"cả đội"`, đủ nhãn `simulated`, câu trả lời ≤ 3 dòng.
2. **Nhiệm vụ C (CP3 — Người gắn nhãn 1):**
   - **8 phút đầu:** Ngồi tách biệt, tự gắn nhãn độc lập toàn bộ 20 ca lỗi theo 5 loại Google PAIR (không trao đổi với TV4).
   - **22 phút tiếp:** So khớp với TV4, tính tỉ lệ đồng thuận (`≥ 80%`), thảo luận thống nhất các ca lệch, viết quy tắc phân biệt (1 câu/ca) và hoàn thiện bảng khắc phục 5 ca (đủ 5 loại, cách phát hiện đo được bằng event + ngưỡng + tần suất, 1 vai trò phụ trách) vào `report/team/bang_loi.md`.
3. **Nhiệm vụ D, E & Báo cáo nhóm (CP4–CP5):**
   - Phối hợp cùng TV2 soạn 3 `stop_rules` (An toàn, Chi phí, Sử dụng) đúng chuẩn 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` và cơ chế `rollback` trong `report/team/pilot_plan.yaml`.
   - Thiết kế bảng **≥ 6 Events** có `trace_id` và phần **Kiểm tra chéo** event ↔ chỉ số trong `report/team/chi_so.md`.
   - Tổng hợp nội dung ngắn gọn vào `report/team/group_report.md` (giữ đúng 8 mục, ≤ 2 trang).
4. **Cá nhân:** Tạo `report/team/<MSSV_TV3>_<HoTen>.md` và điền mục đóng góp của TV3 trong `TEAM.md`.

---

### 👤 Thành viên 4 (TV4): Người gắn nhãn 2 kiêm Giữ Hồ sơ Launch & Chủ trì Gate 2a
1. **Từ đầu buổi (Vai Giữ Hồ sơ cuốn chiếu):**
   - Điền khung thông tin thành viên trong `TEAM.md`.
   - Mở sẵn `report/team/ho_so_launch_v0.md` và điền cuốn chiếu ngay khi có kết quả:
     - Xong CP1 → điền Mục 1 (*Chi phí mỗi việc thành công*) & Mục 3 (*So với nhân viên tự làm*).
     - Xong CP2 → điền Mục 2 (*Ba yếu tố nhạy nhất*).
     - Xong CP3 → điền Mục 5 (*Bảng lỗi và cách khắc phục*).
     - Xong CP4 → điền Mục 6 (*Pilot plan*).
2. **Nhiệm vụ C (CP3 — Người gắn nhãn 2):**
   - **8 phút đầu:** Ngồi tách biệt, tự gắn nhãn độc lập toàn bộ 20 ca lỗi (không trao đổi với TV3).
   - Cùng TV3 đối chiếu nhãn, chốt tỉ lệ đồng thuận và đồng biên tập `report/team/bang_loi.md`.
3. **Nhiệm vụ E & Duyệt chéo Gate 2a (CP5):**
   - Điền bảng đặc tả chỉ số E1 (3 chỉ số tính thử + 2 chỉ số tự đề xuất, lưu ý không viết "trợ lý đã nâng chỉ số") và bảng Rủi ro kinh tế E2 (≥ 2 dòng lấy số từ B1/B4/A4) vào `report/team/chi_so.md`.
   - Hoàn thiện Mục 4, Mục 7, cột `Trạng thái` (`Xong, có bằng chứng` / `Chưa` / `Giả lập`), cột `Người phụ trách` và phần **Đề xuất cuối trang** (`Go có điều kiện` kèm điều kiện, vai trò phụ trách, ngày kiểm tra) trong `report/team/ho_so_launch_v0.md` trước 17:00.
   - Đại diện trình bày 1 phút trước hội đồng Gate 2a và chủ trì ghi nhận kết quả chấm nhóm bạn vào `report/team/phieu_cham.md`.
4. **Cá nhân:** Tạo `report/team/<MSSV_TV4>_<HoTen>.md` và điền mục đóng góp của TV4 trong `TEAM.md`.

---

## 3. Ma trận Trách nhiệm theo File Nộp (RACI)

*(**R** = Responsible/Thực hiện chính · **A** = Accountable/Chịu trách nhiệm chốt · **C** = Consulted/Đối chiếu & đóng góp · **I** = Informed/Nắm thông tin)*

| Deliverable | TV1 | TV2 | TV3 | TV4 | Điều kiện đạt chuẩn (Done Criteria) |
| --- | :---: | :---: | :---: | :---: | --- |
| `src/lab13.py` | **A/R** (A,B) | **R** (D,E) | I | I | Chạy mượt từ đầu đến cuối trong `src/`, in ĐẠT 3 phép thử A1 + đủ số A, B, D1, E1. |
| `report/team/bang_chi_phi.md` | C | **A/R** | C | I | Đủ bảng A1–A4, B1–B4; sai số ≤ 2%; đủ nhãn `simulated`; trả lời ≤ 3 dòng + có số. |
| `report/team/bang_loi.md` | I | I | **A/R** | **R** | 2 cột nhãn độc lập gốc, đồng thuận ≥ 80%, quy tắc ca lệch, 5 dòng khắc phục đo được + 1 vai trò. |
| `report/team/pilot_plan.yaml` | C | **A/R** | **R** | C | Đủ chú thích D1–D2, `yaml.safe_load` OK, sạch dấu `?`, ≥ 3 `stop_rules` đủ 4 vế. |
| `report/team/chi_so.md` | C | C | **R** | **A/R** | 5 dòng chỉ số (3 dòng có số đúng), ≥ 6 events có `trace_id` + kiểm tra chéo, ≥ 2 rủi ro kinh tế. |
| `report/team/ho_so_launch_v0.md` | C | C | C | **A/R** | Gọn 1 trang, đủ 7 mục, trạng thái đúng tập cho phép, 1 vai trò/mục, đề xuất khớp bằng chứng, không có từ `"production"`. |
| `report/team/phieu_cham.md` | C | C | **R** | **A/R** | Chấm đủ 3 tiêu chí có dẫn chứng số, có quyết định hội đồng + 1 câu hỏi & câu trả lời. |
| `report/team/group_report.md` | C | C | **A/R** | C | Giữ nguyên 8 đề mục, ≤ 2 trang, dẫn link tới các file hồ sơ. |
| `TEAM.md` | C | C | C | **A/R** | Đủ thông tin nhóm, bảng 4 thành viên + vai trò, đóng góp & bằng chứng cả 4 người. |
| `report/team/<MSSV>_<HoTen>.md` | **R** (1) | **R** (2) | **R** (3) | **R** (4) | 4 file riêng biệt (giữ nguyên file mẫu `MSSV_HoTen.md`), ghi rõ công cụ AI & cách tự kiểm. |

---

## 4. Lịch trình Phối hợp Đồng bộ theo Checkpoint

| Khung giờ (Mẫu) | Giai đoạn | Luồng làm việc song song của 4 người |
| --- | --- | --- |
| **Bước 0 (10')** | Khởi động | **TV1** dựng `.venv` & chạy thử `lab13.py` · **TV2** đọc công thức & chuẩn bị bảng tính tay · **TV3** đọc 20 ca lỗi & checklist · **TV4** điền khung `TEAM.md` & mở `ho_so_launch_v0.md`. |
| **CP1 (40')** | Nhiệm vụ A | **TV1** code A1 → A2 → A3 → A4 · **TV2** tính tay kiểm số & điền nửa trên `bang_chi_phi.md` · **TV3** soát nhãn `simulated` & giới hạn 3 dòng · **TV4** cập nhật Mục 1 & 3 vào `ho_so_launch_v0.md`. |
| **CP2 (25')** | Nhiệm vụ B | **TV1** code B1 → B4 · **TV2** đối chiếu tính tuyến tính B1/B2, kiểm số B3/B4 & điền nửa dưới `bang_chi_phi.md` · **TV3** soát câu trả lời B3, B4 · **TV4** cập nhật Mục 2 vào `ho_so_launch_v0.md`. |
| *Giải lao (15')* | *Chuyển vai* | **TV1 bàn giao `src/lab13.py` cho TV2** để TV2 trực tiếp code phần sau. |
| **CP3 (30')** | Nhiệm vụ C | **8 phút đầu:** **TV3** & **TV4** ngồi tách nhau gắn nhãn độc lập 20 ca; **TV1** & **TV2** hoàn tất rà soát `bang_chi_phi.md`.<br>**22 phút sau:** **TV3** & **TV4** so nhãn, viết quy tắc & bảng khắc phục 5 ca trong `bang_loi.md`, cập nhật Mục 5 `ho_so_launch_v0.md`. |
| **CP4 (25')** | Nhiệm vụ D | **TV2** code D1 trong `lab13.py` & điền thông số `pilot_plan.yaml` · **TV1** tính tay đối chiếu `DE`, `m >= 299` · **TV3** viết D2 & 3 `stop_rules` + `rollback` · **TV4** cập nhật Mục 6 `ho_so_launch_v0.md`. |
| **CP5 (20')** | Nhiệm vụ E | **TV2** code tính thử 3 chỉ số E1 · **TV3** viết ≥ 6 events có `trace_id` + kiểm tra chéo · **TV4** viết E1, E2 (`chi_so.md`) & chốt toàn bộ 7 mục + đề xuất trong `ho_so_launch_v0.md` · **TV1** chạy script kiểm lỗi tổng thể. |
| **Gate 2a (45')** | Duyệt chéo | Cả nhóm đọc hồ sơ nhóm kế tiếp, chấm điểm vào `phieu_cham.md`; **TV4** trình bày 1 phút, cả nhóm trả lời phản biện. |
| **Đóng gói (15')** | Hoàn thiện & Nộp | **TV3** chốt `group_report.md` · Cả 4 thành viên hoàn tất `TEAM.md` & 4 file `MSSV_HoTen.md` · **TV1** chạy checklist lần cuối, commit, push GitHub; cả 4 người nộp link lên LMS. |
