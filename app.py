import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Công cụ tính lãi suất tiết kiệm_Nguyễn Mai Thảo",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰Công cụ tính lãi suất tiết kiệm_Nguyễn Mai Thảo")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=10_000_000,
    step=1_000_000,
    format="%d"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# =========================
# TÍNH TOÁN
# =========================

# Lãi suất chuyển sang dạng thập phân
lai_suat_nam = lai_suat / 100

# Số tháng trong kỳ hạn
so_thang = ky_han

# Tổng tiền lãi
tong_tien_lai = tien_gui * lai_suat_nam * (so_thang / 12)

# Số kỳ nhận lãi
if hinh_thuc == "Cuối kỳ":
    so_ky = 1

elif hinh_thuc == "Hàng tháng":
    so_ky = so_thang

else:  # Hàng quý
    so_ky = so_thang / 3

# Tiền lãi định kỳ
tien_lai_dinh_ky = tong_tien_lai / so_ky

# Tổng tiền gốc + lãi
tong_tien = tien_gui + tong_tien_lai

# =========================
# HIỂN THỊ KẾT QUẢ
# =========================

st.subheader("📊 Kết quả")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "💰 Tiền lãi định kỳ",
        f"{tien_lai_dinh_ky:,.0f} VNĐ"
    )

with col2:
    st.metric(
        "📈 Tổng tiền lãi",
        f"{tong_tien_lai:,.0f} VNĐ"
    )

st.metric(
    "💵 Tổng tiền gốc + tiền lãi",
    f"{tong_tien:,.0f} VNĐ"
)

# =========================
# CHI TIẾT
# =========================

st.divider()

st.subheader("📋 Chi tiết khoản gửi")

st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
st.write(f"**Kỳ hạn:** {ky_han} tháng")
st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

# =========================
# GHI CHÚ
# =========================

st.info(
    "💡 Công thức sử dụng: Tiền lãi = Tiền gốc × Lãi suất năm × (Số tháng / 12). "
    "Đây là cách tính lãi đơn, chưa tính trường hợp tái tục hoặc nhập lãi vào gốc."
)
