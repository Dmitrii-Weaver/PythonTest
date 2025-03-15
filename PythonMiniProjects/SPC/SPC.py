#Stock price checker via yfinance

import yfinance as yf

def get_stock_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)

    stock_info = stock.history(period="1d")

    if len(stock_info) > 0:
        current_price = stock_info['Close'].iloc[0]  

        prev_close = stock.info.get('previousClose', current_price)  

        price_change = current_price - prev_close
        percentage_change = (price_change / prev_close) * 100 if prev_close != 0 else 0

        market_cap = stock.info.get('marketCap', 'N/A')  
        volume = stock_info['Volume'].iloc[0]

        print(f"Current price: ${current_price:.2f}")
        print(f"Price change: ${price_change:.2f} ({percentage_change:.2f}%)")
        if market_cap != 'N/A':
            print(f"Market cap: ${market_cap/1e12:.2f}T")
        else:
            print("Market cap: N/A")
        print(f"Volume: {volume/1e6:.2f}M")
    else:
        print("No data available for this ticker.")

ticker = input("Enter the stock ticker symbol (e.g., AAPL, GOOGL): ")
get_stock_data(ticker)