from aiogram import Router, F
from aiogram.types import CallbackQuery

from services.auction_service import place_bid
from keyboards.bid_keyboard import bid_keyboard

router = Router()


@router.callback_query(F.data.startswith("bid"))
async def bid_handler(callback: CallbackQuery):

    _, auction_id, increment = callback.data.split(":")

    auction = await place_bid(
        int(auction_id),
        callback.from_user.id,
        float(increment)
    )

    if not auction:

        await callback.answer("Аукцион закрыт")

        return

    text = f"""
Лот: {auction.title}

Текущая ставка: {auction.current_price}

Лидер: {callback.from_user.username}
"""

    await callback.bot.edit_message_text(
        text=text,
        chat_id=callback.message.chat.id,
        message_id=auction.message_id,
        reply_markup=bid_keyboard(auction.id, auction.step)
    )

    await callback.answer("Ставка принята")
