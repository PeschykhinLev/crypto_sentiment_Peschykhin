from pyrogram import Client
from datetime import datetime, timedelta
import os
import re
from dotenv import load_dotenv

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import pandas as pd

load_dotenv()

# Configuration
CONFIG = {
    "telegram_api_id": int(os.getenv("TG_API_ID")),
    "telegram_hash": os.getenv("TG_API_HASH"),
}

app = Client("my_account", CONFIG["telegram_api_id"], CONFIG["telegram_hash"])

chat_id = "markettwits"
hashtag = "#крипто"

one_month_ago = datetime.now() - timedelta(days=90)

data = []

async def main():
    async with app:
        #count = 0
        async for message in app.get_chat_history(chat_id):
            # Check if the message is within the last month
            if message.date > one_month_ago:
                if hashtag in str(message.text):
                    cleaned_message = re.sub(r'^.*?\n', '',  message.text).strip()
                    translated = GoogleTranslator(source='auto', target='english').translate(cleaned_message)
                    sentiment = SentimentIntensityAnalyzer().polarity_scores(translated)
                    data.append({
                        'Date': message.date.date(),
                        'News': translated,
                        'Neg': sentiment['neg'],
                        'Neu': sentiment['neu'],
                        'Pos': sentiment['pos'],
                        'Compound': sentiment['compound']
                    })
            else:
                break

app.run(main())

df = pd.DataFrame(data)
csv_file_name = 'telegram_news_sentiment_2.csv'
df.to_csv(csv_file_name, index=False)

print("Saved")