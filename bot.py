import os
from asyncio import run

from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from functions import start, info, stop

load_dotenv()

from aiogram import Bot, Dispatcher

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()



async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),
            BotCommand(command="/help", description="Yordam")
        ]
    )
    dp.startup.register(start)
    dp.message.register(info)
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))
