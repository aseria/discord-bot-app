from discord.ext import commands
import random

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@bot.command()
async def pick(ctx, *args):
    picked = random.choice(args)
    await ctx.send(picked)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


bot.run('')