from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline_keyboards import location_keyboard
from loader import dp


@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привіт!\nПочнімо працювати.", reply_markup=location_keyboard)
