import discord
from discord.ext import commands, tasks
import os
import json

class rankup(commands.Bot):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener
    async def on_member_join(self, member : discord.Member):
            channel = commands.Bot.get_channel(id=722631384388075550)
            await channel.send(f"Hello {member.mention} and welcome to **Cop Patroller!** In the server, we have a minecraft category, an among us category, and a war thunder category. If you want to be added let an Inspector or CopCanada know so we can give you the role"),

    @commands.Cog.listener
    async def on_member_remove(self, member : discord.Member):
        channel = commands.Bot.get_channel(id=722631384388075550)
        await channel.send(f"We are sad to see you leave, please 10-8, 10-42! on your way out {member}")

    @commands.Cog.listener
    async def on_message(self, message):
        with open('users.json', 'r') as f:
            users = json.load(f)

    async def update_data(self, users, user, message):
        if not user.id in users:
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1

        with open('users.json', 'w') as f:
            json.dump(users, f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message.channel)

    async def level_up(self, ctx, users, user, channel):
        experience = users[user.id]['experience']
        lvl_start = users[user.id]['level']
        lvl_end = int(experience ** (1/4))

        if lvl_start < lvl_end:
            await ctx.send_message(channel, '{} has leveled up to level {}' .format(user.mention, lvl_end))
            users[user.id]['level'] = lvl_end
        
    async def add_experience(self, users, user, exp):
        users[user.id]['experience'] = exp
