from pyrogram import Client, filters
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Xin chào! Bot đã sẵn sàng hoạt động.")

app.run()
