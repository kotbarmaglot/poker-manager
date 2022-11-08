# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#   if message.text == "Привет":
#       bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
#   elif message.text == "/help":
#       bot.send_message(message.from_user.id, "Напиши Привет")
#   else:
#       bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# name = ''
# limit = 0

# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Напиши свое имя/ник?")
#         bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')

# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Какие лимиты играешь?')
#     bot.register_next_step_handler(message, get_limit)

# # def get_limit(message):
# #     global limit
# #     limit = message.text
    
# #     bot.send_message(message.from_user.id, ' Тебя зовут '+name+' и ты играешь '+limit+'?')



# def get_limit(message):
#     global limit
#     while limit == 0: #проверяем что возраст изменился
#         try:
#             limit = int(message.text) #проверяем, что возраст введен корректно
#         except Exception:
#             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

#         # keyboard = types.InlineKeyboardMarkup() #наша клавиатура
#         # key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»
#         # keyboard.add(key_yes); #добавляем кнопку в клавиатуру
#         # key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
#         # keyboard.add(key_no)
#         # question = 'Тебе '+str(limit)+' лимит, тебя зовут '+name+' ?'
#         # bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

#         # bot.send_message(message.from_user.id, ' Тебя зовут '+name+' и ты играешь '+limit+'?')


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,'Привет')


from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	