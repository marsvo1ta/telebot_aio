# bot.py
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('HEALTH_CHECK_CHAT_ID')
bot = Bot(token=TOKEN)

# Initialize the dispatcher
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Define your command handlers
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hello! I am your Telegram bot.")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("You can use the following commands:\n/start - Start the bot\n/help - Show this help message")

# This function starts the bot
def start_polling():
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
