import yfinance as yf

TICKERS = [
    "QQQM",
    "MSFT",
    "GOOGL",
    "AMZN",
    "SPCX"
]

for ticker in TICKERS:

    print(f"Downloading {ticker}...")

    try:
        df = yf.download(
            ticker,
            period="1d",
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            print(f"WARNING: No data returned for {ticker}")
        else:
            print(f"SUCCESS: {ticker}")
            print(f"Rows: {len(df)}")
            print(df.head())

    except Exception as e:
        print(f"ERROR downloading {ticker}")
        print(e)