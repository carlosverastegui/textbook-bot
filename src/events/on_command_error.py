from discord import bot



@bot.event
async def on_command_error(ctx, error):
    print(error, flush=True)
