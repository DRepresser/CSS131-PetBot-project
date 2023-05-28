import asyncio
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

async def load():
    await client.load_extension('cogs.bot')

async def main():
    await load()
    await client.start(TOKEN)

asyncio.run(main())