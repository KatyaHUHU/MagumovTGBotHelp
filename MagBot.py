# Psychological Help Telegram Bot
# Made by Kirill 'iNe1t' Nekrasov

#Импортирование модулей
import telebot
from telebot import types
import templates

#Токен нашего бота
bot = telebot.TeleBot('6899663667:AAGqM48Z0e8FKw6PCBQVutOqMHrpkGLkD2c')

# Тело бота

# Функция приветствия и вывода кнопок
@bot.message_handler(commands = ['start'])
def hello(message):
    if message.text == 'Начать' or message.text == 'Назад' or message.text == '/start':
        # Создание пространства для кнопок
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # Создание самих кнопок
        btn_about = types.KeyboardButton("Обо мне")
        btn_signup = types.KeyboardButton("Запись на консультацию")
        btn_faq = types.KeyboardButton("Часто задаваемые вопросы")
        # Добавление кнопок в пространство
        markup.add(btn_about)
        markup.add(btn_signup)
        markup.add(btn_faq)
        # Отправка привестсвенного сообщения
        bot.send_message(message.from_user.id, "Я твою маму через раму", reply_markup=markup)

# Фукнция обработки прочего текста
@bot.message_handler(content_types = ['text'])
def get_message_text(message):
    # Возврат на главную
    if message.text == "Назад":
        hello(message)
    # Переход на раздел о психологе
    if message.text == "Обо мне":
        # Добавление кнопки
        btn_back = types.KeyboardButton("Назад")
        markup_about = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_about.add(btn_back)
        # Отправка сообщения
        bot.send_message(message.from_user.id, "Тут рассказ о твоей маме :)", reply_markup=markup_about)
    # Переход на раздел с записью на консультацию
    elif message.text == "Запись на консультацию":
        # Добавление кнопок
        btn_back = types.KeyboardButton("Назад")
        btn_link = types.InlineKeyboardButton('Запись', url='https://opora-ptz.ru/')
        # Объявление пространств для кнопок и добавление кнопок
        markup_about = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard = types.InlineKeyboardMarkup()
        markup_about.add(btn_back)
        keyboard.add(btn_link)
        # Отправка сообщений с кнопками
        bot.send_message(message.from_user.id, "Запись можно произвести по номеру: +7 921 220-34-64\nИли по сайту ниже: ", reply_markup=markup_about)
        bot.send_message(message.from_user.id, "Ссылка на сайт", reply_markup=keyboard)
    # Переход на раздел с часто задаваемыми вопросами
    elif message.text == "Часто задаваемые вопросы":
        # Создание кнопки, пространства для кнопки и добавление кнопки в пространство
        btn_back = types.KeyboardButton("Назад")
        markup_about = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_about.add(btn_back)
        # Отправка вопросов
        bot.send_message(message.from_user.id, templates.questions, reply_markup=markup_about, parse_mode='Markdown')

# Строка работы бота
bot.polling(none_stop=True, interval=0)
