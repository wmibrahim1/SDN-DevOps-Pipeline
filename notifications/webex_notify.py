# notifications/webex_notify.py

import requests
import os

WEBEX_TOKEN = os.getenv("MmFmYjI5ODItZTg0NS00YjQ2LTliMTMtZTM0MjVhMTYxMzJlYzE4MDk1NDUtMTM2_P0A1_13494cac-24b4-4f89-8247-193cc92a7636")
WEBEX_ROOM_ID = os.getenv("aHR0cHM6Ly9jb252LXIud2J4Mi5jb20vY29udmVyc2F0aW9uL2FwaS92MS9jb252ZXJzYXRpb25zLzhjMjc5NzMwLWM5YWYtMTFmMC04NzYzLThiZDY2MDdhZGVlMg")

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
