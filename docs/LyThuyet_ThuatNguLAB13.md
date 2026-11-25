# Lý thuyết và thuật ngữ Lab 13

## A · Chi phí

**Lần chạy (run)**: mỗi lần agent xử lý một yêu cầu. Lần chạy có thể lỗi, khi đó agent chạy lại, tối đa 3 lần. Vì vậy 1.200 yêu cầu sinh ra 1.624 lần chạy.

**Trace / `trace_id`**: bản ghi chi tiết của một lần chạy, gồm token vào và ra, số lần gọi tool, trạng thái. `trace_id` là mã định danh để nối các event của cùng một lần chạy với nhau.

**Token, tool call**: token là đơn vị chữ mà model đọc (đầu vào) và viết (đầu ra), tính tiền theo 1.000 token. Tool call là mỗi lần agent gọi hệ thống ngoài (tra đơn, ghi sổ…), tính tiền theo lần.

**Xem lại / làm lại**:
- *Xem lại*: nhân viên kiểm tra câu trả lời của agent rồi chọn **giữ**, **sửa** hoặc **bỏ**.
- *Làm lại*: agent trả lời sai, nhân viên phải làm lại từ đầu.

Cả hai tính bằng phút nhân viên × 2.000 đ.

**Chi phí mỗi việc thành công (cost-of-pass)** là khái niệm trung tâm của bài:

```
(token + tool + xem lại + làm lại) ÷ số yêu cầu thành công
```

- **Tử số tính mọi lần chạy**, vì lần chạy lỗi vẫn phải trả tiền.
- **Mẫu số chỉ đếm việc thành công**, vì chỉ việc thành công mới có giá trị.

Ví dụ: trả 100 đ cho 10 lần chạy nhưng chỉ 5 lần đúng, thì mỗi việc thành công tốn 20 đ chứ không phải 10 đ.

**Hoá đơn token**: chỉ là tiền token và tool, khoảng 275 đ/yêu cầu. Chi phí thật khoảng 4.472 đ, gấp 16 lần, vì phải cộng giờ nhân viên. Đây là cái bẫy chính bài muốn chỉ ra.

**Baseline**: phương án hiện tại để so sánh, ở đây là nhân viên tự làm, 6 phút = 12.000 đ/yêu cầu. Kết quả "0,49×" nghĩa là chi phí bằng 49% baseline.

**Chi phí cả hệ thống**: chi phí của trợ lý cộng thêm 12.000 đ cho mỗi ca thất bại, vì nhân viên phải làm thay. Nếu không cộng phần này, trợ lý trông rẻ hơn thực tế.

**Chi phí cố định**: 40 triệu đ/tháng, không đổi dù xử lý nhiều hay ít. Khối lượng càng nhỏ thì phần cố định chia cho mỗi việc càng lớn.

### A1 · Toán chạy lại
Giả sử mỗi lần chạy đúng với xác suất **p**, và được chạy tối đa **k** lần:
- **Tỉ lệ thành công** = 1 − (1−p)^k. Thất bại nghĩa là sai cả k lần.
- **Số lần chạy trung bình** = (1 − (1−p)^k) / p.
- **Hệ số chi phí** = số lần chạy ÷ tỉ lệ thành công = **1/p**, không phụ thuộc k.

Ví dụ với p = 0,8: tối đa 2 lần thì trung bình 1,20 lần chạy; chạy đến khi đúng thì trung bình 1,25 lần; hệ số chi phí là 1,25.

Công thức này **giả định các lần chạy độc lập**. Dữ liệu thật thì khác: với loại `quoc_te`, lần 1 đúng 30%, lần 2 đúng 11%, lần 3 đúng 2%. Lỗi lặp lại trên cùng một yêu cầu, nên chạy lại chỉ tốn thêm tiền.

## B · Độ nhạy

**Phân tích độ nhạy (sensitivity analysis)**: đổi **một** yếu tố, giữ nguyên các yếu tố khác, xem chi phí thay đổi bao nhiêu phần trăm. Yếu tố làm chi phí đổi nhiều nhất là thứ pilot phải theo dõi sát.

**Mô hình tuyến tính**: chi phí là tổng các khoản cộng lại. Vì vậy:
- Gấp đôi một khoản thì chi phí tăng bằng tỉ trọng của khoản đó (+X%). Giảm nửa thì giảm đúng một nửa mức đó (−X/2%).
- Đổi một cặp yếu tố thì tác động bằng tổng hai tác động riêng (B2).

**Kịch bản giới hạn số lần chạy (B3)**: cho chạy ít lần thì rẻ hơn mỗi việc, nhưng nhiều ca thất bại hơn và nhân viên phải gánh. Tối ưu một chỉ số riêng lẻ có thể làm hại tổng thể.

**Điểm hoà vốn (break-even)**: mức mà tại đó chi phí bằng baseline. Ví dụ, nếu xem lại 100% thì mỗi lần xem lại phải ≤ 5 phút mới còn rẻ hơn nhân viên tự làm.

## C · Phân loại lỗi (Google PAIR)

| Loại | Nghĩa | Ví dụ |
|---|---|---|
| **Do người dùng** | Khách nhập sai hoặc chọn sai | Nhập nhầm mã đơn |
| **Hệ thống** | Trợ lý làm sai thiết kế hoặc chính sách, và có người thấy | Báo "đã hoàn" khi sổ cái chưa ghi |
| **Ngữ cảnh** | Làm đúng nhưng khách thấy sai | Số tiền đúng chính sách nhưng khách không hiểu cách tính |
| **Giới hạn hệ thống** | Không thể làm được: thiếu dữ liệu, ngoài phạm vi | Đơn quốc tế thiếu thông tin |
| **Ngầm (latent)** | Sai nhưng không ai nhận ra, chỉ lộ khi kiểm tra mẫu | Dùng bảng giá cũ suốt 3 tuần |

**Nguyên nhân gốc (root cause)**: gắn nhãn theo *vì sao lỗi xảy ra*, không theo *chỗ cần sửa*. Khách nhập sai mã là lỗi do người dùng, dù trợ lý có thể gợi ý tốt hơn.

**Gắn nhãn độc lập và tỉ lệ đồng thuận (inter-rater agreement)**: hai người tự gắn nhãn riêng, rồi tính tỉ lệ đồng thuận = số ca trùng ÷ 20. Tỉ lệ ≥ 80% cho thấy định nghĩa các loại đủ rõ. Nếu thấp hơn, định nghĩa đang mơ hồ và phải viết lại.

**Cách phát hiện đo được**: mỗi cách phát hiện phải có **event** (cái được ghi lại), **ngưỡng** (bao nhiêu thì báo động) và **tần suất** (bao lâu kiểm tra một lần). "Theo dõi kỹ" không tính là đo được.

## D · Thiết kế pilot (thống kê thí nghiệm)

**Pilot**: chạy thật ở quy mô nhỏ, có kiểm soát, để ra quyết định có mở rộng hay không.

**Nhóm can thiệp và nhóm đối chứng (treatment / control)**: nhóm can thiệp dùng trợ lý, nhóm đối chứng làm như cũ, cả hai **chạy cùng thời gian**. Có đối chứng mới tách được tác động của trợ lý khỏi các yếu tố khác như mùa vụ hay chính sách mới.

**Ngẫu nhiên hoá (randomization)**: bốc thăm ai vào nhóm nào bằng code, có seed ghi trước. Không để quản lý tự chọn, vì họ có thể chọn người giỏi, làm kết quả bị lệch.

**Phân tầng (stratification)**: bốc thăm riêng trong từng depot, để mỗi depot đều có người ở cả hai nhóm.

**Ảnh hưởng tràn (spillover)**: nhóm đối chứng "lây" tác động từ nhóm can thiệp, ví dụ đồng nghiệp chia sẻ câu trả lời của trợ lý. Khi đó khoảng cách giữa hai nhóm bị nhỏ đi.

**Các tham số cỡ mẫu**:
- **Baseline 0,70**: chỉ số chính hiện tại.
- **MDE (mức chênh nhỏ nhất muốn phát hiện)**: +5 điểm, tức từ 0,70 lên 0,75.
- **α = 0,05**: chấp nhận 5% rủi ro kết luận "có tác dụng" khi thật ra không có (dương tính giả).
- **Power = 0,8**: nếu tác động thật sự tồn tại, có 80% khả năng thí nghiệm phát hiện ra. Power thấp thì dễ bỏ sót tác động thật.
- **Cỡ mẫu**: cần khoảng **1.251 yêu cầu mỗi nhóm** nếu các yêu cầu độc lập với nhau.

**Chia theo cụm (cluster randomization)**: chia theo nhân viên hoặc depot thay vì từng yêu cầu. Các yêu cầu của cùng một nhân viên giống nhau (cùng tay nghề, cùng thói quen), nên chúng không độc lập.

**ICC (hệ số tương quan nội cụm)**: mức độ giống nhau giữa các yêu cầu trong cùng một cụm. ICC = 0,02 nghĩa là giống nhau ít, nhưng vẫn có tác động lớn khi cụm đông.

**Hệ số thiết kế (design effect, DE)** = 1 + (m − 1) × ICC, với m là số yêu cầu mỗi cụm. Ví dụ m = 75 thì DE = 2,48: cần gấp 2,48 lần mẫu so với khi chia từng yêu cầu.

**Cỡ mẫu hiệu dụng** = c × m ÷ DE, với c là số cụm. Giá trị này **luôn nhỏ hơn c / ICC**, dù mỗi cụm có bao nhiêu yêu cầu đi nữa. Vì vậy **số cụm mới là thứ quyết định**:
- 20 nhân viên mỗi nhóm thì tối đa 1.000 < 1.251, không đủ.
- 6 depot mỗi nhóm thì tối đa 300, quá ít.

Quy tắc kinh nghiệm là cần **≥ 20 cụm mỗi nhóm**.

**Đánh đổi**: không đủ mẫu cho 5 điểm thì chấp nhận MDE 6 điểm, khi đó cần 859 mỗi nhóm và m ≥ 299. Cái giá là nếu tác động thật chỉ 5 điểm thì power chỉ còn 0,64. Hồ sơ phải nói rõ điều này.

**Rollout theo bậc**: mở dần 10% → 25% → 50%. Mỗi bậc phải đạt điều kiện mới được lên bậc tiếp.

**Luật dừng (stop rule)**: viết trước khi bắt đầu, đủ 4 vế:
- **NẾU** [chỉ số vượt ngưỡng]
- **TRONG** [bao lâu]
- **THÌ** [ai làm gì]
- **KHÔNG THÌ** [điều bị cấm]

Ngưỡng phải đặt dựa trên mức hiện tại. Tỉ lệ mở lại đang là 4,25%, nên đặt ngưỡng 3% thì pilot dừng ngay.

**Interim look**: những lần xem kết quả giữa chừng. Phải định trước sẽ xem khi nào, để tránh xem liên tục rồi dừng khi thấy kết quả "đẹp".

**Rollback**: cách tắt trợ lý và quay về quy trình cũ, có người được quyền bấm tắt.

## E · Chỉ số và hồ sơ

**Chỉ số chính (primary metric)**: thứ quyết định thành công, ở đây là % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày. Trong đợt chạy thử là 82,83%.

**Chỉ số dùng (adoption)**: nhân viên có tin và dùng gợi ý của trợ lý không. Ví dụ tỉ lệ sửa hoặc bỏ gợi ý là 27%.

**Chỉ số an toàn (guardrail)**: chỉ số không được xấu đi, dù chỉ số chính có tốt lên. Ví dụ tỉ lệ mở lại trong 7 ngày là 4,25%.

**Event**: bản ghi một sự kiện, ví dụ "nhân viên bấm sửa", có `trace_id` để truy ngược về lần chạy. Nếu một chỉ số không tính được từ danh sách event thì nó **chưa đo được**.

**Rủi ro kinh tế**: kịch bản xấu kèm con số lấy từ bảng độ nhạy. Ví dụ: làm lại tăng gấp đôi thì chi phí tăng 51,8%.

**Simulated**: số tính từ các cột phút giả lập, chưa phải số đo thật, nên phải ghi nhãn để người đọc biết mức độ tin cậy.

**Tương quan và nhân quả**: không có đối chứng thì chỉ nói được "chỉ số trong đợt chạy thử là…". Không được nói "trợ lý đã nâng chỉ số", vì chưa chứng minh được trợ lý là nguyên nhân.

**Gate 2a / Go – Go có điều kiện – No-go**: cổng duyệt có cho chạy pilot hay không. "Go có điều kiện" phải kèm điều kiện cụ thể, người phụ trách và ngày kiểm tra.

## Một câu xuyên suốt
Bài dạy cách **đánh giá agent như một khoản đầu tư**:
- Tính đủ chi phí thật (A).
- Biết chi phí phụ thuộc vào đâu (B).
- Hiểu nó hỏng ra sao (C).
- Thiết kế thí nghiệm để chứng minh hiệu quả một cách trung thực (D).
- Gói tất cả thành một quyết định có bằng chứng (E).