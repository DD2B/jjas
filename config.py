from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
SESSION1 = os.environ.get("TERMUX")
DEVLOO = os.environ.get("DEVLO")
CHNA = os.environ.get("CHNA")
jalithon = TelegramClient(StringSession(SESSION1), APP_ID, APP_HASH)

ispay = ['yes']
ispay2 = ['yes']
