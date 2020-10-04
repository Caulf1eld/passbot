import telebot
import time
import data


bot = telebot.TeleBot(data.TOKEN)

@bot.message_handler(commands=['mob'])
def mob(message):
    mob = open('passwds/mobpass.txt')
    bot.send_message(message.chat.id, mob)





@bot.message_handler(commands=['sli'])
def sli(message):
    sli = open('passwds/slipass.txt')
    bot.send_message(message.chat.id, sli)


'''

@bot.message_handler(commands=['mob'])
def sli(message):
    sli = open(passwds/slipass.txt)
    bot.send_message(message.chat.id, mob)




@bot.message_handler(commands=['mob'])

'''


bot.polling(none_stop=True)