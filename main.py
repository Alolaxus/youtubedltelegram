from __future__ import unicode_literals
# -*- coding: utf-8 -*-

import requests

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, InputTextMessageContent)
import os
from uuid import uuid4
import logging
import youtube_dl
import pafy

TOKEN = os.environ.get('TOKEN')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    update.message.reply_text('Ciao! Con questo bot puoi scaricare video da youtube! Basta copiare l\'indirizzo del video'
                              'e copiarlo qui. Dopo aver incollato e premuto invio il bot ti manderà il video da scaricare.')


def replyvideo(bot, update):
    chat_id = update.message.chat_id
    video = pafy.new(update.message.text)
    best = video.getbest()
    ''''http://tinyurl.com/api-create.php?url=' + '''
    r = requests.get(best.url)
    message = 'Scarica video da qua: '+ str(r.text)
    update.message.reply_text(r.headers.get('content-type'))


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, replyvideo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()