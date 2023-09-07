import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

# Ініціалізуємо бота та диспетчера
bot = Bot(token=os.environ.get('TELEGRAM_TOKEN'))
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обробник команди /start
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привіт! Я ваш простий бот на веб-хуках.")

# Обробник текстових повідомлень
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Ви сказали: {message.text}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='/',
        on_startup=None,
        on_shutdown=None,
        host='0.0.0.0',  # Адреса сервера
        port=3000,  # Порт сервера
    )






