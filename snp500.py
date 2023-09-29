import os
import FinanceDataReader as fdr
import pandas as pd
import yfinance as yf
from multiprocessing import Pool
from tqdm import tqdm
import time
from datetime import datetime
from utils import *

# Define functions for parallel processing
def fetch_stock_data(symbol):
    ticker = yf.Ticker(symbol)
    return ticker

def preprocessing(data):
    name = data[0]
    symbol = data[1]
    ticker = fetch_stock_data(symbol)
    ticker_info_check(ticker)

    # Calculate PER
    try:

        price = ticker.info["previousClose"]
        eps = ticker.info["trailingEps"]
        if eps is not None and eps > 0:
            per = price / eps  # Calculate PER
        else:
            per = None
        
    except KeyError:
        per = None

    if not "totalRevenue" in ticker.info:
        ticker.info["totalRevenue"] = None

    today = datetime.today()  # 현재 날짜
    last_year_end = today.replace(year=today.year - 1, month=12, day=31).strftime('%Y-%m-%d')  # 작년 12월 31일

    if not 'Operating Income' in ticker.financials.index:
        operating_income = None
    else:
        # 컬럼 존재 여부 체크
        if last_year_end in ticker.financials.columns:
            operating_income = ticker.financials.loc["Operating Income", last_year_end]
        else:
            operating_income = None

    # operating_income = ticker.financials.loc["Operating Income", last_year_end]

    return [name,
            symbol,
            ticker.info["industry"],
            ticker.info["sector"],
            ticker.info["previousClose"],
            per,
            ticker.info["totalRevenue"],
            operating_income,
            ticker.info["dividendRate"],
            # ticker.info["dividendYield"],
            # ticker.info["fiveYearAvgDividendYield"],
            ticker.info["forwardPE"],
            ticker.info["volume"],
            ticker.info["marketCap"],
            # ticker.info["fiftyTwoWeekLow"],
            # ticker.info["fiftyTwoWeekHigh"],
            ticker.info["priceToSalesTrailing12Months"],
            # ticker.info["currency"],
            ticker.info["enterpriseValue"],
            ticker.info["sharesShort"],
            ticker.info["heldPercentInsiders"],
            ticker.info["heldPercentInstitutions"],
            ticker.info["trailingEps"],
            ticker.info["forwardEps"],
            ticker.info["enterpriseToRevenue"],
            ]

def get_data(sp500_components, columns, csv_path):
    # Measure the execution time
    start_time = time.time()

    # Create a Pool with multiple processes (adjust the number as needed)
    # core가 6개라 processes를 6개로 적용함
    print("Get Data...")
    with Pool(processes=6) as pool:
        tickers = list(tqdm(pool.imap(preprocessing, sp500_components[["Name", "Symbol"]].values), total=len(sp500_components)))

    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

    # Create a DataFrame from tickers list
    df = pd.DataFrame(tickers, columns=columns)

    # Save DataFrame to a CSV file
    df.to_csv(csv_path, index=False)

    return df


# Fetch stock price data in parallel using multiprocessing
def get_snp500_data():

    columns = get_columns()

    today = datetime.now()
    today_str = today.strftime('%Y%m%d')
    
    csv_path = f'data/{today_str}.csv'

    sp500_components = fdr.StockListing("S&P500")

    if not os.path.isfile(csv_path):
        df = get_data(sp500_components, columns, csv_path)
    else:
        df = pd.read_csv(csv_path)

    return df
