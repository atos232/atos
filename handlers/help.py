from telethon import TelegramClient , events , Button
from html_telegraph_poster.upload_images import upload_image
import time , logging , os , asyncio , userbot
import handlers.client , handlers.greetins , handlers.alive , handlers.quote
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


botClient = userbot.botClient
dyno = handlers.client.client






