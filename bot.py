import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = 'BOT_TOKEN'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    message_text = 'Main Menu'
    keyboard = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton('Button 1', callback_data='button1')
    button2 = InlineKeyboardButton('Button 2', callback_data='button2')
    button3 = InlineKeyboardButton('Button 3', callback_data='button3')
    button4 = InlineKeyboardButton('Button 4', callback_data='button4')
    button5 = InlineKeyboardButton('Button 5', callback_data='button5')
    keyboard.add(button1, button2, button3, button4, button5)
    bot.send_message(chat_id=message.chat.id, text=message_text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def button(call):
    if call.data == 'button1':
        message = "You pressed button 1."
    elif call.data == 'button2':
        message = "You pressed button 2."
    elif call.data == 'button3':
        message = "You pressed button 3."
    elif call.data == 'button4':
        message = "You pressed button 4."
    elif call.data == 'button5':
        message = "You pressed button 5."
    bot.send_message(chat_id=call.message.chat.id, text=message)
    
bot.polling()
