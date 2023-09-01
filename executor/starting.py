from aiogram import executor
import asyncio

from app import dp, app, bot, CHAT_ID


async def on_startup(dp):
    await bot.send_message(chat_id=CHAT_ID, text="Бот запущений")

    while True:
        try:
            await dp.skip_updates()
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Помилка лонгполінгу: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
