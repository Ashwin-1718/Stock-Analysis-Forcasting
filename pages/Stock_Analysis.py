from queue import Full
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
from pages.utils.plotly_figure import plotly_table


# Page Configuration
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📊",
    layout="wide",
) 

st.title("📊 Stock Analysis Dashboard")

col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Enter Stock Ticker", value="TSLA")

with col2:
    start_date = st.date_input("Start Date", datetime.date(today.year -1, today.month, today.day))

with col3:
    end_date = st.date_input("End Date",datetime.date(today.year, today.month, today.day))

st.subheader(ticker)

stock = yf.Ticker(ticker)

st.write("### Stock Information")
st.write(stock.info['longName'] if 'longName' in stock.info else ticker)
st.write(stock.info['sector'] if 'sector' in stock.info else "Sector info not available")
st.write(f"**Full Time Employees:** {stock.info['fullTimeEmployees'] if 'fullTimeEmployees' in stock.info else 'N/A'}")
st.write(f"**Website:** {stock.info['website'] if 'website' in stock.info else 'N/A'}")
st.write(f"**Market Cap:** {stock.info['marketCap'] if 'marketCap' in stock.info else 'N/A'}")


col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index= ['Market Cap', 'P/E Ratio', 'Dividend Yield'])
    df['Value'] = [
        stock.info['marketCap'] if 'marketCap' in stock.info else 'N/A',
        stock.info['trailingPE'] if 'trailingPE' in stock.info else 'N/A',
        stock.info['dividendYield'] if 'dividendYield' in stock.info else 'N/A'
    ]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)

with col2:
    st.write("### Recent News")
    news = stock.news
    if news:
        for item in news[:5]:  # Show top 5 news items
            st.markdown(f"**{item['title']}**")
            st.markdown(f"{item['publisher']} - {datetime.datetime.fromtimestamp(item['providerPublishTime']).strftime('%Y-%m-%d %H:%M:%S')}")
            st.markdown(f"{item['link']}")
            st.markdown("---")
    else:
        st.write("No recent news available.")

data = yf.download(ticker, start=start_date, end=end_date)
data.reset_index(inplace=True)

col1, col2, col3 = st.columns(3)
daily_change = data['Close'].pct_change() * 100
col1.metric("Daily Change (%)", f"{daily_change.iloc[-1]:.2f}%")
col2.metric("52 Week High", f"${data['Close'].max():.2f}")
col3.metric("52 Week Low", f"${data['Close'].min():.2f}")