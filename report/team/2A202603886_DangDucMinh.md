# Báo cáo cá nhân — Đặng Đức Minh - 2A202603886

## 1. Thông tin thành viên

- Họ tên: Đặng Đức Minh
- MSSV: 2A202603886
- Email: ddminh1102@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ launch và chủ trì Gate 2a

## 2. Phần việc phụ trách

- Cập nhật và giữ hồ sơ launch `report/team/ho_so_launch_v0.md` theo tiến độ các checkpoint A–E.
- Đặc tả ba chỉ số E1, hai chỉ số đề xuất, danh sách event có `trace_id`, kiểm tra chéo và các rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Tự gắn nhãn độc lập 20 ca lỗi (Google PAIR) trước khi đối chiếu với TV3 và hoàn thiện bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Chủ trì phần trình bày và ghi phiếu chấm duyệt chéo Gate 2a trong `report/team/phieu_cham.md`.

## 3. Đóng góp cụ thể

- Hoàn thành thông tin thành viên, vai trò và mục cá nhân của TV4 trong `TEAM.md`.
- Gắn nhãn độc lập 20 ca lỗi (cột `Nhãn người 2`) trong `report/team/bang_loi.md` dựa trên đề bài gốc, đối chiếu với TV3 đạt đồng thuận `18/20 = 90%` (≥ 80%), thống nhất quy tắc cho 2 ca lệch (Ca 6, Ca 16) và hoàn thiện bảng khắc phục 5 ca theo 5 loại lỗi.
- Tính và kiểm tra lại các chỉ số E1 trên 1.200 yêu cầu (`82,83%`, `27,12%`, `4,25%`), đề xuất 2 chỉ số pilot (`assistant_opened / request_assigned`, `refund_amount_audit`), lập khung event có `trace_id` (phối hợp TV3 hoàn thiện 13 event), kiểm tra chéo chỉ số–event và ghi 3 dòng rủi ro kinh tế E2 trong `report/team/chi_so.md`.
- Cập nhật đủ 7 mục của `report/team/ho_so_launch_v0.md` với số liệu A–E đã kiểm chứng (`pilot_plan.yaml`, `bang_chi_phi.md`, `bang_loi.md`) và đề xuất `Go có điều kiện` kèm các con số bất lợi (power `0,64` ở mức +5 điểm; xem lại 100% lên `11.743–12.414 đ/việc` `[simulated]`) cùng điều kiện xử lý.
- Chủ trì chấm duyệt chéo Gate 2a cho nhóm DMTG (`30/30`, `Go có điều kiện`) trong `report/team/phieu_cham.md` và cập nhật kết quả hội đồng DMTG chấm JQKA (`30/30` sau khi bổ sung nhãn `simulated` cho C7, `Go có điều kiện`) vào `report/team/group_report.md`.

## 4. Bằng chứng

- Các file đã cập nhật/tạo: `TEAM.md`, `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`, `report/team/2A202603886_DangDucMinh.md`.
- Số liệu đã đối chiếu trực tiếp từ `src/logix_runs.csv` (1.624 dòng) và `src/logix_requests.csv` (1.200 dòng):
  - Tổng chi phí mẫu: `4.373.585,132 đ` (`token 245.585,132`, `tool 84.000`, `xem_lai 1.780.000 [simulated]`, `lam_lai 2.264.000 [simulated]`); `978` việc thành công → `4.472 đ/việc [simulated]`; toàn hệ thống `5.865 đ/YC = 0,49×` mức `12.000 đ`.
  - Phạm vi `noi_dia + hang_nang`: `900/982` thành công, biến đổi `3.414 đ`, cộng cố định 40 triệu/tháng = `4.599 đ` (`0,38×`) ở 45.000 YC/tháng (`5.784 đ` ở nửa khối lượng).
  - B4 xem lại 100%: `11.743 đ = 0,98×` (làm lại 9 phút) hoặc `12.414–12.415 đ = 1,03×` (làm lại 15,3 phút) `[simulated]`.
  - E1: `994/1.200 = 82,83%`; `48/177 = 27,12%`; `51/1.200 = 4,25%`.
- Commit chốt nhóm: *(bổ sung sau khi nhóm push commit cuối)*.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI (Codex / Antigravity) để kiểm tra chéo các phép tính từ `src/logix_runs.csv` và `src/logix_requests.csv`, rà soát quy tắc chấm trong `RUBRIC.md` / `RULES.md` và chuẩn hoá bảng biểu, danh sách event.
- Cách tự kiểm tra: đối chiếu lại từng công thức và từng con số trực tiếp trên hai file CSV bằng script kiểm tra độc lập; kiểm tra từng ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` trước khi chốt nhãn; không dùng AI để bịa điểm duyệt chéo hay nhãn của thành viên khác.

## 6. Tự đánh giá

- Đã hoàn thành phần việc của TV4: `chi_so.md`, `ho_so_launch_v0.md` (đủ 7 mục A–E), đồng thuận `18/20 = 90%` và bảng 5 ca trong `bang_loi.md`, `group_report.md`, và phiếu chấm DMTG trong `phieu_cham.md` (`30/30`, `Go có điều kiện`).
- Còn chờ: ghi câu trả lời hỏi đáp trực tiếp của DMTG vào `phieu_cham.md` (nếu có), phần cá nhân trong `TEAM.md`, xoá các file trao đổi tạm trước khi push và bổ sung mã commit chốt cuối buổi.
