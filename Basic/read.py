# import pandas as pd

# # Load Excel file
# df = pd.read_excel("copy.xlsx")
# # df = pd.read_excel("copy.xlsx", sheet_name="Sheet1")

# # Get number of rows and columns
# rows, cols = df.shape

# # Get first row (column names)
# columns = list(df.columns)

# print("Rows:", rows)
# print("Columns:", cols)
# print("First Row (Headers):", columns)

# # df.shape → gives (rows, columns)
# # df.columns → reads first row as headers

# # Get sheet names
# sheet_names = df.sheet_names

# # Count number of sheets
# num_sheets = len(sheet_names)

# print("Number of sheets:", num_sheets)
# print("Sheet names:", sheet_names)





import pandas as pd

# Load Excel file as ExcelFile object
excel_file = pd.ExcelFile("copy.xlsx")

# Get sheet names
sheet_names = excel_file.sheet_names

# Count number of sheets
num_sheets = len(sheet_names)

print("Number of sheets:", num_sheets)
print("Sheet names:", sheet_names)

# Now read a specific sheet (first one)
df = pd.read_excel(excel_file, sheet_name=sheet_names[0])

# Get number of rows and columns
rows, cols = df.shape

# Get first row (column names)
columns = list(df.columns)

print("\nFirst sheet analysis:")
print("Rows:", rows)
print("Columns:", cols)
print("Headers:", columns)