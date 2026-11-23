# 📈 Financial Data Analysis & Forecasting using Python & Tableau

**Author:** Rakesh Reddy Gopireddy  
**Tools:** Python (Pandas, Matplotlib, Statsmodels), Tableau  
**Domain:** Finance | Stock Market Analysis | Time Series Forecasting

---

## 📌 Project Overview

This project analyzes historical stock market data to understand stock trends, monthly distribution, technical indicators, and to forecast future stock prices.

The goal is to convert raw stock data into clear insights that help investors understand market behavior and make better decisions.

---

## ❓ Business Questions Answered

1. What are the overall stock trends over the years?
2. What is the monthly revenue / profit distribution?
3. What does Technical Analysis (MA50, MA200) say?
4. What is the predicted stock price for the next 90 days?
5. What is the forecasted future performance of AAPL stock?

---

## 📂 Dataset

- **Source:** Stock Market Historical Data (Google / Public Dataset)
- **Period:** 2013 - 2018
- **Key Columns:** Date, Open, High, Low, Close, Volume, Stock Symbol
- **Stocks Analyzed:** AAPL, PCLN, GOOG, GOOGL, AZO and Top 10 Stocks

---

## 🛠️ Tools & Libraries Used

| Tool | Used For |
| --- | --- |
| Python | Data Cleaning, EDA, Forecasting |
| Pandas | Data Processing, `info()`, `isnull()`, `drop_duplicates()` |
| Matplotlib | Forecasting Charts |
| Statsmodels - ARIMA | Time Series Forecasting |
| Tableau | Dashboard, Technical Analysis, Storytelling |

---

## 🔄 Methodology

### 1. Data Processing & Cleaning
- Imported raw data and checked shape using `df.info()`
- Checked missing values using `df.isnull().sum()`
- Removed duplicates using `df.drop_duplicates()`
- Converted Date column using `pd.to_datetime()`

### 2. Exploratory Data Analysis (EDA)
- Analyzed stock trends year-wise
- Calculated Daily Return = (Close - Open) / Open
- Calculated Volatility using daily returns
- Analyzed monthly distribution of stock prices

### 3. Technical Analysis
- Calculated **MA50** - 50-Day Moving Average
- Calculated **MA200** - 200-Day Moving Average
- Analyzed MA crossovers to identify trend changes

### 4. Forecasting with ARIMA
- Used **ARIMA (AutoRegressive Integrated Moving Average)** model
- ARIMA predicts future values based on historical data
- Forecasted AAPL stock price for next 90 days

### 5. Visualization in Tableau
- Top 10 Stocks Dashboard
- Monthly Distribution Chart
- Technical Analysis Dashboard
- Forecast Trend Dashboard

---

## 📊 Key Insights

### 1. Stock Trend (2013-2017)
- Stock prices increased steadily from 2013 to 2017
- Peak performance occurred in **2017**

### 2. Technical Analysis
- MA50 and MA200 moved upward until 2017
- Both moving averages fell sharply in **2018**, indicating trend reversal

### 3. Top Performing Stocks
- **PCLN, GOOG, GOOGL, AZO** are top-performing stocks based on average closing price
- Indicates strong market value and investor confidence

### 4. Monthly Distribution
- Stock prices remain relatively stable throughout the year
- Stronger performance observed during final months of year

### 5. AAPL Forecast (Feb - June 2018)
- Forecast price increased from **~2.4K in Feb to ~3.5K in March** - Strong growth
- Slight decline in April, recovered in May to highest forecast **~3.6K**
- Sharp decline predicted in **June**, indicating possible market correction

---

## 📁 Project Structure
