import asyncio
from aiogram import F, types
from aiogram.filters import Command, or_f
from aiogram.types import Message

from loader import bot, dp, logger
from database import SqlSchool
from handlers import add_one, bot_echo, bot_help, bot_start





async def clear_commands(robot: Bot) -> None:
    await robot.set_my_commands([])
    await clear_commands(bot)


@dp.message(F.photo)
async def save_photo(message: Message):
    await bot.download(message.photo[-1], destination=f'images/{message.photo[-1].file_id}.jpg')
    await message.answer('Картинка сохранена')







@dp.message(Command('help'))
async def bot_help(message: Message):
    await message.answer(
        'Этот бот умеет выполнять команды:\n'
        '/start - приветствие\n'
        '/help - помощь\n'
        '/add_one - добавление ученика в базу даных\n'
        'Когда вы отправляет боту текстовое сообщение, он переводит его на английский язык\n'
        'Если вы отправите ему изображение, бот сохранит его в папку /images')


async def main():

    logger.info('Бот запущен')
    await dp.start_polling(bot)

@logger.catch
async def bot_start(message: Message):
    logger.info('Бот запущен')
    await message.answer('Привет! Я бот-переводчик, еще я умею сохранять картинки и отправлять голосовое сообщение')


async def stop_bot() -> None:
    await bot.session.close()
    logger.info('Бот остановлен')


if __name__ == '__main__':
    try:
        dp.message.register(bot_start, or_f(Command('start'), F.text.casefold() == 'start'))

        dp.message.register(bot_help, or_f(Command('help'), F.text.casefold() == 'help'))

        dp.message.register(bot_start, or_f(Command('start'), F.text.casefold() == 'start'))




        asyncio.run(bot_start())

    except KeyboardInterrupt:
        asyncio.run(stop_bot())