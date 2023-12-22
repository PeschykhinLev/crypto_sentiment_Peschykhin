import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

csv_file_name = 'telegram_news_sentiment_2.csv'
df = pd.read_csv(csv_file_name)

df['Date'] = pd.to_datetime(df['Date'])

avg_compound = df.groupby('Date')['Compound'].mean()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(avg_compound.index, avg_compound.values, marker='o', color='blue')

# Formatting the dates on x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=90)

plt.title('Average Compound Score per Day')
plt.xlabel('Date')
plt.ylabel('Average Compound Score')
plt.grid(True)
plt.tight_layout()  # Adjust layout to fit the date labels
plt.show()