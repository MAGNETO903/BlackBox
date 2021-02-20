import telebot

import Controller
import BlackBox

from configuration import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
black_box = BlackBox.BlackBox()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, "Здравствуйте!")

@bot.message_handler(content_types=['text'])
def send_message(message):
    answer = black_box.make_transformation(message)
    bot.send_message(message.from_user.id, answer)