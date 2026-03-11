import requests
import time

TOKEN = "8301048438:AAEUyBVAC3rCYACcfkUYY4GBhpp7kOSVHBs"
CHAT_ID = "6898691256"

while True:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": "Bot actif"
    }

    requests.post(url, data=data)

    time.sleep(3600)  # 60 minutes
