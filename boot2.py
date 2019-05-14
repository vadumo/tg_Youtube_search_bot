import urllib
from urllib import request
from urllib.parse import quote
import re
import telebot

Token = '869525203:AAGe6c7GLHcDulwD48mzhAGERH_6QME80B8'

bot = telebot.TeleBot(Token)


@bot.message_handler(content_types=['text'])
def handle_start(message):
    x = message.text
    sq = 'http://www.youtube.com/results?search_query=' + quote(x)
    doc = urllib.request.urlopen(sq).read().decode('cp1251', errors='ignore')
    match = re.findall("\?v\=(.+?)\"", doc)
    a = match[1]
    a = 'https://www.youtube.com/watch?v=' + a
    bot.send_message(message.from_user.id, a)


bot.polling(none_stop=True)
