import telebot
from telebot import types
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())


bot = telebot.TeleBot('5881555444:AAHP-cgyCfngHbanP8uECoHvg_gSuf8ZPSw')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    search_music = types.KeyboardButton('/search_music')
    markup.add(website, start, search_music)
    bot.send_message(message.chat.id, 'Выберите команду', reply_markup=markup)

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить website', url='http://10.117.10.72:8000'))
    bot.send_message(message.chat.id, 'Перейдите на наш сайт', reply_markup=markup)

@bot.message_handler(commands=['search_music'])
def search_mus(message):
    msg = bot.send_message(message.chat.id, 'Введите название песни, которое хотите прослушать на Spotify')
    bot.register_next_step_handler(msg, search)


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'я вас не понимаю, введите команду /help')

def search(message):
    bot.send_message(message.chat.id, 'Начинаю поиск')
    # video = 'https://www.youtube.com/results?search_query=' + message.text
    # driver.get(video)
    music = 'https://open.spotify.com/search/' + message.text
    driver.get(music)





bot.polling(none_stop=True)