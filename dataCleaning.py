
import pandas as pd

# 1. Load Data
df = pd.read_csv("OnlineRetailCSV.csv")

# 2. Data Type Conversion
# Convert relevant columns to appropriate types for analysis
df["InvoiceNo"] = df["InvoiceNo"].astype("string")
df["StockCode"] = df["StockCode"].astype("string")
df["Description"] = df["Description"].astype("string")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df["Country"] = df["Country"].astype("string")

# 3. Data Quality Checks
print("\n===== DATASET OVERVIEW =====")
print(df.info())

print("\n--- Null values per column ---")
print(df.isnull().sum())

num_duplicates = df.duplicated().sum()
print(f"\n--- Number of duplicated rows: {num_duplicates}")

print("\n--- Outlier check: Quantity and UnitPrice ---")
print(f"Quantity: min = {df['Quantity'].min()}, max = {df['Quantity'].max()}")
print(f"UnitPrice: min = {df['UnitPrice'].min()}, max = {df['UnitPrice'].max()}")

# Remove duplicates
# df = df.drop_duplicates()

# Handle missing values 
# df = df.dropna()

# 4. Identify Canceled Invoices
# Canceled invoices typically start with 'C'.
canceled_mask = df["InvoiceNo"].str.startswith("C")
canceled_invoices = df.loc[canceled_mask]
# print(canceled_invoices.head())

# 5. Export Cleaned Data
df.to_csv("OnlineRetail_cleaned.csv", index=False)
print("\nCleaned data exported to 'OnlineRetail_cleaned.csv'.")