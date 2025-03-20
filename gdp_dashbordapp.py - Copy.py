import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Streamlit App")

st.write("""
This app demonstrates two pages:
1) A Stock Price page for Apple ()
2) A simple GDP Dashboard
""")

# Create a sidebar selectbox for page navigation
page = st.sidebar.selectbox(
    "Select a page:",
    ("Stock Price", "GDP Dashboard")
)

# Page 1: Stock Price
if page == "Stock Price":
    st.header("Apple Stock Price")
    ticker_symbol = "AAPL"

    # Fetch data from yfinance
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(start='2010-05-31', end='2020-05-31')

    # Display closing price
    st.subheader("Closing Price")
    st.line_chart(ticker_df['Close'])

    # Display volume
    st.subheader("Volume")
    st.line_chart(ticker_df['Volume'])

# Page 2: GDP Dashboard
elif page == "GDP Dashboard":
    st.header("GDP Dashboard")

    st.write("""
    This is a simple example of a GDP dashboard 
    showing data for a few countries.
    """)

    # Example GDP data
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
