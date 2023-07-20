from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.utils import user_data
from states.form import FormStatesGroup

common_router = Router()


@common_router.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer(
        "Привет!Я бот который умеет показывать погоду. Напиши /city чтобы ввести город и посмотреть погоду.")


@common_router.message(Command(commands=['city']))
async def enter_city(message: Message, state: FSMContext):
    await message.answer('Введите город')
    await state.set_state(FormStatesGroup.fill_city)


@common_router.message(FormStatesGroup.fill_city)
async def enter_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()
    city = data['city']
    user_data[message.from_user.id] = {
        'city': city
    }
    await state.clear()
    await message.answer(f'Ваш город: {user_data[message.from_user.id]["city"]}')


@common_router.message(Command(commands=['show_city']))
async def show_city(message: Message):
    city = user_data[message.from_user.id]["city"]
    await message.answer(f'Ваш город: {city}')
