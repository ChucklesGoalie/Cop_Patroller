import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random
from random import choice
import youtube_dl
import time
import functools
import itertools
import math
import ffmpeg
from cogs import *

from async_timeout import timeout
from discord.ext import commands

from discord.voice_client import VoiceClient
import os
from sys import platform, exit as shutdown

directory = os.path.dirname(os.path.realpath(__file__))

client = commands.Bot(command_prefix = ".", case_insensitive=True)

async def say_after(delay, what):
    await asyncio.sleep(delay)

async def main():
    print(f'started at {time.strftime(("%a, %#d %B %Y, %I:%M %p ET"))}')

asyncio.run(main())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Cop Patrolling this area'))
    print('The Cop Patroller Bot is running!')
    client.add_cog(Music(client))
    client.add_cog(aroles(client))
    client.add_cog(rroles(client))
    client.add_cog(Welcome(client))
    client.add_cog(Leave(client))
    client.add_cog(AmongUsQueue(client))
    client.add_cog(Helps(client))
    client.add_cog(RocketLeagueQueue(client))
    client.add_cog(Channel_Changes(client))
    client.add_cog(DiscordStreaming(client))

@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)
    print(f'{time.strftime(("[%d/%m/%Y, %I:%M:%S %p ET]"))}', error)

## _____________________________ CODE STARTS HERE _______________________________ ##

@client.command()
@commands.has_guild_permissions(manage_channels=True)
async def send_dm(ctx, member : discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)
    await ctx.message.add_reaction('👌')

@client.command()
@commands.has_guild_permissions(manage_channels=True)
async def send_msg(ctx, channel: discord.TextChannel, *, message):
    await channel.send(message)
    await ctx.message.add_reaction('👌')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!\nbot took around {round(client.latency * 1000)}ms to respond')

@client.command()
async def ping_mention(ctx):
    author = ctx.message.author
    await ctx.send (f'Hey {author.mention}!\nPong!.\n the bot took about {round(client.latency * 1000)}ms to respond to the command')

@client.command()
async def poll(ctx, channel : discord.TextChannel, *, question):  
    if channel is client.get_channel(name="poll-chat"):
        if commands.has_permissions(manage_messages=True):
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(
                colour = discord.Colour.greyple())
         # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Poll: ', value=f'{question}\n✅ = Yes\n❎ = No', inline=False)
            message = await channel.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❎')
        elif commands.has_permissions(manage_messages=False):
            await ctx.channel.purge(limit=1)
            await ctx.send("You don't have Perms")
    elif channel is not client.get_channel(name="poll-chat"):
        await ctx.send(f'sorry, Try when you get Mod or higher. if you are a mod, then make the channel #poll-chat.\n{ctx.message.author.mention}')



@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(
        colour=discord.Colour.darker_grey(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p EST"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p EST"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles ]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command(aliases=['getallwithrole', 'check_role'])
async def role_check(ctx, *, role: discord.Role, member : discord.Member = None):
    members = "".join(f'{member.display_name}\n' for member in role.members)
    # await ctx.send(f'```{members}```')
    embed = discord.Embed(
        colour=discord.Colour.darker_grey(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="Role:", value=f'{role}')
    embed.add_field(name="Members:", value=f'{members}')

    await ctx.send(embed=embed)

#mute command using discord.py
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member, *, reason=None):
    if commands.has_permissions(administrator=True):
        muterole=discord.utils.get(user.guild.roles, name="Muted")
        channel = await user.create_dm()
        await user.add_roles(muterole)
        await ctx.send(f"**{user.mention}** has been muted")
        await channel.send(f"You've been muted because: {reason}")
## <----- Mute command end ----->
## unmute command using discord.py
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, user: discord.Member, *, reason=None):
    if commands.has_permissions(mute_members=True):
        muterole=discord.utils.get(user.guild.roles, name="Muted")
        await user.remove_roles(muterole)
        await ctx.send(f"**{user.mention}** has been unmuted")
## <----- unmute command end ----->
#kick command using discord.py
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    channel = await user.create_dm()
    await user.kick(reason=reason)
    await channel.send(f"You've been kicked because: {reason}")
    await ctx.send(f"{user} has been kicked sucessfully")
    print(f'BOT is still running after the Kick. The Kicked User is {user}')
# <----- kick commmand end ------>
#ban Command using discord.py
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    channel = await user.create_dm()
    await user.ban(reason=reason)
    await channel.send(f"You've been banned because: {reason}")
    await ctx.send(f"{user} has been banned sucessfully")
    print(f'BOT is still running after the Ban. The Banned user is {user}')
# <----- ban commmand end ------>
#clear command
@client.command()
@commands.has_permissions(administrator=True)
async def tclear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f'The {amount} message(s) have been removed.')
# <----- Clear Command End ----->
client.remove_command('help')
client.run('')    
