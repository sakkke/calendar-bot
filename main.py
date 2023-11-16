import discord
import os
from dotenv import load_dotenv

from datetime import datetime
from calendar import month

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.slash_command(name = "calendar", description = "Print this month's calendar")
async def calendar(ctx):
    now = datetime.now()
    text = month(now.year, now.month)
    await ctx.respond(f'```{text}\n```')

bot.run(os.getenv('TOKEN'))
