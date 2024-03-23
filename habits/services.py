import os

import requests
from django.conf import settings


class TGBot:
    BASE_URL = 'https://api.telegram.org/bot'
    TOKEN = os.getenv('BOT_KEY')
    MY_CHAT_ID = os.getenv('TELEGRAM_ID')

    def send_message(self, chat_id=None, text=''):
        chat_id = chat_id or self.MY_CHAT_ID
        requests.post(
            url=f'{self.BASE_URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )


