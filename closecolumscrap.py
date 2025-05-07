import yfinance as yf
import pandas as pd

# Function to get stock data for a company
def get_stock_data(ticker, start_date='2010-01-01', end_date='2023-12-31'):
    # Download stock data from Yahoo Finance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# List of company tickers to fetch data for
companies = [
    'AAPL',   # Apple
    'GOOGL',  # Alphabet (Google)
    'MSFT',   # Microsoft
    'AMZN',   # Amazon
    'TSLA',   # Tesla
    'META',   # Meta (Facebook)
    'NVDA',   # NVIDIA
    'NFLX',   # Netflix
    'IBM',    # IBM
    'INTC',   # Intel
    'ORCL',   # Oracle
    'CSCO',   # Cisco
    'V',      # Visa
    'JPM',    # JPMorgan Chase
    'BAC'     # Bank of America
]

# Loop through each company and save stock data to Excel
for company in companies:
    print(f"Fetching data for {company}...")
    stock_data = get_stock_data(company)
    
    # Select only the 'Close' column
    stock_data_close = stock_data[['Close']]
    
    # Save data to Excel file
    file_name = f'{company}_stock_data_close_2010_2023.xlsx'
    stock_data_close.to_excel(file_name)
    print(f"Saved {company} stock data (Close) to {file_name}")
s