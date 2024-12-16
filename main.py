import asyncio
from aiogram import Bot, F, types
from aiogram.filters import Command, or_f

from loader import bot, dp, logger
from keyboards import link_keyboard, more_button, option_buttons

from handlers import bot_echo, bot_help, bot_start
from handlers import add_one


# Удаление меню
async def clear_commands(robot: Bot) -> None:
    await robot.set_my_commands([])
    await clear_commands(robot)


# Реакция на кнопки
async def bot_geeting(message: types.Message) -> None:
    await message.answer(f'Привет, {message.from_user.first_name}!')


async def bot_farewell(message: types.Message) -> None:
    await message.answer(f'До свидания, {message.from_user.first_name}!')


# Функции для inline клавиатур
async def bot_links(message: types.Message) -> None:
    await message.answer('Выберите интересующий вас раздел', reply_markup=link_keyboard)


async def show_button(callback: types.CallbackQuery) -> None:
    await callback.answer('Показать ещё', reply_markup=more_button)


async def show_more(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text('Вот свежие новости!', reply_markup=option_buttons)


async def opt_1(callback: types.CallbackQuery) -> None:
    await callback.answer('Опция 1')
    await bot.send_message(callback.from_user.id, 'Вы выбрали опцию 1')


async def opt_2(callback: types.CallbackQuery) -> None:
    await callback.answer('Опция 2')
    await bot.send_message(callback.from_user.id,'Вы выбрали опцию 2')


# Главные функции
async def main():
    logger.info('Бот запущен')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def stop_bot() -> None:
    # await clear_commands(bot)
    await bot.session.close()
    logger.info('Бот остановлен')


if __name__ == '__main__':
    try:
        dp.message.register(bot_start, or_f(Command('start'), F.text.casefold().func(lambda text: text == 'start')))
        dp.message.register(bot_help, or_f(Command('help'), F.text.casefold().func(lambda text: text == 'help')))
        dp.message.register(bot_links, or_f(Command('links'), F.text.casefold().func(lambda text: text == 'links')))
        dp.message.register(show_button, or_f(Command('dynamic'), F.text.casefold().func(lambda text: text == 'dynamic')))

        dp.callback_query.register(show_more, F.data.casefold() == 'show_more')
        dp.callback_query.register(opt_1, F.data.casefold() == 'opt_1')
        dp.callback_query.register(opt_2, F.data.casefold() == 'opt_2')

        dp.message.register(bot_geeting, F.text.casefold() == 'привет')
        dp.message.register(bot_farewell, F.text.casefold() == 'пока')

        add_one.bot_add_one(dp)
        dp.message.register(bot_echo)

        asyncio.run(main())

    except KeyboardInterrupt:
        asyncio.run(stop_bot())