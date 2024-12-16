from aiogram import Bot, types
from loader import logger

from loader import bot


def is_equal(new, cur) -> bool:
    new_len: int = len(new)
    cur_len: int = len(cur)

    if new_len != cur_len:
        return False

    else:
        for n in range(new_len):
            if new[n] != cur[n]:
                return False
        return True


async def set_commands(robot: Bot) -> None:
    commands = [
        types.BotCommand(command='/start', description='Запустить бота'),
        types.BotCommand(command='/help', description='Помощь'),
        types.BotCommand(command='/add_one', description='Добавление ученика в базу данных'),
    ]

    current_commands = await robot.get_my_commands()
    await robot.set_my_commands(commands)

    if not is_equal(commands, current_commands):
        await robot.set_my_commands(commands)


@logger.catch
async def bot_start(text_message: types.Message) -> None:
    await set_commands(bot)
    await text_message.answer(text='Привет я школьный бот! Создал для Вас меню с командами')