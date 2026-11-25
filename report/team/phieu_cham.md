# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): JQKA · L3B
- Nhóm được chấm: DMTG · L3B (`https://github.com/TDM414/K5-L3B-DAY13-NhomDMTG-LaunchEconomics`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất `Go có điều kiện` khớp số: bắt đầu từ `noi_dia` (`2.696 đ = 0,22×`), chỉ mở `hang_nang` (`8.221 đ = 0,69×`) khi CPS ≤ `8.000 đ` trong 2 tuần; nêu đủ số bất lợi gồm xem lại 100% (`11.743–12.414 đ/việc`, `giả lập`), power `64,2%` ở mức `+5 điểm` và phần cố định tăng lên `2.370 đ/việc` (`5.784 đ`) khi giảm nửa khối lượng, kèm điều kiện xử lý trước `2026-12-06`. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ `_simulated` và số liệu chạy thử trong `ho_so_launch_v0.md`, `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml` đều gắn nhãn `simulated`/`giả lập`; không dùng từ cấm. Phạm vi thu hẹp bằng số (`noi_dia` `0,22×`, `hang_nang` `0,69×`; loại `quoc_te` `1,88×` và `doi_tac` `0,85×`). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Có đối chứng đồng thời, chia ngẫu nhiên theo nhân viên (`seed: 20261207`, phân tầng `depot`), `20` cụm/nhóm (`859` hiệu dụng/nhóm, `299` YC/NV = `5.980` YC gốc/nhóm, `DE = 6,96`, `MDE +6 điểm`). Có `4` luật dừng đủ 4 vế với ngưỡng (`+2 điểm` hoặc `> 6%`, `≥ 1` hoàn trùng, `> 8.000 đ`, `> 40%`), thời hạn, người có quyền dừng và rollback `30 phút`. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp hoàn toàn giữa bằng chứng chi phí, phân tích bất lợi (`11.743–12.414 đ` khi xem lại `100%`, power `64,2%` ở `+5 điểm`), nhãn giả lập đầy đủ và thiết kế pilot có `20` cụm/nhóm cùng `4` luật dừng định lượng. Nhóm cần hoàn tất kiểm thử chống hoàn trùng/đối soát sổ cái trước `2026-12-06`, ký chấp nhận MDE `+6 điểm` (`64,2%` power), và bổ sung 2 event còn thiếu trong `chi_so.md` (`input_validation_failed`, `handoff_to_staff`) để đo đủ bảng lỗi Ca 9, Ca 4 cùng thời gian thực sau tuần đầu.

**Một câu hỏi cho đội trình:** Ngưỡng dừng chi phí nhóm đặt là `> 8.000 đ` trong `2` tuần để quyết định đưa/giữ `hang_nang` (trong khi CPS gốc của riêng `hang_nang` là `8.221 đ` `simulated`), và bảng khắc phục dùng `input_validation_failed` (Ca 9), `handoff_to_staff` (Ca 4) nhưng danh sách 9 event trong `chi_so.md` chưa có 2 event này — nhóm xử lý độ lệch này thế nào trước ngày `2026-12-06`?

**Câu trả lời của đội trình (ghi lại tại buổi):** *(chờ ghi lại câu trả lời của nhóm DMTG tại buổi hỏi đáp Gate 2a)*
