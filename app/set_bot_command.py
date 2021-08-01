from aiogram.types import BotCommand


async def set_bot_command(dp):
	await dp.bot.set_my_commands(
		[
			BotCommand('start', 'Запустить бота'),
			BotCommand('help', 'Вывести справку')
		]
	)
