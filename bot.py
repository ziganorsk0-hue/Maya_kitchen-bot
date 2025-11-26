import telebot

bot = telebot.TeleBot("8023374417:AAHqDHcwM5hzWBzeyJN0Rfe1TUaSc4IseEg")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для кухни 😊")

bot.polling()
