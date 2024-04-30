import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

@st.cache
def download_stock_data(stock_symbol, start_date, end_date):
    # Download historical data using yfinance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date, progress=False)
    return stock_data

def main():
    st.title('Stock Price Prediction App')

    # Sidebar - Input parameters
    st.sidebar.header('Input Parameters')
    stock_symbol = st.sidebar.text_input('Stock Symbol', 'AAPL')
    start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime('2010-01-01'))
    end_date = st.sidebar.date_input('End Date', value=pd.to_datetime('2022-01-01'))

    # Step 1: Data Collection
    stock_data = download_stock_data(stock_symbol, start_date, end_date)

    if not stock_data.empty:
        # Display the first few rows of the downloaded data
        st.write('**Historical Stock Data:**')
        st.write(stock_data.head())

        # Plot the closing price of the stock
        st.write('**Historical Stock Prices:**')
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data['Close'], label='Close Price')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.title('Historical Stock Prices')
        plt.legend()
        st.pyplot(plt)

        # Step 2: Data Preprocessing
        stock_data.dropna(inplace=True)

        # Step 3: Feature Engineering
        feature_data = stock_data['Close'].values.reshape(-1, 1)

        # Step 4: Model Architecture
        sequence_length = 10

        # Step 5: Training
        split_percentage = 0.8
        split_index = int(split_percentage * len(feature_data))

        train_data = feature_data[:split_index]
        test_data = feature_data[split_index:]

        scaler = MinMaxScaler(feature_range=(0, 1))
        train_data_normalized = scaler.fit_transform(train_data)

        X_train, y_train = create_sequences(train_data_normalized, sequence_length)
        X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

        model = Sequential([
            LSTM(50, input_shape=(sequence_length, 1)),
            Dense(1)
        ])

        model.compile(optimizer='adam', loss='mean_squared_error')

        model.fit(X_train, y_train, epochs=10, batch_size=32)

        # Step 6: Evaluation
        test_data_normalized = scaler.transform(test_data)
        X_test, y_test = create_sequences(test_data_normalized, sequence_length)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        predicted_data_normalized = model.predict(X_test)
        predicted_data = scaler.inverse_transform(predicted_data_normalized)

        # Plot actual vs. predicted prices
        st.write('**Actual vs. Predicted Stock Prices:**')
        plt.figure(figsize=(10, 6))
        plt.plot(test_data[sequence_length:], label='Actual Price')
        plt.plot(predicted_data, label='Predicted Price')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Actual vs. Predicted Stock Prices')
        plt.legend()
        st.pyplot(plt)

        # Step 7: Prediction
        new_data = feature_data[-sequence_length:]
        new_data_normalized = scaler.transform(new_data.reshape(-1, 1))
        X_new = np.reshape(new_data_normalized, (1, sequence_length, 1))
        predicted_price_normalized = model.predict(X_new)
        predicted_price = scaler.inverse_transform(predicted_price_normalized.reshape(-1, 1))

        st.write('**Next Day Predicted Price:**')
        st.write("Predicted price for the next day:", predicted_price[0][0])
    else:
        st.write('No data available for the selected stock symbol and date range.')

@st.cache
def create_sequences(data, sequence_length):
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data[i:i+sequence_length])
        y.append(data[i+sequence_length])
    return np.array(X), np.array(y)

if __name__ == "__main__":
    main()
