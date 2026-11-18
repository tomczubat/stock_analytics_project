# Load stock prices from the API and append them
# to the Bronze CSV layer.

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

    new_data = pd.concat(all_data, ignore_index=True)

    Path("data/bronze").mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = "data/bronze/stock_prices.csv"

    # If Bronze already exists, append new data
    if Path(output_file).exists():

        existing_data = pd.read_csv(output_file)

        bronze_df = pd.concat(
            [existing_data, new_data],
            ignore_index=True
        )

    else:
        bronze_df = new_data

    bronze_df.to_csv(
        output_file,
        index=False
    )

    print(f"\nSaved data to {output_file}")
    print(f"Rows loaded: {len(bronze_df)}")


if __name__ == "__main__":
    main()