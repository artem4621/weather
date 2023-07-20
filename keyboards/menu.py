from aiogram.types import BotCommand

main_menu_command = [
    BotCommand(command='/start', description='Перезапустить'),
    BotCommand(command='/city', description='Ввести город'),
    BotCommand(command='/show_city', description='Показать город'),
    BotCommand(command='/show_weather', description='Данные о погоде')
]
