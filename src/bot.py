import discord
import asyncio
import logging
import config
from importlib import import_module
from os import environ
from utils import get_files


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



async def main():
    for directory in config.MODULE_DIR:
        files = get_files(f"src/{directory}")

        for file_name in [f.replace(".py", "") for f in files]:
            import_module(f"{directory}/{file_name}".replace("/", "."))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    token = environ.get("TOKEN") or getattr(config, "TOKEN")

    bot = discord.AutoShardedClient()
    discord.bot = bot

    loop.create_task(main())

    bot.run(token)
