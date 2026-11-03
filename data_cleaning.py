"""
Load and validate the petrol bunk practice data.
Run from the project root: python Python/data_cleaning.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sales_path = ROOT / "Dataset" / "fuel_sales.csv"
df = pd.read_csv(sales_path, parse_dates=["transaction_date"])
df.columns = [c.strip().lower() for c in df.columns]
df = df.drop_duplicates(subset=["transaction_id"])
df["transaction_time"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.time
numeric = ["litres_sold", "price_per_litre_inr", "sales_amount_inr"]
for col in numeric:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["transaction_id", "transaction_date", "fuel_type"] + numeric)
df = df[(df["litres_sold"] > 0) & (df["price_per_litre_inr"] > 0)]
df["calculated_amount_inr"] = (df["litres_sold"] * df["price_per_litre_inr"]).round(2)
df["amount_check"] = (df["sales_amount_inr"] - df["calculated_amount_inr"]).abs() <= 0.05
out = ROOT / "Outputs"
out.mkdir(exist_ok=True)
df.to_csv(out / "fuel_sales_cleaned.csv", index=False)
print(f"Rows after cleaning: {len(df):,}")
print(f"Amount validation failures: {(~df['amount_check']).sum()}")
