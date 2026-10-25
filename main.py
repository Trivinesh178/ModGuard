import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import db

load_dotenv()
logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class ModBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        db.init()
        await self.load_extension("cogs.moderation")
        await self.tree.sync()

    async def on_ready(self):
        logging.info("Logged in as %s", self.user)


def main():
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise SystemExit("No token found, check your .env file")
    ModBot().run(token)


if __name__ == "__main__":
    main()
