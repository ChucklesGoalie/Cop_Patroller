import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random


class aroles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def aroleMinecraft_Player(self, ctx, user : discord.Member):
        MCrole = discord.utils.get(user.guild.roles, name="Minecraft Player")
        await user.add_roles(MCrole)
        await ctx.send(f"{user} now has {MCrole}")

    @commands.command()
    async def aroleRocketLeague_Player(self, ctx, user : discord.Member):
        RLrole = discord.utils.get(user.guild.roles, name="Rocket League Player")
        await user.add_roles(RLrole)
        await ctx.send(f"{user} now has {RLrole}")
    
    @commands.command()
    async def aroleAmongUs_Player(self, ctx, user : discord.Member):
        AUrole = discord.utils.get(user.guild.roles, name="Among Us Player")
        await user.add_roles(AUrole)
        await ctx.send(f"{user} now has {AUrole}")

    @commands.command()
    async def aroleWarThunder_Player(self, ctx, user : discord.Member):
        JSrole = discord.utils.get(user.guild.roles, name="Jon Squad")
        await user.add_roles(JSrole)
        await ctx.send(f'{user} now has {JSrole} / War Thunder')

    @commands.command()
    async def aroleBrawlhalla_Player(self, ctx, user : discord.Member):
        BHrole = discord.utils.get(user.guild.roles, name="Brawlhalla Player")
        await user.add_roles(BHrole)
        await ctx.send(f"{user} now has {BHrole}")

    @commands.command()
    async def aroleGTA_Player(self, ctx, user :discord.Member):
        GTArole = discord.utils.get(user.guild.roles, name="GTA Player")
        await user.add_roles(GTArole)
        await ctx.send(f"{user} now has {GTArole}")

class rroles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def rroleMinecraft_Player(self, ctx, user :discord.Member):
        MCrole = discord.utils.get(user.guild.roles, name="Minecraft Player")
        await user.remove_roles(MCrole)
        await ctx.send(f"{MCrole} has been removed from {user}")

    @commands.command()
    async def rroleAmongUs_Player(self, ctx, user : discord.Member):
        AUrole = discord.utils.get(user.guild.roles, name="Among Us Player")
        await user.remove_roles(AUrole)
        await ctx.send(f"{AUrole} has been removed from {user}")

    @commands.command()
    async def rroleWarThunder_Player(self, ctx, user : discord.Member):
        JSrole = discord.utils.get(user.guild.roles, name="Jon Squad")
        await user.remove_roles(JSrole)
        await ctx.send(f"{JSrole} has been removed from {user}")

    @commands.command()
    async def rroleBrawlhalla_Player(self, ctx, user : discord.Member):
        BHrole = discord.utils.get(user.guild.roles, name="Minecraft Player")
        await user.remove_roles(BHrole)
        await ctx.send(f"{BHrole} has been removed from {user}")

    @commands.command()
    async def rroleRocketleague_Player(self, ctx, user : discord.Member):
        RLrole = discord.utils.get(user.guild.roles, name="Rocket League Player")
        await user.remove_roles(RLrole)
        await ctx.send(f"{RLrole} has been removed from {user}")

    @commands.command()
    async def rroleGTA_Player(self, ctx, user : discord.Member):
        GTArole = discord.utils.get(user.guild.roles, name="GTA Player")
        await user.remove_roles(GTArole)
        await ctx.send(f"{GTArole} has been removed from {user}")