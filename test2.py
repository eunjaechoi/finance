import FinanceDataReader as fdr
import pandas as pd
import yfinance as yf
from multiprocessing import Pool
from datetime import datetime

sp500_components = fdr.StockListing("S&P500")

# Define functions for parallel processing
ticker = yf.Ticker("ADBE")
financials = ticker.financials
print(ticker.financials)

