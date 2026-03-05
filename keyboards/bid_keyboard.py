from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def bid_keyboard(auction_id, step):

    kb = InlineKeyboardBuilder()

    kb.button(
        text=f"+{step}",
        callback_data=f"bid:{auction_id}:{step}"
    )

    kb.button(
        text=f"+{step*5}",
        callback_data=f"bid:{auction_id}:{step*5}"
    )

    kb.button(
        text=f"+{step*10}",
        callback_data=f"bid:{auction_id}:{step*10}"
    )

    kb.adjust(3)

    return kb.as_markup()
