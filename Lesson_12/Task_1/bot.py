from telebot import TeleBot
from models import Telegram_user
from constants import TOKEN, QUESTIONS, USER_ATTRIBUTES

bot = TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_user_info(message):
    global new_user
    if message.text == '/start':
        bot.send_message(
            message.chat.id,
            QUESTIONS[0]
        )
        new_user = Telegram_user()
        new_user.save()
    else:
        if new_user.state != 6:
            new_user[USER_ATTRIBUTES[new_user.state]] = message.text
            new_user.state += 1
            new_user.save()
            bot.send_message(
                message.chat.id,
                QUESTIONS[new_user.state]
            )
        else:
            new_user.wish = message.text.split(',')
            new_user.save()


if __name__ == '__main__':
    bot.polling()
