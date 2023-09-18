from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from triggers.health_check_dispatch import health_check_dispatch
from aiogram.utils.markdown import hbold
router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@router.message(Command('health'))
async def start_health_check(message: Message) -> None:
    await message.answer("Start Dispatch")
    health_check_dispatch()


@router.message(Command('regress'))
async def start_regress(message: Message) -> None:
    await message.answer("Starting Regress")
    health_check_dispatch()