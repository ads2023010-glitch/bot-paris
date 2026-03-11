import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")  # récupère ton token depuis Railway
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # ton chat ID

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Test Telegram !")
