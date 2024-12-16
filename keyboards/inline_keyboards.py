from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

#  Кнопки для выбора раздела
link_keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton(text='Новости', url='https://dzen.ru/news/'),
                InlineKeyboardButton(text='Музыка', url='https://zaycev.net/'),
                InlineKeyboardButton(text='Видео', url='https://rutube.ru/')]],
                resize_keyboard=True,
                row_width=1)

# Динамическая кнопка
more_button = InlineKeyboardMarkup(inline_keyboard=[[
              InlineKeyboardButton(text='Показать больше', callback_data='show_more')]])


# Кнопки с опциями
option_buttons = InlineKeyboardMarkup(inline_keyboard=[[
                 InlineKeyboardButton(text='Опция 1', callback_data='opt_1'),
                 InlineKeyboardButton(text='Опция 2', callback_data='opt_2')]])