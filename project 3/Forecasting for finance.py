import pandas as pd
import matplotlib.pyplot as plt

# ======================
# Import Data
# ======================

df = pd.read_csv("all_stocks_5yr.csv")

print(df.head())
print(df.info())

# ======================
# Data Cleaning
# ======================

print(df.isnull().sum())

df.dropna(inplace=True)

df['date'] = pd.to_datetime(df['date'])

# ======================
# Exploratory Analysis
# ======================

top_stocks = (
    df.groupby('Name')['close']
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop Stocks:")
print(top_stocks)

# ======================
# Daily Returns
# ======================

df = df.sort_values(['Name', 'date'])

df['Daily_Return'] = (
    df.groupby('Name')['close']
      .pct_change()
)

# ======================
# Volatility
# ======================

volatility = (
    df.groupby('Name')['Daily_Return']
      .std()
      .sort_values(ascending=False)
)

print("\nMost Volatile Stocks:")
print(volatility.head(10))

# ======================
# Moving Averages
# ======================

df['MA50'] = (
    df.groupby('Name')['close']
      .transform(lambda x: x.rolling(50).mean())
)

df['MA200'] = (
    df.groupby('Name')['close']
      .transform(lambda x: x.rolling(200).mean())
)

# ======================
# Forecasting
# ======================


from statsmodels.tsa.arima.model import ARIMA

stock = df[df['Name'] == 'AAPL'].copy()

stock['date'] = pd.to_datetime(stock['date'])

stock = stock.sort_values('date')

stock.set_index('date', inplace=True)

stock = stock.asfreq('B')

stock['close'] = stock['close'].ffill()

ts = stock['close']

model = ARIMA(ts, order=(5,1,0))
model_fit = model.fit()

forecast = model_fit.forecast(steps=90)

forecast_output = pd.DataFrame({
    'Date': forecast.index,
    'Forecast_Price': forecast.values
})

forecast_output.to_csv(
    'forecast_results.csv',
    index=False
)

plt.figure(figsize=(12,6))
plt.plot(ts, label='Historical')
plt.plot(forecast.index, forecast.values, label='Forecast')
plt.title('AAPL Forecast using ARIMA')
plt.legend()
plt.show()

# ======================
# Save Analysis Dataset
# ======================

df.to_csv(
    "stock_analysis.csv",
    index=False
)

