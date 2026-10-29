# extract data from yfinance and return as a pandas dataframe

import yfinance as yf
import pandas as pd


def get_stock_data(ticker):
    df = yf.download(
        ticker,
        period="1d",
        auto_adjust=True,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data returned for {ticker}")

    # Flatten columns if yfinance returns MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df["ticker"] = ticker

    return df.reset_index()