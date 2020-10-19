import discord
from integrations import *


@discord.bot.command()
async def search(ctx, isbn: str):
    """
    item_details_amazon = await amazon(isbn)
    item_details_chegg = await chegg(isbn)

    item_details = item_details_amazon.update(item_details_chegg)

    sorted_items = sorted(item_details.items(), key=lambda x: x["price"], reverse=True)

    print(sorted_items, flush=True)
    """
    pass
