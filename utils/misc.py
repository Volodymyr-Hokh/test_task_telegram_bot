from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext

from loader import bot


async def get_last_callback(state: FSMContext):
    async with state.proxy() as data:
        last_callback = data.get("last_callback")
    return last_callback
