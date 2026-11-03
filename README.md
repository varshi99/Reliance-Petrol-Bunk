# ⛽ Reliance Petrol Bunk – Business Intelligence & Data Analytics

## 📌 Project Overview

The **Reliance Petrol Bunk Analytics Project** is an end-to-end data analytics and business intelligence solution designed to analyze petrol bunk operations, monitor fuel sales, evaluate revenue performance, reconcile billing data, and improve operational efficiency.

This project integrates **Excel, SQL, Python, Pandas, Matplotlib, and Microsoft Power BI** to transform raw operational data into meaningful business insights and actionable reports.

The project focuses on three major business analytics domains:

1. Utility Revenue Assurance & Billing Reconciliation Analytics
2. Sales Performance & Profitability Intelligence
3. Business Operations & Data Quality Performance Analytics

> **Disclaimer:** This is an independent educational project. All datasets are synthetic and created for demonstration purposes. It is not an official Reliance Industries project and is not based on actual company transaction records.

---

## 🎯 Business Objectives

- Analyze fuel sales and revenue performance.
- Monitor daily, weekly, and monthly revenue trends.
- Identify high-performing fuel categories.
- Evaluate transaction patterns and peak business hours.
- Analyze payment methods and shift-wise performance.
- Monitor fuel inventory and identify low-stock conditions.
- Analyze operating expenses and revenue after operating expenses.
- Detect billing inconsistencies and data quality issues.
- Develop interactive dashboards to support business decisions.

---

## 📊 Three Business Analytics Domains

### 1. Utility Revenue Assurance & Billing Reconciliation Analytics

**Business Goal:** Improve revenue accuracy and identify potential billing inconsistencies.

Key Analysis:
- Compare litres sold against recorded sales amounts.
- Validate fuel prices and transaction calculations.
- Identify incorrect or suspicious transaction records.
- Analyze revenue differences across fuel types.
- Monitor transaction-level data quality.
- Generate billing validation reports.

**Business Questions:**
- Are recorded sales amounts consistent with litres sold and fuel prices?
- Are there transactions with invalid quantities or prices?
- Which fuel category contributes the highest revenue?
- Are there potential billing discrepancies?

### 2. Sales Performance & Profitability Intelligence

**Business Goal:** Understand sales performance and improve revenue management.

Key Analysis:
- Total fuel revenue.
- Total litres sold.
- Average transaction value.
- Revenue per litre.
- Daily and monthly revenue trends.
- Fuel-type performance.
- Payment-method analysis.
- Weekday versus weekend sales.
- Operating expenses and revenue after operating expenses.

**Business Questions:**
- Which fuel type generates the highest revenue?
- What are the peak sales hours?
- Which payment method contributes the most revenue?
- How does monthly revenue change over time?
- What is the relationship between revenue and operating expenses?

**Note:** Gross profit and gross profit margin are not calculated because fuel purchase costs are not included in the dataset.

### 3. Business Operations & Data Quality Performance Analytics

**Business Goal:** Improve operational visibility, inventory management, and data reliability.

Key Analysis:
- Daily fuel inventory monitoring.
- Opening and closing stock analysis.
- Fuel delivery tracking.
- Reorder-level monitoring.
- Shift-wise sales performance.
- Attendant-wise transaction analysis.
- Nozzle-wise performance.
- Missing value and invalid record detection.
- Data quality reporting.

**Business Questions:**
- Which fuel types are approaching their reorder levels?
- How efficiently is inventory being monitored?
- Which shifts record the highest sales?
- Which nozzles handle the most transactions?
- Are there missing, invalid, or inconsistent records?

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Microsoft Excel | Data storage and initial analysis |
| MySQL | Database management and SQL analysis |
| Python | Data processing and automation |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Microsoft Power BI | Interactive business dashboards |
| DAX | Business metrics and KPI calculations |
| Git & GitHub | Version control and project management |

---

## 📂 Project Structure

```text
Reliance_Petrol_Bunk_Analytics/
│
├── Dataset/
│   ├── fuel_sales.csv
│   ├── fuel_inventory.csv
│   └── operating_expenses.csv
│
├── Excel/
│   └── Reliance_Petrol_Bunk_Data.xlsx
│
├── SQL/
│   └── petrol_bunk_analysis.sql
│
├── Python/
│   ├── data_cleaning.py
│   ├── pandas_analysis.py
│   ├── matplotlib_visuals.py
│   ├── executive_dashboard.py
│   └── requirements.txt
│
├── PowerBI/
│   ├── DAX_Measures.dax
│   ├── PowerBI_Theme.json
│   └── PowerBI_Dashboard_Guide.md
│
├── Images/
│   ├── revenue_by_fuel.png
│   ├── daily_revenue_trend.png
│   ├── transactions_by_hour.png
│   ├── executive_overview.png
│   └── payment_method_share.png
│
└── Outputs/
    ├── data_quality_report.txt
    ├── fuel_sales_cleaned.csv
    ├── fuel_inventory_cleaned.csv
    ├── operating_expenses_cleaned.csv
    └── analysis_results/
```


## 🧹 Data Cleaning & Processing

Python and Pandas are used to prepare the datasets for analysis.

Activities include:

- Checking missing values.
- Identifying duplicate records.
- Validating numeric fields.
- Checking transaction amounts.
- Cleaning and preparing datasets.
- Generating cleaned CSV files.
- Creating a data quality report.

---

## 🗄️ SQL Analysis

The MySQL scripts cover important business queries:

1. Revenue and litres sold by fuel type.
2. Daily revenue trends.
3. Peak sales hours.
4. Payment method distribution.
5. Shift-wise performance.
6. Attendant-wise transaction analysis.
7. Weekend versus weekday sales.
8. Inventory below reorder levels.
9. Monthly operating expenses.
10. Transaction-level data quality checks.

---

## 🐍 Python Analysis

Python is used for:

- Data cleaning with Pandas.
- Business KPI calculations.
- Revenue trend analysis.
- Fuel performance analysis.
- Transaction pattern analysis.
- Data visualization with Matplotlib.
- Executive dashboard preview generation.

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Reliance-Petrol-Bunk-Analytics.git
```

Navigate to the project directory:

```bash
cd Reliance-Petrol-Bunk-Analytics
```

Install dependencies:

```bash
pip install -r Python/requirements.txt
```

Run data cleaning:

```bash
python Python/data_cleaning.py
```

Run Pandas analysis:

```bash
python Python/pandas_analysis.py
```

Generate visualizations:

```bash
python Python/matplotlib_visuals.py
```

Generate executive dashboard preview:

```bash
python Python/executive_dashboard.py
```

---

## 📊 Power BI Dashboard

Microsoft Power BI is used to create an interactive business intelligence dashboard.

**Suggested Dashboard Pages:**

| Dashboard Page | Key Metrics |
|---|---|
| Executive Overview | Revenue, litres sold, transactions, average transaction value |
| Fuel Performance | Revenue and volume by fuel type |
| Time & Payment | Peak hours, shift performance, payment distribution |
| Inventory & Expenses | Stock levels, reorder alerts, operating expenses |

The project includes:
- DAX measures.
- Power BI theme JSON.
- Dashboard development guide.
- Data model and relationship recommendations.

**Note:** A native `.pbix` file is not included. The dashboard can be built in Power BI Desktop using the provided datasets and instructions.

---

## 💡 Business Impact

This project demonstrates how data analytics can support petrol bunk business operations through:

- Better revenue monitoring.
- Improved billing validation.
- Identification of potential transaction discrepancies.
- Better understanding of customer purchasing patterns.
- Improved fuel inventory visibility.
- More effective operating expense monitoring.
- Data-driven operational decisions.
- Centralized business performance reporting.

---

## 🚀 Skills Demonstrated

- Data Analysis
- Exploratory Data Analysis (EDA)
- Data Cleaning
- SQL Query Development
- Python Programming
- Pandas & NumPy
- Matplotlib Visualization
- Excel Data Analysis
- Power BI Dashboard Development
- DAX Measures
- Business Intelligence
- KPI Development
- Data Quality Analysis
- Business Problem Solving

---

## 👨‍💻 Author

**Varshitha Pavuluri**

GitHub: [Add Your GitHub Profile](https://github.com/varshi99)

---

## ⭐ Project Highlights

An end-to-end business analytics project combining three important business domains: **Revenue Assurance, Sales Intelligence, and Operational Performance Analytics**.

Built using Excel, SQL, Python, Pandas, Matplotlib, and Power BI to demonstrate practical data analytics and business intelligence skills.

