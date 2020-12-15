import telebot
from telebot import types


bot = telebot.TeleBot('1397833889:AAE14aC774Am-BTYHMJ8NN2x_IXtTBiqdVs')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton("Молочная девочка")
    item2 = types.KeyboardButton("Красный бархат")
    item3 = types.KeyboardButton("Торт вупи пай")
    item4 = types.KeyboardButton("Чизкейк Нью Йорк")
    item5 = types.KeyboardButton("Чёрный лес торт")
    item6 = types.KeyboardButton("Торт орео")

 
    markup.add(item1, item2, item3, item4, item5, item6)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать рецепты тортов напишите название тортов, например: Яблочный, Бархатный, Медовый и так далее\n" 
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    if message.chat.type == 'private':
        if message.text == 'Молочная девочка':
            final_message = f"Молочная девочка\n\n1 банка сгущёнка\n3 яйцо\n220 гр мука\n10гр разрыхлитель\n\nКрем\n\n700 гр сливки 33%\n150 гр сахарная пудра"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Красный бархат':
            final_message = f"Красный бархат\n\n200 гр сахар\n3 яйцо\n280 кефир 2,5%\n1 ч.л сода\n190 подсолнечная масло\n15 разрыхлитель\nКраситель 1/2 ст ложки\n1 ч.л какао\n\nКрем\n\n600 гр тв. Сыр\n150 сахарная пудра\n500 мл сливки"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Торт вупи пай':
            final_message = f"Торт вупи пай\n\n4 яйцо\n160 сахар\n80 гр слив масло\n160 шоколад казахстан\n200 гр мука\n20 гр какао\n15 гр копсыткыш\n\nКрем\n\n500 гр маскарпоне\n700 гр тв сыр\n300 сахарная пудра\n300 сливки 33%"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Чизкейк Нью Йорк':
            final_message = f"Чизкейк Нью Йорк\n\n300 гр печенье\n100 гр слив масло\n\nНачинка\n\n600 гр творожный сыр\n150 гр сахарная пудра\n200 гр сметана 33%\n3 яйцо"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Черный лес торт':
            final_message = f"Чёрный лес торт\n\n200гр слив масло\n300гр Қазақстан шоколад\n200гр сахар\n200 гр мука\n20 гр разрыхлитель\n\nВишневый желе\n\n300 замороженные фрукты\n75 сахар\nКрахмал 15гр\n\nКрем\n\n500гр сливки\n500гр маскарпоне\n250 гр сахарная пудра"
            bot.send_message(message.chat.id, final_message)
        elif message.text == 'Торт орео':
            final_message = f"Торт орео\n\n6 яйцо\n200 гр сахар\n200 гр молоко\n100 гр подсолнечная масло\n60 гр какао\n10 гр разрыхлитель\n\nКрем\n\n500гр сливки\n300 гр тв сыр\n120 сахарная пудра\nПеченье орео 10-12 шт\n\nГанаш\n\n100гр шоколад\n80 гр сливки"
            bot.send_message(message.chat.id, final_message)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить...')


# Это нужно чтобы бот работал
bot.polling(none_stop=True)