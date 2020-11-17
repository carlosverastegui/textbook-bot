import discord
from integrations import *

amazon = Amazon()
chegg = Chegg()
pearson = Pearson()



@discord.bot.command()
async def search(ctx, isbn: str):
    channel = ctx.channel
    embed = discord.Embed(title="Textbook Results")

    async with channel.typing():
        amazon_data = await amazon.search(isbn) or {}
        pearson_data = await pearson.search(isbn) or {}
        chegg_data = await chegg.search(isbn) or {}

        book_title = amazon_data.get("name") or pearson_data.get("name") or chegg_data.get("name")
        authors = amazon_data.get("authors") or pearson_data.get("authors") or chegg_data.get("authors") or "unknown"

        combined_data = [x for x in (amazon_data, pearson_data, chegg_data) if x]

        if combined_data:
            sorted_prices = sorted(combined_data, key=lambda k: k["price"])
            desc = [f"**{book_title}**", f"_by {authors}_", ""]
            i = 1

            for book in sorted_prices:
                if book["price"]:
                    price = "{:.2f}".format(book["price"])
                    desc.append(f"{i}.) {book['integration'].title()} - [${price}]({book.get('url')})")
                    i += 1

            embed.description = "\n".join(desc)
        else:
            embed.description = "No results found. Please double check your ISBN and try again."


        await ctx.send(embed=embed)
