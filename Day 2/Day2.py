import pandas as pd

df = pd.read_excel("Day 2/Day2.xlsx")

df["Revenue"] = df["Quantity"] * df["UnitPrice"] * (1 - df["Discount%"]/100)
df["Cost"] = df["Quantity"] * df["UnitCost"]
df["Profit"] = df["Revenue"] - df["Cost"]
df["Margin"] = df["Profit"] / df["Revenue"]

Revenue = df["Revenue"].sum()
Before_Discount_Revenue = (df["Quantity"] * df["UnitPrice"]).sum()
Revenue_by_category = df.groupby("Category")["Revenue"].sum()
Revenue_by_region = df.groupby("Region")["Revenue"].sum()
# Revenue_by_month = df.groupby(df["OrderDate"].dt.to_period("M"))["Revenue"].sum()
Revenue_by_customer = df.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False).head(5)
Revenue_by_product = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
Revenue_by_discount = df.groupby("Discount%")["Revenue"].sum()
Revenue_by_profit_margin = df.groupby(pd.cut(df["Margin"], bins=[0, 0.1, 0.2, 0.3, 1], labels=["<10%", "10-20%", "20-30%", ">30%"]))["Revenue"].sum()
total_profit = df["Profit"].sum()

region_margin = df.groupby("Region").agg({
    "Revenue":"sum",
    "Profit":"sum"
})

region_margin["Margin%"] = region_margin["Profit"] / region_margin["Revenue"]

low_margin_products = df[df["Margin"] < 0.10][["Product","Margin"]]
print("Total Profit After Discount:",Revenue)
print("Total Profit Without Discount:",Before_Discount_Revenue)
print("Total Profit:\n",total_profit)
print("Revenue by Category:\n",Revenue_by_category)
print("Revenue by Region:",Revenue_by_region) 
# print("Revenue by Month:\n",Revenue_by_month)
print("Revenue by Customer:\n",Revenue_by_customer)

print("Region-wise Margin:",region_margin)
print("Low Margin Products:",low_margin_products)