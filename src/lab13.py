"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

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


# ---------- Nhiệm vụ D1 · Cỡ mẫu và thiết kế cụm ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ độc lập (kiểm định 2 phía)."""
    za = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2.0
    tu_so = za * math.sqrt(2.0 * pb * (1.0 - pb)) + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))
    return math.ceil((tu_so ** 2) / ((p2 - p1) ** 2))


def he_so_thiet_ke(m, icc=0.02):
    """Design Effect (DE) = 1 + (m - 1) * ICC."""
    return 1.0 + (m - 1.0) * icc


def co_mau_hieu_dung_toi_da(so_cum, icc=0.02):
    """Giới hạn trên của cỡ mẫu hiệu dụng c * m / DE khi m -> vô cùng là c / ICC."""
    return so_cum / icc


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

    print('\n=== D1 · CỠ MẪU THEO BA CÁCH CHIA (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ===')
    icc = 0.02
    n_5pt = co_mau(0.70, 0.75, alpha=0.05, power=0.80)
    de_m75 = he_so_thiet_ke(75, icc)
    n_cluster_m75 = math.ceil(n_5pt * de_m75)
    so_nv_moi_nhom_m75 = math.ceil(n_cluster_m75 / 75)
    n_eff_max_20nv = co_mau_hieu_dung_toi_da(20, icc)
    n_eff_max_6depot = co_mau_hieu_dung_toi_da(6, icc)

    n_6pt = co_mau(0.70, 0.76, alpha=0.05, power=0.80)
    # Giải bất phương trình: 20 * m / (1 + (m - 1) * 0.02) >= n_6pt
    m_toi_thieu_6pt = math.ceil(n_6pt * (1.0 - icc) / (20.0 - n_6pt * icc))
    de_6pt = he_so_thiet_ke(m_toi_thieu_6pt, icc)

    # Power thực tế ở mức chênh +5 điểm (0.70 -> 0.75) khi cỡ mẫu hiệu dụng chỉ đạt n_6pt = 859
    es_5pt = abs(proportion_effectsize(0.75, 0.70))
    power_thuc_5pt = NormalIndPower().power(effect_size=es_5pt, nobs1=n_6pt, alpha=0.05, ratio=1.0)

    print(f"  a) Chia theo yêu cầu (+5 điểm, 0.70 -> 0.75) : {n_5pt:,d} yêu cầu/nhóm")
    print(f"  b) Theo nhân viên (m=75, DE={de_m75:.2f})            : {n_cluster_m75:,d} yêu cầu/nhóm (~{so_nv_moi_nhom_m75} NV/nhóm, tổng {so_nv_moi_nhom_m75 * 2} > 40 -> không đủ người)")
    print(f"  c) 20 nhân viên/nhóm (giới hạn c/ICC)         : tối đa {n_eff_max_20nv:,.0f} < {n_5pt:,d} -> không đạt cho +5 điểm")
    print(f"  d) 6 depot/nhóm (giới hạn c/ICC)              : tối đa {n_eff_max_6depot:,.0f} < {n_5pt:,d} -> không đạt")
    print(f"  e) Mức chênh +6 điểm ({n_6pt} YC/nhóm), 20 NV/nhóm: cần m >= {m_toi_thieu_6pt} YC/nhân viên (DE = {de_6pt:.2f})")
    print(f"  -> Đánh đổi: với n_eff = {n_6pt}, nếu tác động thật chỉ +5 điểm thì power thực tế = {power_thuc_5pt:.2f}")

    tl_mo_lai_toan_bo = (reqs['mo_lai_trong_7_ngay'] == 1).mean() * 100
    tl_mo_lai_pham_vi = (pham_vi_reqs['mo_lai_trong_7_ngay'] == 1).mean() * 100
    print(f"  -> Tỉ lệ mo_lai_trong_7_ngay hiện tại: {tl_mo_lai_toan_bo:.2f}% ({int((reqs['mo_lai_trong_7_ngay'] == 1).sum())}/{len(reqs)} toàn mẫu) | {tl_mo_lai_pham_vi:.2f}% (trong noi_dia + hang_nang)")

    print('\n=== E1 · TÍNH THỬ BA CHỈ SỐ TRÊN 1.200 YÊU CẦU ===')
    cs_chinh_mask = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    cs_chinh = cs_chinh_mask.mean() * 100
    xem_reqs = reqs[reqs['duoc_xem_lai'] == 1]
    cs_bo_qua_mask = xem_reqs['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    cs_bo_qua = cs_bo_qua_mask.mean() * 100
    cs_an_toan_mask = reqs['mo_lai_trong_7_ngay'] == 1
    cs_an_toan = cs_an_toan_mask.mean() * 100

    print(f"  1. Chỉ số chính (% đóng <=24h & không mở lại 7 ngày): {cs_chinh:.2f}% ({int(cs_chinh_mask.sum())}/{len(reqs)})")
    print(f"  2. Chỉ số dùng  (Tỉ lệ sửa + bỏ / số được xem lại)   : {cs_bo_qua:.2f}% ({int(cs_bo_qua_mask.sum())}/{len(xem_reqs)})")
    print(f"  3. Chỉ số an toàn (Tỉ lệ mở lại trong 7 ngày)        : {cs_an_toan:.2f}% ({int(cs_an_toan_mask.sum())}/{len(reqs)})")
