import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from dotenv import load_dotenv

from app.handlers.start import router as start_router
from app.handlers.tasks import router as tasks_router

from app.dialogs.dialog import create_task_dialog

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(tasks_router)
    dp.include_router(create_task_dialog)

    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())