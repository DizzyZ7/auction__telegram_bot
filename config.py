import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

GROUP_ID = int(os.getenv("GROUP_ID"))

ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS").split(",")))

DATABASE_URL = "sqlite+aiosqlite:///auction.db"

ANTI_SNIPER_SECONDS = 60
