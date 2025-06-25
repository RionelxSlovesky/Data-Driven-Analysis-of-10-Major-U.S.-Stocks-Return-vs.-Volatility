import requests
import time
import os

api_key = "ZC5OFG5K83O85NQ8"

stock_symbols = ["AAPL", "MSFT", "TSLA", "AMZN", "GOOGL", "NVDA", "META", "V", "JNJ", "JPM"]

base_url = "https://www.alphavantage.co/query"

folder_name = "Company Overviews datasets"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"📂 Folder '{folder_name}' created successfully!")
else:
    print(f"📂 Folder '{folder_name}' already exists.")

for symbol in stock_symbols:
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": api_key
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        filename = os.path.join(folder_name, f"{symbol}_CompanyOverview.json")
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download overview for {symbol} - Status Code: {response.status_code}")

    time.sleep(15)
