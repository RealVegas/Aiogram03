from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки по команде starSt
start_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Привет'), KeyboardButton(text='Пока')]], resize_keyboard=True)