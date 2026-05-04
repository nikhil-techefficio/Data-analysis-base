import pandas as pd

file_path = "copy.xlsx"

# Load all sheets
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names

total_sheets = len(sheet_names)

print(f"Total Sheets: {total_sheets}")
print("=" * 60)

summary = []

for sheet in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet)

    rows, cols = df.shape
    headers = list(df.columns)

    print(f"\n📄 Sheet Name: {sheet}")
    print(f"Rows: {rows}")
    print(f"Columns: {cols}")
    print(f"Headers: {headers}")

    print("\nSample Data (First 5 Rows):")
    print(df.head(5))

    print("-" * 60)

    summary.append({
        "sheet": sheet,
        "rows": rows,
        "columns": cols
    })

# Final Summary
print("\n📊 FINAL SUMMARY")
print("=" * 60)

for s in summary:
    print(f"{s['sheet']} → Rows: {s['rows']}, Columns: {s['columns']}")