import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Step 1: Data Collection
def download_stock_data(stock_symbol, start_date, end_date):
    # Download historical data using yfinance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

def main():
    st.title('Stock Data Visualizer')

    # Add a text input box for the stock symbol
    stock_symbol = st.text_input('Enter Stock Symbol', 'AAPL')

    # Add a date picker for selecting start and end dates
    start_date = st.date_input('Start Date', value=None)
    end_date = st.date_input('End Date', value=None)

    if start_date is not None and end_date is not None:
        # Download stock data
        stock_data = download_stock_data(stock_symbol, start_date, end_date)

        if not stock_data.empty:
            # Display the downloaded data
            st.write('**Historical Stock Data:**')
            st.write(stock_data)

            # Plot the closing price
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data.index, stock_data['Close'], label='Close Price')
            plt.title('Historical Close Price of {}'.format(stock_symbol))
            plt.xlabel('Date')
            plt.ylabel('Price ($)')
            plt.legend()
            st.pyplot(plt)
        else:
            st.write('No data available for the selected stock symbol and date range.')

if __name__ == "__main__":
    main()
