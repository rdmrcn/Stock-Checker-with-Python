import yfinance as yf

##The period is currently set to "1d", which fetches 1 day of trading data.

Ticker symbols must be valid (e.g., AAPL for Apple, TSLA for Tesla, MSFT for Microsoft).

STK = input("Enter share name:")

data = yf.Ticker(STK).history(period="id")

last_market_price = data['close'].iloc[-1]


print("Last Market Price: ", last_market_price)
