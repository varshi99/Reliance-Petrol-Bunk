# Power BI build guide

## Import
1. Open Power BI Desktop.
2. Select **Get Data > Text/CSV**.
3. Import `Dataset/fuel_sales.csv`.
4. Import `Dataset/fuel_inventory.csv` and `Dataset/operating_expenses.csv` if you want the extended model.
5. In Power Query, set `transaction_date` to Date, `transaction_time` to Time, and numeric columns to Decimal Number.
6. Add the measures from `DAX_Measures.dax`.

## Suggested report pages
### 1. Executive Overview (dark theme)
Import `PowerBI_Theme.json` via **View > Themes > Browse for themes**, then set the page to 16:9 with the navy background `#0F1B33`. A preview of the target layout is in `Images/executive_overview.png` (regenerate with `python Python/executive_dashboard.py`).

**Header:** page title "Executive Overview", subtitle text box, page navigator buttons (Executive Overview | Fuel Performance | ...), and slicers for Date, fuel_type, payment_method and shift.

**Left KPI column (5 cards, stacked):** Total Revenue, Total Litres Sold, Total Transactions, Average Transaction Value, Revenue per Litre. Add a small sparkline to each card (Revenue by Calendar[Date]).

**Centre-top:** *Revenue Trend Analysis* - line and clustered column chart. X axis = week (or Calendar[Month]), columns = Total Revenue, line = Total Litres Sold on the secondary axis.

**Right-top:** *Revenue Composition* - Revenue by fuel_type (bar or decomposition tree) plus a 100% stacked bar for payment_method.

**Centre-bottom:** *Transactions by Hour* - column chart on Sales Hour; conditional-format the peak hour in amber.

**Right-bottom:** *Top Nozzle Performance* - table with nozzle_id, Total Transactions, Total Litres Sold, Total Revenue (data bars on Revenue), sorted by revenue descending.

**Bottom strip:** *Monthly Executive Summary* - three cards (Revenue, Transactions, Litres), each with its "Previous Month" label and MoM % measure. Use `MoM Colour` for conditional font colour.

> Note: the data has no purchase cost, so there is no Gross Profit/Margin card. Use `Revenue After Opex` and `Opex % of Revenue` if you want a profitability view.

### 2. Fuel Performance
- Clustered bar: Revenue by fuel_type.
- Column chart: Litres Sold by fuel_type.
- Matrix: Fuel type by month.

### 3. Time & Payment
- Column chart: Transactions by Sales Hour.
- Bar chart: Revenue by shift.
- Donut: Revenue by payment_method.
- Bar chart: Revenue by weekday/weekend.

### 4. Inventory & Expenses
- Line chart: Closing stock by inventory_date, with fuel_type legend.
- Table: Inventory rows where closing_stock_litres is below reorder_level_litres.
- Bar chart: Operating expenses by expense_category.

## Model relationships
- Create a date table named Calendar.
- Relate Calendar[Date] (one) to fuel_sales[transaction_date] (many).
- Relate Calendar[Date] (one) to fuel_inventory[inventory_date] (many).
- Relate Calendar[Date] (one) to operating_expenses[expense_month] (many).
- Mark Calendar as the date table.

## Important
A native `.pbix` report must be created and saved in Power BI Desktop. This project package provides import-ready data, DAX measures, and a report build guide, but does not contain a fabricated PBIX file.
