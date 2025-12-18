from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.api.client import auth_user
from aiogram_dialog import DialogManager, StartMode
from app.dialogs.states import CreateTaskSG

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    user = await auth_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username or "telegram_user"
    )

    await message.answer(
        f"Привет!\n"
        f"Ты зарегистрирован в TaskNest.\n"
        f"Твой ID: {user['id']}"
    )



@router.message(Command("add"))
async def add_task(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(
        CreateTaskSG.title,
        mode=StartMode.RESET_STACK,
    )