from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


Bot=Client(
    "Pyrogram_bot"
    bot_token="6004112610:AAF8AMEnrDIlQDDUu68PFrjApLu9UzfYmCU",
    api_id="17296819",
    api_hash="baa838bcf579f71dbcd5ef2ab9ca8f2b"
)


@Bot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="hi bro sugam aano?",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Button", url="https://t.me/New_Mallu_Movies_2")
            ]]
            )
        )


@Bot.on_message(filters.command("help"))
async def help(bot: Bot, message: Message):
    await message.reply_text("help✅")

Bot.run()
