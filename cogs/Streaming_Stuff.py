import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random

member = discord.Member
act = member.activity
acts = member.activities

class DiscordStreaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # @commands.Cog.listener()
    # async def on_member_update(self, ctx, user, Game, url):
    #     stream_channel = discord.utils.get(user.guilds.channel, name="Streaming")
    #     stream_role = discord.utils.get(user.guilds.roles, name="Streamer")
    #     if discord.ActivityType == discord.Streaming:
    #         await stream_channel.send("{0.user} is streaming {0.Game}! Go check it out at {url}")
    #     else:
    #         return

    @commands.Cog.listener()
    async def on_member_update(self, ctx):
        for act in acts:
            if isinstance(self, act, discord.Streaming):
                Game = discord.Member.Game
                url = act.url
                stream_channel = discord.utils.get(member.guild.channel, name="Streaming")
                stream_role = discord.utils.get(member.guild.role, name="Streamer")
                await stream_channel.send(f"Hello {stream_role}, {member} is streaming {Game}! Come stop by at {url}")
                