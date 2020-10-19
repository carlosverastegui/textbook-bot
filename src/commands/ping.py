import discord
import time


@discord.bot.command()
async def ping(ctx):
    t_1 = time.perf_counter()

    await ctx.trigger_typing()

    t_2 = time.perf_counter()

    time_delta = round((t_2-t_1)*1000)

    await ctx.send(f"Pong! ``{time_delta}ms``")
