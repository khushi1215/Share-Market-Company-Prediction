import yfinance as yf
def fetch_live_company_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get("regularMarketPrice")
        high_52 = info.get("fiftyTwoWeekHigh")
        low_52 = info.get("fiftyTwoWeekLow")
        market_cap = info.get("marketCap")
        if not all([price, high_52, low_52, market_cap]):
            return None
        return {
            "Price": price,
            "High_52": high_52,
            "Low_52": low_52,
            "Market_Cap": market_cap
        }
    except Exception:
        return None
