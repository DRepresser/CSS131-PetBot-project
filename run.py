import asyncio
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await client.start('MTEwNjYzNzU5MTIyODQ1NzA1MQ.GLqJbD.M-UVt_hbz4HPCTo9QLyDnBCCnGOzxMB875wrSg')

asyncio.run(main())