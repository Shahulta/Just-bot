from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery

Bot=Client(
    "Pyrogram_bot",
    bot_token="6004112610:AAF8AMEnrDIlQDDUu68PFrjApLu9UzfYmCU",
    api_id="17296819",
    api_hash="baa838bcf579f71dbcd5ef2ab9ca8f2b"
)

START_MESSAGE = "Lets start the bot"
START_BUTTON = [
  [
    InlineKeyboardButton('start', callback_data="start")
  ]
]



@Bot.on_message(filters.command("start") & filters.private)
def start(Bot, Message):
  Message.reply(
        text=START_MESSAGE,
reply_markup=InlineKeyboardMarkup(START_BUTTON)
                  )

@Bot.on_callback_query()
def callback_query(Client, CallbackQuery):
  if CallbackQuery.data == "start":

    PAGE1_TEXT = "How are you ?"
    PAGE1_BUTTON = [[
InlineKeyboardButton("BACK TO MENU",callback_data="GO TO MENU")
]]
    
  CallbackQuery.edit_message_text(
      PAGE1_TEXT,
      reply_markup=InlineKeyboardMarkup(PAGE1_BUTTON))
    
    elif CallbackQuery.data == "GO TO MENU":
       CallbackQuery.edit_message_text(
       START_MESSAGE,  
       reply_markup=InlineKeyboardMarkup(START_BUTTON)
    )
  

print("Bot_Started")

Bot.run()
