import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        server = self.bot.get_server(id)
        channel = self.bot.get_channel(id)
        await channel.send(f"Welcome {member.mention}! Enjoy your stay at {server}")

class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_leave(self, member):
        server = self.bot.get_server(id)
        channel = self.bot.get_channel(id)
        await channel.send(f"Goodbye {member}! I hope you enjoyed your stay at {server}")