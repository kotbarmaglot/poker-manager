from xmlrpc.client import boolean
import telebot, sqlite3, json, os.path

from telebot import types

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








jsonBD = {
    "katka": [
        {
            "id": id,
            "session": [
                {
                    "Start": start,
                    "End": end,
                    "Dlina": dlina
                }
            ]
        }
    ],
    "theory": [
        {
            "id": id,
            "session": [
                {
                    "Start": start,
                    "End": end,
                    "Dlina": dlina
                }
            ]
        }
    ]
}


state_storage = StateMemoryStorage()

bot = telebot.TeleBot(token, state_storage=state_storage)

class MyStates(StatesGroup):
    # Just name variables differently
    start = State() # creating instances of State class is enough from now
    start_katka = State()
    katka = State()
    start_theory = State()


@bot.message_handler(commands=['start'])
def button(message):

    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать сессию")
    markup.add(item1)
    item2=types.KeyboardButton("Начать теорию")
    markup.add(item2)

    date = datetime.now()
    str_date = date.strftime("%m/%d/%Y, %H:%M:%S")
    bot.set_state(message.from_user.id, MyStates.start, message.chat.id)
    bot.send_message(message.chat.id,'Сейчас: '+str_date,reply_markup=markup)



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
        if os.path.exists('data.txt'):
            print('файл найден жсон')
            with open('data.txt') as json_file:
                data = json.load(json_file)

            length = len(data['day'])

            print (length)
            for x in range(length):
                
                if data['day'][x]['id'] == id:
                    data['day'][x]['katka'].append([{
                        "Start": katkastart,
                        "End": '1',
                        "Dlina": '1'
                    }])
                else:

                    data['day'].append({
                        'id': id,
                        'katka': [{
                                "Start": '1',
                                "End": '1',
                                "Dlina": '1'
                        }],
                        'theory': [{
                                "Start": 'start',
                                "End": 'end',
                                "Dlina": 'dlina'
                        }]
                    })


        else:
            data = {}
            data['day'] = []

            data['day'].append({
                'id': id,
                'katka': [{
                        "Start": '1',
                        "End": '1',
                        "Dlina": '1'
                }],
                'theory': [{
                        "Start": 'start',
                        "End": 'end',
                        "Dlina": 'dlina'
                }]
            })
            print('файла жсон нет, создам новый')


        

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

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
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Начать сессию")
    markup.add(item1)
    item2=types.KeyboardButton("Начать теорию")
    markup.add(item2)

    date = datetime.now()
    str_date = date.strftime("%m/%d/%Y, %H:%M:%S")

    bot.send_message(message.chat.id,'Вы закончили катать в: '+str_date,reply_markup=markup)
    bot.set_state(message.from_user.id, MyStates.start, message.chat.id)



# @bot.message_handler(content_types='text')
# def message_reply(message):

#     # conn = sqlite3.connect('poker-manager/db/stat.db')
#     # cur = conn.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS sessions(
#     #     date_session BLOB PRIMARY KEY,
#     #     start_time BLOB,
#     #     end_time BLOB,
#     #     length INTEGER);
#     # """)
#     # conn.commit()


#     if message.text=="Начать сессию":

#         date = datetime.now()

#         start = date.strftime("%H:%M:%S/%m-%d-%Y")

#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item_1 = types.KeyboardButton('Закончить сессию')
#         item_2 = types.KeyboardButton('Back🔙')
#         markup.add(item_1, item_2)

#         bot.send_message(message.chat.id, 'Вы начали сессию:' + start, reply_markup = markup)
    
#         # date_session = date.strftime("%m-%d-%Y")

#         # session = (date_session, start_time)



#         # print (start)
#         # cur.execute("""INSERT INTO users(date_session, start_time) ;""", session)
#         # conn.commit()


#         # bot.send_message(message.chat.id,"Сессия запущена в " + start )

#     elif message.text=="Начать теорию":
#         # print (start)


#         date = datetime.now()

#         end = date.strftime("%H:%M:%S/%m-%d-%Y")

#         date = datetime.now()

#         start = date.strftime("%H:%M:%S/%m-%d-%Y")

#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         item_1 = types.KeyboardButton('Закончить теорию')
#         item_2 = types.KeyboardButton('Back🔙')
#         markup.add(item_1, item_2)

#         bot.send_message(message.chat.id, 'Вы начали теорию:' + start, reply_markup = markup)
    
#         print (end)

#         # length = 




#         # bot.send_message(message.chat.id,"Сессия окончена в " + end )

        
#     else:
#         bot.send_message(message.chat.id,"Я не понимаю команду. Напишите /start чтобы запустить бота")


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.polling(none_stop=True, interval=0)