
def get_columns():
    columns = ["name", 
               "symbol", 
               "industry", 
               "sector", 
               "previousClose", 
               "per",
               "totalRevenue",
               "Operating Income",
               "dividendRate", 
            #    "dividendYield", 
            #    "fiveYearAvgDividendYield", 
               "forwardPE", 
               "volume", 
               "marketCap", 
            #    "fiftyTwoWeekLow", 
            #    "fiftyTwoWeekHigh", 
               "priceToSalesTrailing12Months", 
            #    "currency", 
               "enterpriseValue", 
               "sharesShort", 
               "heldPercentInsiders", 
               "heldPercentInstitutions'", 
               "trailingEps", 
               "forwardEps", 
               "enterpriseToRevenue"]
    return columns

def ticker_info_check(ticker):
    if not "industry" in ticker.info:
        ticker.info["industry"] = None

    if not "sector" in ticker.info:
        ticker.info["sector"] = None

    if not "previousClose" in ticker.info:
        ticker.info["previousClose"] = None

    if not "dividendRate" in ticker.info:
        ticker.info["dividendRate"] = None

    if not "dividendYield" in ticker.info:
        ticker.info["dividendYield"] = None

    if not "fiveYearAvgDividendYield" in ticker.info:
        ticker.info["fiveYearAvgDividendYield"] = None

    if not "forwardPE" in ticker.info:
        ticker.info["forwardPE"] = None

    if not "volume" in ticker.info:
        ticker.info["volume"] = None

    if not "marketCap" in ticker.info:
        ticker.info["marketCap"] = None

    if not "fiftyTwoWeekLow" in ticker.info:
        ticker.info["fiftyTwoWeekLow"] = None

    if not "fiftyTwoWeekHigh" in ticker.info:
        ticker.info["fiftyTwoWeekHigh"] = None

    if not "priceToSalesTrailing12Months" in ticker.info:
        ticker.info["priceToSalesTrailing12Months"] = None

    if not "currency" in ticker.info:
        ticker.info["currency"] = None

    if not "enterpriseValue" in ticker.info:
        ticker.info["enterpriseValue"] = None

    if not "sharesShort" in ticker.info:
        ticker.info["sharesShort"] = None

    if not "heldPercentInsiders" in ticker.info:
        ticker.info["heldPercentInsiders"] = None

    if not "heldPercentInstitutions" in ticker.info:
        ticker.info["heldPercentInstitutions"] = None

    if not "trailingEps" in ticker.info:
        ticker.info["trailingEps"] = None

    if not "forwardEps" in ticker.info:
        ticker.info["forwardEps"] = None

    if not "enterpriseToRevenue" in ticker.info:
        ticker.info["enterpriseToRevenue"] = None
