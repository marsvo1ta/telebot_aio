from app import dp
from aiogram import types
from triggers.health_check_dispatch import health_check_dispatch


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("We are online")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Hi,\nI'm here, need some help?")


@dp.message_handler(commands=['regress'])
async def regress_command(message: types.Message):
    await message.reply("Regress has started")


@dp.message_handler(commands=['health_check'])
async def health_check_command(message: types.Message):
    health_check_dispatch()
    await message.reply("Health Check has started")


