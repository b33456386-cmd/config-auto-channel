import requests
import os

bot_token = os.getenv("BOT_TOKEN")
target_channel = os.getenv("TARGET_CHANNEL")

message = "🔥 Bot Connected Successfully"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

data = {
    "chat_id": target_channel,
    "text": message
}

requests.post(url, data=data)

print("Message Sent")
