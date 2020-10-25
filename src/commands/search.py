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


    """
    embed = discord.Embed(title="Textbook Results")

    embed.description = "Textbook name: **test**\n\n" \
                        "1.) Amazon - $10\nLink: [click here](https://google.com)\n\n" \
                        "2.) Chegg - $15\nLink: [click here](https://google.com)\n\n" \
                        "3.) Pearson - $20\nLink: [click here](https://google.com)"

    await ctx.send(embed=embed)

    failed_embed = discord.Embed(title="Textbook Results")
    failed_embed.description = "No results found. Please double-check your ISBN and try again."
    await ctx.send(embed=failed_embed)
    """

    pass