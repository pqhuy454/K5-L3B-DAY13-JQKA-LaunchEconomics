# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: chờ TV3 (Trịnh Gia Huy) · Người gắn nhãn 2: TV4 (Đặng Đức Minh, đã gắn độc lập). Chỉ tính đồng thuận sau khi cả hai người đã chốt nhãn riêng.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | Do người dùng | ... | ... |
| 2 | ... | Hệ thống | ... | ... |
| 3 | ... | Ngữ cảnh | ... | ... |
| 4 | ... | Giới hạn hệ thống | ... | ... |
| 5 | ... | Ngầm | ... | ... |
| 6 | ... | Do người dùng | ... | ... |
| 7 | ... | Hệ thống | ... | ... |
| 8 | ... | Hệ thống | ... | ... |
| 9 | ... | Do người dùng | ... | ... |
| 10 | ... | Ngữ cảnh | ... | ... |
| 11 | ... | Giới hạn hệ thống | ... | ... |
| 12 | ... | Ngầm | ... | ... |
| 13 | ... | Giới hạn hệ thống | ... | ... |
| 14 | ... | Do người dùng | ... | ... |
| 15 | ... | Hệ thống | ... | ... |
| 16 | ... | Ngữ cảnh | ... | ... |
| 17 | ... | Ngầm | ... | ... |
| 18 | ... | Ngữ cảnh | ... | ... |
| 19 | ... | Giới hạn hệ thống | ... | ... |
| 20 | ... | Hệ thống | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò có quyền xử lý. *(Khung đề xuất từ nhãn TV4, rà soát lại cùng TV3 sau khi chốt đồng thuận 20 ca.)*

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi tỉ lệ vượt 2% tổng yêu cầu/ngày | Bổ sung bộ nhận diện mã đơn sàn TMĐT để tự ánh xạ sang mã vận đơn; nếu không tra được thì hiển thị hướng dẫn kèm ảnh mẫu | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát hằng giờ: event `refund_ledger_write` lỗi hoặc thiếu bản ghi `ok` nhưng có thông báo "đã hoàn" cùng `trace_id`; ngưỡng > 0 ca | Chỉ gửi thông báo "đã hoàn" khi sổ cái trả trạng thái `ok`; lỗi 503 sau 3 lần thử phải báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hằng tuần `ticket_reopened` có lý do số tiền nhưng kết quả đối chiếu đúng chính sách; ngưỡng > 1% số đơn đóng/tuần | Cập nhật mẫu phản hồi luôn ghi rõ công thức tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) ngay trong tin nhắn hoàn phí | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu_ngoai_pham_vi` theo dõi theo `loai` mỗi tuần; ngưỡng > 5% ở `noi_dia`/`hang_nang` | Giữ cơ chế chuyển nhân viên kèm tóm tắt ngữ cảnh; loại `quoc_te` và `doi_tac` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `refund_amount_audit` kiểm tra mẫu 100 đơn ngẫu nhiên/tuần so với bảng giá hiện hành; ngưỡng `amount_mismatch = true` ≥ 1% | Xoá cache bảng giá tự động khi phát hành bảng giá mới và ghi `pricing_version` vào thuộc tính trace | Kế toán trưởng |
