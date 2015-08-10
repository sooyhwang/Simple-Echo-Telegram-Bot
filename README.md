# Simple-Echo-Telegram-Bot
*A simple Python Telegram bot that echoes your input with Flask microframework, setWebhook method, and Google App Engine (optional)*

This example shows you how to set up webhook, and how to receive and send a text message using the [python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot) library.

Please exchange the TOKEN, the webhook URL, and the HOOK path with your own.

* The bot.py file is for general purpose.
* The bot_gae.py file with app.yaml is for Google App Engine. The only difference is the sys.path.append statement at the top. You may need to edit the virtual environment path to match yours.

Tested on Google App Engine (GAE) with virtualenv enabled. I followed the tutorial in [this Youtube video](https://www.youtube.com/watch?v=FRI3QGNWJYI) to set things up. Basically you set up virtualenv inside the GAE directory, and then append the path to it in every script that runs. (Otherwise you get an error in the import.)

## Required
* Python 2.7
* [python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot) module
* [Flask](http://flask.pocoo.org/) microframework

## How to use
* Install the script
* Visit https://URL/set_webhook on your web browser to set up webhook.
* Start chatting in Telegram and enjoy your echoes! :)
