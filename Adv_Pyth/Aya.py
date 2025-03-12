import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA'] 

stock_dt = yf.download(tickers, start="2023-09-01", end="2024-09-01", group_by='ticker') 
stock_prices = []
for ticker in tickers: 
    closing_prices = stock_dt[ticker]['Close'].values[:200]   
    stock_prices.append(closing_prices) 
stock_prices_numpyy = np.array(stock_prices) 
print(stock_prices_numpyy.shape)


# Date
stock_dt.index = pd.to_datetime(stock_dt.index)

# Monthly averages, max and mins
def calculate_monthly_stats():
    monthly_stats = {}
    for ticker in tickers:
        # Group data in month and calc mean max min
        monthly_data = stock_dt[ticker]['Close'].resample('M').agg(['mean', 'max', 'min'])
        monthly_stats[ticker] = monthly_data
    return monthly_stats


#Task3 daily price change
def calculate_the_daily_share_price_change():
    daily_returns={}
    for ticker in tickers:
        daily_returns[ticker]=stock_dt[ticker]['Close'].pct_change().dropna()
    return daily_returns

daily_returns=calculate_the_daily_share_price_change()


#Task3 highest share price change
def highest_single_day_changes():
    highest_increase={}
    highest_decrease={}

    for ticker in tickers:
        highest_decrease[ticker]=daily_returns[ticker].idxmin(), daily_returns[ticker].min()
        highest_increase[ticker]=daily_returns[ticker].idxmax(), daily_returns[ticker].max()

    return highest_decrease, highest_increase

highest_decrease,highest_increase=highest_single_day_changes()
print("The highest single day price increases: ")

for ticker, (date, change) in highest_increase.items():
    print(f"{ticker} {date} with increase of {change:.2%}")

print("\nHighest single day decrease ")

for ticker,(date, change) in highest_decrease.items():
    print(f"{ticker}:{date} with decrease of {change:.2%}")
 
volatility = {ticker: np.std(daily_returns[ticker]) for ticker in daily_returns.keys()}
most_volatile_element_ticker=max(volatility,key=volatility.get)

print(f"\nMost Volatile stock: {most_volatile_element_ticker} with volatility {volatility[most_volatile_element_ticker]:.4f}")

#Task 4
def cluster_stocks(number_clusters=3):
    the_returned_matrix=np.array([daily_returns[ticker] for ticker in tickers]) 
    kmeans_algorithm=KMeans(n_clusters=number_clusters, random_state=42)
    kmeans_algorithm.fit(the_returned_matrix)
    return kmeans_algorithm.labels_

the_stock_clusters=cluster_stocks(number_clusters=3)

print("Stock Clusters")

for ticker,cluster in zip(tickers, the_stock_clusters):
    print(f"{ticker} is within the cluster {cluster}")

monthly_stats = calculate_monthly_stats()
for ticker, stats in monthly_stats.items():
    print(f"{ticker} Monthly Stats:\n", stats)

# Find how many days Tesla stock was above $500
def days_above_500(ticker, threshold=500):
    above_threshold = stock_dt[ticker]['Close'][stock_dt[ticker]['Close'] > threshold].count()
    return above_threshold

tesla_above_500 = days_above_500('TSLA', 500)
print(f"The tesla share price was above $500 on {tesla_above_500} days.")

def find_top_5_days(ticker):
    top5days = stock_dt[ticker]['Close'].nlargest(5)
    return top5days

for ticker in tickers:
    top_5 = find_top_5_days(ticker)
    print(f"Top 5 days for {ticker}:\n", top_5)



def high_and_low():
    highest_price = stock_dt.xs('Close', level=1, axis=1).idxmax(axis=1)
    lowest_price = stock_dt.xs('Close', level=1, axis=1).idxmin(axis=1)
    return highest_price, lowest_price

highest_price, lowest_price = high_and_low()
print(f"Company with highest prices on each day:\n{highest_price}")
print(f"Company with lowest prices on each day:\n{lowest_price}")

#Task 4
company_idx = 2
google_prices = stock_prices_numpyy[company_idx, :]


#Task 5 finding the mean and std and generate 200 values
the_mean = np.mean(google_prices)
standard_deviation = np.std(google_prices)
new_stock_prices = np.random.normal(the_mean, standard_deviation, 200)
new_stock_prices= new_stock_prices.reshape(1,-1)
updated_stock_share_price = np.concatenate((stock_prices_numpyy, new_stock_prices))
print("Updated stock share price shape: ",updated_stock_share_price.shape)


#Task 6  META
company_idx = 4
meta_share_price = stock_prices_numpyy[company_idx, :]

meta_share_price_changes = np.diff(meta_share_price)/meta_share_price[:-1]

## mean 
mean_percent_diff = np.mean(meta_share_price_changes)
standard_percent_change = np.std(meta_share_price_changes)

#daily percentage
number_of_days=30
forecast_percent_difference= np.random.normal(mean_percent_diff, standard_percent_change, number_of_days)


forecasted_prices = [meta_share_price[-1]]

for standard_percent_change in forecast_percent_difference:
    upcoming_price= forecasted_prices[-1]*(1+standard_percent_change)
    forecasted_prices.append(upcoming_price)

forecasted_prices = np.array(forecasted_prices[1:])

print("The predicted price of Meta is for the next 30 days: ")
print(forecasted_prices)

predicted_days_in_time = pd.date_range(start=stock_dt.index[-1],periods=number_of_days, freq='D')
predicted_data_frame = pd.DataFrame({'Date': predicted_days_in_time, 'Predicted Share Price': forecasted_prices})


print(predicted_data_frame)


#saved file
np.savetxt("file.txt",stock_prices_numpyy)