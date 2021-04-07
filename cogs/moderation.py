import discord
from discord.ext import commands

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = bot

    #mute command using discord.py
    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def mute(self, ctx, user: discord.Member, *, reason=None):
        if commands.has_permissions(administrator=True):
            muterole=discord.utils.get(user.guild.roles, name="Muted")
            channel = await user.create_dm()
            await user.edit(mute=True)
            await user.add_roles(muterole)
            await ctx.send(f"**{user.mention}** has been muted")
            if reason == None:
                await channel.send("You've been Muted.")
            if reason != None:
                await channel.send(f"You've been muted because: {reason}")
    ## <----- Mute command end ----->
    ## unmute command using discord.py
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, user: discord.Member, *, reason=None):
        if commands.has_permissions(mute_members=True):
            muterole=discord.utils.get(user.guild.roles, name="Muted")
            await user.edit(mute=False)
            await user.remove_roles(muterole)
            await ctx.send(f"**{user.mention}** has been unmuted")
    ## <----- unmute command end ----->
    #kick command using discord.py
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        channel = await user.create_dm()
        await user.kick(reason=reason)
        await channel.send(f"You've been kicked because: {reason}")
        await ctx.send(f"{user} has been kicked sucessfully")
        print(f'BOT is still running after the Kick. The Kicked User is {user}')
    # <----- kick commmand end ------>
    #ban Command using discord.py
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        channel = await user.create_dm()
        await user.ban(reason=reason)
        await channel.send(f"You've been banned because: {reason}")
        await ctx.send(f"{user} has been banned sucessfully")
        print(f'BOT is still running after the Ban. The Banned user is {user}')
    # <----- ban commmand end ------>
    #clear command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def tclear(self, ctx, amount=2):
        amount = amount + 2
        await ctx.channel.purge(limit=amount)
        amount = amount - 2
        await ctx.channel.send(f'The {amount} message(s) have been removed.')
    # <----- Clear Command End ----->
