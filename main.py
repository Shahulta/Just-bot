from pyrogram import Client, filters
from pyrogram.types import Message


Bot=Client(
    "Pyrogram_bot"
    bot_token="6004112610:AAF8AMEnrDIlQDDUu68PFrjApLu9UzfYmCU",
    api_id="17296819",
    api_hash="baa838bcf579f71dbcd5ef2ab9ca8f2b"
)


@Bot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("hi bro sugam aano?")
@Bot.on_message(filters.command("help"))
async def help(bot: Bot, message: Message):
    await message.reply_text("help✅")

Bot.run()
