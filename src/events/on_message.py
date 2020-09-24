from discord import bot



@bot.event
async def on_message(message):
    print(message, flush=True)
