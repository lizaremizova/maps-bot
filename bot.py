import telebot
from config import *
from logic import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hi! I am a bot, that shows cities on a map. Enter /help for available commands list.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Available commands: /help /show_city <city_name> /remember_city <city_name> /show_my_cities")


@bot.message_handler(commands=['show_city'])
def handle_show_city(message):
    city_name = message.text.split()[-1]
    # city drawing on a map
    user_id = message.chat.id
    manager.create_graph(f'{user_id}.png', [city_name])  # creating a map 
    with open(f'{user_id}.png', 'rb') as map:  # sendind the map
        bot.send_photo(user_id, map)


@bot.message_handler(commands=['remember_city'])
def handle_remember_city(message):
    user_id = message.chat.id
    city_name = message.text.split()[-1]
    if manager.add_city(user_id, city_name):
        bot.send_message(message.chat.id, f'City {city_name} was succesfully saved!')
    else:
        bot.send_message(message.chat.id, 'I don't know this city. Make sure it is written in english!')

@bot.message_handler(commands=['show_my_cities'])
def handle_show_visited_cities(message):
    cities = manager.select_cities(message.chat.id)
    # this function is in development

if __name__=="__main__":
    manager = DB_Map(DATABASE)
    bot.polling()
