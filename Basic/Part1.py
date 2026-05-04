import pandas as pd

file_path = "copy.xlsx"

# Read all sheets And get sheet names and data samples
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

results = []

for sheet in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet)

    rows, cols = df.shape
    headers = list(df.columns)

    # Take first 5 columns (if less, take all)
    sample_cols = headers[:5]
    sample_data = df[sample_cols].head(5)

    result = {
        "sheet_name": sheet,
        "rows": rows,
        "columns": cols,
        "headers": headers,
        "sample_columns": sample_cols,
        "sample_data": sample_data
    }

    results.append(result)

# Print output
for r in results:
    print(f"\n=== Sheet: {r['sheet_name']} ===")
    print(f"Rows: {r['rows']}")
    print(f"Columns: {r['columns']}")
    print(f"Headers: {r['headers']}")
    print("\nSample Data (first 5 columns):")
    print(r["sample_data"])