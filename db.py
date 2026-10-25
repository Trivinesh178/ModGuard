import sqlite3
import time
from contextlib import closing

DB_PATH = "modbot.db"


def _conn():
    return sqlite3.connect(DB_PATH)


def init():
    with closing(_conn()) as conn, conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS strikes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guild_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                reason TEXT NOT NULL,
                created_at INTEGER NOT NULL
            )"""
        )


def add_strike(guild_id, user_id, reason):
    with closing(_conn()) as conn, conn:
        conn.execute(
            "INSERT INTO strikes (guild_id, user_id, reason, created_at) VALUES (?, ?, ?, ?)",
            (guild_id, user_id, reason, int(time.time())),
        )
        row = conn.execute(
            "SELECT COUNT(*) FROM strikes WHERE guild_id=? AND user_id=?",
            (guild_id, user_id),
        ).fetchone()
    return row[0]  # total strikes so far


def get_strikes(guild_id, user_id):
    with closing(_conn()) as conn:
        return conn.execute(
            "SELECT reason, created_at FROM strikes WHERE guild_id=? AND user_id=? ORDER BY id DESC",
            (guild_id, user_id),
        ).fetchall()


def clear_strikes(guild_id, user_id):
    with closing(_conn()) as conn, conn:
        conn.execute(
            "DELETE FROM strikes WHERE guild_id=? AND user_id=?", (guild_id, user_id)
        )
