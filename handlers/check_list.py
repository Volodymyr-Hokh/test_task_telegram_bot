from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from keyboards.inline_keyboards import comment_keyboard, location_keyboard
from keyboards.reply_keyboards import photo_upload_keyboard
from loader import dp
from database.repository import add_report
from openai_client import get_report
from states.check_list import CheckList
from utils.misc import get_last_callback


##############################СТАРТ ДІАЛОГУ##############################
@dp.callback_query_handler(filters.Regexp("location_"))
async def handle_location_callback(query: types.CallbackQuery, state: FSMContext):
    location = query.data
    async with state.proxy() as data:
        data["location"] = location
    await query.message.reply(
        "Чудово! Прокоментуйте, будь ласка, якість їжі.", reply_markup=comment_keyboard
    )
    await query.answer()
    await CheckList.food_quality.set()


##############################ОБРОБКА ЯКОСТІ ЇЖІ##############################
@dp.callback_query_handler(filters.Regexp("all_clear"), state=CheckList.food_quality)
async def process_clean_food_quality(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["food_quality"] = None
        data["last_callback"] = query.data
    await query.message.reply(
        "Супер! Тепер поділіться враженнями стосовно обслуговування у нашому закладі.",
        reply_markup=comment_keyboard,
    )
    await CheckList.service.set()
    await query.answer()


@dp.callback_query_handler(filters.Regexp("comment"), state=CheckList.food_quality)
async def process_comment_food_quality(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["last_callback"] = query.data
    await query.message.reply("Введіть коментар.")
    await query.answer()


@dp.message_handler(state=CheckList.food_quality, content_types=types.ContentTypes.TEXT)
async def load_food_quality(message: types.Message, state: FSMContext):
    last_callback = await get_last_callback(state)
    if last_callback == "comment":
        async with state.proxy() as data:
            data["food_quality"] = message.text
            data["last_callback"] = None
        await message.reply(
            "Супер! Тепер поділіться враженнями стосовно обслуговування у нашому закладі.",
            reply_markup=comment_keyboard,
        )
        await CheckList.service.set()
    else:
        await message.reply(
            "Для введення коментаря, будь ласка, натисніть 'Додати коментар'.",
            reply_markup=comment_keyboard,
        )


##############################ОБРОБКА ЯКОСТІ ОБСЛУГОВУВАННЯ##############################
@dp.callback_query_handler(filters.Regexp("all_clear"), state=CheckList.service)
async def process_clean_service(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["service"] = None
        data["last_callback"] = query.data
    await query.message.reply(
        "Чудово! Оцініть, будь ласка, атмосферу нашого закладу.",
        reply_markup=comment_keyboard,
    )
    await CheckList.ambiance.set()
    await query.answer()


@dp.callback_query_handler(filters.Regexp("comment"), state=CheckList.service)
async def process_comment_service(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["last_callback"] = query.data
    await query.message.reply("Введіть коментар.")
    await query.answer()


@dp.message_handler(state=CheckList.service, content_types=types.ContentTypes.TEXT)
async def load_service(message: types.Message, state: FSMContext):
    last_callback = await get_last_callback(state)
    if last_callback == "comment":
        async with state.proxy() as data:
            data["service"] = message.text
            data["last_callback"] = None
        await message.reply(
            "Чудово! Оцініть, будь ласка, атмосферу нашого закладу.",
            reply_markup=comment_keyboard,
        )
        await CheckList.ambiance.set()
    else:
        await message.reply(
            "Для введення коментаря, будь ласка, натисніть 'Додати коментар'.",
            reply_markup=comment_keyboard,
        )


##############################ОБРОБКА АТМОСФЕРИ У ЗАКЛАДІ##############################
@dp.callback_query_handler(filters.Regexp("all_clear"), state=CheckList.ambiance)
async def process_clean_ambiance(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["ambiance"] = None
        data["last_callback"] = query.data
    await query.message.reply(
        "Чудово! Напишіть, будь ласка, як Ви оцінюєте наше меню.",
        reply_markup=comment_keyboard,
    )
    await CheckList.menu.set()
    await query.answer()


@dp.callback_query_handler(filters.Regexp("comment"), state=CheckList.ambiance)
async def process_comment_ambiance(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["last_callback"] = query.data
    await query.message.reply("Введіть коментар.")
    await query.answer()


@dp.message_handler(state=CheckList.ambiance, content_types=types.ContentTypes.TEXT)
async def load_ambiance(message: types.Message, state: FSMContext):
    last_callback = await get_last_callback(state)
    if last_callback == "comment":
        async with state.proxy() as data:
            data["ambiance"] = message.text
            data["last_callback"] = None
        await message.reply(
            "Чудово! Напишіть, будь ласка, як Ви оцінюєте наше меню.",
            reply_markup=comment_keyboard,
        )
        await CheckList.menu.set()
    else:
        await message.reply(
            "Для введення коментаря, будь ласка, натисніть 'Додати коментар'.",
            reply_markup=comment_keyboard,
        )


##############################ОБРОБКА МЕНЮ##############################
@dp.callback_query_handler(filters.Regexp("all_clear"), state=CheckList.menu)
async def process_clean_menu(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["menu"] = None
        data["last_callback"] = query.data
    await query.message.reply(
        "Прокоментуйте, будь ласка, наскільки Ви задоволені чистотою у нашому закладі.",
        reply_markup=comment_keyboard,
    )
    await CheckList.cleanliness.set()
    await query.answer()


@dp.callback_query_handler(filters.Regexp("comment"), state=CheckList.menu)
async def process_comment_menu(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["last_callback"] = query.data
    await query.message.reply("Введіть коментар.")
    await query.answer()


@dp.message_handler(state=CheckList.menu, content_types=types.ContentTypes.TEXT)
async def load_menu(message: types.Message, state: FSMContext):
    last_callback = await get_last_callback(state)
    if last_callback == "comment":
        async with state.proxy() as data:
            data["menu"] = message.text
            data["last_callback"] = None
        await message.reply(
            "Прокоментуйте, будь ласка, наскільки Ви задоволені чистотою у нашому закладі.",
            reply_markup=comment_keyboard,
        )
        await CheckList.cleanliness.set()
    else:
        await message.reply(
            "Для введення коментаря, будь ласка, натисніть 'Додати коментар'.",
            reply_markup=comment_keyboard,
        )


##############################ОБРОБКА П'ЯТОЇ ОПЦІЇ##############################
@dp.callback_query_handler(filters.Regexp("all_clear"), state=CheckList.cleanliness)
async def process_clean_cleanliness(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["cleanliness"] = None
        data["last_callback"] = query.data
    await query.message.reply(
        "Чудово! Тепер відправте фото. Натисніть 'Пропустити', якщо не бажаєте додавати зображення.",
        reply_markup=photo_upload_keyboard,
    )
    await CheckList.image.set()
    await query.answer()


@dp.callback_query_handler(filters.Regexp("comment"), state=CheckList.cleanliness)
async def process_comment_cleanliness(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["last_callback"] = query.data
    await query.message.reply("Введіть коментар.")
    await query.answer()


@dp.message_handler(state=CheckList.cleanliness, content_types=types.ContentTypes.TEXT)
async def load_cleanliness(message: types.Message, state: FSMContext):
    last_callback = await get_last_callback(state)
    if last_callback == "comment":
        async with state.proxy() as data:
            data["cleanliness"] = message.text
            data["last_callback"] = None
        await message.reply(
            "Чудово! Тепер відправте фото. Натисніть 'Пропустити', якщо не бажаєте додавати зображення.",
            reply_markup=photo_upload_keyboard,
        )
        await CheckList.image.set()
    else:
        await message.reply(
            "Для введення коментаря, будь ласка, натисніть 'Додати коментар'.",
            reply_markup=comment_keyboard,
        )


##############################ОБРОБКА ФОТО##############################
@dp.message_handler(state=CheckList.image, content_types=types.ContentTypes.PHOTO)
async def load_image(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["image"] = message.photo[-1].file_id
        await message.reply(
            "Дякую! Ваш чек-лист збережено.\nФормується звіт. Будь ласка, зачекайте.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        report = await get_report(data)
        await message.reply(report.get("report"))
        await message.answer("Також користувач додав до звіту фото:")
        await message.answer_photo(photo=data.get("image"))
        data.pop("last_callback")
        add_report(telegram_id=message.from_user.id, **data, **report)
    await state.finish()
    await state.reset_state()
    await message.answer(
        "Якщо бажаєте залишити ще один відгук, оберіть локацію.",
        reply_markup=location_keyboard,
    )


@dp.message_handler(state=CheckList.image, content_types=types.ContentTypes.ANY)
async def invalid_input_image(message: types.Message, state: FSMContext):
    if message.text == "Пропустити":
        await message.reply(
            "Дякую! Ваш чек-лист збережено.\nФормується звіт. Будь ласка, зачекайте.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        async with state.proxy() as data:
            data["image"] = None
            report = await get_report(data)
            await message.reply(report.get("report"))
            data.pop("last_callback")
            add_report(telegram_id=message.from_user.id, **data, **report)
        await state.finish()
        await state.reset_state()
        await message.answer(
            "Якщо бажаєте залишити ще один відгук, оберіть локацію.",
            reply_markup=location_keyboard,
        )
    else:
        await message.reply("Ви можете відправляти тільки фото.")


##############################ОБРОБКА НЕПРАВИЛЬНОГО КОНТЕНТ ТИПУ##############################
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def invalid_input_options(message: types.Message):
    await message.reply("Ви можете вводити тільки текст.")
