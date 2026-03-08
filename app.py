import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from live_data_fetch import fetch_live_company_data
from model import generate_live_investment_score
st.set_page_config(
    page_title="Live Share Market Investment Predictor",
    page_icon="💹",
    layout="centered"
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.card {
    background-color: #111827;
    padding: 24px;
    border-radius: 16px;
    margin-top: 20px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.35);
}

.title-box {
    background: linear-gradient(135deg, #2563EB, #1E40AF);
    padding: 28px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 35px;
}

.subtext {
    font-size: 15px;
    color: #CBD5E1;
}

.metric-label {
    font-size: 14px;
    color: #9CA3AF;
}

.metric-value {
    font-size: 26px;
    font-weight: 700;
    color: #F9FAFB;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="title-box">
    <h1>💹Live Share Market Investment Predictor</h1>
    <p class="subtext">
        Real-time investment scoring using live market price positioning & stability indicators
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("🔍Company Input")

company_input = st.text_input(
    "Enter NSE Company",
    placeholder="Example: TCS, INFY, WIPRO"
)


if company_input.strip():

    company = company_input.upper().strip()
    if not company.endswith(".NS"):
        company += ".NS"

    with st.spinner("Fetching live market data..."):
        data = fetch_live_company_data(company)

    if data is None:
        st.error("Live market data is currently unavailable for this company.")
    else:
        score = generate_live_investment_score(data)

        if score >= 70:
            category = "Strong"
            emoji = "🟢"
        elif score >= 40:
            category = "Moderate"
            emoji = "🟡"
        else:
            category = "Weak"
            emoji = "🔴"

        st.markdown(f"""
        <div class="card">
            <div class="metric-label">Company</div>
            <div class="metric-value">{company}</div>
            <br>
            <div class="metric-label">Investment Score</div>
            <div class="metric-value">{score} / 100</div>
            <br>
            <div class="metric-label">Category</div>
            <div class="metric-value">{emoji} {category}</div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📘How is this score calculated?"):
            st.markdown("""
            **Scoring Components**

            • **Price Position (60%)**  
            Measures where the current price lies within its 52-week range.

            • **Market Capitalization (40%)**  
            Represents company stability and long-term strength.

            This score indicates **relative investment attractiveness**  
            and is intended **for educational analysis only**.
            """)

st.markdown("---")
st.caption(
    "Final Year Project • Live Data via Yahoo Finance • Educational Use Only (Not Financial Advice)"
)