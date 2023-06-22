from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests

jalithon.start()



c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [1759470911]



        
        
     
@jalithon.on(events.NewMessage(outgoing=False, pattern='TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@jalithon.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
𝐒𝐘𝐓𝐇𝐎𝐍 𝐏𝐎𝐈𝐍𝐓 


1 - لـفحص عمل السورس عند حساب معين 

•`/TEST`

2 - لـبدء التجميع النقاط من بوتات التمويل 

•`/point1` - يقوم بتجميع نقاط بوت المليار
•`/point2` - يقوم بتجميع نقاط بوت الجوكر
•`/point3` - يقوم بتجميع نقاط بوت العقاب
•`/point4` - يقوم بتجميع نقاط بوت العرب

3 - لـبدء تجميع نقاط من بوت غير موجود ارسل

•`/point` + يوزر البوت 

4 - لـجعل الحساب ينضم لقنوات بوتات التمويل

•`/join`

5 - لـلدخول الى قائمة معلومات الحساب

• `/infoacc`

6 - لـلدخول الى قائمة تحويل النقاط 

•`/transfer`

7 - لـمغادرة الحساب جميع القنوات والمجموعات

•`/lpoint`

8 - لـلدخول الى قائمة اخرى تحتوي اوامر اخرى

•`/sython`

━━━━━━━━━━━━━━━━━━━━━━━━

ꌚꂖꋖꀍꁏꋊ ꉣꁏꀤꋊꋖ
**""")


@jalithon.on(events.NewMessage(outgoing=False, pattern='/sython'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
𝐒𝐘𝐓𝐇𝐎𝐍 𝐏𝐎𝐈𝐍𝐓 

1 - لـجعل الحساب يقوم بالدخول الى رابط الدعوه

•`/bot + ايدي الحساب + يوزر البوت`

2 - لـجعل الحساب ينضم الى قناة معينه 
او الانضمام الى قنوات البوت 

•`/jn + يوزر القناة` 

3 - لـجلب اخر رسالة من محادثه معينه 

•`/forward + يوزر المحادثة`

4 - لـبدء تجميع نقاط من بوت تمويل بدون توقف 

•`/collect + يوزر البوت`

5 - لـاعادة تشغيل السورس 

•`/restart`
━━━━━━━━━━━━━━━━━━━━━━━━

ꌚꂖꋖꀍꁏꋊ ꉣꁏꀤꋊꋖ
**""")


@jalithon.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")


@jalithon.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await jalithon(JoinChannelRequest('jalithon'))
        channel_entity = await jalithon.get_entity(bot_username)
        await jalithon.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await jalithon.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await jalithon.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | off")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await jalithon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await jalithon(ImportChatInviteRequest(bott))
                msg2 = await jalithon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await jalithon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | off")
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await jalithon(JoinChannelRequest('jalithon'))
        channel_entity = await jalithon.get_entity(bot_usernamee)
        await jalithon.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await jalithon.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await jalithon.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | off")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await jalithon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await jalithon(ImportChatInviteRequest(bott))
                msg2 = await jalithon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await jalithon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | off")

@jalithon.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await jalithon(JoinChannelRequest('jalithon'))
        channel_entity = await jalithon.get_entity(bot_usernameee)
        await jalithon.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await jalithon.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await jalithon.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | off")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await jalithon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await jalithon(ImportChatInviteRequest(bott))
                msg2 = await jalithon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await jalithon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | off")

@jalithon.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await jalithon(JoinChannelRequest('jalithon'))
        channel_entity = await jalithon.get_entity(bot_usernameeee)
        await jalithon.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await jalithon.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await jalithon.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | off")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await jalithon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await jalithon(ImportChatInviteRequest(bott))
                msg2 = await jalithon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await jalithon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@jalithon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await jalithon(JoinChannelRequest('jalithon'))
    channel_entity = await jalithon.get_entity(bot_username)
    await jalithon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await jalithon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await jalithon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await jalithon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | off**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await jalithon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await jalithon(ImportChatInviteRequest(bott))
            msg2 = await jalithon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await jalithon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await jalithon.send_message(event.chat_id, "**تم الانتهاء من التجميع | off**")
    
    
    
@jalithon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await jalithon(JoinChannelRequest('jalithon'))
    channel_entity = await jalithon.get_entity(bot_usernamee)
    await jalithon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await jalithon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await jalithon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await jalithon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | off**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await jalithon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await jalithon(ImportChatInviteRequest(bott))
            msg2 = await jalithon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await jalithon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await jalithon.send_message(event.chat_id, "**تم الانتهاء من التجميع | off**")

@jalithon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await jalithon(JoinChannelRequest('jalithon'))
    channel_entity = await jalithon.get_entity(bot_usernameee)
    await jalithon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await jalithon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await jalithon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await jalithon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | off**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await jalithon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await jalithon(ImportChatInviteRequest(bott))
            msg2 = await jalithon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await jalithon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await jalithon.send_message(event.chat_id, "**تم الانتهاء من التجميع | off**")


@jalithon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await jalithon(JoinChannelRequest('jalithon'))
    channel_entity = await jalithon.get_entity(bot_usernameeee)
    await jalithon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await jalithon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await jalithon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await jalithon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | off**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await jalithon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await jalithon(ImportChatInviteRequest(bott))
            msg2 = await jalithon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await jalithon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await jalithon.send_message(event.chat_id, "**تم الانتهاء من التجميع | off**")


##########################################

@jalithon.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await jalithon(JoinChannelRequest('jalithon'))
        channel_entity = await jalithon.get_entity(pot)
        await jalithon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await jalithon.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await jalithon.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await jalithon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await jalithon(ImportChatInviteRequest(bott))
                msg2 = await jalithon.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await jalithon.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("جاري بدء عملية التجميع اللانهائية")

                joinu = await jalithon(JoinChannelRequest('jalithon'))
                channel_entity = await jalithon.get_entity(pot)
                await jalithon.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await jalithon.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await jalithon.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await jalithon(JoinChannelRequest(url))
                        except:
                            bott = url.split('/')[-1]
                            await jalithon(ImportChatInviteRequest(bott))
                        msg2 = await jalithon.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"تم الانضمام في {chs} قناة")
                    except:
                        msg2 = await jalithon.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"القناة رقم {chs}")
                        await asyncio.sleep(60)

                await jalithon.send_message(event.chat_id, "حدث خطأ ولكن لاتقلق سوف اعالج المشكلة واستمر ")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass

@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
        await jalithon.disconnect()
        await jalithon.send_message(event.chat_id, "تم اعادة تشغيل السورس ")
        


@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await jalithon.send_message(bot_username, pt)
    sleep(4)
    msg = await jalithon.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await jalithon.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await jalithon.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await jalithon.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await jalithon.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await jalithon.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await jalithon.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await jalithon.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await jalithon.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await jalithon.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await jalithon.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await jalithon.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await jalithon(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                




@jalithon.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await jalithon.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@jalithon.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@jalithon.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(userbt, '/start')
     sleep(2)
    msg1 = await jalithon.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await jalithon.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await jalithon.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await jalithon(JoinChannelRequest('d3boot_7'))
        joinw = await jalithon(JoinChannelRequest('Fvvvv'))
        joine = await jalithon(JoinChannelRequest('DzDDDD'))
        joinr = await jalithon(JoinChannelRequest('botbillion'))
        joint = await jalithon(JoinChannelRequest('zzzzzz1'))
        joiny = await jalithon(JoinChannelRequest('zzzzzz'))
        joini = await jalithon(JoinChannelRequest('zz_MX'))
        joino = await jalithon(JoinChannelRequest('lI7777Il'))
        joinp = await jalithon(JoinChannelRequest('KTTTT'))
        joina = await jalithon(JoinChannelRequest('RRXFR'))
        sendd = await jalithon.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await jalithon.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await jalithon(JoinChannelRequest(usercht))
        sendy = await jalithon.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")



jalithon.run_until_disconnected()
