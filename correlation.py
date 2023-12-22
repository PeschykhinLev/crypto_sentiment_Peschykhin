import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load sentiment data
sentiment_df = pd.read_csv('telegram_news_sentiment_2.csv')
sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date'])

# Load BTC price data
btc_df = pd.read_csv('BTC-USD.csv')
btc_df['Date'] = pd.to_datetime(btc_df['Date'])

# Filter data from 2023-11-21 onwards
start_date = pd.to_datetime('2023-09-22')
sentiment_df = sentiment_df[sentiment_df['Date'] >= start_date]
btc_df = btc_df[btc_df['Date'] >= start_date]

# Calculate average compound score
avg_compound = sentiment_df.groupby('Date')['Compound'].mean()

# Create plot with two y-axes
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot sentiment score
ax1.plot(avg_compound.index, avg_compound.values, marker='o', color='blue', label='Average Compound Score')
ax1.set_xlabel('Date')
ax1.set_ylabel('Average Compound Score', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax1.xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=90)
plt.grid(True)

# Create another y-axis for BTC price
ax2 = ax1.twinx()
ax2.plot(btc_df['Date'], btc_df['Close'], marker='x', color='green', label='BTC Close Price')
ax2.set_ylabel('BTC Close Price (USD)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Title and layout adjustments
plt.title('Average Compound Score and BTC Close Price')
fig.tight_layout()
plt.show()
