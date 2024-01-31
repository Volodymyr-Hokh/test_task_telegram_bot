from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


location_buttons = [
    [
        InlineKeyboardButton(text="Локація 1", callback_data="location_1"),
        InlineKeyboardButton(text="Локація 2", callback_data="location_2"),
    ],
    [
        InlineKeyboardButton(text="Локація 3", callback_data="location_3"),
        InlineKeyboardButton(text="Локація 4", callback_data="location_4"),
        InlineKeyboardButton(text="Локація 5", callback_data="location_5"),
    ],
]

location_keyboard = InlineKeyboardMarkup(inline_keyboard=location_buttons)


comment_buttons = [
    [InlineKeyboardButton(text="📝 Додати коментар", callback_data="comment")],
    [
        InlineKeyboardButton(text="✅ Все чисто", callback_data="all_clear"),
    ],
]

comment_keyboard = InlineKeyboardMarkup(inline_keyboard=comment_buttons)
