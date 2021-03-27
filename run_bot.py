import telebot

import Controller
import BlackBox

from configuration import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
black_box = BlackBox.BlackBox()

controller = Controller.Controller()



@bot.message_handler(commands=['start'])
def start_message(message):
    controller.add_user(message.from_user.id)
    answer = black_box.get_greeting_message()
    bot.send_message(message.from_user.id, answer)

@bot.message_handler(content_types=['text'])
def send_message(message):
    answer = black_box.make_transformation(message.text)
    bot.send_message(message.from_user.id, answer)


bot.polling()