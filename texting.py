import telebot as tb
from time import sleep,time
from random import randint
bot = tb.TeleBot('')
adlist = bot.get_chat_administrators(-1002005260221)
@bot.message_handler(content_types=['text'])
def getting_message(message):
    mes = message.text.lower()
    if mes == 'бот':
        bot.reply_to(message, '✅ Робот в полном порядке!')
    if mes == 'рулетка':
        gitler(message)
    if mes == 'мут':
        if message.reply_to_message:
            mute(message)
        else:
            bot.reply_to(message, 'Ответьте провинившемуся на сообщение!')
    if 'насколько' == mes.split()[0]:
        nask(message)

def gitler(message):
    ochko = bot.send_dice(message.chat.id).dice.value
    sleep(4)
    if ochko == 1:
        gotta = bot.reply_to(message, 'АХаххахаххаха тудаааааа ботяриус')
        bot.kick_chat_member(message.chat.id, message.from_user.id, until_date= int(gotta.date + 20))
    else:
        bot.reply_to(message, 'Живи, ладно уж 😈')

def lastcheck(message, timed, perm):
    isadmin = any(admin.user.id == message.from_user.id for admin in adlist)
    if not isadmin:
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date=timed, permissions=perm)
        mute_duration = int(message.text.split()[1])
        bot.reply_to(message, f'{message.reply_to_message.from_user.username} был замучен на {mute_duration} секунд')
    elif isadmin:
        bot.reply_to(message, 'Админов мутить нельзя')
    else:
        bot.reply_to(message, 'Ты слабак, поэтому ты никого мутить не можешь лошара')

def mute(message):
    perm = tb.types.ChatPermissions(can_send_messages=False)
    try:
        mute_duration = int(message.text.split()[1])
        timed = int(time()) + mute_duration
        lastcheck(message, timed, perm)
    except (IndexError, ValueError):
        bot.reply_to(message,'Напишите мне время в секундах, чтобы забанить человека')

def nask(message):
    bot.reply_to(message, f'Я уверен, что на {randint(0,100)}% !')
    
bot.infinity_polling()
