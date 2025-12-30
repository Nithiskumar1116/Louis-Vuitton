import pandas as pd
import numpy as np
import os

# Check file exists
file_path = "data/lv_raw_data.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError("❌ Raw data file not found")

# Load data
df = pd.read_csv(file_path)

# Check empty file
if df.empty:
    raise ValueError("❌ Raw data file is empty")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Ensure price is numeric
df["Price"] = df["Price"].astype(float)

# Add simulated sales data
np.random.seed(42)
df["Units_Sold"] = np.random.randint(10, 200, size=len(df))
df["Revenue"] = df["Price"] * df["Units_Sold"]

# Add date columns
df["Month"] = np.random.choice(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], size=len(df)
)
df["Year"] = 2024

# Save cleaned Excel
df.to_excel("data/lv_cleaned_data.xlsx", index=False)

print("✅ Data preprocessing completed successfully")
