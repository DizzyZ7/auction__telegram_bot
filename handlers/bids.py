from aiogram import Router, F
from aiogram.types import CallbackQuery

from services.auction_service import place_bid
from services.bid_history_service import get_last_bids
from keyboards.bid_keyboard import bid_keyboard

router = Router()


@router.callback_query(F.data.startswith("bid"))
async def bid_handler(callback: CallbackQuery):

    try:

        # callback формат
        # bid:auction_id:increment
        parts = callback.data.split(":")

        auction_id = int(parts[1])
        increment = float(parts[2])

        auction = await place_bid(
            callback.bot,
            auction_id,
            callback.from_user,
            increment
        )

        if not auction:

            await callback.answer(
                "Аукцион уже завершён",
                show_alert=True
            )

            return

        # Получаем историю ставок
        bids = await get_last_bids(auction.id)

        history = ""

        if bids:

            history = "\n".join(
                [
                    f"@{b.username} — {b.amount}"
                    for b in bids
                ]
            )

        else:

            history = "Пока нет ставок"

        text = f"""
🏷 {auction.title}

💰 Текущая ставка: {auction.current_price}

👑 Лидер: @{callback.from_user.username}

📊 Последние ставки
{history}
"""

        await callback.bot.edit_message_text(
            text=text,
            chat_id=callback.message.chat.id,
            message_id=auction.message_id,
            reply_markup=bid_keyboard(
                auction.id,
                auction.step
            )
        )

        await callback.answer("Ставка принята")

    except Exception as e:

        await callback.answer(
            "Ошибка ставки",
            show_alert=True
        )

        print("BID ERROR:", e)
