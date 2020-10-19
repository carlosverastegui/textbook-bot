from discord import bot



@bot.event
async def on_error(event, *args, **kwargs):
    print(event, args, kwargs, flush=True)
