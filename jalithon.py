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





# Copyright (C) 2022 Zed-Thon . All Rights Reserved
@jalithon.on(events.NewMessage(outgoing=False, pattern="المليار ?(.*)")
async def OwnerStart(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنـاً .. تأكـد من انك مشتـرك بـ قنـوات الاشتـراك الاجبـاري لتجنب الأخطـاء @zmmbot**")
    channel_entity = await jalithon.get_entity('@zmmbot')
    await jalithon.send_message('@zmmbot', '/start')
    await asyncio.sleep(4)
    msg0 = await jalithon.get_messages('@zmmbot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await jalithon.get_messages('@zmmbot', limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقه مختلفه**') != -1:
            await jalithon.send_message(event.chat_id, f"**⎉╎مـافي قنـوات بالبـوت حاليـاً ...**")
            break
        if con == "ايقاف":
            await jalithon.send_message(event.chat_id, f"**⎉╎تم إيقـاف تجميـع النقـاط ☑️ ...**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await jalithon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await jalithon(ImportChatInviteRequest(bott))
            msg2 = await zedub.get_messages('@zmmbot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم بنجـاح الاشتـراك في {chs} قنـاة ...✓**")
        except:
            msg2 = await jalithon.get_messages('@zmmbot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} خطـأ .. يمكـن تبنـدت**")
    await jalithon.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")
    
@jalithon.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️\n[ . ᯏ𝖩𝖺𝖨𝗂𝗍𝗁᥆ꪀ ~ ꪀꫀ᥊ ᭡ .](t.me/Jalithon)\n**',
                                  link_preview=False,
                                 )
        
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️\n[ . ᯏ𝖩𝖺𝖨𝗂𝗍𝗁᥆ꪀ ~ ꪀꫀ᥊ ᭡ .](t.me/Jalithon)\n**',
                                  link_preview=False,
                                 )

@jalithon.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
\n[ . ᯏ𝖩𝖺𝖨𝗂𝗍𝗁᥆ꪀ ~ ꪀꫀ᥊ ᭡ .](t.me/Jalithon)\n\n› فحص سورس : ارسل `/TEST`\n.\n› امر تجميع نقاط بوت المليار لانهائي : `/somy ZMMBOT 300`\n.\n› امر تجميع نقاط بوت الجوكر لانهائي : `/somy A_MAN9300BOT 300`\n.\n› امر تجميع نقاط بوت العقاب لانهائي : `/somy MARKTEBOT 300`\n.\n› امر تجميع نقاط بوت العرب لانهائي : `/somy xnsex21bot 300`\n.\n› امر تجميع نقاط بوت المليار : `/Bom`\n.\n› امر تجميع نقاط بوت الجوكر : `/Bok`\n.\n› امر تجميع نقاط بوت العقاب : `/Bol`\n.\n› امر تجميع نقاط بوت العرب : `/Bor`\n.\n\n› بدء تجميع نقاط من بوت اخر : ارسل `/point يوزر البوت بدون (@)`\n.\n\n› الاشتراك الاجباري بوتات تمويل : `/ch`\n.\n\n› للدخول آلى قائمة معلومات الحساب : `/Information`\n.\n› للدخول آلى قائمة تحويل النقاط : `/Transfer`\n.\n\n› امر مغادرة جميع قنوات والمجموعات: `/Leaving`\n.\n\n› امر يجعل الحساب ينضم الى قناة معينة : `/Joined` يوزر القناة (@)\n.\n\n› امر طلب اخر رسالة من محادثه معينة : `/Transfer` بدون (@)\n.\n
**""",
                                  link_preview=False,
                                 )
@jalithon.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 

2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : somy/ 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [bot , /Bom/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**""")

@jalithon.on(events.NewMessage(outgoing=True, pattern=".اوامري"))
async def _(event):
      await event.edit("""**• اوامر الحساب المستخدم التجميع .**\n\n› بـوت تمويل المليار** : `.تجميع المليار**`\n.\n› بـوت تمويل العقاب** : `.تجميع العقاب**`\n.\n› بـوت تمويل العرب** : `.تجميع العرب**`\n.\n› بـوت تمويل الجوكر** : `.تجميع الجوكر**`\n.\n
              [ . ᯏ𝖩𝖺𝖨𝗂𝗍𝗁᥆ꪀ ~ ꪀꫀ᥊ ᭡ .](t.me/Jalithon)
""",
                         link_preview=False,
                      )
@jalithon.on(events.NewMessage(outgoing=False, pattern='/Bom'))
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
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='/Bok'))
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

@jalithon.on(events.NewMessage(outgoing=False, pattern='/Bol'))
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

@jalithon.on(events.NewMessage(outgoing=False, pattern='/Bor'))
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

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | off")
        
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
                await jalithon.send_message(event.chat_id, f"تم الانتهاء من التجميع | off")

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

        await jalithon.send_message(event.chat_id, "تم الانتهاء من التجميع | off")
        
@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await jalithon.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await jalithon.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@jalithon.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
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
                        await jalithon.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
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
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await jalithon.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await asyncio.sleep(60)

                await jalithon.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


@jalithon.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")

                joinu = await jalithon(JoinChannelRequest('jalithon'))
                channel_entity = await jalithon.get_entity(pot)
                await jalithon.send_message(pot, '**جاري بدأ عملية التجميع بواسطة جليثون**')
                await jalithon.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await jalithon.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await jalithon.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await jalithon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await jalithon.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await jalithon(JoinChannelRequest(url))
                        except:
                            syth = url.split('/')[-1]
                            await jalithon(ImportChatInviteRequest(syth))
                        msg2 = await jalithon.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 10
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                    except:
                        msg2 = await jalithon.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة\n✣ لأنني وجدت قناة خاصة قمت بتخطيها\n✣ البوت التي حدث فيه الخطأ: @{pot}**""")
                        
                await jalithon.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        except Exception as e:
            
            await asyncio.sleep(numw)
            
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
    

@jalithon.on(events.NewMessage(outgoing=False, pattern=r'/Leaving'))
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
    
    
@jalithon.on(events.NewMessage(outgoing=False, pattern='/Transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@jalithon.on(events.NewMessage(outgoing=False, pattern='/Information'))
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
    await jalithon.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@jalithon.on(events.NewMessage(outgoing=False, pattern=r'^/Transfer (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await jalithon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await jalithon.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@jalithon.on(events.NewMessage(outgoing=False, pattern='/ch'))
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
        
@jalithon.on(events.NewMessage(outgoing=False, pattern='/Joined (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await jalithon.send_message(event.chat_id,f"**جاري الانضمام في القناة \n@{usercht}**")
        joinch = await jalithon(JoinChannelRequest(usercht))
        sendy = await jalithon.send_message(event.chat_id,f"**تم الانضمام في القناة \n@{usercht}**")


print("✖️")
jalithon.run_until_disconnected()

