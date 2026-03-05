from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Auction(Base):

    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    topic_id = Column(Integer)

    start_price = Column(Float)

    current_price = Column(Float)

    step = Column(Float)

    end_time = Column(DateTime)

    leader_id = Column(Integer)

    message_id = Column(Integer)

    status = Column(String, default="active")


class Bid(Base):

    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)

    auction_id = Column(Integer)

    user_id = Column(Integer)

    username = Column(String)

    amount = Column(Float)

    time = Column(DateTime)
