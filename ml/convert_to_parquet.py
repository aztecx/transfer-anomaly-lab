import time
import pandas as pd

SRC = "data/HI-Medium_Trans.csv"
DST = "data/HI-Medium_Trans.parquet"

dtypes = {
    "From Bank": "int32",
    "To Bank": "int32",
    "Account": "category",
    "Account.1": "category",
    "Receiving Currency": "category",
    "Payment Currency": "category",
    "Payment Format": "category",
    "Is Laundering": "int8",
}

start = time.time()
df = pd.read_csv(
    SRC,
    dtype=dtypes,
    parse_dates=["Timestamp"],
    date_format="%Y/%m/%d %H:%M",
)
print("Loaded", df.shape, "in", round(time.time() - start), "seconds")
print("Memory use (GB):", round(df.memory_usage(deep=True).sum() / 1e9, 2))

df = df.rename(columns={"Account": "from_account", "Account.1": "to_account"})
df.to_parquet(DST, index=False)
print("Saved", DST, "in", round(time.time() - start), "seconds")