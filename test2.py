import FinanceDataReader as fdr
import pandas as pd
import yfinance as yf
from multiprocessing import Pool
import time

sp500_components = fdr.StockListing("S&P500")

# Define functions for parallel processing
ticker = yf.Ticker("MMM")
print(ticker.info)
