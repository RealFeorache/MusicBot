from telegram import Update
from maincode import BOT

from telegram.ext import CallbackContext, run_async


@run_async
def start(update: Update, context: CallbackContext):
    text = 'Отправь мне ссылку на видео с YouTube, а я тебе отправлю аудио файл.'
    BOT.send_message(
        chat_id=update.effective_chat.id,
        text=text
        )
