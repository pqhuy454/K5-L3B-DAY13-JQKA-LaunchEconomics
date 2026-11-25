# Báo cáo cá nhân — Trịnh Gia Huy - 2A202603924

## 1. Thông tin thành viên

- Họ tên: Trịnh Gia Huy
- MSSV: 2A202603924
- Email: trgyahuy1710@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (TV3); phụ trách luật dừng ở Nhiệm vụ D và danh sách event ở Nhiệm vụ E

## 2. Phần việc phụ trách

- **Nhiệm vụ C:** gắn nhãn độc lập 20 ca lỗi theo năm loại Google PAIR, so nhãn với người gắn nhãn 2 (TV4), thống nhất ca lệch và viết quy tắc phân biệt trong `report/team/bang_loi.md`.
- **Nhiệm vụ D:** viết các luật dừng (`stop_rules`) trong `report/team/pilot_plan.yaml`, mỗi luật đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ và có số căn cứ từ đợt chạy thử.
- **Nhiệm vụ E:** bổ sung event còn thiếu và bảng kiểm tra chéo luật dừng, bảng lỗi với event trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- **C · Gắn nhãn:** tự gắn 20 ca trước khi xem nhãn của TV4; đồng thuận 18/20 = 90% (≥ 80%). Hai ca lệch:
  - Ca 6: tôi gắn Giới hạn hệ thống, TV4 gắn Do người dùng. Thống nhất **Do người dùng**, vì gốc lỗi là khách chọn sai mục; việc trợ lý không nhận ra ý định thật là chỗ cần cải thiện, không đổi nguyên nhân gốc.
  - Ca 16: tôi gắn Hệ thống, TV4 gắn Ngữ cảnh. Thống nhất **Ngữ cảnh**, vì trợ lý chạy đúng thiết kế "gửi ngay khi xong", chỉ giả định đó không hợp với giờ sinh hoạt của khách.
  - Nhãn gốc của tôi giữ nguyên trong cột "Nhãn người 1", không sửa sau khi so.
- **D · Bốn luật dừng**, mỗi ngưỡng đặt theo số của đợt chạy thử:
  - An toàn, mở lại 7 ngày: dừng khi nhóm trợ lý cao hơn đối chứng ≥ 2 điểm hoặc vượt 6% trong 3 ngày liên tiếp. Tỉ lệ hiện tại là 3,97% (39/982) trong phạm vi `noi_dia` + `hang_nang` và 4,25% toàn mẫu, nên không đặt trần 3%, vì pilot sẽ dừng ngay tuần đầu.
  - An toàn, sai tiền đã lộ ra (ca 7, ca 20): ngưỡng 0 ca hoàn trùng hoặc báo "đã hoàn" khi sổ cái không trả `ok`.
  - Chi phí: dừng khi chi phí mỗi việc thành công trong phạm vi vượt 6.800 đ trong 2 tuần. Mức này gấp đôi 3.414 đ (simulated) và vẫn dưới 0,6× của 12.000 đ.
  - Sử dụng: dừng khi tỉ lệ bỏ qua gợi ý vượt 40% trong 1 tuần. Đợt chạy thử là 21,1% (27/128) trong phạm vi.
- **E · Event:** thêm `input_validation_failed` (đo ca 9) và `refund_notice_sent` (đối soát với `refund_ledger_write` cho ca 7; ghi giờ gửi cho ca 16 và cách tính cho ca 18), nâng danh sách lên 13 event có `trace_id`. Viết bảng kiểm tra chéo nối 4 luật dừng và 5 cách phát hiện của bảng lỗi với event dùng để tính.

## 4. Bằng chứng

- `0b85696` docs: C gán nhãn lỗi (`report/team/bang_loi.md`: cột nhãn người 1, tỉ lệ đồng thuận, quy tắc ca 6 và ca 16).
- `f474238` docs: D luật dừng (`report/team/pilot_plan.yaml`, mục `stop_rules` và các dòng chú thích số căn cứ).
- `cb6381b` docs: event chi so (`report/team/chi_so.md`: hai event cuối và bảng "Kiểm tra chéo luật dừng và bảng lỗi").
- Số căn cứ tự kiểm trên `src/logix_requests.csv`: mở lại 7 ngày 39/982 = 3,97% trong phạm vi; sửa + bỏ 27/128 = 21,1% trong phạm vi; tỉ lệ làm lại 4,89% trong phạm vi.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code.
- **Dùng vào việc gì:**
  - Giải thích lý thuyết của lab (cost-of-pass, hệ số thiết kế, ICC, năm loại lỗi Google PAIR).
  - Đưa ví dụ gắn nhãn trên các ca tự đặt, không nằm trong 20 ca của đề.
  - Gợi ý cấu trúc cho bốn luật dừng và bảng kiểm tra chéo event.
  - Viết script kiểm số căn cứ.
- **Không dùng AI để gắn nhãn 20 ca.** Tôi tự gắn bằng 4 câu hỏi quyết định trước khi xem cột của TV4, theo đúng quy định gắn nhãn độc lập trong `RULES.md`.
- **Cách tự kiểm tra:**
  - Đối chiếu mọi ngưỡng luật dừng với số đếm trực tiếp từ `src/logix_requests.csv` (đọc với `keep_default_na=False`).
  - Kiểm `pilot_plan.yaml` bằng `yaml.safe_load`, không còn dấu `?` ngoài chú thích.
  - Quét toàn bộ `report/team` không còn từ bị cấm theo quy tắc 5 của lab.
  - Rà từng event trong bảng kiểm tra chéo đều có trong danh sách event.

## 6. Tự đánh giá

- Hoàn thành đủ phần việc của vai Người gắn nhãn 1: hai bộ nhãn độc lập đạt 90% đồng thuận, bốn luật dừng có ngưỡng, thời hạn và người có quyền dừng, mọi ngưỡng đều đo được từ event.
- Điểm cần cải thiện: ca 6 và ca 16 tôi gắn theo chỗ cần sửa thay vì nguyên nhân gốc. Lần sau cần hỏi "trợ lý có làm đúng thiết kế không" và "ai sai trước" trước khi chọn nhãn.
