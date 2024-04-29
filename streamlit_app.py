import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

import subprocess
# Define the pip install command
pip_command = ['pip', 'install', 'yfinance', '--upgrade', '--no-cache-dir']
# Run the pip install command
subprocess.run(pip_command)


with st.sidebar.expander('Risk Management'):
    st.markdown("""
        In 1952, Harry Markowitz came up with **Modern Portfolio Theory** which, among other things, showed how you can construct a collection or portfolio of stocks to reduce or even minimize the risk of the overall investment. 
        One of Markowitz's insights was that the volatility of a stock's price was a suitable measure of the risk of the investment. You can **reduce the overall volatility of a portfolio by investing stocks that are NOT correlated with each other**. Thus, one stock may go up with inflation and another might go down. These movements can offset each other and reduce the portfolio's volatility or risk.
        You can **fully diversify your portfolio by holding 30 or so stocks - assuming that they are not correlated**. One hundred years ago, investors thought they were diversified if they owned 20 different railroad stocks. Go figure.
        
        These days we measure **volatility of the entire stock market with the volatility index or VIX**. It is also known as the **fear index or fear gauge**. 
        The **higher the VIX, the riskier the market**. A rule of thumb is if the **VIX is below 14, the market is not risky**.
    """)

with st.sidebar.expander('Portfolio Management - Growth & Value'):
    st.markdown(
            """
            We assume that everyone wants to avoid losing money. However, there are many different ways to make money. 
            Many stocks pay dividends (usually quarterly) which can provide income to the investor. Usually companies that pay dividends are older and more stable and established, such as banks and utilities. These stocks are often called **value stocks**.
            Many stocks do not pay dividends. Instead they reinvest that money in the company to help it grow and expand. These stocks are often called **growth stocks**.
            Usually, **growth stocks are more volatile than value stocks**, which is to say that they are **more risky**.
            These categories are not always clear cut.

            Another metric that relates to MPT, is **beta, a measure of a stock volatility relative to the market as a whole**. 
            A beta of 1 means that the stock has the same volatility as the entire market (usually the S and P 500). 
            A stable stock will have a beta below 1. 
            A risky stock will have a beta over 1.
        """)
    
with st.sidebar.expander('Portfolio Management - Sector/Industries'):
    st.markdown(
            """
            To diversify the risk in a portfolio, you need to **buy stocks with different volatility patterns**. One common way to do this is by investing in **different sectors or industries**.

            Different sectors respond differently to market conditions. In recent years, technology has outperformed sectors like materials or real estate. However, there is no clear pattern over time.
            """)

with st.sidebar.expander('Security Analysis'):
    st.markdown(
            """
            Many Wall Street firms, like Morgan Stanley, Goldman Sachs, and Merrill Lynch, employ finance professionals who advise investors which stocks to buy and sell. For example, see a recent Merrill Lynch report on Apple (AAPL). An analysis will usually assign a **recommendation of buy, sell, or hold, as well as a price target or price objective - their prediction of the price within the next 12 months**. 
            Merrill Lynch assigns Apple a NEUTRAL rating and a price objective of 158 from the current price of 151. This is pretty bullish. 
            Note that Merrill Lynch also reports an **ESGMeter score** of high for Apple. **ESG stands for Environmant, Social, and Governance which measures a company commitment to climate change, diversity and related initiatives**. The hope is that a company can do well by doing good. According to Merrill Lynch, Apple is one of the good guys.
            
            One focus of a security analyst is to **predict future earnings**. This figure becomes part of **price/earnings ratio** or simply p/e ratio. 
            A low PE suggest that the stock is cheap. 
            A high PE suggests that the stock is expensive.
            However, the **PE ratio varies considerably across industries**.
            
            Also, there are **quantitative models that can value a stock based on future earnings or discounted cash flows (DCF)**. This approach can be used on other assets in addition to stock. 
            A security analyst can project company earnings and then plug those numbers into a DCF model to get a valuation for the company. 
            Using earnings per share, the valuation is the estimated current price of the company. If that price is higher than the market price, then the stock is a BUY. If the valuation price is lower than the market price, the stock is a SELL.
            In the homework, you are to write some code that could replace a security analyst. """ )
    
with st.sidebar.expander('Model Portfolios'):
    st.markdown(
            """
            In addition to analyzing companies, Merrill Lynch also provides sample model portfolios, namely:
            - Large Cap Defensive
            - Income
            - Income and Growth
            - Growth
            - Mid-Cap
            - International
            
            Each of these portfolios comprise 30 or so individual stocks across a dozen industrial sectors. The portfolio specifies the weightings of each holding. Every few weeks or months, Merrill Lynch will publish changes to weightings or holdings to recalibrate the portfolio. See the Research Portfolio Holdings:MLHoldings.pdf

            Merrill Lynch publishes a primer which explains the investment philosophy and process used to construct these portfolios. The basic premise is that each portfolio has its own risk profile, with Large Cap Defensive being safer than Income, and so forth. Here is last month's Research Portfolio Primer: MLPrimer.pdf

            As a machine learning exercise, you could use the holdings of these portfolios as training data to learn the properties of an income stock versus a growth stock.
            """)



st.title('Modern Portfolio Theory (MPT)')
# User Input
ticker_symbol = st.text_input('Enter Stock Ticker')
start_date = st.date_input('Start Date')
end_date = st.date_input('End Date')

# Dataframe
ticker_df = pd.DataFrame(yf.download(ticker_symbol,start=start_date,end=end_date))
st.write(ticker_df)

# Plot Adj Close for Dataframe
fig1 = px.line(ticker_df, x=ticker_df.index, y='Adj Close', title=f'{ticker_symbol} Stock Price')
st.plotly_chart(fig1)

with st.expander('Fundamentals'):
    # Stock Info
    stock = yf.Ticker(ticker_symbol)
    st.write(stock.info)

    #Fundamentals
    # Display additional financial metrics
    st.metric("Market Cap", stock.info.get('marketCap','Not Available'), help="Market cap is the toal market value of all of a company's outstanding shares", label_visibility="visible")
    st.metric("ROE (Return on Equity)", stock.info.get('returnOnEquity','Not Available'), help="Return on Equity(ROE) is a measure of financial performance,calculated by dividing net income by shareholders' equity", label_visibility="visible")
    st.metric("EPS (TTM)", stock.info.get('trailingEps','Not Available'), help="Earnings per share(EPS) is a company's net profit divided by the number of its common outstanding shares. It indicated how much money a company makes for each share of its stock. (TTM = trailing 12 months)", label_visibility="visible")
    st.metric("Dividend Yield", stock.info.get('dividendYield','Not Available'), help="Dividend yield percentage is the amount of money a company pays its shareholders for owning a share of its stock divided by its current stock price", label_visibility="visible")
    st.metric("P/E Ratio (TTM)", stock.info.get('trailingPE','Not Available'), help="P/E(price-to-earnings) ratio is the ratio of a company's share price to its earnings per share (EPS). P/E ratio is used to determine whether a company is overvalued or undervalued.", label_visibility="visible")
    st.metric("P/B Ratio", stock.info.get('priceToBook','Not Available'), help="P/B (price-to-book) ratio is the ratio of a company's share price to its book value. Any value under 1.0 is considered a good P/B value.", label_visibility="visible")
    st.metric("Industry P/E", stock.info.get('industryPe','Not Available'), help="The average P/E ratio of all the stocks in any sector. Different sectors consider different P/E ratios as healthy.", label_visibility="visible")
    st.metric("Debt to Equity", stock.info.get('debtToEquity','Not Available'), help="Debt to Equity is the percentage of the total liabilities of a company(debt) to its shareholders' equity. A higher debt to equity means the comppany is using more debt funds than equity funds, and a lower debt to equity means more equity than debt funds.", label_visibility="visible")
    st.metric("Book Value", stock.info.get('bookValue','Not Available'), help="The amount of money that a company's shareholders would earn if it is liquidated and has paid off all liabilities.", label_visibility="visible")
    st.metric("Face Value", stock.info.get('faceValue','Not Available'), help="The original value of a company's stock as written in its books of accounts and its share certificates. Also known as par value, it is fixed when the stock is first issued.", label_visibility="visible")

    st.info("**beta** is a measure of the stock's volatility relative to the market.")
    beta = stock.info['beta']
    st.write(f"{ticker_symbol}'s Beta is: {beta}")

    col1,col2 = st.columns([1,2])
    with col1:
        maj_hold = pd.DataFrame(stock.major_holders)
        st.write(f"{ticker_symbol}'s Major Hodlers are:")
        st.write(maj_hold)
    with col2:
        inst_hold = pd.DataFrame(stock.institutional_holders)
        st.write(f"{ticker_symbol}'s Institutional Hodlers are:")
        st.write(inst_hold)

    # Dividends
    stock_div = stock.actions
    st.write(stock_div)

with st.expander('Recommendations'):
    st.markdown(""" We see **Buy** and **Neutral**, which is like **Hold**. 
    There is also **Outperform**, which means that it should do better than its peers, and **Overweight**, which means that you should hold more Apple as a percentage in your portfolio than Apple's percentage weight in the relevant index.
                
    This brings up an interesting point. If you are a portfolio manager, how are you evaluated? The obvious answer is "How much money did I make for my clients?" However, that is incorrect. 
    Finance professionals know that they will have good years and bad years. They are happy to be rewarded for the good years, but they don't want to be punished for the bad ones. 
                
    Years ago, a smart portfolio manager proposed that he be measured relative to an index or benchmark, such as the S&P 500. 
    Thus, if his fund made 15% last year and the S&P made 10%, then the manager outperformed by 5% or 500 basis points. (A basis point is 1/100th of a percentage point.)
    If the fund lost10% last year but the S&P lost 15%, the manager still outperformed by 5% or 500 basis points. So the rating "Overweight" is relative to the appropriate benchmark index.
    That's how they keep score in asset management world. """)
    # Get the recommendations data
    stock_reco = stock.recommendations

    # Plotting bar chart for recommendations
    if not stock_reco.empty:
        fig2 = px.bar(stock_reco, x='period', y=['strongBuy', 'buy', 'hold', 'sell', 'strongSell'],
                    title=f'{ticker_symbol} Recommendations',
                    labels={'value': 'Count', 'variable': 'Recommendation'},
                    height=400)
        st.plotly_chart(fig2)
    else:
        st.warning("No recommendation data available for the selected stock.")



with st.expander('Stock Performance'):
    col3,col4 = st.columns(2)
    with col3:
        # Fetch stock information
        today_high = stock.info.get('dayHigh')
        today_low = stock.info.get('dayLow')
        fifty_two_week_high = stock.info.get('fiftyTwoWeekHigh')
        fifty_two_week_low = stock.info.get('fiftyTwoWeekLow')

        # Display other metrics using st.slider with labeled marked points
        st.slider('Stock Performance - Today',
                min_value=today_low,
                max_value=today_high,
                value=stock.info.get('ask'),
                disabled=True,
                label_visibility="visible")
        # Display other metrics using st.slider with labeled marked points
        st.slider('Stock Performance - 52 Week',
                min_value=fifty_two_week_low,
                max_value=fifty_two_week_high,
                value=(stock.info.get('ask')),
                disabled=True,
                label_visibility="visible")

    with col4:
        # Set start and end dates (today and yesterday)
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

        # Download stock data for today and yesterday
        today_df = pd.DataFrame(yf.download(ticker_symbol, start=today, end=today))
        yesterday_df = pd.DataFrame(yf.download(ticker_symbol, start=yesterday, end=yesterday))

        # Calculate delta between today and yesterday
        delta_df = today_df - yesterday_df
        delta_df_rounded = delta_df.round(2)
        col5,col6 = st.columns(2)
        with col5: 
            # Display stock information for today with delta based on yesterday's performance
            st.metric("Open", value=today_df['Open'].iloc[0].round(2), delta=delta_df_rounded['Open'].iloc[0])
            st.metric("Close", value=today_df['Close'].iloc[0].round(2), delta=delta_df_rounded['Close'].iloc[0])
            st.metric("Adj Close", value=today_df['Adj Close'].min().round(2), delta=delta_df_rounded['Adj Close'].min())
        with col6: 
            st.metric("High", value=today_df['High'].max().round(2), delta=delta_df_rounded['High'].max())
            st.metric("Low", value=today_df['Low'].min().round(2), delta=delta_df_rounded['Low'].min())
            st.metric("Volume", value=today_df['Volume'].sum().round(2), delta=delta_df_rounded['Volume'].sum())

# Fetch financials data
stock_fin = stock.financials
st.write(stock_fin)

# Display Revenue, Profit, Net Worth (Quarterly and Annual)
st.write("Quarterly Financials:")
st.write(f"Revenue (Quarterly): {stock_fin['Revenue'].iloc[0]}")
st.write(f"Profit (Quarterly): {stock_fin['Net Income'].iloc[0]}")
st.write(f"Net Worth (Quarterly): {stock_fin['Total Assets'].iloc[0]}")

st.write("Annual Financials:")
st.write(f"Revenue (Annual): {stock_fin['Revenue'].iloc[-1]}")
st.write(f"Profit (Annual): {stock_fin['Net Income'].iloc[-1]}")
st.write(f"Net Worth (Annual): {stock_fin['Total Assets'].iloc[-1]}")
