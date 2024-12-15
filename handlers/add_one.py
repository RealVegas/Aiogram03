from aiogram import F, types

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, or_f

from loader import Dispatcher, logger

from database import SqlSchool
from states import CommonSchool


@logger.catch
def bot_add_one(dp: Dispatcher) -> None:
    dp.message.register(start_add, or_f(Command('add_one'), F.text.casefold().func(lambda text: text == 'add_one')))
    dp.message.register(set_name, CommonSchool.name)
    dp.message.register(set_age, CommonSchool.age)
    dp.message.register(set_grade, CommonSchool.grade)


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

    pupil_name = str(pupil_data['name'])
    pupil_age = int(pupil_data['age']) if pupil_data['age'].isdigit() else str(pupil_data['age'])
    pupil_grade = str(pupil_data['grade'])

    add_to_base(pupil_name, pupil_age, pupil_grade)
    await state.clear()
    await message.answer(f'Ученик {pupil_name} добавлен в базу данных')


def add_to_base(name: str, age: int | str, grade: str) -> None:
    school_base = SqlSchool()

    school_base.school_start()
    school_base.add_pupil(name, age, grade)