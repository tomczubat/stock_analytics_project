# Load stock prices from the API and save to a CSV file in the raw data folder.

from pathlib import Path
import pandas as pd

from stock_api import get_stock_data


TICKERS = [
    "QQQM",
    "MSFT",
    "GOOGL",
    "AMZN",
    "SPCX"
]


def main():

    all_data = []

    for ticker in TICKERS:
        print(f"Downloading {ticker}...")

        try:
            df = get_stock_data(ticker)

            all_data.append(df)

            print(f"Success: {ticker}")

        except Exception as e:
            print(f"Failed: {ticker} - {e}")

    combined_df = pd.concat(all_data, ignore_index=True)

    Path("data/raw").mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = "data/raw/stock_prices.csv"

    combined_df.to_csv(
        output_file,
        index=False
    )

    print(f"\nSaved data to {output_file}")
    print(f"Rows loaded: {len(combined_df)}")


if __name__ == "__main__":
    main()