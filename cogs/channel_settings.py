import discord
from discord.ext import commands

class Channel_Changes(commands.Cog):
    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await channel.send("Locked!")
    @commands.command()
    @commands.has_guild_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : discord.TextChannel = None):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await channel.send("Un-Locked!")

    @commands.command()
    async def fucku(self, ctx, *, member : discord.Member=None):
        user = ctx.message.author
        if member == None:
            await ctx.send(f"no, Fuck **YOU** {user.mention}! Don't argue with me")
        if member != None:
            await ctx.send(f"No, Fuck **YOU** {member.mention}! Don't argue with me")
        