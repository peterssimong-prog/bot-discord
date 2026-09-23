import discord
from discord.ext import commands
from bot_logic import gen_emoji, gen_pass, flip_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, longitud):
    longitud = int(longitud)
    await ctx.send("tu nueva contraseña es: "+ gen_pass(longitud))

@bot.command()
async def emoji(ctx):
    await ctx.send("un emoji aleatorio es: "+ gen_emoji())

@bot.command()
async def coin(ctx):
    await ctx.send("salio: "+ flip_coin())


bot.run("MTU0OTU2MzM2OTc1OTk3MzQyNg.Gi5eWK.xJ1F0t-ASLYfERFnFx0th8euMR85T4cngQC73g")