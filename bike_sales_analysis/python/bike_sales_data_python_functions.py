"""
Bike Sales Performance Analysis — 2015
Exploratory Data Analysis (EDA)

Dataset: bike_sales_clean.csv
Author: Maksym Herasymiuk
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Data ─────────────────────────────────────────────────────────────────

df = pd.read_csv('bike_sales_clean.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Filter 2015 only
df_2015 = df[df['Year'] == 2015]

print(f"Total rows (2015): {len(df_2015)}")
print(df_2015.info())
print(df_2015.describe())


# ── Chart 1: Top 10 Products by Revenue ───────────────────────────────────────

top_10 = (
    df_2015.groupby('Product', as_index=False)['Revenue']
    .sum()
    .sort_values('Revenue', ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
plt.bar(top_10['Product'], top_10['Revenue'])
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Revenue')
plt.title('Top 10 Products by Revenue — 2015')
plt.tight_layout()
plt.savefig('visuals/python/top10_products_by_revenue.png', dpi=150)
plt.show()

# Insight: Road-150 Red, 62 is the highest revenue product (~1M),
# followed closely by Mountain-200 Black, 38 (~910K).


# ── Chart 2: Monthly Revenue Trend ────────────────────────────────────────────

df_2015 = df_2015.copy()
df_2015['Month'] = df_2015['Date'].dt.month
monthly_revenue = df_2015.groupby('Month')['Revenue'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(monthly_revenue['Month'], monthly_revenue['Revenue'], marker='o')
plt.xticks(
    ticks=range(1, 13),
    labels=['Jan','Feb','Mar','Apr','May','Jun',
            'Jul','Aug','Sep','Oct','Nov','Dec']
)
plt.ylabel('Revenue')
plt.ticklabel_format(style='plain', axis='y')
plt.title('Monthly Revenue — 2015')
plt.grid(True)
plt.tight_layout()
plt.savefig('visuals/python/monthly_revenue.png', dpi=150)
plt.show()

# Insight: Revenue is flat Jan–Jun (~700K–900K/month), then grows sharply
# from July, peaking in December at 3.8M — strong seasonal pattern.


# ── Chart 3: Revenue by Country ───────────────────────────────────────────────

country_revenue = (
    df.groupby('Country')['Revenue']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 6))
plt.bar(country_revenue.index, country_revenue.values)
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Revenue')
plt.title('Revenue by Country — 2015')
plt.tight_layout()
plt.savefig('visuals/python/revenue_by_country.png', dpi=150)
plt.show()

# Insight: United States leads with ~27.5M, followed by Australia (~21M).
# Canada is the weakest market at ~8M despite similar product availability.


# ── Chart 4: Revenue Share by Product Category ────────────────────────────────

category_revenue = (
    df_2015.groupby('Product_Category')['Revenue']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 8))
plt.pie(
    category_revenue.values,
    labels=category_revenue.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Revenue Share by Product Category — 2015')
plt.axis('equal')
plt.tight_layout()
plt.savefig('visuals/python/revenue_by_product_category.png', dpi=150)
plt.show()

# Insight: Bikes dominate with 72.4% of total revenue.
# Accessories account for 17.7%, Clothing only 9.9%.


# ── Chart 5: Correlation Heatmap (Order Quantity, Profit, Revenue) ────────────

corr_data = df_2015[['Order_Quantity', 'Profit', 'Revenue']].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(
    corr_data,
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    linewidths=0.5
)
plt.title('Correlation Heatmap — 2015')
plt.tight_layout()
plt.savefig('visuals/python/correlation_heatmap.png', dpi=150)
plt.show()

# Insight: Profit and Revenue are strongly correlated (0.96).
# Order_Quantity has a weak negative correlation with both Revenue (-0.31)
# and Profit (-0.25) — higher quantity orders tend to be lower-value items.