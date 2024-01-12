from SmartEncoder.Database.db import myDb
from SmartEncoder import TGBot, logger
from SmartEncoder.Plugins.url_work import short_me
from config import Config

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client

def access(func):
	async def wrapper(client: Client, msg: Message):
		try:
			if msg.from_user.id in Config.AUTH_USERS:
				print("IS ADMIN")
				return await func(client, msg)

			token_live = myDb.check_access(msg.from_user.id)

			if not token_live:

				token = myDb.gen_token(msg.from_user.id)
				bot_ = await TGBot.get_me()


				btn = [[InlineKeyboardButton("Gen Token", url=short_me(f"https://telegram.me/{bot_.username}?start={token}"))]]

				await msg.reply(
					text=f"You need to generate Token to use me {msg.from_user.mention} .\n\n",
					reply_markup=InlineKeyboardMarkup(btn),
				)

				myDb.client.set(f"acc^{msg.from_user.id}", 0)

				return

			elif not myDb.got_key(msg.from_user.id):

				await msg.reply("You need to send access token to use me.")
				return

			else: await func(client, msg)

		except Exception as e:

			await msg.reply("There was an error. Please try again later..")

			logger.error(e)

	return wrapper
