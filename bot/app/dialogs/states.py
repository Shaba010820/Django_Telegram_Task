from aiogram.fsm.state import StatesGroup, State

class CreateTaskSG(StatesGroup):
    title = State()
    due_date = State()
    confirm = State()