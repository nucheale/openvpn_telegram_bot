from config_data import config
from aiogram import types, F, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
# from admin import administrators
# from my_database import Database
import re
import subprocess
from subprocess import check_output
import logging

router = Router()


# db = Database(config.DATABASE_FILE)


@router.message(Command("start"))
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        # if not db.user_exists(message.from_user.id):
        #     db.add_user(message.from_user.username, message.from_user.id)
        await message.answer(f'<b>Добро пожаловать, {message.from_user.first_name}!</b>')


# @router.message(F.text)
# async def any_text(message: Message):
#     command = message.text
#     # command = ["echo", "Hello World!"]
#     try:
#         result = check_output(command)
#         # result = str(result, "cp866")  # cp866 это для Windows
#         # await message.answer(check_output(command))
#     except Exception as e:
#         logging.error(e)
#         result = "Команда не распознана"
#     finally:
#         print(result)
#         await message.answer(result)


@router.message(F.text)
async def any_text(message: Message):
    command = message.text
    try:
        command = message.text
        result = subprocess.run([command], capture_output=True)
        result = f'Response: \n{result.stdout.decode()}'
        print(result)
    except subprocess.CalledProcessError as e:
        logging.error(e)
        result = f'Ошибка'
    finally:
        await message.answer(result)

# @router.message(F.text)
# async def any_text(message: Message):
#     command = message.text
#     result = subprocess.run([command], capture_output=True)
#     print(result.stdout.decode())
#     decoded_result = f'Response: {result.stdout.decode()}'
#     await message.answer(decoded_result)
