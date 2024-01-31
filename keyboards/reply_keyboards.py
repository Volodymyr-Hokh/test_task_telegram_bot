from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

photo_upload_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Пропустити")],
    ],
    resize_keyboard=True,
)
