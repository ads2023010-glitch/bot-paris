import os
import time
from telegram import Bot

TOKEN = os.getenv(8301048438:AAEUyBVAC3rCYACcfkUYY4GBhpp7kOSVHBs)  # Sécurise le token en variable d'environnement
CHAT_ID = os.getenv(6898691256)  # Ton chat ID
bot = Bot(token=TOKEN)

while True:
    bot.send_message(chat_id=CHAT_ID, text="Salut ! Ceci est un message toutes les 5 minutes.")
    time.sleep(300)  # 300 secondes = 5 minutes
