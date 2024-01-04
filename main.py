import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise Exception("Bot token not found in environment variable. Make sure to set BOT_TOKEN in your .env file.")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

my_profile_button = KeyboardButton("\U0001F464 Мой профиль")
my_events_button = KeyboardButton("\U0001F5D3 Мои мероприятия")
help_button = KeyboardButton("\U00002754 Помощь")

main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    my_profile_button, my_events_button, help_button
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Это твой бот.", reply_markup=main_menu_keyboard)

@dp.message_handler(lambda message: message.text == my_profile_button.text)
async def my_profile(message: types.Message):
    await message.answer("Функция 'Мой профиль' еще не реализована. Подождите немного!")

@dp.message_handler(lambda message: message.text == my_events_button.text)
async def my_events(message: types.Message):
    await message.answer("Функция 'Мои мероприятия' еще не реализована. Подождите немного!")

@dp.message_handler(lambda message: message.text == help_button.text)
async def help_command(message: types.Message):
    await message.answer("Функция 'Помощь' еще не реализована. Подождите немного!")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
