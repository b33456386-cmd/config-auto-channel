import requests
import os

bot_token = os.getenv("BOT_TOKEN")
target_channel = os.getenv("TARGET_CHANNEL")

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": target_channel,
        "text": "✅ TEST MESSAGE"
    }
)

print(response.text)
