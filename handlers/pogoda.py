from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from pyowm import OWM

from utils.utils import user_data
from states.form import FormStatesGroup

pogoda_router = Router()


# @pogoda_router.message(StateFilter(FormStatesGroup.fill_city))
# async def handle_get_city(message: Message, state: FSMContext):
#     city_from_message = message.text
#     await state.update_data(city=city_from_message)
#     state_data = await state.get_data()
#
#     city = state_data['city']
#
#     user_data[message.from_user.id] = {
#         'city': city,
#     }
#     try:
#         city = city_from_message
#         owm = OWM('e74364496265a4f0e55148a40a8f23d6')
#         mgr = owm.weather_manager()
#         observation = mgr.weather_at_place(city)
#         weather = observation.weather
#         humidity = weather.humidity
#         temp = weather.temperature('celsius')
#         wind = weather.wind()
#         await message.answer(
#             f"В городе {city} сейчас\nтемпература составляет🏝: {temp['temp']} °С\nCкорость ветра🌪: {wind['speed']} м/с\n Влажность воздуха {humidity}%\n \nМожете ввести город еще раз")
#
#     except:
#         await message.answer('Вы ввели несуществующий город🌎')


@pogoda_router.message(Command('show_weather'))
async def handle_show_weather(message: Message):
    try:
        city = user_data[message.from_user.id]['city']
        owm = OWM('e74364496265a4f0e55148a40a8f23d6')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        humidity = weather.humidity
        temp = weather.temperature('celsius')
        wind = weather.wind()
        await message.answer(
            f"В городе {city} сейчас\nтемпература составляет🏝: {temp['temp']} °С\nCкорость ветра🌪: {wind['speed']} м/с\n Влажность воздуха {humidity}%\n \nМожете ввести город еще раз")

    except:
        await message.answer('Город не выбран')
