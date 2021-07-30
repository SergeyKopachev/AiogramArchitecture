from aiogram.types import Message, CallbackQuery

from core.Base.BaseHandler import BaseHandler

from app.User.UserKeyboard import UserKeyboard
from app.User.UserRedis import UserRedis


class UserHandler(BaseHandler):

	def __init__(self):
		super().__init__()

		self.keyboard = UserKeyboard()
		self.redis = UserRedis()

	@classmethod
	async def register_handlers(cls, dp):
		handler = cls()

		dp.register_message_handler(handler.start, commands=['start'])

	async def start(self, msg: Message):
		await msg.answer('Успехов в разработке приложения!')
