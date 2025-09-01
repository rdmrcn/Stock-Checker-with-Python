import yfinance as yf

STK = input("Enter share name:")

data = yf.Ticker(STK).history(period="id")

last_market_price = data['close'].iloc[-1]

print("Last Market Price: ", last_market_price)