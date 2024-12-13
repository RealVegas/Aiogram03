from aiogram.dispatcher.filters.state import State, StatesGroup
from main import bot


class OrdSchool(StatesGroup):
    """
    Класс Машина состояний для school

    Attributes:
        name(State): Имя, Фамилия ученика
        age(State): возраст ученика
        grade(State): класс ученика с буквой класса

    """
    name: State = State()
    age: State = State()
    grade: State = State()