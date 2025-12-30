import yfinance as yf

symbol = "TCS.NS"

stock = yf.Ticker(symbol)

# latest market price
price = stock.info.get("regularMarketPrice")

print(f"{symbol} current price: {price}")
