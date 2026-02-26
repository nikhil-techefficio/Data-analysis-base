import pandas as pd

# Load data
df = pd.read_excel("Day 1/Book.xlsx")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Total revenue
total_revenue = df["Revenue"].sum()

# Revenue by Region
region_sales = df.groupby("Region")["Revenue"].sum()

# Revenue by Category
category_sales = df.groupby("Category")["Revenue"].sum()

# Monthly Trend
df["Month"] = pd.to_datetime(df["OrderDate"]).dt.to_period("M")
monthly_sales = df.groupby("Month")["Revenue"].sum()

# Top 5 Customers
top_customers = df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(5)
print(df.columns)
print(list(df.columns))
print(total_revenue)
print(region_sales)
print(category_sales)
print(monthly_sales)
print(top_customers)