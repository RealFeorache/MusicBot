"""Download the video.`"""
from telegram import Update
from maincode import BOT

from maincode import YT_DOWNLOADER, DOWNLOAD_DIR
from telegram.ext import CallbackContext, run_async
from maincode import helpers


@run_async
def send_audio(update: Update, context: CallbackContext):
    filename = _download_audio(update.effective_message.text).result()
    if filename:
        BOT.send_chat_action(
            chat_id=update.effective_chat.id,
            action='upload_audio'
            )
        BOT.send_audio(
            chat_id=update.effective_chat.id,
            audio=open(file=DOWNLOAD_DIR / filename, mode='rb'),
            title=filename[:-4]
            )

@run_async
def _download_audio(video_url: Update):
    """Download the audio file."""
    video_data = YT_DOWNLOADER.extract_info(video_url, download=True)
    if video_data:
        # Delete the remaining thumbnail
        if (DOWNLOAD_DIR / (video_data.get('title') + '.jpg')).exists():
            (DOWNLOAD_DIR / (video_data.get('title') + '.jpg')).unlink()
        return video_data.get('title') + '.m4a'