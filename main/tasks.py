import json

from celery import shared_task
from dotenv import load_dotenv
from pathlib import Path
import requests
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


# celery -A config worker --loglevel=info


@shared_task
def send_telegram_notification(user_id, message, notify=True):

    token_bot = settings.TELEGRAM_BOT_TOKEN

    url_get_chat_id = f'https://api.telegram.org/bot{token_bot}/getUpdates'
    url_send_msg = f'https://api.telegram.org/bot{token_bot}/sendMessage'

    response_get_chat_id = requests.get(url_get_chat_id)

    data_get_chat_id = response_get_chat_id.json()
    if data_get_chat_id['ok']:
        for i in data_get_chat_id['result']:

            if i['message']['from']['username'] == user_id:
                chat_id = i['message']['chat']['id']
                response_send_msg = requests.post(url_send_msg, params={
                    'chat_id': chat_id,
                    'text': f"You should do: {message}! JUST DO IT!"
                })
                break
