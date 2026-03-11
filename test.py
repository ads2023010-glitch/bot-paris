from telegram import Bot

TOKEN = "8301048438:AAEUyBVAC3rCYACcfkUYY4GBhpp7kOSVHBs"
CHAT_ID = 6898691256  # ton vrai chat ID

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="Salut ! Test Telegram reçu ?")
