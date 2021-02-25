import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random

class DiscordStreaming(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_member_update(self, ctx, user, Game, url):
        stream_channel = discord.utils.get(user.guilds.channel, name="Streaming")
        stream_role = discord.utils.get(user.guilds.roles, name="Streamer")
        if discord.ActivityType == discord.Streaming:
            await stream_channel.send("{0.user} is streaming {0.Game}! Go check it out at {url}")
        else:
            return