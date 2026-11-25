# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò có quyền quyết định. Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: JQKA · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.472 đ/việc (978/1.200 YC, gấp 16,3× hoá đơn 274,7 đ); phạm vi `noi_dia` + `hang_nang`: 3.414 đ biến đổi, cộng cố định 40 triệu/tháng đạt 4.599 đ ở 45.000 YC/tháng (5.784 đ ở nửa khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (+51,8%, lên 6.787 đ) · 2. Tỉ lệ xem lại (+40,7%, lên 6.292 đ) · 3. Lương nhân viên (+23,1%, lên 5.506 đ) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Toàn hệ thống 5.865 đ/YC = 0,49× mức 12.000 đ; theo loại: `noi_dia` 0,22×, `hang_nang` 0,69× (gộp cố định = 0,38×), `quoc_te` 1,88×, `doi_tac` 0,85×; nếu xem lại 100% vọt lên 11.743 đ = 0,98× (12.414 đ = 1,03× nếu làm lại 15,3 phút) [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, dùng, an toàn | 82,83% (994/1.200); 27,12% (48/177); 4,25% (51/1.200) trong đợt chạy thử; đã đặc tả 5 chỉ số và 11 event có `trace_id` trong `chi_so.md` | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca; TV4 đã chốt nhãn độc lập (20/20) và khung 5 biện pháp; chờ nhãn độc lập TV3 để tính đồng thuận ≥ 80% | Chưa | Trưởng nhóm CSKH |
| 6 · Pilot plan | Mục tiêu +5 điểm cần 1.251 YC/nhóm; 20 NV/nhóm chỉ đạt cỡ mẫu hiệu dụng ≤ 1.000. Chấp nhận MDE +6 điểm (859 YC/nhóm, m ≥ 299), bất lợi: power ở +5 điểm còn ~0,64; chờ chốt `pilot_plan.yaml` | Chưa | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại 2×: 6.787 đ (+51,8%); xem lại 2×: 6.292 đ (+40,7%); xem lại 100%: 11.743 đ = 0,98× (12.414 đ = 1,03× nếu làm lại 15,3 phút); nửa khối lượng: cố định +2.370 đ/việc [simulated] | Giả lập | Giám đốc vận hành LogiX-VN |

**Đề xuất: Go có điều kiện** cho pilot giới hạn ở `noi_dia` và `hang_nang` (900/982 yêu cầu thành công, 0,22× và 0,69× mức 12.000 đ [simulated]; loại `quoc_te` 1,88× và `doi_tac` 0,85×). Chỉ kích hoạt pilot khi đáp ứng đủ bốn điều kiện sau:

- **Sửa lỗi nghiêm trọng (Ca 7, Ca 20):** Kỹ sư trưởng agent bổ sung khoá chống trùng lệnh hoàn tiền và cơ chế chỉ báo "đã hoàn" khi sổ cái trả `ok` (ngày kiểm tra: 25/11/2026 trước Gate 2a / trước ngày mở pilot).
- **Chốt thiết kế pilot và chấp nhận đánh đổi power:** Giám đốc vận hành LogiX-VN ký xác nhận chia cụm theo 20 nhân viên/nhóm với MDE +6 điểm (ghi rõ power ở +5 điểm là ~0,64), duyệt `pilot_plan.yaml`, 3 luật dừng và nút tắt rollback 30 phút (ngày kiểm tra: 25/11/2026 trước 17:00).
- **Hoàn tất bộ nhãn C và bật telemetry:** Trưởng nhóm CSKH và TV3/TV4 đối chiếu nhãn độc lập (đồng thuận ≥ 80%); Kỹ sư trưởng agent bật đủ 11 event có `trace_id` và thay phút `simulated` bằng `phut_xem_lai` / `phut_lam_lai` đo thật sau tuần đầu pilot.
- **Lộ trình giảm tỉ lệ xem lại:** PM trợ lý hoàn phí thiết kế kế hoạch giảm xem lại theo bậc (từ 100% xuống khi tỉ lệ `sua + bo` < 15% và mở lại đạt ngưỡng an toàn), vì xem lại 100% đẩy chi phí lên 11.743–12.414 đ/việc [simulated], không còn tiết kiệm so với 12.000 đ.
