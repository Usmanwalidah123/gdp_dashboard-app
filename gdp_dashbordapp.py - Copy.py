import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Streamlit App")

st.write("""
This app demonstrates two pages:
1) A Stock Price page for real-time stock data (default AAPL)
2) A simple GDP Dashboard (auto-refresh simulation)
""")

# Sidebar for page navigation
page = st.sidebar.selectbox("Select a page:", ("Stock Price", "GDP Dashboard"))

# Page 1: Stock Price
if page == "Stock Price":
    st.header("Stock Price")
    
    # Optional: Auto-refresh this page every 60 seconds
    # st_autorefresh is only available in Streamlit >= 1.18
    st_autorefresh = st.experimental_rerun  # fallback if st_autorefresh is not available
    # Uncomment the line below if you have a recent Streamlit version
    # st_autorefresh(interval=60000, key="stock_autorefresh")

    ticker_symbol = st.text_input("Enter Ticker Symbol", "AAPL")
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch the last 1 day of data with a 1-minute interval
    data = ticker.history(period="1d", interval="1m")
    
    st.write(f"Real-time data for: **{ticker_symbol}**")
    st.dataframe(data)
    
    # Plot the closing prices over time
    fig = px.line(
        data,
        x=data.index,
        y="Close",
        title=f"Real-time Stock Price for {ticker_symbol}"
    )
    st.plotly_chart(fig)

# Page 2: GDP Dashboard
elif page == "GDP Dashboard":
    st.header("GDP Dashboard")

    # Auto-refresh every 60 seconds (simulated "real-time")
    # Remove or comment out if you don't need auto-refresh.
    # st_autorefresh(interval=60000, key="gdp_autorefresh")

    # Example "static" GDP data
    # Replace this block with real data or an API call if available.
    data = {
        'Country': ['USA', 'China', 'Japan', 'Germany', 'India'],
        'GDP (Trillions USD)': [22.9, 16.9, 5.1, 4.2, 3.2]
    }
    
    df_gdp = pd.DataFrame(data)
    st.subheader("GDP Table")
    st.dataframe(df_gdp)
    
    fig = px.bar(
        df_gdp,
        x='Country',
        y='GDP (Trillions USD)',
        title='GDP by Country'
    )
    st.plotly_chart(fig)
