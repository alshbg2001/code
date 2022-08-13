import json, requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from requests import post,get

bot = Client(
    "Echo_bot",
    api_id=2033318,
    api_hash='223cde1537f217dda4e16183f47af958',
    #bot_token='5067621147:AAEeKEBjWuNMl82UJYOd_LgQE2WIcwTdttg'
)

@bot.on_message(filters.command('start'))
def trply_to_hi(bot, msg):
    bot.send_message(msg.chat.id, f"مرحبا بك في بوت تحميل")

@bot.on_message(filters.text)
def trply_to_hi(bot, msg):
    if msg.text:
        chat_id = msg.chat.id
        bot.send_message(chat_id, f"done...")
        api = requests.get(f"https://alsh-ax.ml/api/v3/dl/media.php?url={msg.text}").json()
    
        bot.send_video(chat_id, api['data']['links'][0]['url'])


bot.run()
