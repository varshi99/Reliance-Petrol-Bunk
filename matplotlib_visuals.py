"""
Matplotlib charts.
Run from project root: python Python/matplotlib_visuals.py
Charts are saved to Images/.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Images"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(ROOT / "Dataset" / "fuel_sales.csv", parse_dates=["transaction_date"])
df["hour"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.hour

# Revenue by fuel type
fuel = df.groupby("fuel_type")["sales_amount_inr"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
fuel.plot(kind="bar")
plt.title("Revenue by Fuel Type")
plt.xlabel("Fuel type")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(OUT / "revenue_by_fuel.png", dpi=160)
plt.close()

# Daily revenue trend
daily = df.groupby("transaction_date")["sales_amount_inr"].sum()
plt.figure(figsize=(11, 5))
daily.plot()
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig(OUT / "daily_revenue_trend.png", dpi=160)
plt.close()

# Hourly transactions
hourly = df.groupby("hour")["transaction_id"].count()
plt.figure(figsize=(9, 5))
hourly.plot(kind="bar")
plt.title("Transactions by Hour")
plt.xlabel("Hour of day")
plt.ylabel("Number of transactions")
plt.tight_layout()
plt.savefig(OUT / "transactions_by_hour.png", dpi=160)
plt.close()

# Payment method revenue
payment = df.groupby("payment_method")["sales_amount_inr"].sum().sort_values(ascending=False)
plt.figure(figsize=(7, 5))
payment.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Revenue Share by Payment Method")
plt.ylabel("")
plt.tight_layout()
plt.savefig(OUT / "payment_method_share.png", dpi=160)
plt.close()

print(f"Charts saved in: {OUT}")
