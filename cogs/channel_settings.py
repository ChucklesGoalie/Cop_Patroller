import discord
from discord.ext import commands

class Channel_Changes(commands.Cog):
    @commands.command()
    async def lock(self, ctx, channel : discord.TextChannel):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await channel.send("Locked!")
    @commands.command()
    async def unlock(self, ctx, channel : discord.TextChannel):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await channel.send("Un-Locked!")