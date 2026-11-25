# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Đếm `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng yêu cầu | 994/1.200 = **82,83%** trong đợt chạy thử `[dữ liệu chạy thử giả lập, simulated]` |
| Dùng | Tỉ lệ bỏ qua gợi ý | Đếm `quyet_dinh_xem_lai` là `sua` hoặc `bo` / số yêu cầu `duoc_xem_lai = 1` | 48/177 = **27,12%** trong đợt chạy thử `[dữ liệu chạy thử giả lập, simulated]` |
| An toàn | Tỉ lệ yêu cầu mở lại trong 7 ngày (chỉ báo lỗi lọt tới khách) | Đếm `mo_lai_trong_7_ngay = 1` / tổng yêu cầu | 51/1.200 = **4,25%** trong đợt chạy thử `[dữ liệu chạy thử giả lập, simulated]` |
| Dùng | Tỉ lệ yêu cầu thuộc nhóm can thiệp thực sự mở trợ lý | Đếm `assistant_opened` / đếm `request_assigned` với `arm = intervention` | Chưa đo; cần event của pilot |
| An toàn | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu hằng tuần | Đếm `refund_amount_audit` có `amount_mismatch = true` / số đơn được kiểm tra | Chưa đo; cần kiểm tra mẫu và event |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

**Cách kiểm:** lọc và đếm trực tiếp 1.200 dòng trong `src/logix_requests.csv` với điều kiện ghi ở bảng. Đọc CSV giữ ô trống của `quyet_dinh_xem_lai` là chuỗi trống. Toàn bộ mẫu 1.200 yêu cầu của đợt chạy thử là dữ liệu giả lập của lab (`simulated`), chỉ mang tính mô tả mẫu chứ chưa phải tác động nhân quả; kết quả khớp hoàn toàn với output E1 của `src/lab13.py`.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_assigned` | Hệ thống điều phối | `request_id`, `loai`, `staff_id`, `depot`, `arm` (`intervention`/`control`), `trace_id` | Khi phân bổ yêu cầu vào nhóm thử nghiệm hoặc đối chứng |
| `assistant_opened` | Giao diện CSKH | `request_id`, `staff_id`, `arm`, `trace_id` | Khi nhân viên ở nhóm can thiệp mở trợ lý |
| `agent_run_completed` | Agent hoàn phí | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `pricing_version`, `trace_id` | Sau mỗi lần chạy của agent (kể cả lỗi) |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `duoc_xem_lai`, `trace_id` | Khi gợi ý của trợ lý hiển thị cho nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh_xem_lai` (`giu`/`sua`/`bo`), `phut_xem_lai`, `staff_id`, `trace_id` | Khi nhân viên chốt xem lại gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `staff_id`, `trace_id` | Khi nhân viên hoàn tất làm lại ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `status`, `trace_id` | Khi ghi nhận lệnh hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent hoàn phí | `reason`, `loai`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu sang nhân viên xử lý |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `dong_trong_24h`, `trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `mo_lai_trong_7_ngay`, `reason`, `trace_id` | Khi yêu cầu bị mở lại trong vòng 7 ngày |
| `refund_amount_audit` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `amount_mismatch`, `trace_id` | Khi kiểm tra mẫu 100 đơn/tuần |
| `input_validation_failed` | Agent hoàn phí | `request_id`, `truong_loi` (ví dụ `ma_van_don`, `so_tai_khoan`), `gia_tri_nhap_dang_che`, `loai_ma_nhan_dien` (ví dụ `ma_san_tmdt`), `trace_id` | Khi đầu vào của khách không qua kiểm tra định dạng |
| `refund_notice_sent` | Agent hoàn phí | `request_id`, `kenh` (`zalo`/`sms`/`app`), `noi_dung_loai` (`da_hoan`/`dang_xu_ly`/`tu_choi`), `so_tien_bao`, `cach_tinh`, `sent_at`, `trace_id` | Khi gửi thông báo kết quả hoàn phí cho khách |

Hai event cuối do TV3 bổ sung để đo được bảng lỗi (`bang_loi.md`) và luật dừng (`pilot_plan.yaml`): `input_validation_failed` cho ca 9; `refund_notice_sent` đối soát với `refund_ledger_write` cho ca 7 và cho biết giờ gửi (ca 16), có kèm cách tính hay không (ca 18).

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24 giờ và không mở lại 7 ngày):** tính từ `request_assigned` (tổng yêu cầu), `ticket_closed` (`dong_trong_24h = 1`) và `ticket_reopened` (không có event mở lại trong 7 ngày, `mo_lai_trong_7_ngay = 0`), nối theo `trace_id` / `request_id`.
- **Chỉ số dùng 1 (Tỉ lệ bỏ qua gợi ý):** tính từ `agent_suggestion_shown` (các ca `duoc_xem_lai = 1`) và `staff_review_decision` (`quyet_dinh_xem_lai` là `sua` hoặc `bo`).
- **Chỉ số an toàn 1 (Tỉ lệ mở lại trong 7 ngày):** tính từ `ticket_reopened` (`mo_lai_trong_7_ngay = 1`) chia tổng số `request_assigned`.
- **Chỉ số dùng 2 (Tỉ lệ nhóm can thiệp mở trợ lý):** tính từ `assistant_opened` chia `request_assigned` lọc `arm = intervention`.
- **Chỉ số an toàn 2 (Tỉ lệ hoàn sai tiền qua kiểm tra mẫu):** tính từ `refund_amount_audit` lọc `amount_mismatch = true` chia tổng số đơn được audit trong tuần.

**Kiểm tra chéo luật dừng và bảng lỗi (TV3):** mỗi ngưỡng trong `stop_rules` và mỗi cách phát hiện trong `bang_loi.md` phải tính được từ event ở bảng trên.

| Cần đo | Ngưỡng | Event dùng để tính |
| --- | --- | --- |
| Luật dừng an toàn 1: mở lại 7 ngày, nhóm trợ lý so với đối chứng | Chênh ≥ 2 điểm hoặc > 6% trong 3 ngày liên tiếp (đợt chạy thử `simulated`: 3,97% trong phạm vi) | `request_assigned` (`arm`), `ticket_closed`, `ticket_reopened` |
| Luật dừng an toàn 2: hoàn trùng hoặc báo "đã hoàn" khi sổ cái lỗi | ≥ 1 ca/ngày | `refund_ledger_write` (hai bản ghi `ok` cùng `request_id`, hoặc `status` khác `ok`) đối soát với `refund_notice_sent` (`noi_dung_loai = da_hoan`) cùng `trace_id` |
| Luật dừng chi phí: chi phí mỗi việc thành công trong phạm vi | > 6.800 đ trong 2 tuần liên tiếp (đợt chạy thử: 3.414 đ, `simulated`) | `agent_run_completed` (token, tool), `staff_review_decision` (`phut_xem_lai`), `staff_rework_completed` (`phut_lam_lai`), `ticket_closed` và `ticket_reopened` (đếm việc thành công) |
| Luật dừng sử dụng: tỉ lệ bỏ qua gợi ý | > 40% trong 1 tuần (đợt chạy thử `simulated`: 21,1% trong phạm vi) | `agent_suggestion_shown`, `staff_review_decision` |
| Bảng lỗi ca 9 (do người dùng) | > 2% yêu cầu/ngày | `input_validation_failed` chia `request_assigned` |
| Bảng lỗi ca 7 (hệ thống) | > 0 ca, đối soát mỗi giờ | `refund_notice_sent` đối soát với `refund_ledger_write` |
| Bảng lỗi ca 18 (ngữ cảnh) | > 1% đơn đóng/tuần | `ticket_reopened` (`reason`), `refund_amount_audit`, `refund_notice_sent` (`cach_tinh`) |
| Bảng lỗi ca 4 (giới hạn hệ thống) | > 5% ở `noi_dia`/`hang_nang` mỗi tuần | `handoff_to_staff` (`reason`, `loai`) |
| Bảng lỗi ca 17 (ngầm) | ≥ 1% đơn lệch/tuần | `refund_amount_audit`, `agent_run_completed` (`pricing_version`) |

Mọi chỉ số và ngưỡng ở trên đều tính được từ 13 event có `trace_id`; số đối chiếu của đợt chạy thử lấy từ `src/logix_requests.csv` (toàn bộ dữ liệu chạy thử giả lập, `simulated`), và mọi số chi phí có phút nhân viên từ cột `_simulated` đều là `simulated`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Chi phí làm lại gấp đôi | Chi phí mỗi việc thành công **6.787 đ** [simulated], tăng **51,8%** so với 4.472 đ [simulated] | `staff_rework_completed`, tỉ lệ làm lại > 7%/tuần và phút làm lại thực đo | Thu hẹp phạm vi về `noi_dia`, chuyển ca rủi ro cao cho nhân viên; rà 20 trace làm lại | Trưởng nhóm CSKH |
| Tỉ lệ xem lại gấp đôi hoặc phải xem lại 100% | Xem lại gấp đôi: **6.292 đ** (+40,7%); xem lại 100% phạm vi pilot: **11.743 đ** = 0,98× (**12.414 đ** = 1,03× nếu làm lại 15,3 phút) [simulated] | % `duoc_xem_lai` > 50% cuối bước 0,25 hoặc `phut_xem_lai` > 5 phút/ca | Phân tầng yêu cầu xem lại; có lộ trình giảm tỉ lệ xem lại theo bậc khi `sua + bo` < 15% | Giám đốc vận hành LogiX-VN |
| Khối lượng pilot thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng: **+1.185 đ/việc** ở 45.000 YC/tháng, tăng lên **+2.370 đ/việc** (thành 5.784 đ) ở nửa khối lượng [simulated] | Số việc thành công/tuần < 50% kế hoạch | Không mở rộng phạm vi trước khi đủ sản lượng; rà soát lại chi phí hạ tầng cố định | PM trợ lý hoàn phí |

**Cách tính E2 độc lập để đối chiếu B1:** từ 1.624 dòng `src/logix_runs.csv`, chi phí token = 245.585,132 đ và tool = 84.000 đ; từ `src/logix_requests.csv`, xem lại = 1.780.000 đ [simulated], làm lại = 2.264.000 đ [simulated], số việc thành công = 978. Tổng = 4.373.585,132 đ [simulated]. Kịch bản gấp đôi một khoản cộng thêm chính khoản đó vào tổng rồi chia 978; phần trăm tăng = khoản thêm / tổng gốc. Các số trên đã đối chiếu khớp với bảng B1 trong `bang_chi_phi.md` và output của `src/lab13.py`.
