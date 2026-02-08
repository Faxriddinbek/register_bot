import asyncio
import logging

from aiogram import Dispatcher, Bot

from core.database_settings import database
from handlers import register, settings
from core.config import BOT_TOKEN, DEVELOPER
from utils.set_defaulds_commands import set_default_commands

async def startup(bot:Bot):
    await database.connect()
    await set_default_commands(bot)# set_default_commands()=> bu (/) bosganda rekombinatsa qilish
    await bot.send_message(text="Bot start to work", chat_id=DEVELOPER)

async def shutdown(bot: Bot):
    await database.disconnect()
    await bot.send_message(text="Bot stopped", chat_id=DEVELOPER)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    # Bu ro'tur haqidagi asosiyga habar
    dp.include_router(router=register.router)
    dp.include_router(router=settings.router)

    await dp.start_polling(bot, polling_timeout=0)

if __name__ == "__main__":
    logging.basicConfig(
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    asyncio.run(main())