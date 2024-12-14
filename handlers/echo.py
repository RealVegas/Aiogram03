from aiogram import types
from loader import logger


@logger.catch
async def bot_echo(message: types.Message) -> None:
    message_text = message.text.casefold()

    bot_commands = ['/start', 'start', '/help', 'help',  '/add_one', 'add_one']

    if message_text in bot_commands:
        return

    greeting: tuple = (
        'привет',
        'здравствуй',
        'здравствуйте',
        'кто это',
        'это кто',
        'кто ты',
        'ты кто'
    )
    response: tuple = (
        'Здравствуйте, я школьный бот - добавляю учеников в базу данных школы.',
        'Я не чат-бот, я просто школьный бот.',
        'Для вывода подробной справки и списка команд наберите help',
        'Неизвестная команда, для вывода списка допустимых команд наберите help'
    )

    if message_text.startswith(greeting) or message_text.endswith(greeting):
        response_text = f'{response[0]} {response[2]}'
    elif message_text.startswith('/'):
        response_text = f'{response[3]}'
    else:
        response_text = f'{response[1]} {response[2]}'

    await message.answer(text=response_text)