import discord
from discord.ext import commands
import random
from random import choice
import time
import functools
import itertools
import math

class RocketLeagueQueue(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.RLQqueue = []
        self.Queue_Size = 0
        self.Max_Queue_Size = 6
        self.qtoggle = True

    # def create_queue(ctx, queue):
    #     squeue = ''.join(str(e) for e in queue)
    #     embed = discord.Embed(
    #     colour = discord.Colour.red())
    # # embed.add_field(name=' ', value=' ', inline=False)
    #     embed.add_field(name='Among Us Queue: ', value=f'{squeue}', inline=False)
    #     await ctx.send("The queue has filled, Please hop in a voice channel and play Among us!\n", embed=embed)

    @commands.command(pass_context=True)
    async def RLQ(self, ctx):
        ''' Add yourself to the queue!'''
        author = ctx.message.author
        if self.qtoggle == False:
            return

        if author.mention not in self.RLQqueue:
            self.Queue_Size = self.Queue_Size + 1
            await ctx.send('you have been added to the queue.')

            if self.Queue_Size > self.Max_Queue_Size:
               self.Queue_Size = self.Queue_Size - 1
               return
            else:
                self.RLQqueue.append(author.mention)
                embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
                embed.add_field(name='Rocket League Queue: ', value=f'{self.RLQqueue}', inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.send('you are already in the queue!')
            
        if self.Queue_Size == self.Max_Queue_Size:
            embed = discord.Embed(
            colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value=f'{self.RLQqueue}', inline=False)
            await ctx.send(f"{self.RLQqueue}")
            self.RLQqueue = []
            self.Queue_Size = 0
            self.room_name = self._generate_name_pass()
            self.room_pass = self._generate_name_pass()
            await ctx.send(f"The queue has filled, Please hop in a voice channel and play Rocket League! Please look at new channel for info")
            await self.create_channels(ctx)

    @commands.command(name='RLQLeave', pass_context=True)
    async def RLQremove(self, ctx):
        ''' Remove yourself from the queue'''
        author = ctx.message.author
        
        if author.mention in self.RLQqueue:
            self.RLQqueue.remove(author.mention)
            await ctx.send(f'you have been removed from the queue.\n')
            self.Queue_Size = self.Queue_Size - 1
            embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Rocket League Queue: ', value=f'{self.RLQqueue}', inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send('you were not in the queue.')
        ctx.send(embed=embed)

    @commands.command(name='CQ', pass_context=True)
    async def _RLQqueue(self, ctx):
        ''' See who's up next!'''
        embed = discord.Embed(
            colour = discord.Colour.red())
         # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='Rocket League Queue: ', value=f'{self.RLQqueue}', inline=False)
        message = embed
        await ctx.send(embed=message)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def RLQclear(self, ctx):
        ''' Clears the queue'''
        self.RLQqueue = []
        self.Queue_Size = 0
        await ctx.send('Queue has been cleared')

    @commands.command(aliases=["RL_CQS", "RL_QS"])
    async def Check_Queue_Size_RL(self, ctx):
        await ctx.send(f"Queue size is {self.Queue_Size}\nMax Queue size is {self.Max_Queue_Size}")

    @commands.command()
    async def RLQStart(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.red())
    # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='Rocket League Queue: ', value=f'{self.RLQqueue}', inline=False)
        self.room_name = self._generate_name_pass()
        self.room_pass = self._generate_name_pass()
        await ctx.send(f"||{self.RLQqueue}|| \nThe queue has filled, Please hop in a voice channel and play Rocket League! Please look at new channel for info")
        await ctx.send(embed=embed)
        await self.create_channels(ctx)

    @commands.command()
    async def RLQPing(self, ctx):
        await ctx.send(f"{self.RLQqueue}, You have been summonned. If this is a queue start then you have {self.Queue_Size}. Start if people say so@.")



    @commands.command()
    async def end_game(self, ctx):
        category = discord.utils.get(ctx.guild.categories, name="Rocket League")
        await ctx.delete(f"6Mans", category=category)
        await ctx.channel.delete(f"Blue Team", category=category)
        await ctx.channel.delete(f"Orange Team", category=category)


    async def create_channels(self, ctx):
        category = discord.utils.get(ctx.guild.categories, name="Rocket League")
        await ctx.guild.create_text_channel(f"6Mans", category=category)
        await ctx.guild.create_voice_channel(f"Blue Team",category=category)
        await ctx.guild.create_voice_channel(f"Orange Team",category=category)
        time.sleep(5) #sleep for 5 seconds
        text_channel = discord.utils.get(ctx.guild.TextChannel, name="6Mans")
        embed = discord.Embed (
            colour = discord.Colour.red())
         # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='Rocket League Queue: ', value=f'{self.RLQqueue}', inline=False)
        embed = embed
        await ctx.send in text_channel(f"{self.RLQqueue} ", embed=embed)
        await ctx.send in text_channel(f"```Lobby info\nUsername: {self.room_pass}\nPassword: {self.room_pass}```\nPlease create the game and join voice chats, When done please do .end_game command and it will delete the channels. Have fun and make teams!")

    @commands.command(pass_context=True)
    async def RLQhelp(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.darker_grey())
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='RLQ', value='Joins the Rocket league Queue', inline=False)
        embed.add_field(name='RLQremove', value='Removes you from the Rocket League Queue', inline=False)
        embed.add_field(name='RLQstart', value="See when a user has joined Rocket Wars discord, as well as joined discord. You'll be able to see roles and their ID.", inline=False)
        embed.add_field(name='RLQPing', value='Pings the queue for starting low number games', inline=False)
        embed.add_field(name='End_Game', value='Ends the game and deletes Channels', inline=False)
        embed.add_field(name='RLQclear', value='Clears the queue *(Need to be mod or higher)*', inline=False)
        embed.add_field(name='Check_Queue_Size (RL_QS, RL_CQS)', value='See how many people are in queue and max queue size', inline=False)

        # embed.add_field(name=' ', value=' ', inline=False)

        await ctx.send(embed=embed)

    def _generate_name_pass(self):
        return room_pass[random.randrange(len(room_pass))]
room_pass = [
    'octane', 'takumi', 'dominus', 'hotshot', 'batmobile', 'mantis',
    'paladin', 'twinmill', 'centio', 'breakout', 'animus', 'venom',
    'xdevil', 'endo', 'masamune', 'merc', 'backfire', 'gizmo',
    'roadhog', 'armadillo', 'hogsticker', 'luigi', 'mario', 'samus',
    'sweettooth', 'cyclone', 'imperator', 'jager', 'mantis', 'nimbus',
    'samurai', 'twinzer', 'werewolf', 'maverick', 'artemis', 'charger',
    'skyline', 'aftershock', 'boneshaker', 'delorean', 'esper',
    'fast4wd', 'gazella', 'grog', 'jeep', 'marauder', 'mclaren',
    'mr11', 'proteus', 'ripper', 'scarab', 'tumbler', 'triton',
    'vulcan', 'zippy',

    'aquadome', 'beckwith', 'champions', 'dfh', 'mannfield',
    'neotokyo', 'saltyshores', 'starbase', 'urban', 'utopia',
    'wasteland', 'farmstead', 'arctagon', 'badlands', 'core707',
    'dunkhouse', 'throwback', 'underpass', 'badlands',

    '20xx', 'biomass', 'bubbly', 'chameleon', 'dissolver', 'heatwave',
    'hexed', 'labyrinth', 'parallax', 'slipstream', 'spectre',
    'stormwatch', 'tora', 'trigon', 'wetpaint',

    'ara51', 'ballacarra', 'chrono', 'clockwork', 'cruxe',
    'discotheque', 'draco', 'dynamo', 'equalizer', 'gernot', 'hikari',
    'hypnotik', 'illuminata', 'infinium', 'kalos', 'lobo', 'looper',
    'photon', 'pulsus', 'raijin', 'reactor', 'roulette', 'turbine',
    'voltaic', 'wonderment', 'zomba',

    'unranked', 'prospect', 'challenger', 'risingstar', 'allstar',
    'superstar', 'champion', 'grandchamp', 'bronze', 'silver', 'gold',
    'platinum', 'diamond',

    'dropshot', 'hoops', 'soccar', 'rumble', 'snowday', 'solo',
    'doubles', 'standard', 'chaos',

    'armstrong', 'bandit', 'beast', 'boomer', 'buzz', 'cblock',
    'casper', 'caveman', 'centice', 'chipper', 'cougar', 'dude',
    'foamer', 'fury', 'gerwin', 'goose', 'heater', 'hollywood',
    'hound', 'iceman', 'imp', 'jester', 'junker', 'khan', 'marley',
    'maverick', 'merlin', 'middy', 'mountain', 'myrtle', 'outlaw',
    'poncho', 'rainmaker', 'raja', 'rex', 'roundhouse', 'sabretooth',
    'saltie', 'samara', 'scout', 'shepard', 'slider', 'squall',
    'sticks', 'stinger', 'storm', 'sultan', 'sundown', 'swabbie',
    'tex', 'tusk', 'viper', 'wolfman', 'yuri']
