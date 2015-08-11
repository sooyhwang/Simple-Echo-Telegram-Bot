#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.abspath('.'), 'venv/Lib/site-packages'))

import telegram
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token='TOKEN')


@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://URL/HOOK')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'
