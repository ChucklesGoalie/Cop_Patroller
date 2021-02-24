import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random

class Poll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.member = discord.Member

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, channel : discord.TextChannel, *, question):
        channel = discord.TextChannel
        if commands.has_permissions(manage_messages=True):
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(
                colour = discord.Colour.purple())
         # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Poll: ', value=f'{question}\n✅ = Yes\n❎ = No', inline=False)
            message = await channel.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        elif commands.has_permissions(manage_messages=False):
            await ctx.channel.purge(limit=1)
            await ctx.send("You don't have Perms")


