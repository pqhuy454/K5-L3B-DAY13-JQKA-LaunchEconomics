"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng/tháng cho vận hành, giám sát, cập nhật chính sách


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return dict(
        token=float(tien_token.sum()),
        tool=float(tien_tool.sum()),
        chay_lai=float(chay_lai),
        xem_lai=float(xem_lai),
        lam_lai=float(lam_lai),
        tong=float(tong),
        thanh_cong=thanh_cong,
        cps=float(tong / thanh_cong),
        hoa_don_moi_yc=float((tien_token.sum() + tien_tool.sum()) / len(reqs)),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('=== A1 · BA PHÉP THỬ ĐÁP ÁN BIẾT TRƯỚC ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'  p=0.8, k=2      -> E[chạy] = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  p=0.8, k=None   -> E[chạy] = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  p=0.8, k=3      -> Hệ số CPS = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')

    print('\n=== A2 · MÔ HÌNH CHI PHÍ TỪ TRACE (1.200 YÊU CẦU) ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:15s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:15s} {gia_tri:>14,.0f}')
    boi_so_hoa_don = ket_qua['cps'] / ket_qua['hoa_don_moi_yc']
    ti_trong_lam_lai = ket_qua['lam_lai'] / ket_qua['tong'] * 100
    ti_trong_xem_lai = ket_qua['xem_lai'] / ket_qua['tong'] * 100
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'  CPS / hoá đơn mỗi YC     : {boi_so_hoa_don:.1f} lần (simulated)')
    print(f'  Tỉ trọng làm lại / xem lại: {ti_trong_lam_lai:.1f}% / {ti_trong_xem_lai:.1f}% (simulated)')
    print(f'  Chi phí cả hệ thống / YC : {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x baseline, simulated)')

    print('\n=== A3 · TÁCH THEO LOẠI YÊU CẦU ===')
    print(f"{'Loại':12s} {'Số YC':>7s} {'Thành công':>11s} {'Lần chạy/YC':>12s} {'CPS (sim)':>12s} {'So với 12k':>11s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub_reqs = reqs[reqs['loai'] == loai]
        sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        kq_loai = mo_hinh(runs, sub_reqs)
        tl_tc = kq_loai['thanh_cong'] / len(sub_reqs) * 100
        lan_chay_tb = len(sub_runs) / len(sub_reqs)
        so_voi_base = kq_loai['cps'] / BASELINE
        print(f"{loai:12s} {len(sub_reqs):>7d} {tl_tc:>10.1f}% {lan_chay_tb:>12.2f} {kq_loai['cps']:>10,.0f} đ {so_voi_base:>10.2f}x")

    print('\n--- Tỉ lệ lần chạy status == ok theo từng attempt ---')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    bang_attempt = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100
    print(bang_attempt.round(1).to_string())

    print('\n=== A4 · CHI PHÍ CỐ ĐỊNH (PHẠM VI noi_dia + hang_nang) ===')
    pham_vi_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi_reqs)
    print(f"CPS biến đổi trong phạm vi (900/982 YC thành công): {kq_pv['cps']:,.0f} đ (simulated)")
    print(f"{'Khối lượng/tháng':22s} {'Việc TC/tháng':>14s} {'Cố định/việc':>14s} {'CPS + cố định':>15s} {'So với 12k':>11s}")
    for ten_kl, tong_yc_thang in [('45.000 yêu cầu/tháng', 45_000), ('Một nửa (22.500/tháng)', 22_500)]:
        viec_tc_thang = tong_yc_thang * kq_pv['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / viec_tc_thang
        cps_cong_co_dinh = kq_pv['cps'] + co_dinh_moi_viec
        print(f"{ten_kl:22s} {viec_tc_thang:>14,.0f} {co_dinh_moi_viec:>12,.0f} đ {cps_cong_co_dinh:>13,.0f} đ {cps_cong_co_dinh / BASELINE:>10.2f}x")

    print('\n=== B1 · BẢNG ĐỘ NHẠY (ĐỔI TỪNG YẾU TỐ) ===')
    kich_ban_b1 = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại gấp đôi', dict(he_so_xem_lai=2.0)),
        ('Tỉ lệ xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại gấp đôi', dict(he_so_lam_lai=2.0)),
        ('Số ca làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương nhân viên tăng 25%', dict(luong_phut=2500)),
        ('Chỉ cho chạy tối đa 2 lần', dict(max_lan_chay=2)),
        ('Chỉ cho chạy 1 lần', dict(max_lan_chay=1)),
    ]
    cps_goc = ket_qua['cps']
    print(f"{'Kịch bản':28s} {'CPS (sim)':>12s} {'Thay đổi':>10s} {'Thành công':>11s}")
    for ten_kb, tham_so in kich_ban_b1:
        kq_kb = mo_hinh(runs, reqs, **tham_so)
        thay_doi = (kq_kb['cps'] / cps_goc - 1.0) * 100
        print(f"{ten_kb:28s} {kq_kb['cps']:>10,.0f} đ {thay_doi:>+9.1f}% {kq_kb['thanh_cong']:>11d}")

    print('\n=== B2 · ĐỔI MỘT CẶP VÀ XẾP HẠNG ===')
    kq_b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    print(f"Giá token ×2 + Xem lại ×2: {kq_b2['cps']:,.0f} đ ({(kq_b2['cps'] / cps_goc - 1.0) * 100:+.1f}%, simulated)")
    print('Xếp hạng 3 yếu tố mạnh nhất: 1. Số ca làm lại · 2. Tỉ lệ xem lại · 3. Lương nhân viên')

    print('\n=== B3 · GIỚI HẠN CHẠY LẠI VÀ CHI PHÍ CẢ HỆ THỐNG ===')
    print(f"{'Giới hạn':10s} {'Tổng trợ lý (sim)':>18s} {'Không TC':>10s} {'Cả hệ thống (sim)':>19s} {'CPS (sim)':>12s}")
    for gh in [1, 2, 3]:
        kq_gh = mo_hinh(runs, reqs, max_lan_chay=gh)
        khong_thanh_cong = len(reqs) - kq_gh['thanh_cong']
        ca_he_thong = kq_gh['tong'] + khong_thanh_cong * BASELINE
        print(f"{f'{gh} lần':10s} {kq_gh['tong']:>16,.0f} đ {khong_thanh_cong:>10d} {ca_he_thong:>17,.0f} đ {kq_gh['cps']:>10,.0f} đ")

    print('\n=== B4 · NẾU PHẢI XEM LẠI TẤT CẢ (noi_dia + hang_nang) ===')
    pv_runs = runs[runs['request_id'].isin(pham_vi_reqs['request_id'])]
    so_yc_chay_ok = pv_runs[pv_runs['status'] == 'ok']['request_id'].nunique()
    so_ca_lam_lai = int((pham_vi_reqs['ket_qua'] == 'lam_lai').sum())
    tien_tok_tool_pv = kq_pv['token'] + kq_pv['tool']
    tien_xem_100 = so_yc_chay_ok * 5 * LUONG_PHUT
    tien_lam_lai_9p = so_ca_lam_lai * 9 * LUONG_PHUT
    cps_b4_9p = (tien_tok_tool_pv + tien_xem_100 + tien_lam_lai_9p) / kq_pv['thanh_cong']

    phut_ll_tb = round(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean(), 1)
    cps_b4_thuc = (tien_tok_tool_pv + tien_xem_100 + so_ca_lam_lai * phut_ll_tb * LUONG_PHUT) / kq_pv['thanh_cong']
    hoa_von_9p = (BASELINE * kq_pv['thanh_cong'] - tien_tok_tool_pv - tien_lam_lai_9p) / (so_yc_chay_ok * LUONG_PHUT)
    hoa_von_thuc = (BASELINE * kq_pv['thanh_cong'] - tien_tok_tool_pv - so_ca_lam_lai * phut_ll_tb * LUONG_PHUT) / (so_yc_chay_ok * LUONG_PHUT)
    print(f"YC có ít nhất 1 lần ok: {so_yc_chay_ok} | Ca làm lại: {so_ca_lam_lai} | Việc thành công: {kq_pv['thanh_cong']}")
    print(f"CPS xem lại 100% (9 phút làm lại)   : {cps_b4_9p:,.0f} đ ({cps_b4_9p / BASELINE:.2f}x baseline, simulated)")
    print(f"CPS xem lại 100% ({phut_ll_tb} phút làm lại): {cps_b4_thuc:,.0f} đ ({cps_b4_thuc / BASELINE:.2f}x baseline, simulated)")
    print(f"Phút xem lại hoà vốn tối đa         : {hoa_von_9p:.1f} phút (với 9p) | {hoa_von_thuc:.1f} phút (với {phut_ll_tb}p)")

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
