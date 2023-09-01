from aiogram.utils import executor
from app import CHAT_ID
from handlers import *


async def notify_message(dp): # THIS FUNCTION
    print('Bot is starting')
    await dp.bot.send_message(CHAT_ID, text="Bot is starting")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=notify_message)
