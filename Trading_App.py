import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Stock Analysis & Forecasting",
    page_icon="📈",
    layout="wide",
)

# Main Title
st.title("📈 Stock Analysis & Forecasting Dashboard")

# Features Section
st.header("🚀 Key Features")

# Banner Image
st.image("assets/stock.jpg", use_column_width=True)


# Introduction Section
st.markdown(
    """
    Welcome to the **Stock Analysis & Forecasting Application** 🚀  

    This platform is designed to help you **analyze historical stock market data,
    explore trends, and forecast future price movements** using
    **time series analysis techniques**.

    The application simulates a **real-world data analyst workflow** by combining:
    - Data analysis
    - Statistical modeling
    - Predictive forecasting
    - Interactive visualizations
    """
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        - 📊 Interactive stock charts  
        - 📈 Time series forecasting  
        - 🔍 Exploratory data analysis (EDA)  
        - 🧠 Model-driven predictions  
        """
    )

with col2:
    st.info(
        """
        💡 **How to use this app**

        Navigate using the sidebar to explore:
        - Stock analysis and visualization
        - Price prediction and forecasting models
        """
    )

st.divider()

# Footer / Next Steps
st.header("📉 Get Started")

st.markdown(
    """
    Use the sidebar to:
    - Explore **Stock Analysis** for historical insights  
    - Try **Stock Prediction** to forecast future trends  
    """
)
