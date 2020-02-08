from telegram.ext import Updater         # пакет называется python-telegram-bot, но Python-
from telegram.ext import CommandHandler  # модуль почему-то просто telegram ¯\_(ツ)_/¯

def start(bot, update):
    # подробнее об объекте update: https://core.telegram.org/bots/api#update
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")

TOKEN='1016794449:AAG7PN8Gjf47cTAhpKFR7Isb1fFSATfaaho'
REQUEST_KWARGS={
    'proxy_url': 'socks5://s5.priv.opennetwork.cc:1080',
    'urllib3_proxy_kwargs': {
        'username': 'v3_470788620',
        'password': 'BJBANUXu',
    }
}

updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)

start_handler = CommandHandler('start', start)  # этот обработчик реагирует
                                                # только на команду /start

updater.dispatcher.add_handler(start_handler)   # регистрируем в госреестре обработчиков
updater.start_polling()  # поехали!