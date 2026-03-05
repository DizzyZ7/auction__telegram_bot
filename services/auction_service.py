from datetime import datetime

from sqlalchemy import select
from database.db import SessionLocal
from database.models import Auction, Bid


async def get_auction(auction_id):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Auction).where(Auction.id == auction_id)
        )

        return result.scalar_one_or_none()


async def place_bid(auction_id, user_id, increment):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Auction).where(Auction.id == auction_id)
        )

        auction = result.scalar_one()

        if auction.status != "active":
            return None

        new_price = auction.current_price + increment

        auction.current_price = new_price
        auction.leader_id = user_id

        bid = Bid(
            auction_id=auction_id,
            user_id=user_id,
            amount=new_price,
            time=datetime.utcnow()
        )

        session.add(bid)

        await session.commit()

        return auction
