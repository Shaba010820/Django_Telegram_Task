from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button

from .states import CreateTaskSG
from .handlers import (
    on_title_entered,
    on_due_date_entered,
    on_confirm,
)

title_window = Window(
    Const("Введи название задачи"),
    TextInput(
        id="title_input",
        on_success=on_title_entered,
    ),
    state=CreateTaskSG.title,
)

due_date_window = Window(
    Const("Введи дату исполнения\nФормат: YYYY-MM-DD HH:MM"),
    TextInput(
        id="date_input",
        on_success=on_due_date_entered,
    ),
    state=CreateTaskSG.due_date,
)

confirm_window = Window(
    Const("Подтвердить создание задачи?"),
    Button(
        Const("Создать"),
        id="confirm_btn",
        on_click=on_confirm,
    ),
    state=CreateTaskSG.confirm,
)