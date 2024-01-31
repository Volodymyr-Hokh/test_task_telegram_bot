from aiogram.dispatcher.filters.state import State, StatesGroup


class CheckList(StatesGroup):
    location = State()
    food_quality = State()
    service = State()
    ambiance = State()
    menu = State()
    cleanliness = State()
    image = State()
    last_callback = State()
    # last_callback для того, щоб приймати тільки ті коментарі, які ввів користувач після натискання на кнопку
