from config_data import config
from admin import bot
from subprocess import check_output
from aiogram import types, F, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
import asyncio
import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router
import time

# db = Database(config.DATABASE_FILE)


async def main():
    disp = Dispatcher(storage=MemoryStorage())
    disp.include_router(router)
    print('Бот запущен')
    await bot.delete_webhook(drop_pending_updates=True)
    await disp.start_polling(bot, allowed_updates=disp.resolve_used_update_types())


async def main_ubuntu_vpn():
    await asyncio.gather(main())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main_ubuntu_vpn())