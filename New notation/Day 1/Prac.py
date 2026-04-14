import pandas as pd

# Load data
df = pd.read_excel("New notation\Day 1\Book1.xlsx")
print( df.info())

print(df.head(5))

#Total revenue :
print("Total Revenue:", df["Revenue"].sum())

#Revenue by region
rev_region = df.groupby("Region")["Revenue"].sum()  
print("Revenue by Region:", rev_region)

#Total revenue :
print("Total Units Sold:", df["Units_Sold"].sum())
#Units sold by category
units_category = df.groupby("Product_Category")["Units_Sold"].sum() 
print("Units by Category:", units_category)