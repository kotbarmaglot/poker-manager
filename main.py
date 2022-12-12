from xmlrpc.client import boolean
import telebot, sqlite3, json, os.path

from telebot import types

from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from datetime import datetime

from telebot.storage import StateMemoryStorage
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup #States

token='1718561535:AAFRknVjmaORLS3Q1ykaiOflYhEoRDzk7K8'

todo = str
completed = boolean
login = str
start = str
end = str
br = int
status = ['yes', 'no']
id = str
dlina = str
start_date = str
start_time = str
end_time = str
br_ipoker = str
br_pokerking = str
start_day = str

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(token, state_storage=state_storage)

class MyStates(StatesGroup):
    # Just name variables differently
    start = State() # creating instances of State class is enough from now
    start_katka = State()
    katka = State()
    start_theory = State()
    end_katka = State()


@bot.message_handler(commands=['start'])
def button(message):

    msg = bot.send_message(message.from_user.id, "Во сколько ты сегодня проснулся?", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, yoga)


def yoga(message):
    msg = bot.send_message(message.from_user.id, "Во сколько вчера заснул?")
    bot.register_next_step_handler(msg, start_day)
    
def start_day(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать сессию")
    markup.add(item1)
    item2=types.KeyboardButton("Начать теорию")
    markup.add(item2)
    bot.send_message(message.chat.id,'Отлично! Начнем катать или заниматься теорией?\n sadf',reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.start, message.chat.id)

@bot.message_handler(state=MyStates.start)
def button(message):

    if message.text == "Начать сессию":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Закончить сессию")
        markup.add(item1)

        date = datetime.now()
        str_date = date.strftime("%m/%d/%Y, %H:%M:%S")
        bot.set_state(message.from_user.id, MyStates.start_katka, message.chat.id)
        bot.send_message(message.chat.id,'Катка начата в: '+str_date,reply_markup=markup)

        id = date.strftime("%m/%d/%Y")
        katkastart = date.strftime("%H:%M:%S")

        con = sqlite3.connect("PokerManager.db")
        cur = con.cursor()

        globals()['start_date'] = str_date

        
    else:
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Закончить теорию")
        markup.add(item1)

        date = datetime.now()
        str_date = date.strftime("%m/%d/%Y, %H:%M:%S")
        bot.set_state(message.from_user.id, MyStates.start_theory, message.chat.id)
        bot.send_message(message.chat.id,'Теория начата в: '+str_date,reply_markup=markup)



@bot.message_handler(state=MyStates.start_theory)
def button(message):
    inp = message.text
    if inp not in ["Закончить теорию"]:
        bot.send_message(message.chat.id, 'Вы все еще занимаетесь теорией, если хотите закончить теорию, нажмите "Закончить теорию"')
        return

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать сессию")
    markup.add(item1)
    item2=types.KeyboardButton("Начать теорию")
    markup.add(item2)

    date = datetime.now()
    str_date = date.strftime("%m/%d/%Y, %H:%M:%S")

    bot.send_message(message.chat.id,'Вы закончили заниматься теорией в: '+str_date,reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.start, message.chat.id)


@bot.message_handler(state=MyStates.start_katka)
def button(message):
    inp = message.text
    if inp not in ["Закончить сессию"]:
        bot.send_message(message.chat.id, 'Вы все еще катаетет, если хотите закончить сессию, нажмите "Закончить сессию"')
        return

    bot.send_message(message.from_user.id, "Введи бр Ipoker в поле сообщения и нажми enter:", reply_markup=types.ReplyKeyboardRemove())


    print(start_date)

    date = datetime.now()
    str_date = date.strftime("%m/%d/%Y, %H:%M:%S")

    bot.set_state(message.from_user.id, MyStates.end_katka, message.chat.id)

@bot.message_handler(state=MyStates.end_katka)
def send_welcome(message):
    globals()['br_ipoker'] = message.text
    msg = bot.send_message(message.from_user.id, "Введи бр king в поле сообщения и нажми enter:")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    print(br_ipoker)
    globals()['br_pokerking'] = message.text
    print(br_pokerking)

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать сессию")
    markup.add(item1)
    item2=types.KeyboardButton("Начать теорию")
    markup.add(item2)

    bot.send_message(message.chat.id,'Вы закончили катать в: '+br_pokerking+br_ipoker,reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.start, message.chat.id)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.polling(none_stop=True, interval=0)