import pandas as pd

df = pd.read_csv("OnlineRetailCSV.csv")

#print(df.dtypes())
mask = df["InvoiceNo"].astype(str).str.contains(r"\D")
correct_valsInvoice = df.loc[mask, "InvoiceNo"].astype(str).str[1:]

Cvals = df.loc[df["InvoiceNo"].astype(str).str[::] == "C537413"]
vals = df.loc[df["InvoiceNo"].astype(str).str[::] == "537413"]
#print(Cvals.head())
#print(vals.head())

#print(df.dtypes)
#print(df["InvoiceNo"].head())
df["InvoiceNo"] = df["InvoiceNo"].astype("string")
#print(df["StockCode".head()])
df["StockCode"] = df["StockCode"].astype("string")
df["Description"] = df["Description"].astype("string")
#print(df["InvoiceDate"].head())
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
#print(df["InvoiceDate"].head())
#print(df["InvoiceDate"].isna().any())
#print(df.dtypes)
df["Country"] = df["Country"].astype("string")

#print(df.dtypes)
print(df.info())
df.to_csv("OnlineRetail_cleaned.csv", index=False)