



import streamlit as st

st.set_page_config(
    page_title="Lal Kitab Payment",
    layout="centered"
)

# ==========================
# CHANGE THESE
# ==========================

RAZORPAY_URL = "https://rzp.io/rzp/dD6MMJb"

KUNDALI_APP_URL = "https://lalkitab.streamlit.app"

# ==========================
# UI
# ==========================

st.title("🔮 Lal Kitab AI Astrology")

st.markdown("---")

st.subheader("Premium Kundali Report")

st.write("""
✅ Complete Birth Chart

✅ Lal Kitab Analysis

✅ Yogas & Doshas

✅ Career Analysis

✅ Marriage Analysis

✅ Wealth Analysis

✅ Remedies

✅ PDF Report
""")

st.markdown("---")

st.success("💰 Report Charges: ₹299")

st.link_button(
    "💳 Pay Now",
    RAZORPAY_URL
)

st.markdown("---")

if st.button("✅ Payment Completed"):

    st.success("Payment Confirmed")

    st.markdown(
        f"""
        <meta http-equiv="refresh" content="2;url={KUNDALI_APP_URL}">
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🔮 Open Kundali Generator",
        KUNDALI_APP_URL
    )
