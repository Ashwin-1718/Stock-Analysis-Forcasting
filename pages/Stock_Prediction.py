import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
from statsmodels.tsa.arima.model import ARIMA

# Page Configuration
st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Stock Price Prediction")

# User Inputs
col1, col2, col3 = st.columns(3)
today = datetime.date.today()

with col1:
    stock_symbol = st.text_input(
        "Enter Stock Ticker Symbol", value="AAPL"
    ).upper()

with col2:
    start_date = st.date_input(
        "Training Start Date",
        value=today - datetime.timedelta(days=365 * 2),
    )

with col3:
    forecast_days = st.number_input(
        "Forecast Days",
        min_value=1,
        max_value=90,
        value=30,
    )

# --------------------------------------------------
# Cached Data Loader
# --------------------------------------------------
@st.cache_data(show_spinner=False)
def load_stock_data(symbol, start):
    data = yf.download(symbol, start=start)
    data.reset_index(inplace=True)
    return data

# --------------------------------------------------
# Main Logic
# --------------------------------------------------
if stock_symbol:
    try:
        stock_data = load_stock_data(stock_symbol, start_date)

        if stock_data.empty:
            st.warning("No data found for this stock symbol.")
            st.stop()

        st.subheader(f"{stock_symbol} Price Forecast")

        # --------------------------------------------------
        # Prepare Time Series
        # --------------------------------------------------
        ts_data = stock_data[["Date", "Close"]].dropna()
        ts_data.set_index("Date", inplace=True)

        # --------------------------------------------------
        # Train ARIMA Model
        # --------------------------------------------------
        with st.spinner("Training forecasting model..."):
            model = ARIMA(ts_data["Close"], order=(5, 1, 0))
            model_fit = model.fit()

        # --------------------------------------------------
        # Forecast
        # --------------------------------------------------
        forecast = model_fit.forecast(steps=forecast_days)

        forecast_dates = pd.date_range(
            start=ts_data.index[-1] + pd.Timedelta(days=1),
            periods=forecast_days,
            freq="B",
        )

        forecast_df = pd.DataFrame(
            {"Forecast": forecast.values},
            index=forecast_dates,
        )

        # --------------------------------------------------
        # Visualization
        # --------------------------------------------------
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=ts_data.index,
            y=ts_data["Close"],
            mode="lines",
            name="Historical Price",
        ))

        fig.add_trace(go.Scatter(
            x=forecast_df.index,
            y=forecast_df["Forecast"],
            mode="lines",
            name="Forecasted Price",
            line=dict(dash="dash"),
        ))

        fig.update_layout(
            template="plotly_dark",
            height=600,
            title="Actual vs Forecasted Stock Price",
        )

        st.plotly_chart(fig, use_container_width=True)

        # --------------------------------------------------
        # Forecast Table
        # --------------------------------------------------
        st.subheader("📊 Forecasted Prices")
        st.dataframe(forecast_df)

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")