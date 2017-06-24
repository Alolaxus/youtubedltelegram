from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InputTextMessageContent)
import os
from uuid import uuid4
import logging
import youtube_dl

TOKEN = os.environ.get('TOKEN')

def start(bot, update):
    update.message.reply_text('Ciao! Con questo bot puoi scaricare video da youtube! Basta copiare l\'indirizzo del video'
                              'e copiarlo qui. Dopo aver incollato e premuto invio il bot ti manderà il video da scaricare.')


def replyvideo(bot, update):

    ydl_opts = {
        'format': 'bestaudio/best'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([update.message.text])
    update.message.reply_text(ydl.urlopen())


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, replyvideo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()