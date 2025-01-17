import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client
from config import Config
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from SmartEncoder.Database.db import myDb
from SmartEncoder.Plugins.url_work import short_me
from SmartEncoder.helper import TASKS

TGBot = Client(
	"bot_mode",
	bot_token=Config.BOT_TOKEN,
	api_id=Config.API_ID,
	api_hash=Config.API_HASH,
	workers=2
)



logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.getLogger("pyrogram").setLevel(logging.WARNING)
