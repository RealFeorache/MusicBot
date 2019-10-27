from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from maincode import BOT, send_audio, start


def main():
    updater = Updater(bot=BOT, use_context=True, workers=16)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start.start))
    dispatcher.add_handler(MessageHandler(Filters.all, send_audio.send_audio))
    updater.start_polling(clean=True)
    updater.idle()

if __name__ == '__main__':
    main()
