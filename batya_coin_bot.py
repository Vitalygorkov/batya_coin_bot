import telebot
from config import api_key
import time


bot = telebot.TeleBot(api_key)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('баланс', 'банк')
print('start')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'Go':
        bot.send_message(message.from_user.id, 'начинаем эффективную работу', reply_markup=keyboard1)
        print('Баланс')
    elif message.text.lower().split()[0].isdigit() == True:
        bot.send_message(message.from_user.id, 'задание '+ message.text, reply_markup=keyboard1)
        print('задание')

    else:
        print(message.text)
        bot.send_message(message.from_user.id, 'Минуты пробел задача', reply_markup=keyboard1)

bot.polling(none_stop=True, interval=0)
