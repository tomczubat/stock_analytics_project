import pandas as pd

df = pd.read_parquet(
    "data/raw/stock_prices.parquet"
)

print(df.dtypes)