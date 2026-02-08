import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Stock Analysis & Forecasting",
    page_icon="📈",
    layout="wide",
)


# Global Styling (Modern Fintech UI)
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.hero-title {
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 10px;
}
.hero-subtitle {
    font-size: 20px;
    color: #9CA3AF;
    margin-bottom: 40px;
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    height: 100%;
}
.card h3 {
    margin-bottom: 10px;
}
.card p {
    color: #9CA3AF;
}
.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 60px;
    margin-bottom: 20px;
}
.footer {
    color: #6B7280;
    font-size: 14px;
    margin-top: 80px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown(
    """
    <div>
        <div class="hero-title">📈 Stock Analysis & Forecasting Platform</div>
        <div class="hero-subtitle">
            Analyze market trends, explore financial insights, and forecast stock prices
            using data-driven models and interactive dashboards.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📊 Market Analysis</h3>
        <p>
        Explore historical stock prices, key financial metrics, and company fundamentals
        through interactive visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📈 Price Forecasting</h3>
        <p>
        Predict future stock prices using time-series forecasting models like ARIMA,
        designed for short-term trend analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>⚡ Real-Time Data</h3>
        <p>
        Fetch live and historical market data directly from Yahoo Finance
        for accurate and up-to-date insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

# How It Works Section
st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4>1️⃣ Select a Stock</h4>
        <p>Enter a stock ticker symbol to retrieve real-time and historical market data.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>2️⃣ Analyze Trends</h4>
        <p>Visualize price movements, key metrics, and company information.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>3️⃣ Forecast Prices</h4>
        <p>Use time-series models to forecast future stock price trends.</p>
    </div>
    """, unsafe_allow_html=True)


# Call to Action
st.markdown('<div class="section-title">Get Started</div>', unsafe_allow_html=True)

st.info(
    "👉 Use the sidebar to navigate to **Stock Analysis** or **Stock Prediction** and start exploring the market."
)

# Footer
st.markdown("""
<div class="footer">
⚠️ Disclaimer: This application is for educational purposes only and does not constitute financial advice.
</div>
""", unsafe_allow_html=True)
