import asyncio
import logging
import sys
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="\U0001F464 Мой профиль"),
            types.KeyboardButton(text="\U0001F5D3 Мои мероприятия"),
            types.KeyboardButton(text="\U00002754 Помощь")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню"
    )
    await message.answer("Вас приветсвует Event бот СГУ", reply_markup=keyboard)

@dp.message(F.text == "\U0001F464 Мой профиль")
async def with_puree(message: types.Message):
    await message.answer("Функция 'Профиль' еще не реализована. Подождите немного!")

@dp.message(F.text == "\U0001F5D3 Мои мероприятия")
async def without_puree(message: types.Message):
    await message.answer("Функция 'Мои мероприятия' еще не реализована. Подождите немного!")

@dp.message(F.text == "\U00002754 Помощь")
async def without_puree(message: types.Message):
    await message.answer("Функция 'Помощь' еще не реализована. Подождите немного!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())