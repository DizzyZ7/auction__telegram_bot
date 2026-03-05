from datetime import datetime, timedelta

from sqlalchemy import select
from database.db import SessionLocal
from database.models import Auction, Bid
from config import ANTI_SNIPER_SECONDS


async def get_auction(auction_id):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Auction).where(Auction.id == auction_id)
        )

        return result.scalar_one_or_none()


async def place_bid(bot, auction_id, user, increment):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Auction).where(Auction.id == auction_id)
        )

        auction = result.scalar_one_or_none()

        if not auction:
            return None

        # Проверка статуса
        if auction.status != "active":
            return None

        # Проверка окончания
        if auction.end_time and auction.end_time < datetime.utcnow():

            auction.status = "finished"
            await session.commit()

            return None

        # Проверка шага ставки
        if increment < auction.step:
            return None

        old_leader = auction.leader_id

        new_price = auction.current_price + increment

        auction.current_price = new_price
        auction.leader_id = user.id

        # Антиснайпер
        if auction.end_time:

            seconds_left = (auction.end_time - datetime.utcnow()).total_seconds()

            if seconds_left < ANTI_SNIPER_SECONDS:

                auction.end_time = datetime.utcnow() + timedelta(
                    seconds=ANTI_SNIPER_SECONDS
                )

        # Сохраняем ставку
        bid = Bid(
            auction_id=auction.id,
            user_id=user.id,
            username=user.username,
            amount=new_price,
            time=datetime.utcnow()
        )

        session.add(bid)

        await session.commit()

        # Уведомление перебитому игроку
        if old_leader and old_leader != user.id:

            try:

                await bot.send_message(
                    old_leader,
                    f"""
⚠️ Вашу ставку перебили!

🏷 Лот: {auction.title}

💰 Новая ставка: {new_price}

Попробуйте сделать новую ставку!
"""
                )

            except Exception:
                pass

        return auction
