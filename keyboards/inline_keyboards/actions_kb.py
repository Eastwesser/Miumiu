from random import randint

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

random_num_updated_cb_data = "random_num_updated_cb_data"  # модальное окно


class FixedRandomNumberCbData(CallbackData, prefix="fixed-random-num"):
    number: int


def build_actions_kb(random_number_button_text="Random number", ) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=random_number_button_text,
        callback_data=random_num_updated_cb_data,
    )
    cb_data_1 = FixedRandomNumberCbData(number=randint(1, 100))
    builder.button(
        text=f"Random number: {cb_data_1.number}",
        callback_data=cb_data_1.pack(),  # сохраняем информацию в CallbackData методом pack(), сложит все в строчку
    )
    builder.button(
        text="Random number: [HIDDEN]",
        callback_data=FixedRandomNumberCbData(number=randint(1, 100)).pack(),

    )
    builder.adjust(1)  # чтобы перенести кнопки на разные строчки, друг под другом
    return builder.as_markup()
