import json, requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from requests import post,get

bot = Client(
    "Echo_bot",
    api_id=2033318,
    api_hash='223cde1537f217dda4e16183f47af958',
    bot_token='1128799285:AAH634XjJOUgU1CfeMYK35uU0GJOkAypiL4'
)

@bot.on_message(filters.command('start'))
def trply_to_hi(bot, msg):
    bot.send_message(msg.chat.id, f"مرحبا بك في بوت تحميل")

@bot.on_message(filters.text)
def trply_to_hi(bot, msg):
    if msg.text:
        chat_id = msg.chat.id
        msgid = bot.send_message(chat_id, f"جاري التحميل...")
        api = requests.get(f"https://lovetik.com/api/ajax/search?k={msg.text}").json()
        bot.send_video(chat_id, api['links'][0]['a'], f"@alsh_3k - size {api['links'][0]['s']}")
        bot.delete_messages(chat_id, msgid.id)


bot.run()
