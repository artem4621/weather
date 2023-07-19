import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, state  # Фильтр для /start, /...

from aiogram.types import Message, message  # Тип сообщения
from pyowm import OWM

from aiogram.fsm.context import FSMContext
from config import config  # Config


API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer(
        "Привет!Я бот который умеет показывать погоду. Напиши /weather чтобы посмотреть погоду🌎.")  # Отвечаем на полученное сообщение


@dp.message(Command(commands=['weather']))
async def pogoda_command(message: Message):
    await message.answer('Введите город')
@dp.message(F.text)
async def get_weather(message: Message):
    try:
        city = message.text
        owm = OWM('e74364496265a4f0e55148a40a8f23d6')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temp = weather.temperature('celsius')
        wind = weather.wind()
        await message.answer(f"В городе {city} сейчас  температура составляет🏝: {temp['temp']} °С\n Cкорость ветра🌪: {wind['speed']} м/с")
    except:
            message.answer('Вы ввели несуществующий город🌎')

async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
