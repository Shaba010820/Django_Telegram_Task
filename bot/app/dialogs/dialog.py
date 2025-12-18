from aiogram_dialog import Dialog
from .windows import title_window, due_date_window, confirm_window

create_task_dialog = Dialog(
    title_window,
    due_date_window,
    confirm_window,
)