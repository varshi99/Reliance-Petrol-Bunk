"""
Executive Overview dashboard preview (dark theme, Power BI style).
Run from project root: python Python/executive_dashboard.py
Output: Images/executive_overview.png
All data is synthetic (see README).
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Images"
OUT.mkdir(exist_ok=True)

BG, CARD, TXT, MUTED = "#0F1B33", "#1B2A4A", "#FFFFFF", "#9FB0CF"
BLUE, TEAL, AMBER, RED, GREEN = "#3B8BFF", "#2EC4B6", "#FFB000", "#FF5C5C", "#3DDC97"

df = pd.read_csv(ROOT / "Dataset" / "fuel_sales.csv", parse_dates=["transaction_date"])
df["hour"] = pd.to_datetime(df["transaction_time"], format="%H:%M:%S").dt.hour
df["month"] = df["transaction_date"].dt.to_period("M")

rev, litres, txns = df["sales_amount_inr"].sum(), df["litres_sold"].sum(), len(df)

def inr(v):
    return f"\u20b9{v/1e6:.2f}M" if v >= 1e6 else f"\u20b9{v/1e3:.1f}K"

fig = plt.figure(figsize=(14, 7.8), facecolor=BG)

def card(x, y, w, h):
    fig.patches.append(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.002,rounding_size=0.01",
                       transform=fig.transFigure, fc=CARD, ec="none", zorder=-10))

def style(ax):
    ax.set_facecolor(CARD)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=8, length=0)
    ax.grid(axis="y", color="#2C3E66", lw=0.6)
    ax.set_axisbelow(True)

# Header
fig.text(0.03, 0.935, "Executive Overview", color=TXT, fontsize=24, fontweight="bold")
fig.text(0.03, 0.895, "Reliance Petrol Bunk  |  Strategic Business Insights  |  1 Aug - 29 Oct 2026 (synthetic data)",
         color=MUTED, fontsize=10, style="italic")

# KPI column
card(0.02, 0.04, 0.17, 0.82)
kpis = [("Total Revenue", inr(rev)), ("Litres Sold", f"{litres/1e3:.1f}K L"),
        ("Transactions", f"{txns/1e3:.1f}K"), ("Avg Transaction", f"\u20b9{rev/txns:,.0f}"),
        ("Revenue per Litre", f"\u20b9{rev/litres:.2f}")]
for i, (lab, val) in enumerate(kpis):
    y = 0.80 - i * 0.16
    fig.text(0.035, y, lab, color=MUTED, fontsize=11)
    fig.text(0.035, y - 0.065, val, color=TXT, fontsize=22, fontweight="bold")

# Weekly revenue trend
ax = fig.add_axes([0.23, 0.50, 0.40, 0.31]); card(0.215, 0.47, 0.43, 0.39); style(ax)
wk = df.set_index("transaction_date").resample("W-SUN").agg(rev=("sales_amount_inr", "sum"), lit=("litres_sold", "sum"))
wk = wk.iloc[1:-1]  # drop partial first/last weeks so the trend is not distorted
ax.bar(range(len(wk)), wk["rev"] / 1e3, color=BLUE, width=0.65)
ax.set_xticks(range(len(wk))); ax.set_xticklabels([d.strftime("%d %b") for d in wk.index], rotation=45)
ax.set_ylabel("Revenue (\u20b9K)", color=MUTED, fontsize=8)
ax2 = ax.twinx(); ax2.plot(range(len(wk)), wk["lit"] / 1e3, color=TEAL, lw=2, marker="o", ms=3)
ax2.tick_params(colors=MUTED, labelsize=8, length=0); ax2.set_ylabel("Litres (K)", color=MUTED, fontsize=8)
for s in ax2.spines.values(): s.set_visible(False)
ax.set_title("Weekly Revenue vs Litres Sold (full weeks)", color=TXT, loc="left", fontsize=12, fontweight="bold", pad=16)

# Revenue composition
ax = fig.add_axes([0.76, 0.60, 0.21, 0.19]); card(0.665, 0.47, 0.315, 0.39); style(ax)
f = df.groupby("fuel_type")["sales_amount_inr"].sum().sort_values()
ax.barh(f.index, f.values / f.sum() * 100, color=[TEAL, BLUE, AMBER][: len(f)], height=0.55)
for i, v in enumerate(f.values / f.sum() * 100):
    ax.text(v + 1, i, f"{v:.1f}%", va="center", color=TXT, fontsize=9)
ax.set_xlim(0, 100); ax.grid(False); ax.set_xticks([])
ax.tick_params(axis="y", colors=TXT, labelsize=9)
ax.set_title("Revenue by Fuel Type", color=TXT, loc="left", fontsize=12, fontweight="bold", pad=14, x=-0.3)
ax = fig.add_axes([0.685, 0.50, 0.28, 0.07]); style(ax)
p = df.groupby("payment_method")["sales_amount_inr"].sum().sort_values(ascending=False)
left = 0
for name, v, c in zip(p.index, p.values / p.sum() * 100, [BLUE, TEAL, AMBER]):
    ax.barh(0, v, left=left, color=c, height=0.6)
    ax.text(left + v / 2, 0, f"{name} {v:.0f}%", ha="center", va="center", color="#0F1B33", fontsize=8, fontweight="bold")
    left += v
ax.set_xlim(0, 100); ax.axis("off")

# Peak hours
ax = fig.add_axes([0.23, 0.17, 0.40, 0.19]); card(0.215, 0.14, 0.43, 0.30); style(ax)
h = df.groupby("hour")["transaction_id"].count()
ax.bar(h.index, h.values, color=[AMBER if v == h.max() else BLUE for v in h.values], width=0.7)
ax.set_xticks(h.index); ax.set_xlabel("Hour of day", color=MUTED, fontsize=8)
ax.set_title("Transactions by Hour (peak highlighted)", color=TXT, loc="left", fontsize=12, fontweight="bold", pad=16)

# Nozzle table
card(0.665, 0.14, 0.315, 0.30)
fig.text(0.68, 0.40, "Top Nozzle Performance", color=TXT, fontsize=12, fontweight="bold")
nz = (df.groupby("nozzle_id").agg(Txns=("transaction_id", "count"), Litres=("litres_sold", "sum"),
      Revenue=("sales_amount_inr", "sum")).sort_values("Revenue", ascending=False))
for j, (lab, x) in enumerate([("Nozzle", 0.68), ("Txns", 0.76), ("Litres", 0.83), ("Revenue", 0.90)]):
    fig.text(x, 0.365, lab, color=MUTED, fontsize=9)
mx = nz["Revenue"].max()
for i, (n, r) in enumerate(nz.iterrows()):
    y = 0.33 - i * 0.032
    fig.patches.append(FancyBboxPatch((0.895, y - 0.008), 0.075 * r["Revenue"] / mx, 0.022, boxstyle="round,pad=0,rounding_size=0.003",
                       transform=fig.transFigure, fc=BLUE, ec="none", zorder=1))
    fig.text(0.68, y, n, color=TXT, fontsize=9); fig.text(0.76, y, f"{int(r['Txns']):,}", color=TXT, fontsize=9)
    fig.text(0.83, y, f"{r['Litres']:,.0f}", color=TXT, fontsize=9); fig.text(0.90, y, inr(r["Revenue"]), color=TXT, fontsize=9)

# Monthly executive summary (Oct vs Sep)
card(0.215, 0.02, 0.765, 0.105)
m = df.groupby("month").agg(rev=("sales_amount_inr", "sum"), tx=("transaction_id", "count"), lit=("litres_sold", "sum"))
cur, prev = m.iloc[-1], m.iloc[-2]
fig.text(0.23, 0.07, "Monthly Executive Summary", color=TXT, fontsize=11, fontweight="bold")
fig.text(0.23, 0.04, f"{m.index[-1]} (to 29 Oct) vs {m.index[-2]}", color=MUTED, fontsize=8)
for x, lab, c, pv, fmt in [(0.45, "Revenue", cur.rev, prev.rev, inr), (0.62, "Transactions", cur.tx, prev.tx, lambda v: f"{v:,.0f}"),
                           (0.80, "Litres", cur.lit, prev.lit, lambda v: f"{v/1e3:.1f}K L")]:
    d = (c - pv) / pv * 100
    fig.text(x, 0.095, lab, color=MUTED, fontsize=9)
    fig.text(x, 0.055, fmt(c), color=TXT, fontsize=16, fontweight="bold")
    fig.text(x, 0.03, f"Prev month: {fmt(pv)} ({d:+.1f}%)", color=GREEN if d >= 0 else RED, fontsize=8)

fig.savefig(OUT / "executive_overview.png", dpi=130, facecolor=BG)
print(f"Saved {OUT / 'executive_overview.png'}")
