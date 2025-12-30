import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

url = "https://www.louisvuitton.com/eng-in/women/handbags/_/N-tfr7qdp"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = []

for item in soup.select("div[data-testid='product-card']"):
    try:
        name = item.select_one("p").text.strip()
        price = item.select_one("span").text.strip()

        products.append({
            "Product_Name": name,
            "Category": "Handbags",
            "Price": price,
            "Gender": "Women",
            "Currency": "INR"
        })
    except:
        continue

df = pd.DataFrame(products)

# Save safely
df.to_csv("data/lv_raw_data.csv", index=False)

print("✅ Data saved to data/lv_raw_data.csv")
