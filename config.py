from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = ("‏hha2hbot")
session1 = os.environ.get("TERMUX")
SESSION1 = os.environ.get("TERMUX")
token = ("6031928256:AAFJ-WfewxHof8ek37KcXGG3wgN-GhkfCEI")
DEVLOO = os.environ.get("DEVLO")
CHNA = os.environ.get("CHNA")
jalithon = TelegramClient(StringSession(session1), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)


ispay = ['yes']
ispay2 = ['yes']
bot.start()

