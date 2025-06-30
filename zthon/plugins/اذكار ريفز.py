#Refz ®
#الملـف حقـوق وكتابـة سينزر الهيبـه ⤶ @senzir1 خاص بسـورس ⤶ Refz
#الملف مرفـوع ع استضـافتـي مهمـا خمطت راح تطلـع حقـــوقــي بســورســـك
#هههههههههههههههههه


import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from Tepthon import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "البحث"


ZelzalPH_cmd = (
    "**الأذكــار :**\n\n"
    "**الحمدُ لله 📿**\n\n"
    "**لا إله إلّا الله 🤍**\n\n"
    "**صلوا على النبي ♥️**\n\n"
    "**داوموا الأذكار 🥰 - سورس ريفز 🇵🇸🤍 .**"
)


# Copyright (C) 2025 RE-FZ . All Rights Reserved
@zedub.zed_cmd(pattern="اذكار")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalPH_cmd)
