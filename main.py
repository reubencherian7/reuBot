#A telgram BOT

import os
import telebot
from datetime import date



API_KEY = os.environ['API']
bot = telebot.TeleBot(API_KEY)

today = date.today()
day = today.strftime("%d/%m/%Y")

@bot.message_handler(commands=['hello'])
def greet(message):
  name = message.from_user.first_name
  bot.reply_to(message, "Hey %s, Hows it going?" % name)

@bot.message_handler(commands=['greet'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['date'])
def date(message):
  bot.send_message(message.chat.id, "Today's date is %s" % day)  

bot.polling()
