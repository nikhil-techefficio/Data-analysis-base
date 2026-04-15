import pandas as pd

# Load data
df = pd.read_excel("New notation\Day 1\Book1.xlsx")
# dcsv = pd.read_csv("file.csv")
# dj = pd.read_json("file.json")
# pandas cant read PDF files directly, we need to use a library like PyPDF2 or pdfplumber to extract text from PDF files and then create a DataFrame from that text.
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
units_category_Revenue = df.groupby("Product_Category")["Revenue"].sum() 
print("Units by Category:", units_category)
print("Revenue by Category:", units_category_Revenue)

# Average revenue per day
avg_revenue = df["Revenue"].mean()

# Top store
top_store = df.groupby("Store_ID")["Revenue"].sum().idxmax()

# Detect anomalies
df["Price_per_unit"] = df["Revenue"] / df["Units_Sold"]
anomalies = df[df["Price_per_unit"] > 200]
mean = df["Price_per_unit"].mean()
std = df["Price_per_unit"].std()
print("price per unit:", mean)
print("anomalies:", anomalies )