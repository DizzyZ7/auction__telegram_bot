from aiogram import Router
from aiogram.types import Message
from datetime import datetime, timedelta

from config import ADMIN_IDS, GROUP_ID
from database.db import SessionLocal
from database.models import Auction
from keyboards.bid_keyboard import bid_keyboard

router = Router()


@router.message(lambda m: m.text.startswith("/create_lot"))
async def create_lot(message: Message):

    if message.from_user.id not in ADMIN_IDS:
        return

    parts = message.text.split("|")

    title = parts[1]

    start_price = float(parts[2])

    step = float(parts[3])

    minutes = int(parts[4])

    end_time = datetime.utcnow() + timedelta(minutes=minutes)

    topic = await message.bot.create_forum_topic(
        chat_id=GROUP_ID,
        name=title
    )

    text = f"""
Лот: {title}

Старт: {start_price}
Шаг: {step}

Текущая ставка: {start_price}
"""

    msg = await message.bot.send_message(
        chat_id=GROUP_ID,
        message_thread_id=topic.message_thread_id,
        text=text,
        reply_markup=bid_keyboard(0, step)
    )

    async with SessionLocal() as session:

        auction = Auction(
            title=title,
            topic_id=topic.message_thread_id,
            start_price=start_price,
            current_price=start_price,
            step=step,
            end_time=end_time,
            message_id=msg.message_id
        )

        session.add(auction)

        await session.commit()
