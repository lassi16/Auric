import yfinance as yf
from db import get_connection

def update_stock_prices():
    conn = get_connection()
    cur = conn.cursor()

    # 1. Read all stocks
    cur.execute("SELECT id, api_symbol FROM stocks;")
    stocks = cur.fetchall()

    print("Found stocks:", stocks)

    for stock_id, api_symbol in stocks:
        try:
            ticker = yf.Ticker(api_symbol)
            price = ticker.info.get("regularMarketPrice")

            if price is None:
                print(f"Price not found for {api_symbol}")
                continue

            # 2. Update price in DB
            cur.execute(
                "UPDATE stocks SET current_price = %s WHERE id = %s;",
                (price, stock_id)
            )

            print(f"Updated {api_symbol} → ₹{price}")

        except Exception as e:
            print(f"Error updating {api_symbol}:", e)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    update_stock_prices()
