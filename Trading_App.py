import streamlit as st

# ────────────────────────────────────────────────
# Page Config
# ────────────────────────────────────────────────
st.set_page_config(
    page_title="StockVision • Analysis & Forecasting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ────────────────────────────────────────────────
# Modern Fintech + Glassmorphism Styling
# ────────────────────────────────────────────────
st.markdown("""
<style>
    /* Global */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #0e1117 100%);
    }
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
    }

    /* Hero */
    .hero-container {
        text-align: center;
        padding: 5rem 1rem 4rem;
        background: linear-gradient(180deg, rgba(30,41,59,0.4) 0%, rgba(15,23,42,0) 100%);
        border-radius: 24px;
        margin-bottom: 3rem;
    }
    .hero-title {
        font-size: 4.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #c084fc, #60a5fa, #38bdf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        line-height: 1.05;
    }
    .hero-subtitle {
        font-size: 1.35rem;
        color: #94a3b8;
        max-width: 780px;
        margin: 0 auto 2.5rem;
        line-height: 1.6;
    }

    /* Cards */
    .feature-card {
        background: rgba(30, 41, 59, 0.45);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 2rem 1.8rem;
        height: 100%;
        transition: all 0.28s ease;
        box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.35);
        border-color: rgba(139, 92, 246, 0.3);
    }
    .feature-icon {
        font-size: 2.8rem;
        margin-bottom: 1.2rem;
        display: block;
    }
    .feature-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #e2e8f0;
    }
    .feature-text {
        color: #94a3b8;
        line-height: 1.6;
    }

    /* Steps */
    .step-card {
        text-align: center;
        position: relative;
    }
    .step-number {
        width: 64px;
        height: 64px;
        background: linear-gradient(135deg, #8b5cf6, #3b82f6);
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        font-weight: 800;
        margin: 0 auto 1.4rem;
        box-shadow: 0 10px 25px rgba(59,130,246,0.35);
    }
    .step-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    /* CTA */
    .cta-button {
        background: linear-gradient(90deg, #8b5cf6, #60a5fa);
        color: white !important;
        font-weight: 600;
        padding: 1rem 2.2rem !important;
        border-radius: 999px !important;
        font-size: 1.15rem !important;
        border: none !important;
        transition: all 0.3s ease;
        box-shadow: 0 10px 25px rgba(139,92,246,0.4) !important;
        margin: 1.5rem 0.8rem;
    }
    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(139,92,246,0.55) !important;
    }

    /* Section Titles */
    .section-title {
        font-size: 2.6rem;
        font-weight: 800;
        text-align: center;
        margin: 5rem 0 3rem;
        background: linear-gradient(90deg, #e0f2fe, #c084fc, #a5b4fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.95rem;
        margin-top: 6rem;
        padding: 2rem 0;
        border-top: 1px solid rgba(255,255,255,0.08);
    }
</style>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Hero Section
# ────────────────────────────────────────────────
st.markdown("""
<div class="hero-container">
    <div class="hero-title">StockVision</div>
    <div class="hero-subtitle">
        Advanced stock analysis, interactive visualizations<br>
        and intelligent short-term price forecasting — all in one place.
    </div>
</div>
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Features
# ────────────────────────────────────────────────
st.markdown('<div class="section-title">Powerful Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1], gap="medium")

with col1:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">📊</span>
        <div class="feature-title">Deep Market Analysis</div>
        <p class="feature-text">
            Historical price trends, technical indicators, volume analysis,
            moving averages, key financial ratios and company fundamentals.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">🧠</span>
        <div class="feature-title">Smart Forecasting</div>
        <p class="feature-text">
            Time-series forecasting with ARIMA, Prophet & simple ML models.
            Generate short-term price predictions with confidence intervals.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <span class="feature-icon">⚡</span>
        <div class="feature-title">Live Market Data</div>
        <p class="feature-text">
            Real-time & historical data from Yahoo Finance.
            News sentiment, analyst ratings, insider activity & more.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────
# How It Works
# ────────────────────────────────────────────────
st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">1</div>
        <div class="step-title">Choose a Stock</div>
        <p style="color:#94a3b8;">Enter any ticker symbol (e.g. AAPL, TSLA, NVDA)</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">2</div>
        <div class="step-title">Explore & Analyze</div>
        <p style="color:#94a3b8;">Interactive charts, metrics, financials & news</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">3</div>
        <div class="step-title">Forecast Future</div>
        <p style="color:#94a3b8;">View predicted price trends & ranges</p>
    </div>
    """, unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Call to Action
# ────────────────────────────────────────────────
st.markdown('<div style="text-align:center; margin: 5rem 0 3rem;">', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1,2,1])

with col_center:
    st.markdown("""
    <a href="#Stock Analysis" target="_self">
        <div class="cta-button">Start Analyzing Stocks →</div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown("""
    <a href="#Stock Prediction" target="_self">
        <div class="cta-button" style="background: linear-gradient(90deg, #ec4899, #f43f5e);">
            Try Price Forecasting →
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ────────────────────────────────────────────────
# Footer / Disclaimer
# ────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    ⚠️ This platform is created for educational and research purposes only.<br>
    Not financial advice — always conduct your own due diligence.
    <br><br>
    Built with Streamlit • Data from Yahoo Finance • 2025–2026
</div>
""", unsafe_allow_html=True)