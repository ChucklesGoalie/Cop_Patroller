import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random

banned_roles = [
    "Superintendent",
    "Staff Inspector"
]

class aroles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


    @commands.command()
    async def arole(self, ctx, *, role : discord.Role):
        user = ctx.message.author
        await user.add_roles(role)
        await ctx.send(f"{user.mention} now has {role}")     

class rroles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def rrole(self, ctx, *, role : discord.Role):
        user = ctx.message.author
        await user.remove_roles(role)
        await ctx.send(f"{role} has been removed from {user.mention}")
