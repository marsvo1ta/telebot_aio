import os
from aiogram import Bot, Dispatcher
# from fastapi import FastAPI


# app = FastAPI()
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('HEALTH_CHECK_CHAT_ID')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


