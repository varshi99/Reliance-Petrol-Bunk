
-- Reliance Petrol Bunk Analytics (practice project)
-- All data is synthetic and for learning only.
CREATE DATABASE IF NOT EXISTS petrol_bunk_analytics;
USE petrol_bunk_analytics;

DROP TABLE IF EXISTS fuel_sales;
CREATE TABLE fuel_sales (
    transaction_id VARCHAR(20) PRIMARY KEY,
    transaction_date DATE NOT NULL,
    transaction_time TIME NOT NULL,
    fuel_type VARCHAR(30) NOT NULL,
    litres_sold DECIMAL(10,2) NOT NULL,
    price_per_litre_inr DECIMAL(10,2) NOT NULL,
    sales_amount_inr DECIMAL(12,2) NOT NULL,
    payment_method VARCHAR(20),
    shift VARCHAR(20),
    attendant_id VARCHAR(20),
    nozzle_id VARCHAR(20),
    is_weekend VARCHAR(3)
);

DROP TABLE IF EXISTS fuel_inventory;
CREATE TABLE fuel_inventory (
    inventory_date DATE NOT NULL,
    fuel_type VARCHAR(30) NOT NULL,
    opening_stock_litres DECIMAL(12,2),
    delivery_litres DECIMAL(12,2),
    litres_sold DECIMAL(12,2),
    closing_stock_litres DECIMAL(12,2),
    reorder_level_litres DECIMAL(12,2),
    PRIMARY KEY (inventory_date, fuel_type)
);

DROP TABLE IF EXISTS operating_expenses;
CREATE TABLE operating_expenses (
    expense_month DATE NOT NULL,
    expense_category VARCHAR(30) NOT NULL,
    expense_amount_inr DECIMAL(12,2) NOT NULL,
    PRIMARY KEY (expense_month, expense_category)
);

-- Import the CSV files into the matching tables using MySQL Workbench
-- Table Data Import Wizard. Keep column order as in the CSV files.

-- 1. Revenue and volume by fuel type
SELECT fuel_type, SUM(litres_sold) AS total_litres,
       SUM(sales_amount_inr) AS total_revenue
FROM fuel_sales GROUP BY fuel_type ORDER BY total_revenue DESC;

-- 2. Daily revenue trend
SELECT transaction_date, SUM(sales_amount_inr) AS daily_revenue
FROM fuel_sales GROUP BY transaction_date ORDER BY transaction_date;

-- 3. Peak sales hours
SELECT HOUR(transaction_time) AS sales_hour,
       COUNT(*) AS transactions,
       SUM(sales_amount_inr) AS revenue
FROM fuel_sales GROUP BY HOUR(transaction_time) ORDER BY revenue DESC;

-- 4. Payment method mix
SELECT payment_method, COUNT(*) AS transaction_count,
       SUM(sales_amount_inr) AS revenue
FROM fuel_sales GROUP BY payment_method ORDER BY revenue DESC;

-- 5. Shift performance
SELECT shift, COUNT(*) AS transactions,
       SUM(litres_sold) AS litres_sold,
       SUM(sales_amount_inr) AS revenue
FROM fuel_sales GROUP BY shift ORDER BY revenue DESC;

-- 6. Attendant performance (volume/revenue, not a staff productivity judgement)
SELECT attendant_id, COUNT(*) AS transactions,
       SUM(sales_amount_inr) AS revenue
FROM fuel_sales GROUP BY attendant_id ORDER BY revenue DESC;

-- 7. Weekend vs weekday
SELECT is_weekend, COUNT(*) AS transactions,
       SUM(sales_amount_inr) AS revenue
FROM fuel_sales GROUP BY is_weekend;

-- 8. Inventory below reorder level
SELECT inventory_date, fuel_type, closing_stock_litres, reorder_level_litres
FROM fuel_inventory
WHERE closing_stock_litres < reorder_level_litres
ORDER BY inventory_date, fuel_type;

-- 9. Monthly operating expenses
SELECT DATE_FORMAT(expense_month, '%Y-%m') AS month,
       SUM(expense_amount_inr) AS operating_expenses
FROM operating_expenses
GROUP BY DATE_FORMAT(expense_month, '%Y-%m') ORDER BY month;

-- 10. Transaction data quality checks
SELECT * FROM fuel_sales
WHERE litres_sold <= 0 OR price_per_litre_inr <= 0
   OR ABS(sales_amount_inr - litres_sold * price_per_litre_inr) > 1;
