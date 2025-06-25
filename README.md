# 📊 Data-Driven Analysis of 10 Major U.S. Stocks: Return vs. Volatility

[![Power BI](https://img.shields.io/badge/Built%20With-Power%20BI-blue.svg)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Data%20Extraction-Python-yellow.svg)](https://www.python.org/)
[![Alpha Vantage](https://img.shields.io/badge/Data-Alpha%20Vantage-brightgreen)](https://www.alphavantage.co/)

This project presents a comprehensive, sector-diverse stock performance analysis using data from 10 major U.S. companies. It visualizes key financial metrics—such as 1-Year Return, Volatility, Average Volume, and Drawdown—to identify high-growth, low-risk investment opportunities.

📍 GitHub Repo:  
**[RionelxSlovesky/Data-Driven-Analysis-of-10-Major-U.S.-Stocks-Return-vs.-Volatility](https://github.com/RionelxSlovesky/Data-Driven-Analysis-of-10-Major-U.S.-Stocks-Return-vs.-Volatility.git)**

---

## 🚀 Project Summary

This Power BI dashboard was created as part of an academic data analytics project (BANL 6600). It focuses on analyzing daily price movements and fundamentals of 10 top U.S. stocks to understand sector dynamics and performance patterns.

---

## 🧾 Key Features

- 📈 **Visual Analytics**: KPIs, bar charts, and line graphs for Return %, Volatility, and Volume
- 🔍 **Stock-Level Deep Dives**: Track historical price movement and drawdowns by symbol
- 🧠 **Insight Metrics**: DAX measures for 1-Year Return, Volatility (stdev), Avg Volume, and Max Drawdown
- 🛠 **3-Page Dashboard**:
  - **Summary**: Top performers and risk metrics
  - **Comparison**: Cross-stock visualization
  - **Deep Dive**: Stock-specific trend view
- 📊 **Calculated Columns**: Daily Return %, Price Direction, Day of Week

---

## 🗃️ Datasets Used

- **Stock Prices**: `TIME_SERIES_DAILY` from Alpha Vantage (JSON, 10 stocks)
- **Company Fundamentals**: `OVERVIEW` endpoint for PE ratio, sector, and market cap

Companies analyzed:  
`AAPL`, `MSFT`, `TSLA`, `AMZN`, `GOOGL`, `NVDA`, `META`, `V`, `JNJ`, `JPM`

---

## 🛠️ Tech Stack

**Technologies:**  
`Python`, `Power BI`, `DAX`, `Power Query`, `JSON`, `REST API`, `Alpha Vantage API`

---

## 📂 Folder Structure

/Stock Prices datasets/ ← JSON files for daily price data
/Company Overviews datasets/ ← JSON files for company metadata
/Power BI Report/ ← .pbix file (dashboard)
/Scripts/ ← Python scripts for data download

---

## 📦 How to Use

1. Clone this repo  
2. Run the Python script to download or update datasets  
3. Open the `.pbix` file in Power BI Desktop  
4. Refresh to import the static JSON files  
5. Explore the interactive dashboard!

---

## 📅 Timeline

**Start:** April 2025  
**Completed:** May 2025

---

## 🧑‍💼 Author

**Rionelx Slovesky**  
[GitHub Profile](https://github.com/RionelxSlovesky)

---

## 📜 License

This project is for academic and educational purposes only.  
Stock data sourced via the free-tier [Alpha Vantage API](https://www.alphavantage.co/).

