Bike Sales Performance Analysis — 2015
One-line Description (for GitHub repo)

End-to-end sales analysis of a global bike store for 2015 — SQL, Python, and Power BI focused on revenue performance, seasonality, and customer segments.


Project Overview
This project is a full end-to-end analysis of a global bike store dataset for the year 2015, covering 6 countries, 130+ products, and 112,000+ transactions. The primary focus was revenue analysis — understanding where revenue comes from, how it behaves across time, products, geographies, and customer segments.
The full pipeline covers data cleaning in PostgreSQL, exploratory data analysis in Python/pandas, and an interactive 3-page Power BI dashboard.

Tech Stack
ToolPurposePostgreSQLData cleaning, revenue aggregations, window functionsPython (pandas, matplotlib, seaborn)EDA, revenue visualisationsPower BIInteractive dashboard with revenue KPIs and drill-downExcelPivot summary for non-technical stakeholders

Dataset

Source: Europe Bike Store Sales (Kaggle)
Year analysed: 2015
Size: 112,036 rows after cleaning
Key columns: Date, Country, State, Product, Sub-Category, Customer Age, Gender, Order Quantity, Unit Cost, Unit Price, Revenue, Profit, Cost


Project Structure
bike_sales_analysis/
│
├── data/
│   └── bike_sales.csv
│
├── powerbi/
│   └── bike_sales_data.pbix
│
├── python/
│   └── bike_sales_data_python_functions.py
│
├── sql/
│   ├── top10_products_by_revenue_2015.sql
│   ├── total_revenue_and_profit_by_country_2015.sql
│   ├── total_revenue_for_every_month_2015.sql
│   ├── total_revenue_by_age_group_2015.sql
│   ├── total_revenue_for_genders_2015.sql
│   ├── avg_order_quantity_for_sub_category_2015.sql
│   ├── england_total_revenue_2015.sql
│   ├── margin_for_every_sub_category_2015.sql
│   ├── ranking_products_by_total_revenue_for_sub_categories_2015.sql
│   ├── top_states_by_total_revenue_australia_2015.sql
│   ├── top_states_by_total_revenue_canada_2015.sql
│   ├── top_states_by_total_revenue_germany_2015.sql
│   ├── top10_states_by_total_revenue_france_2015.sql
│   └── top10_states_by_total_revenue_usa_2015.sql
│
├── visuals_python/
│   ├── correlation_order_quantity_profit_revenue.png
│   ├── monthly_revenue.png
│   ├── revenue_by_product_category.png
│   ├── revenue_for_country.png
│   └── top10_products_by_revenue.png
│
└── README.md

Data Cleaning (SQL + Python)

Checked for NULL values across all columns — none found
Removed ~900 duplicate rows (112,036 clean rows remaining)
Converted data types: date columns to DATE, financial columns to NUMERIC
Validated revenue formula: Order_Quantity × Unit_Price


Revenue Analysis (SQL)
Revenue was the central metric across all 9 SQL queries:
QueryDescriptionTop 10 products by revenueIdentified highest-earning products in 2015Revenue by countryCompared total revenue across 6 marketsMonthly revenue seasonalityTracked revenue trend across all 12 monthsAverage revenue per order by age groupMeasured spending behaviour by customer segmentProfit margin by category (Profit/Revenue)Evaluated how efficiently revenue converts to profitRolling 3-month average revenueSmoothed monthly fluctuations to identify trendRevenue by customer genderCompared average order revenue M vs FTop states by revenue within each countryDrilled down geography to state levelAverage order quantity by sub-categoryIdentified which categories drive volume vs value

Key Findings — 2015
Revenue Performance
Total revenue for 2015 reached 20M with a profit of 8M, giving an overall margin of ~40%. Average order revenue was 819.
Seasonality
Revenue showed a strong seasonal pattern in 2015 — flat from January to June (~0.7–0.9M/month), then growing sharply from July and peaking in December at 3.8M. This suggests holiday-driven demand in the second half of the year.
Product Revenue
Road Bikes generated 36.31% of total revenue, followed by Mountain Bikes at 27.84%. The single highest-revenue product was Road-150 Red, 62 at ~1M. Accessories contributed a minor share despite high order volume.
Geographic Revenue
Australia and the United States were the top revenue markets in 2015. Canada significantly underperformed compared to other markets despite similar product availability — potential opportunity for growth.
Customer Revenue Segments

Adults (35–64) generated the highest revenue (~8–9M) — the most valuable segment
Seniors (64+) contributed negligible revenue
Gender split was nearly equal (50/50 revenue share), but female customers had a slightly higher average order revenue (829 vs 809)


Power BI Dashboard — 2015
3-page interactive dashboard with slicers for Country and Product Category:
Page 1 — Overview: Revenue and Profit KPI cards, average order revenue, monthly revenue trend (2015), top 5 products by revenue, sub-category revenue breakdown
Page 2 — Geography: World map by country revenue, Revenue/Profit by country per month (small multiples)
Page 3 — Customer: Average order revenue by gender, top products by age group, revenue by gender and country, revenue by age group

How to Run
SQL:

Import data/bike_sales.csv into PostgreSQL
Run queries from /sql folder in order

Python:

Install dependencies: pip install pandas matplotlib seaborn jupyter
Open notebook/bike_sales_eda.ipynb
Run all cells

Power BI:

Open .pbix file in Power BI Desktop
Update data source path if needed
