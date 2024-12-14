from aiogram import types
from loader import logger


@logger.catch
async def bot_help(text_message: types.Message) -> None:
    info: str = '''
    <b>Команда /start или start</b>
    Запустить бота, бот создаст меню

    <b>Команда /help, или help</b>
    Вывод этой информации

    <b>Команда /add_one, или add_one</b>
    Добавление ученика в базу данных 
    '''

    await text_message.answer(text=info)