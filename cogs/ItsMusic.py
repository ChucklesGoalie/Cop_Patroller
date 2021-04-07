import discord
import youtube_dl
from discord.ext import commands, tasks
import random
from random import choice
import time
import functools
import itertools
import math
import asyncio
import time
players = {}
queue = {}
client = commands.Bot

class TheMusique(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vcjoin(self, ctx):
        """Joins a voice channel."""
        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return
        await ctx.send('Joining Voice Chat')
        ctx.voice_state.voice = await destination.connect()
        
    @commands.command()
    async def vcleave(self, ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()
        await ctx.send(f"**Leaving {voice_client}")

    @commands.command()
    async def ytplay(self, ctx, url):
        channel = ctx.message.author.voice.channel
        if client not in channel:
            await client.join_voice_channel(channel)
        else:
            server = ctx.message.server
            voice_client = self.bot.voice_client_in(server)
            player = await voice_client.create.ytdl_player(url)
            players[server.id] = player
            player.start
            await ctx.send(create_embed)

    @commands.command()
    async def vcpause(self, ctx):
        id = ctx.message.server.id
        players[id].pause()
        await ctx.send("Paused!")

    @commands.command()
    async def vcstop(self, ctx):
        id = ctx.message.server.id
        players[id].stop()
        await ctx.send("Stopped!")

    @commands.command()
    async def vcresume(self, ctx):
        id = ctx.message.server.id
        players[id].resume()
        await ctx.send("Resumed!")




    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                                description='```css\n{0.source.title}\n```'.format(self),
                                color=discord.Color.blurple())
                    .add_field(name='Duration', value=self.source.duration)
                    .add_field(name='Requested by', value=self.requester.mention)
                    .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                    .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                    .set_thumbnail(url=self.source.thumbnail))

        return embed


class VoiceError(Exception):
    pass

