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
# -

# -ل

sython1.start()

c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5159123009]


async def join_channel():
    try:
        await sython(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass

@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@RRXDR"))
    except BaseException:
        pass
        
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@RRXJR"))
    except BaseException:
        pass
        
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@RRXOR"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@RRXBR"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@RRXFR"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@KTTTT"))
    except BaseException:
        pass
        
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@zzzzzz"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@zz_MX"))
    except BaseException:
        pass 

@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@zN_E4"))
    except BaseException:
        pass

@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@sy_tem"))
    except BaseException:
        pass


        
        

@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@d3boot_7"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@DzDDDD"))
    except BaseException:
        pass
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@botbillion"))
    except BaseException:
        pass
        
        
@sython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython1(JoinChannelRequest("@fvvvv"))
    except BaseException:
        pass

        
@sython1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@sython1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`**
• Translate Source - `/sy`""")



@sython1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@sython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_username)
    await sython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernamee)
    await sython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameee)
    await sython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameeee)
    await sython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_username)
    await sython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernamee)
    await sython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameee)
    await sython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@sython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await sython1(JoinChannelRequest('saythonh'))
    channel_entity = await sython1.get_entity(bot_usernameeee)
    await sython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await sython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await sython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await sython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await sython1(ImportChatInviteRequest(bott))
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await sython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await sython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

       

@sython1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await sython1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    


@sython1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")


@sython1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@sython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = int(event.pattern_match.group(3))
        haso = await sython1.get_entity(chn)
        join = await sython1(JoinChannelRequest(chn))
        joion = await sython1(JoinChannelRequest('saythonh'))
        somy = await sython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await sython1.send_message(CHNA,'**Done Send Voice**')




print("💠 Sython Userbot Running 💠")
sython1.run_until_disconnected()


#code skip accumulate points by t.me.zzzzl1l thank you my bro
