import logging
import youtube_dl
from telegram import Bot
from telegram.utils.request import Request
from pathlib import Path
from os import environ

__author__ = "Vlad Chitic"
__copyright__ = "Copyright 2019, Vlad Chitic"
__credits__ = ["Vlad Chitic"]
__license__ = "MIT License"
__version__ = "0.1 beta"
__maintainer__ = "Vlad Chitic"
__email__ = "feorache@protonmail.com"
__status__ = "Prototype"

# Setup logging
logging.basicConfig(
    filename='logs.log',
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

BOT = Bot(
    token=environ.get('MUSIC_BOT_TOKEN'),
    request=Request(con_pool_size=20)
)
DOWNLOAD_DIR = Path(__file__).parent.parent / 'downloads'

DOWNLOAD_PARAMS = {
    'outtmpl': f'{DOWNLOAD_DIR.absolute()}/%(title)s.%(ext)s',
    'format': 'bestaudio/best',
    'audioquality': 9,
    'quiet': True,
    'writethumbnail': True,
    'extractaudio': True,
    'postprocessors': [
        {
            'key': 'EmbedThumbnail'
        },
        {
            'key': 'FFmpegMetadata'
        },
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }
    ],
    'embedthumbnail': True,
    'ignoreerrors': True,
    'addmetadata': True
}
YT_DOWNLOADER = youtube_dl.YoutubeDL(DOWNLOAD_PARAMS)
