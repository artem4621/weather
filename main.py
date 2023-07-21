import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import config  # Config
from handlers import common, pogoda
from keyboards.menu import main_menu_command

API_TOKEN = config.token


def register_all_routers(dp: Dispatcher):
    dp.include_router(common.common_router)
    dp.include_router(pogoda.pogoda_router)


async def main():
    bot = Bot(token=config.token, parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())  # Менеджер бота

    register_all_routers(dp)

    try:
        print('Bot Started')
        await bot.set_my_commands(main_menu_command)
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
