import telebot 
import wikipedia as wkp
from telebot import types

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/wikipedia')

bot= telebot.TeleBot('1420721845:AAHDdZQ27e6Zx-2lT7MIUH8Ex9YUq0bKwQ8')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Хей, привет!',  reply_markup=keyboard1)

@bot.message_handler(commands=['wikipedia'])
def start_message(message):
    bot.send_message(message.chat.id, 'Write something:',  reply_markup=keyboard1)
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        txt = message.text
        wkp.set_lang("ru")
        try:
            bot.send_message(message.chat.id, wkp.summary(txt))
        except Exception as e:
            bot.send_message(message.chat.id,"oops! No such information on Wikipedia.")
    

bot.polling(none_stop=True)
