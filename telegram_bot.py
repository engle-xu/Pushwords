# -*- coding:utf-8 -*-
import datetime
import time

import requests
import logging
from lib.config_tool import ConfigTool
from lib.models import Words

today = datetime.date.today()


class TelegramBot(object):
    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.config = ConfigTool()
        self.config.set_section('telegram_bot')
        self.group_chat_id = self.config.get('group_chat_id')
        self.token = self.config.get('token')

    def my_message(self):
        words = Words.get_unprocessed_words(limit=10)
        for word in words:
            word.updates_status()
        select_words = Words.get_select_words(limit=10)

        new_word = {}
        my_message = []
        i = 10
        for select_word in select_words:
            new_word[select_word['word']] = select_word['translation']
            message = "{}  {} : {} ".format(i, select_word['word'], select_word['translation'])
            my_message.append(message)
            i -= 1
        my_message.reverse()

        return ('Today is {}, Tofel Words are:\n\n'.format(today)) + '\n\n'.join(my_message)

    def telegram_bot_sendtext(self):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.group_chat_id + '&parse_mode=Markdown&text=' + self.my_message()
        response = requests.get(send_text)
        return response.json()


if __name__ == '__main__':
    TelegramBot().telegram_bot_sendtext()
