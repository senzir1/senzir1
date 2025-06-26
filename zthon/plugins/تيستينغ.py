from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError, FloodWaitError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.errors import UserAdminInvalidError, ChatAdminRequiredError
from telethon import events, functions
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import User
from telethon.types import InputWebDocument
from telethon.errors import MediaEmptyError, WebpageMediaEmptyError, WebpageCurlFailedError
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.types import InputMediaDice
from telethon.tl.types import InputMessagesFilterDocument
from telethon.utils import get_input_photo
from telethon import functions, events
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.types import ChannelParticipantsAdmins, UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusRecently, UserStatusOnline
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.errors.rpcerrorlist import PeerIdInvalidError
from pySmartDL import SmartDL
from telethon.tl.types import MessageActionChannelMigrateFrom
from telethon import events, Button
from queue import Queue
from telethon.sync import functions
from telethon.tl.types import InputChatUploadedPhoto
from user_agent import generate_user_agent
from telethon import events, functions, sync
from telethon.tl.functions.channels import CreateChannelRequest, EditPhotoRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.types import PeerChannel, PeerUser
from telethon.errors import RPCError
from threading import Thread
from telethon.tl.functions.messages import ReportSpamRequest
from telethon import types
from telethon.tl import functions
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events, functions
from telethon.tl.types import Message
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.events import NewMessage
from telethon import events 
from telethon.tl.types import InputPeerChat
from telethon import errors
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import MessageMediaDocument
from telethon import events, functions, utils
from telethon.tl import functions, types
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telethon.tl.types import MessageEntityMentionName
from telethon.errors import ChatAdminRequiredError
from telethon.tl.types import InputChannel
from deep_translator import GoogleTranslator
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins        
from telethon.errors import ChannelInvalidError
from langdetect import detect  
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import EditTitleRequest
from datetime import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.errors.rpcerrorlist import (
    StickerMimeInvalidError, 
    PhotoExtInvalidError, 
    PhotoCropSizeSmallError, 
    ImageProcessFailedError )
from telethon import TelegramClient, events
from telethon import TelegramClient, events, sync 
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from sqlalchemy.ext.declarative import declarative_base
from gpytranslate import Translator
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from telethon.tl.functions.channels import EditPhotoRequest
from telethon import events
from telethon import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from telethon import events, functions, types
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from sqlalchemy import create_engine
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos
from asyncio import sleep
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from telethon.tl.types import Channel, Chat
from dateutil import tz
from emoji import emojize
from datetime import datetime
from telethon.tl.custom import Button
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import WebpageMediaEmptyError
from telethon.tl.functions.messages import DeleteMessagesRequest
import sys
import pytz
import asyncio
import os
import datetime as dt
import base64
import events
import platform
from telethon import version as telethon_version
from telethon import events
from ping3 import ping
import pickle
import string
import re
import json
import mention
import requests
import io
import pybase64
import aiohttp
import random
import threading
import html
import telethon
import logging
import shutil
import time
import os
import pickle
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest



YOUTUBE_API_KEY = 'AIzaSyBfb8a-Ug_YQFrpWKeTc88zuI6PmHVdzV0'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@zedub.on(events.NewMessage(from_users='me', pattern=r'.تت (.+)'))
async def youtube_search(event):
    await event.delete()
    query = event.pattern_match.group(1)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(YOUTUBE_API_URL, params={
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }) as response:
            data = await response.json()
            if data['items']:
                video_id = data['items'][0]['id']['videoId']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                await event.reply(f"📹 هنا رابط الفيديو الذي تم العثور عليه:\n{video_url}")
            else:
                await event.reply("⎙ لم يتم العثور على فيديو يتطابق مع العنوان المطلوب.")
              
