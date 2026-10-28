from stock_api import get_stock_data
import pandas as pd

TICKERS = [
    "QQQM",
    "MSFT",
    "GOOGL",
    "AMZN",
    "SPCX"
]

all_data = []

for ticker in TICKERS:

    print(f"Downloading {ticker}...")

    try:
        df = get_stock_data(ticker)
        all_data.append(df)

    except Exception as e:
        print(e)

bronze_df = pd.concat(all_data)

bronze_df.to_parquet(
    "data/raw/stock_prices.parquet",
    index=False
)

print("Bronze layer loaded successfully")