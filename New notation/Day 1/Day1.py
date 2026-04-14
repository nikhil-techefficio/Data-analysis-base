import pandas as pd

# Load data
df = pd.read_excel("New notation\Day 1\Book.xlsx")
# df = pd.read_excel(r"C:\Users\amit\Documents\GitHub\Data-analysis-base\New notation\Day 1\Book.xlsx")

# Total revenue by region
rev_region = df.groupby("Region")["Revenue"].sum()
print("Revenue by Region:", rev_region)

# Units by category
units_category = df.groupby("Product_Category")["Units_Sold"].sum()
print("Units by Category:", units_category)

# Average revenue per day
avg_revenue = df["Revenue"].mean()
print("Average Revenue per Day:", avg_revenue)

# Top store
top_store = df.groupby("Store_ID")["Revenue"].sum().idxmax()
print("Top Store:", top_store)

# Detect anomalies
df["Price_per_unit"] = df["Revenue"] / df["Units_Sold"]
anomalies = df[df["Price_per_unit"] > 200]

print("Revenue by Region:", rev_region)
print("Units by Category:", units_category)
print("Average Revenue per Day:", avg_revenue)
print("Top Store:", top_store)
print("Anomalies:", anomalies)