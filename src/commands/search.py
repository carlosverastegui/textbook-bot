import discord
from integrations import *

amazon = Amazon(None)


@discord.bot.command()
async def search(ctx, isbn: str):
    embed = discord.Embed(title="Textbook Results")

    amazon_data = await amazon.search(isbn)

    if amazon_data:
        title = amazon_data["name"]
        price = amazon_data["price"]
        amazon_url = amazon_data["url"]
        embed.description = f"Textbook name: **{title}**\n\n" \
                            f"1.) Amazon - [${price}]({amazon_url})"

    else:
        embed.description = "No results found. Please double check your ISBN and try again."


    await ctx.send(embed=embed)