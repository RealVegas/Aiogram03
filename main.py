import asyncio
from aiogram import Bot, F
from aiogram.filters import Command, or_f

from loader import bot, dp, logger

from handlers import bot_echo, bot_help, bot_start
from handlers import add_one


# Удаление меню
async def clear_commands(robot: Bot) -> None:
    await robot.set_my_commands([])
    await clear_commands(robot)


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

        add_one.bot_add_one(dp)
        dp.message.register(bot_echo)

        asyncio.run(main())

    except KeyboardInterrupt:
        asyncio.run(stop_bot())