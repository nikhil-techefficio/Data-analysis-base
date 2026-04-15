# Add new colum to XL 
# Remove column from XL
# Rename column in XL
# Filter data based on conditions (e.g., age > 30, country = 'USA')<--
# unique values in a column
# unique values in a Row
# Load data from different formats (CSV, JSON, PDF) <--
# Perform basic data analysis (sum, mean, group by) 
# complex data analysis (pivot tables, cross-tabulations, time series analysis) <--


 # import pandas library 
import pandas as pd
  # read the excel file
df = pd.read_excel("New notation\Day 1\Book2.xlsx")
  # get basic info about the data and sample of the data
# print(df.info())
print(df.head(5))

# Add new colum to XL Temperoary column(only updates the DataFrame in memory (temporary))

df["test1"] = ""
df["test2"] = 0
df["test3"] = "True"

# Rename column in XL
df.rename(columns={"test1": "Nikhil"}, inplace=True)

print(df.head(5))

# Remove column from XL

df.drop("test3", axis=1, inplace=True)

# Now the changes are stored in data frames but not in the original excel file.
#  To save the changes to the excel file, 
# we need to use the to_excel() method.
 #Option 1: Overwrite the same file
# df.to_excel("New notation\Day 1\Book2.xlsx", index=False)

# Option 2: Save to a new file
df.to_excel("New notation\Day 1\Book2_updated.xlsx", index=False)

 # option 3: Save in same file but in a different sheet

# with pd.ExcelWriter("New notation\Day 1\Book2.xlsx", mode='a') as writer:
#     df.to_excel(writer, sheet_name='Updated', index=False)


# To dispaly the unique values in a column, we can use the unique() method.
unique_values = df["Region"].unique()
print(unique_values)

#add ons 

df["Region"].nunique() # to get the number of unique values in a column
df["Region"].value_counts() # to get the count of each unique value in a column

# now to display the unique values in a row, we can use the unique() method on the row as well.
unique_values_row = df.iloc[0].unique()
print("Row 0:", unique_values_row) # not much useful

# Perform basic data analysis (sum, mean, group by) 
print("Sum of Sales:", df["Sales"].sum())
print("Mean of Sales:", df["Sales"].mean())
print("Group by Region:")
print(df.groupby("Region")["Sales"].sum())
# Add on Advanced
df["sum"] = df["Sales"].sum()
df["mean"] = df["Sales"].mean() 


# Math Formulas usage in data analysis


# Load data from different formats (CSV, JSON, PDF) <--
df_csv = pd.read_csv("data.csv")
df_json = pd.read_json("data.json")


#Now to handle missing values in the data, we can use the fillna() method to fill the missing values with a specific value or with the mean/median/mode of the column.
df["Sales"].fillna(df["Sales"].mean(), inplace=True) # fill missing values with mean of the column
#1. Handling missing values (VERY important)
df.isnull().sum()
df.dropna()
df.fillna(0)

# Sorting data
df.sort_values(by="Sales", ascending=False, inplace=True)
df.sort_values("Revenue", ascending=False)

# Grouping (VERY important for analysis)
grouped = df.groupby("Region")["Sales"].sum()

# Index basics
df.set_index("Region", inplace=True) # set Region as index
df.set_index("Date")
df.reset_index()

# Column operations (advanced basics)
df["Revenue"] = df["Sales"] * df["Price_per_unit"] # create a new column Revenue by multiplying Sales and Price_per_unit

df["cum_sales"] = df["Sales"].cumsum() # create a new column cum_sales which is the cumulative sum of sales
df["pct"] = df["Sales"] / df["Sales"].sum() * 100 # create a new column pct which is the percentage of sales out of total sales

# Duplicate handling
df.duplicated() # to check for duplicate rows
df.drop_duplicates(inplace=True) # to drop duplicate rows
df.duplicated().sum() # to get the count of duplicate rows


# filtering + grouping + missing values
filtered = df[df["Sales"] > 1000] # filter rows where Sales is greater than 1000
grouped_filtered = filtered.groupby("Region")["Sales"].sum() # group the filtered data by Region and sum the Sales
grouped_filtered.fillna(0, inplace=True) # fill missing values in the grouped data          



 # Multiple conditions or and and usage
filtered_multi = df[(df["Sales"] > 1000) & (df["Region"] == "North")] # filter rows where Sales is greater than 1000 and Region is North
filtered_multi_or = df[(df["Sales"] > 1000) | (df["Region"] == "North")] # filter rows where Sales is greater than 1000 or Region is North
df[(df["Revenue"] > 1000) & (df["Region"] == "South")]
df[(df["Region"] == "South") | (df["Region"] == "East")]
# IN condition (very important)
df[df["Region"].isin(["South", "East"])]        
# BETWEEN range     
df[df["Revenue"].between(500, 2000)]    

# Multiple aggregations
agg = df.groupby("Region").agg({"Sales": ["sum", "mean"], "Revenue": ["sum", "mean"]})
