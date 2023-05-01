from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random

Bot=Client(
    "Pyrogram_bot",
    bot_token="6004112610:AAF8AMEnrDIlQDDUu68PFrjApLu9UzfYmCU",
    api_id="17296819",
    api_hash="baa838bcf579f71dbcd5ef2ab9ca8f2b"
)


ALL_PHOTOS = [
 "https://telegra.ph/file/99f483c7fb9d813a37c0b.jpg",
 "https://telegra.ph/file/7cbf1ce73f70740bd0af6.jpg",
 "https://telegra.ph/file/5febb89f64baf2c08cc6d.jpg"
]


@Bot.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PHOTOS),
        caption="hi bro sugam aano?",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Group", url="https://t.me/New_Mallu_Movies_2"),
            InlineKeyboardButton("Channel", url="https://t.me/+GV8HnJAzx_hhNmE1")
            ],[
            InlineKeyboardButton("Help", url="@shanibsanu_bot"),
            InlineKeyboardButton("Owner", url="@Shanib_c_k")
            ]]
            )
        )


@Bot.on_message(filters.command("help"))
async def help(bot: Bot, message: Message):
    await message.reply_text("help✅")


print("Bot_Started")

Bot.run()
