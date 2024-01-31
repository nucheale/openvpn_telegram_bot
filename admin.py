from config_data import config
from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode

administrators = [201994697]
bot = Bot(token=config.BOT_TOKEN.get_secret_value(), parse_mode=ParseMode.HTML)
