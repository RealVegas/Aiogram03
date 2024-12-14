from aiogram import F, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from loader import dp, logger

from database import SqlSchool
from states import CommonSchool


@logger.catch
async def bot_add_one(text_message: types.Message) -> None:
    dp.message.register(StateFilter(None), start_add, or_f(Command('add_one'), F.text.casefold() == 'add_one'))
    dp.message.register(set_name, state=CommonSchool.name)
    dp.message.register(set_age, state=CommonSchool.age)
    dp.message.register(set_grade, state=CommonSchool.grade)


async def start_add(message: types.Message, state: FSMContext) -> None:
    await message.answer('Введите имя и фамилию ученика')
    await state.set_state(CommonSchool.name)


async def set_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer('Введите возраст ученика')
    await state.set_state(CommonSchool.age)


async def set_age(message: types.Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer('Введите класс ученика с буквой класса')
    await state.set_state(CommonSchool.grade)


async def set_grade(message: types.Message, state: FSMContext) -> None:
    await state.update_data(grade=message.text)
    pupil_data = await state.get_data()

    add_to_base(pupil_data['name'], pupil_data['age'], pupil_data['grade'])

    await state.clear()


def add_to_base(name: str, age: int, grade: str) -> None:
    school_base = SqlSchool()

    school_base.school_start()
    school_base.add_pupil(name, age, grade)