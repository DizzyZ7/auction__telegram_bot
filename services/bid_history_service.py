from sqlalchemy import select, desc
from database.db import SessionLocal
from database.models import Bid


async def get_last_bids(auction_id, limit=5):

    async with SessionLocal() as session:

        result = await session.execute(
            select(Bid)
            .where(Bid.auction_id == auction_id)
            .order_by(desc(Bid.time))
            .limit(limit)
        )

        return result.scalars().all()
