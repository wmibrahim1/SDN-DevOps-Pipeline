# notifications/webex_notify.py

import requests
import os

WEBEX_TOKEN = os.getenv("WEBEX_TOKEN")
WEBEX_ROOM_ID = os.getenv("WEBEX_ROOM_ID")

def send_message(text):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {WEBEX_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": WEBEX_ROOM_ID,
        "markdown": text
    }
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

if __name__ == "__main__":
    send_message("CI/CD pipeline finished ✅")
