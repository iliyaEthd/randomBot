import os

import telebot
import random

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, '''give a number range seprated by space for example 
6 11
I generate random for you''')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    try:
        messageText = message.text
        min , max = list(map(int,messageText.split(' ')))
        randomNumber = random.randint(min,max)
        bot.reply_to(message, randomNumber)
    except:
        bot.reply_to(message, message.text + '   format not supported   minNumber maxNumber')
    
bot.infinity_polling()