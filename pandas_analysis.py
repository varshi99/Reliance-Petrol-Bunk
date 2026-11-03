"""
Pandas exploratory data analysis.
Run from the project root: python Python/pandas_analysis.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "Dataset" / "fuel_sales.csv", parse_dates=["transaction_date"])
df["sales_amount_inr"] = pd.to_numeric(df["sales_amount_inr"])
df["litres_sold"] = pd.to_numeric(df["litres_sold"])
df["hour"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.hour

print("\\n--- DATA OVERVIEW ---")
print(df.info())
print("\\n--- NUMERIC SUMMARY ---")
print(df[["litres_sold", "price_per_litre_inr", "sales_amount_inr"]].describe().round(2))
print("\\n--- KPI SUMMARY ---")
print(f"Transactions: {df.transaction_id.nunique():,}")
print(f"Revenue: ₹{df.sales_amount_inr.sum():,.2f}")
print(f"Litres sold: {df.litres_sold.sum():,.2f}")
print(f"Average transaction value: ₹{df.sales_amount_inr.mean():,.2f}")
print("\\n--- FUEL TYPE PERFORMANCE ---")
print(df.groupby("fuel_type").agg(
    transactions=("transaction_id", "count"),
    litres=("litres_sold", "sum"),
    revenue=("sales_amount_inr", "sum")
).sort_values("revenue", ascending=False).round(2))
print("\\n--- PAYMENT MIX ---")
print(df.groupby("payment_method")["sales_amount_inr"].sum().sort_values(ascending=False).round(2))
print("\\n--- HOURLY PERFORMANCE ---")
print(df.groupby("hour")["sales_amount_inr"].sum().sort_values(ascending=False).head(5).round(2))
