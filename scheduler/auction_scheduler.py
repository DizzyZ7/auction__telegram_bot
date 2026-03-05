from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

from database.db import SessionLocal
from database.models import Auction
from sqlalchemy import select


scheduler = AsyncIOScheduler()


async def check_auctions():

    async with SessionLocal() as session:

        result = await session.execute(
            select(Auction).where(Auction.status == "active")
        )

        auctions = result.scalars().all()

        now = datetime.utcnow()

        for auction in auctions:

            if auction.end_time < now:

                auction.status = "finished"

        await session.commit()


scheduler.add_job(
    check_auctions,
    "interval",
    seconds=10
)
