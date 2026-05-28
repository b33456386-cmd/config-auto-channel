from telethon import TelegramClient
import re
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
target_channel = os.getenv("TARGET_CHANNEL")

client = TelegramClient('session', api_id, api_hash)

source_channels = [
    'freewireguard',
]

vmess_pattern = r'vmess://[^\s]+'
vless_pattern = r'vless://[^\s]+'

async def main():

    await client.start()

    for channel in source_channels:

        async for message in client.iter_messages(channel, limit=20):

            if not message.text:
                continue

            configs = []

            configs += re.findall(vmess_pattern, message.text)
            configs += re.findall(vless_pattern, message.text)

            for config in configs:

                text = f"🔥 New Config\n\n{config}"

                await client.send_message(target_channel, text)

                print("Sent")

with client:
    client.loop.run_until_complete(main())
