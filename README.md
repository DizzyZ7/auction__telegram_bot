# 🏇 Telegram Auction Bot - DizzyZ7

<p align="center">
  <pre>
     /\_/\  
    ( o.o )   🐱 "My Supervisor"
     > ^ <
  </pre>
</p>

A powerful **Telegram auction bot** designed for closed groups with topics. Users bid via **interactive buttons** instead of messages, keeping the chat clean, automated, and professional.

---

## ✨ Features

- 📂 **Topic-based auctions** – Organizes lots in specific Telegram topics.
- 🖱️ **Button Bidding System** – No more messy text bids; one click to raise.
- 📜 **Automatic Bid History** – Real-time updates of the last 3–5 bidders.
- 🔔 **Outbid Notifications** – Instant alerts to users when they are no longer leading.
- 🛡️ **Anti-Sniper System** – Automatically extends the auction if a bid is placed in the last seconds.
- 🤖 **Automatic Closing** – Auction ends exactly on time with a winner announcement.
- 🖥️ **Admin Web Panel** – Manage lots and view stats via a FastAPI dashboard.
- 🗄️ **SQLite + SQLAlchemy** – Robust and lightweight data management.

---

## 🧠 Architecture & Tech Stack

- **Language:** Python 3.10+
- **Framework:** [aiogram 3.x](https://github.com/aiogram/aiogram) (Telegram Bot API)
- **Database:** SQLite with SQLAlchemy (ORM)
- **Scheduler:** APScheduler (for auction timers)
- **Web Interface:** FastAPI + Uvicorn (Admin Panel)

---

## 📂 Project Structure

```text
auction_bot/
├── bot.py                # Main entry point for the bot
├── config.py             # Environment variables & configuration
├── admin_panel.py        # FastAPI admin dashboard
├── requirements.txt      # Project dependencies
├── database/
│   ├── db.py             # Engine & Session setup
│   └── models.py         # SQLAlchemy models (Lot, Bid, User)
├── handlers/
│   ├── admin.py          # Admin commands & logic
│   └── bids.py           # Bidding logic & button interactions
├── services/
│   ├── auction_service.py      # Core auction business logic
│   └── bid_history_service.py  # History formatting & tracking
├── keyboards/
│   └── bid_keyboard.py   # Dynamic inline buttons for bidding
└── scheduler/
    └── auction_scheduler.py # Time-based events (closing, extensions)
