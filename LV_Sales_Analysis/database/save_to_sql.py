import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_excel("data/lv_cleaned_data.xlsx")

# Create SQLite database
engine = create_engine("sqlite:///data/lv_sales.db")

# Save to SQL table
df.to_sql("lv_sales", engine, if_exists="replace", index=False)

print("✅ Data saved to SQL database")
