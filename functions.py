from pprint import pprint

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f""" Sizning ismingiz : {user.first_name} \nId raqamingiz: {user.id} \n"""
    if user.username:
        data += f"Siznig usernameiz @{user.username}\n"
    if user.last_name:
        data += f"Sizning familyangiz {user.last_name}\n"
    if profile.bio:
        data += f"Sizning bioingiz {profile.bio}\n"
    pprint(data)
    await message.answer(text=data)


async def start(bot: Bot):
    await bot.send_message(chat_id="751843547", text="Bot Ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="751843547", text="Bot To'xtadi ⚠️")

