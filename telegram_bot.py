# -*- coding:utf-8 -*-
import datetime
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
        words = Words.get_unprocessed_words(10)
        new_word = {}
        my_message = []
        i = 0
        for word in words:
            i += 1
            new_word[word['word']] = word['translation']
            message = "{}  {}  {} : {} ".format(today, i, word['word'], word['translation'])
            my_message.append(message)

        return '\n\n'.join(my_message)

    def telegram_bot_sendtext(self):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.group_chat_id + '&parse_mode=Markdown&text=' + self.my_message()
        response = requests.get(send_text)
        return response.json()


if __name__ == '__main__':
    # TelegramBot().telegram_bot_sendtext()
    # time.sleep(1)
    t = TelegramBot()
    print(t.my_message())
