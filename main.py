import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from requests import post,get

bot = Client(
    "Echo_bot",
    api_id=2033318,
    api_hash='223cde1537f217dda4e16183f47af958',
    bot_token='1128799285:AAH634XjJOUgU1CfeMYK35uU0GJOkAypiL4'
)

@bot.on_message(filters.regex('start'))
def trply_to_hi(bot, message):
    bot.send_message(message.chat.id, f"welcom is id : {message.text}")
    
@bot.on_message(filters.regex('id'))
def trply_to_hi(bot, message):
    bot.send_message(message.chat.id, f"welcom is id : {message.chat.id}")

@bot.on_message(filters.regex('ss'))
def echo(bot, message):
    username = message.from_user.username
    message.reply(message)

@bot.on_callback_query()
def answer(bot, callback_query):
    callback_query.answer(
        f"Button contains: '{callback_query.data}'",
        show_alert=True)

bot.run()
