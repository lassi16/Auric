from db import get_connection

STOCKS = [
    ("RELIANCE", "Reliance Industries", "RELIANCE.NS"),
    ("TCS", "Tata Consultancy Services", "TCS.NS"),
    ("INFY", "Infosys", "INFY.NS"),
    ("HDFCBANK", "HDFC Bank", "HDFCBANK.NS"),
    ("ICICIBANK", "ICICI Bank", "ICICIBANK.NS"),
]

def seed_stocks():
    conn = get_connection()
    cur = conn.cursor()

    for symbol, name, api_symbol in STOCKS:
        cur.execute(
            """
            INSERT INTO stocks (symbol, name, api_symbol)
            VALUES (%s, %s, %s)
            ON CONFLICT (symbol) DO UPDATE
            SET api_symbol = EXCLUDED.api_symbol;
            """,
            (symbol, name, api_symbol)
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Stocks seeded into Neon DB")

if __name__ == "__main__":
    seed_stocks()
