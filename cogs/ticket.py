import discord
from discord.ext import commands
import json


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        with open("data.json") as f:
            data = json.load(f)

    @commands.command()
    async def startticket(self, ctx, user : discord.Member):
        embed = discord.Embed(
            colour = discord.Colour.red())
    # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='This is the Ticket station,', value='Please click the reaction below to create a ticket', inline=False)
        await ctx.message.add_reaction("📧")
        
