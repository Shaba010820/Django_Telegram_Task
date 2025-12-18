from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.api.client import get_tasks

router = Router()


@router.message(Command("tasks"))
async def tasks_handler(message: Message):
    tasks = await get_tasks(message.from_user.id)

    if not tasks:
        await message.answer("У тебя пока нет задач.")
        return

    lines = ["*Твои задачи:*", ""]

    for i, task in enumerate(tasks, start=1):
        category = task["category"] or "Без категории"
        created_at = task["created_at"][:10]

        lines.append(
            f"{i}. *{task['title']}*\n"
            f"   {category}\n"
            f"   Создано: {created_at}"
        )

    await message.answer(
        "\n\n".join(lines),
        parse_mode="Markdown",
    )
