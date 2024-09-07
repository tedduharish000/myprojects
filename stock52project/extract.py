import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# MySQL connection details
DB_USERNAME = 'root'
DB_PASSWORD = 'Harish143'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'stock_data'

# Connection string for SQLAlchemy
connection_string = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(connection_string)

def fetch_and_store_stock_data(stock_symbol):
    # Define date range (last 1 year)
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=365)

    # Fetch stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    if stock_data.empty:
        print(f"No data fetched for {stock_symbol}")
        return

    # Calculate 52-week high and low
    high_52_week = stock_data['High'].max()
    low_52_week = stock_data['Low'].min()

    # Prepare data for insertion
    stock_data.reset_index(inplace=True)
    stock_data['stock_symbol'] = stock_symbol
    stock_data['high_52_week'] = high_52_week
    stock_data['low_52_week'] = low_52_week

    # Rename columns
    stock_data.rename(columns={
        'Date': 'date',
        'Open': 'open_price',
        'High': 'high_price',
        'Low': 'low_price',
        'Close': 'close_price',
        'Volume': 'volume'
        'Adj Close': 'adj_close'
    }, inplace=True)

    # Insert data into MySQL
    try:
        stock_data.to_sql('stock_prices', con=engine, if_exists='append', index=False)
        print(f"Data for {stock_symbol} inserted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
fetch_and_store_stock_data('RELIANCE.NS')
