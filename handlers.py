from config_data import config
from aiogram import types, F, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
# from admin import administrators
# from my_database import Database
import re
from subprocess import check_output

router = Router()

# db = Database(config.DATABASE_FILE)


@router.message(Command("start"))
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        # if not db.user_exists(message.from_user.id):
        #     db.add_user(message.from_user.username, message.from_user.id)
        await message.answer(f'<b>Добро пожаловать, {message.from_user.first_name}!</b> Для начала добавьте нужные валюты через команду /add (либо выберите нужную в меню внизу экрана), затем установите время для уведомления командой /time.')


@router.message(F.text)
async def any_text(message: Message):
    command = message.text
    print(message.text)
    try:
        await message.answer(check_output(command))
    except:
        await message.answer("Команда не распознана")




# user_id = 0 #id вашего аккаунта
# @bot.message_handler(content_types=["text"])
# def main(message):
#   comand = message.text  #текст сообщения
#   try: #если команда невыполняемая - check_output выдаст exception
#      bot.send_message(message.chat.id, check_output(comand, shell = True))
#   except:
#      bot.send_message(message.chat.id, "Invalid input") #если команда некорректна