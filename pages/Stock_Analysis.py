import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📊",
    layout="wide",
)

# --------------------------------------------------
# Modern UI Styling
# --------------------------------------------------
st.markdown("""
<style>
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}
.card h4 {
    margin-bottom: 5px;
}
.subtle {
    color: #9CA3AF;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Stock Analysis Dashboard")

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Enter Stock Ticker", value="TSLA").upper().strip()

with col2:
    start_date = st.date_input("Start Date", today - datetime.timedelta(days=365))

with col3:
    end_date = st.date_input("End Date", today)

if start_date >= end_date:
    st.error("End date must be after start date.")
    st.stop()

# --------------------------------------------------
# Load Data (Cached)
# --------------------------------------------------
@st.cache_data(ttl=300)  # cache 5 minutes
def load_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end, progress=False)

try:
    stock = yf.Ticker(ticker)
    info = stock.info
    data = load_data(ticker, start_date, end_date)
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

if data.empty:
    st.warning("No data found for the selected ticker and date range.")
    st.stop()

# Reset index so Date is a column
data.reset_index(inplace=True)

# --------------------------------------------------
# Safely get Close prices as Series
# --------------------------------------------------
close_prices = data["Close"]

# Handle multi-index / single-ticker weirdness in recent yfinance
if isinstance(close_prices, pd.DataFrame):
    # Most common case: columns = MultiIndex with ticker name
    if ticker in close_prices.columns:
        close_prices = close_prices[ticker]
    else:
        # Fallback: take first column
        close_prices = close_prices.iloc[:, 0]

# Final squeeze just in case
close_prices = close_prices.squeeze()

if not isinstance(close_prices, pd.Series):
    st.error("Could not extract Close prices as a Series. Data format issue.")
    st.stop()

# --------------------------------------------------
# Company Info
# --------------------------------------------------
st.markdown("## Company Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card">
    <h3>{info.get('longName', ticker)}</h3>
    <p class="subtle">{info.get('sector', '—')} • {info.get('industry', '—')}</p>
    <p><b>Website:</b> {info.get('website', 'N/A')}</p>
    <p><b>Employees:</b> {info.get('fullTimeEmployees', 'N/A'):,}</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    market_cap = info.get('marketCap')
    pe = info.get('trailingPE')
    
    st.markdown(f"""
    <div class="card">
    <h4>Market Cap</h4>
    <h2>{f"${market_cap:,.0f}" if market_cap else 'N/A'}</h2>
    <hr>
    <h4>P/E Ratio (TTM)</h4>
    <h2>{f"{pe:.2f}" if pe else 'N/A'}</h2>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# KPIs
# --------------------------------------------------
st.markdown("## Key Metrics")

col1, col2, col3 = st.columns(3)

# Daily change
daily_change_pct = close_prices.pct_change() * 100

with col1:
    if len(close_prices) > 1:
        last_change = daily_change_pct.iloc[-1]
        delta_color = "normal" if last_change >= 0 else "inverse"
        st.metric(
            "Daily Change",
            f"{last_change:+.2f}%",
            delta=None,
            delta_color=delta_color
        )
    else:
        st.metric("Daily Change", "N/A")

with col2:
    high_52 = close_prices.max()
    st.metric("52-Week High", f"${high_52:,.2f}")

with col3:
    low_52 = close_prices.min()
    st.metric("52-Week Low", f"${low_52:,.2f}")

# --------------------------------------------------
# Moving Averages
# --------------------------------------------------
data["MA20"] = close_prices.rolling(window=20).mean()
data["MA50"] = close_prices.rolling(window=50).mean()

# --------------------------------------------------
# Price Chart
# --------------------------------------------------
st.markdown("## Price Trend")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data["Date"],
    y=close_prices,
    mode="lines",
    name="Close Price",
    line=dict(width=2.2, color='#6366f1')
))

fig.add_trace(go.Scatter(
    x=data["Date"],
    y=data["MA20"],
    mode="lines",
    name="20-day MA",
    line=dict(dash="dot", color='#10b981')
))

fig.add_trace(go.Scatter(
    x=data["Date"],
    y=data["MA50"],
    mode="lines",
    name="50-day MA",
    line=dict(dash="dash", color='#f59e0b')
))

fig.update_layout(
    template="plotly_dark",
    height=580,
    hovermode="x unified",
    margin=dict(l=10, r=10, t=30, b=10),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Volume Chart
# --------------------------------------------------
st.markdown("## Trading Volume")

vol_fig = go.Figure()

vol_fig.add_trace(go.Bar(
    x=data["Date"],
    y=data["Volume"],
    name="Volume",
    marker_color='#6b7280'
))

vol_fig.update_layout(
    template="plotly_dark",
    height=320,
    margin=dict(l=10, r=10, t=30, b=10),
    xaxis_rangeslider_visible=False
)

st.plotly_chart(vol_fig, use_container_width=True)

# --------------------------------------------------
# News Section
# --------------------------------------------------
st.markdown("## Recent News")

news = stock.news

if news:
    for item in news[:6]:
        pub_time = item.get('providerPublishTime', '')
        if pub_time:
            from datetime import datetime
            pub_time = datetime.fromtimestamp(pub_time).strftime("%b %d, %Y")
        
        st.markdown(f"""
        <div class="card">
        <h4>{item.get('title', '—')}</h4>
        <p class="subtle">{item.get('publisher', '—')} • {pub_time}</p>
        <a href="{item.get('link', '#')}" target="_blank">Read More →</a>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No recent news available at the moment.")

# --------------------------------------------------
# Disclaimer
# --------------------------------------------------
st.markdown("""
<br><br>
⚠️ **Disclaimer:** This dashboard is for educational and informational purposes only.  
It is **not** financial advice. Always do your own research and consult a qualified advisor.
""")