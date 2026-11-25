# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: JQKA
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0 (Gate 2a)** cho trợ lý hoàn phí LogiX-VN từ mẫu chạy thử giả lập gồm `1.200` yêu cầu và `1.624` lần chạy agent, nhằm trả lời bốn câu hỏi quyết định pilot:

1. **Có đáng chạy không?** Tính chi phí thật mỗi việc thành công gồm cả token, tool, lần chạy lỗi và thời gian nhân viên xem lại/làm lại (`simulated`), sau đó phân tích độ nhạy và chi phí cố định.
2. **Nhân viên có dùng không?** Đặc tả chỉ số chính, chỉ số dùng, chỉ số an toàn cùng `13` event có `trace_id`.
3. **Khi hỏng thì sao?** Gắn nhãn độc lập `20` ca lỗi theo Google PAIR, đối chiếu đồng thuận và lập biện pháp khắc phục đo được cho `5` loại.
4. **Thiết kế pilot thế nào để ra quyết định?** Tính cỡ mẫu theo cụm, kiểm tra khả năng tách tác động và đặt `4` luật dừng bốn vế.

## 3. Giải pháp

- **Nhiệm vụ A & B ([`src/lab13.py`](../../src/lab13.py), [`bang_chi_phi.md`](bang_chi_phi.md)):** Đạt cả ba phép thử A1 (`1,20 · 1,25 · 1,25`), xây dựng hàm `mo_hinh` tính chi phí từ trace, tách theo `4` loại yêu cầu (A3), cộng chi phí cố định `40` triệu đ/tháng (A4), chạy `9` kịch bản độ nhạy B1, B2, giới hạn chạy lại B3 và kịch bản xem lại `100%` B4.
- **Nhiệm vụ C ([`bang_loi.md`](bang_loi.md)):** TV3 và TV4 gắn nhãn độc lập `20` ca lỗi, tính đồng thuận (`18/20 = 90%`), ghi quy tắc phân biệt cho `2` ca lệch (Ca 6, Ca 16) và lập bảng khắc phục `5` ca với event, ngưỡng, tần suất và một vai trò phụ trách.
- **Nhiệm vụ D ([`pilot_plan.yaml`](pilot_plan.yaml)):** Tính đủ `5` câu D1, kiểm tra `5` câu D2, chọn chia cụm theo nhân viên (`20 + 20`, phân tầng theo `12` depot, `seed = 20261125`) và viết `4` luật dừng đủ bốn vế `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **Nhiệm vụ E ([`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md)):** Tính thử `3` chỉ số E1, đề xuất thêm `2` chỉ số pilot, đặc tả `13` event có `trace_id` kèm bảng kiểm tra chéo và `3` rủi ro kinh tế E2; tổng hợp thành hồ sơ một trang `7` mục và đề xuất.
- **Duyệt chéo Gate 2a ([`phieu_cham.md`](phieu_cham.md)):** Chuẩn bị khung phiếu chấm và câu hỏi cho phiên duyệt chéo lúc 17:00.

## 4. Kết quả

- **Chi phí và độ nhạy (`simulated`):** Toàn mẫu `4.472 đ/việc` (`978/1.200` thành công, gấp `16,3×` hoá đơn `274,7 đ`); chi phí cả hệ thống `5.865 đ/yêu cầu = 0,49×` mức `12.000 đ`. Trong phạm vi `noi_dia + hang_nang` (`900/982` thành công), chi phí biến đổi `3.414 đ`, cộng cố định đạt `4.599 đ` (`0,38×`) ở `45.000 YC/tháng` và `5.784 đ` (`0,48×`) ở nửa khối lượng. Ba yếu tố nhạy nhất: làm lại 2× (`+51,8%`), xem lại 2× (`+40,7%`), lương +25% (`+23,1%`). Xem lại `100%` đẩy chi phí lên `11.743 đ = 0,98×` (hoặc `12.414 đ = 1,03×` nếu làm lại `15,3 phút`) `[simulated]`.
- **Phân loại lỗi & chỉ số:** Đồng thuận gắn nhãn đạt `18/20 = 90%` (`≥ 80%`). Trong đợt chạy thử, chỉ số chính đạt `82,83%` (`994/1.200`), tỉ lệ bỏ qua gợi ý `27,12%` (`48/177`), tỉ lệ mở lại 7 ngày `4,25%` (`51/1.200`, trong phạm vi pilot là `3,97%`).
- **Pilot plan & đề xuất:** Chia theo `20` nhân viên/nhóm với MDE `+6 điểm` (`n_per_arm = 859`, `m ≥ 299`, `DE = 6,96`, `power = 0,64` ở mức `+5 điểm`), rollout `[0.10, 0.25, 0.50]`, rollback `30 phút`, `decision_date: 2027-01-05`. **Đề xuất:** **`Go có điều kiện`** cho phạm vi `noi_dia` và `hang_nang` kèm `4` điều kiện trước khi khởi chạy.
- **Kết quả duyệt chéo từ hội đồng Gate 2a:** *(chờ cập nhật sau phiên duyệt chéo lúc 17:00)*.

## 5. Khó khăn và cách xử lý

- **Cỡ mẫu bị chặn khi chia cụm (`c/ICC`):** Với `40` nhân viên (`20/nhóm`) và `ICC = 0,02`, cỡ mẫu hiệu dụng tối đa chỉ là `1.000 < 1.251`, không đủ cho MDE `+5 điểm`. Nhóm xử lý bằng cách nới MDE lên `+6 điểm` (`859/nhóm`, `m ≥ 299`) và ghi rõ đánh đổi bất lợi (`power` ở `+5 điểm` giảm còn `0,64`) trong `pilot_plan.yaml` và `ho_so_launch_v0.md`.
- **Phút nhân viên hoàn toàn giả lập và rủi ro xem lại 100%:** Chi phí giờ nhân viên chiếm `92,5%` tổng chi phí và xem lại `100%` làm mất lợi thế tiết kiệm (`0,98×–1,03×`, `simulated`). Nhóm đưa yêu cầu đo phút thực qua event `staff_review_decision` / `staff_rework_completed` và lộ trình giảm xem lại theo bậc vào điều kiện bắt buộc của đề xuất.
- **Ngưỡng dừng an toàn:** Tỉ lệ mở lại hiện tại là `4,25%` (`3,97%` trong phạm vi pilot), nên đặt ngưỡng tuyệt đối `3%` sẽ làm pilot dừng ngay tuần đầu; nhóm chuyển sang ngưỡng kép (`+2 điểm` so với đối chứng hoặc trần `6%` trong `3` ngày liên tiếp).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và báo cáo cá nhân `report/team/MSSV_HoTen.md`.

| Thành viên | Vai | Đóng góp chính | File |
| --- | --- | --- | --- |
| TV1 · Phạm Quốc Huy | Viết code A, B → kiểm số D, E | Ba hàm A1, `mo_hinh`, A2–A4, B1–B4; tính tay đối chiếu D1, E1; QA kỹ thuật | `src/lab13.py` |
| TV2 · Nguyễn Thành Tâm | Kiểm số A, B → viết code D, E | Kiểm số và điền bảng chi phí A, B; code cỡ mẫu D1 và chỉ số E1; điền D1, D2, các trường số của pilot | `bang_chi_phi.md`, `src/lab13.py`, `pilot_plan.yaml` |
| TV3 · Trịnh Gia Huy | Gắn nhãn 1 | Gắn nhãn độc lập 20 ca, quy tắc ca 6 và ca 16; bốn luật dừng; event bổ sung và bảng kiểm tra chéo | `bang_loi.md`, `pilot_plan.yaml` (`stop_rules`), `chi_so.md` |
| TV4 · Đặng Đức Minh | Gắn nhãn 2, giữ hồ sơ | Gắn nhãn độc lập 20 ca, bảng khắc phục 5 ca; chỉ số E1, 11 event, rủi ro E2; hồ sơ launch 7 mục và đề xuất; khung báo cáo nhóm; chủ trì Gate 2a | `bang_loi.md`, `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`, `phieu_cham.md` |

## 7. Hạn chế và hướng cải thiện

- **Dữ liệu thời gian nhân viên là giả lập:** Cần thay `phut_xem_lai_simulated` và `phut_lam_lai_simulated` bằng số đo thật trong tuần đầu pilot trước khi mở rộng rollout.
- **Giới hạn thống kê với 40 nhân viên:** Power ở mức `+5 điểm` chỉ đạt `0,64`; cần tuân thủ nghiêm quy trình phân quyền theo `staff_id` để hạn chế spillover trong cùng depot.
- **Mục tiêu kỹ thuật trước khi bật pilot:** Hoàn tất khoá chống trùng và đối soát sổ cái (Ca 7, Ca 20) và bật đầy đủ `13` event có `trace_id`.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`statsmodels.stats.power`)
- [docs/du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md)
