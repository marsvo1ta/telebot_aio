import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEBHOOK_URL = 'telebot-aio.vercel.app'  # URL вашого Vercel застосунку
WEBHOOK_PATH = "/webhook"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)

# Налаштування вебхука
async def on_start_webhook(dp):
    await bot.set_webhook(WEBHOOK_URL)

# Обробник команди /start
@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привіт! Я бот, який відповідає на ваші повідомлення.")

# Обробник всіх інших повідомлень
@dp.message_handler()
async def on_message(message: types.Message):
    await message.answer(f"Ви сказали: {message.text}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_webhook(
        dp,
        on_start=on_start_webhook,
        skip_updates=True,
        host="0.0.0.0",
        port=3000,
        webhook_path=WEBHOOK_PATH
    )

