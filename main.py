
# -*- coding: utf-8 -*-

import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InputTextMessageContent)
import os
from uuid import uuid4
import logging
from __future__ import unicode_literals
import youtube_dl

TOKEN = os.environ.get('TOKEN')

def start(bot, update):
    update.message.reply_text('Ciao! Con questo bot puoi scaricare video da youtube! Basta copiare l\'indirizzo del video'
                              'e copiarlo qui. Dopo aver incollato e premuto invio il bot ti manderà il video da scaricare.')

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()