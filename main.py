import logging
import sys
import os
import time

import telebot
from telebot import types

API_TOKEN = os.getenv('API_KEY')

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)

def mock(st):
    str=''
    for index, l in enumerate(st):
        if index % 2 == 0:
            str+=l.upper()
        else:
            str+=l.lower()
    return str

@bot.inline_handler(func=lambda chosen_inline_result: True)
def default_query(chosen_inline_result):
    try:
        r = types.InlineQueryResultArticle('1', 'mOcK',  types.InputTextMessageContent(mock(str(chosen_inline_result.query))))
        bot.answer_inline_query(chosen_inline_result.id, [r])
    except Exception as e:
        print(e)


def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)