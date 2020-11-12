import discord
from integrations import *

amazon = Amazon(None)
chegg = Chegg(None)
pearson = Pearson(None)



@discord.bot.command()
async def search(ctx, isbn: str):
    embed = discord.Embed(title="Textbook Results")

    amazon_data = await amazon.search(isbn) or {}
    pearson_data = await pearson.search(isbn) or {}

    book_title = amazon_data.get("name") or pearson_data.get("name")
    authors = amazon_data.get("authors") or pearson_data.get("authors") or "unknown"

    combined_data = [x for x in (amazon_data, pearson_data) if x]

    if combined_data:
        sorted_prices = sorted(combined_data, key=lambda k: k["price"])
        desc = [f"**{book_title}**", f"_by {authors}_", ""]

        for i, book in enumerate(sorted_prices, 1):
            price = "{:.2f}".format(book["price"])
            desc.append(f"{i}.) {book['integration'].title()} - [${price}]({book.get('url')})")

        embed.description = "\n".join(desc)

    else:
        embed.description = "No results found. Please double check your ISBN and try again."


    await ctx.send(embed=embed)