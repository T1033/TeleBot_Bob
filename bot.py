from config import TOKEN
import time
import telebot
from telebot import types
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item = types.KeyboardButton("Привет!")
	markup.add(item)
	bot.send_message(message.chat.id, "Здраствуй, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def step(message):
	if message.chat.type == 'private':
		if message.text == 'Привет!':
			time.sleep(int(1))
			bot.send_message(message.chat.id, ':)\nhttps://youtu.be/fHjZQb-kGek')
		elif message.text == 'что-то, что-то':
			time.sleep(int(1))
			bot.send_message(message.chat.id, 'что-то')
			sti = open('D:/python/TEST/TeleBot_Bob/reply_1.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)
		elif message.text == 'еще что-то':
			time.sleep(int(1))
			sti = open('D:/python/TEST/TeleBot_Bob/reply_2.webp', 'rb')
			bot.send_sticker(message.chat.id, sti)

		else:
			time.sleep(int(1))
			bot.send_message(message.chat.id, 'повтори')

bot.polling(none_stop=True)