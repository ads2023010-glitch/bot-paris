import os
import time
import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")  # token du bot
CHAT_ID = os.getenv("CHAT_ID")        # ton id Telegram

while True:
    message = "Salut ! C'est un message automatique 😊"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url)
    time.sleep(300)  # 5 minutes = 300 secondes
