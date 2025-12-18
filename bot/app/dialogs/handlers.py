from aiogram_dialog import DialogManager
from app.api.client import create_task
from datetime import datetime

async def on_title_entered(message, widget, dialog_manager: DialogManager, text: str):
    dialog_manager.dialog_data["title"] = text
    await dialog_manager.next()


async def on_due_date_entered(message, widget, dialog_manager: DialogManager, text: str):
    try:
        due_date = datetime.strptime(text, "%Y-%m-%d %H:%M")
    except ValueError:
        await message.answer("Неверный формат. Используй YYYY-MM-DD HH:MM")
        return

    dialog_manager.dialog_data["due_date"] = due_date.isoformat()
    await dialog_manager.next()


async def on_confirm(callback, button, dialog_manager: DialogManager):
    data = dialog_manager.dialog_data
    user = callback.from_user

    await create_task(
        telegram_id=user.id,
        title=data["title"],
        due_date=data["due_date"],
    )

    await callback.message.answer("Задача создана")
    await dialog_manager.done()