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