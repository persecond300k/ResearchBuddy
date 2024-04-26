from aiogram import Router, types
from aiogram.filters import Command
from src.config.config import config_yaml

router = Router()

@router.message(Command(commands=["start", "help"]))
async def command_help(message: types.Message):
    welcome_message = config_yaml["messages"]["welcome"]
    await message.answer(welcome_message, parse_mode="markdown")
