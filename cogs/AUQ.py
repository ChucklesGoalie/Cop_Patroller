import discord
from discord.ext import commands

class AmongUsQueue(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.AUQqueue = []
        self.Queue_Size = 0
        self.Max_Queue_Size = 10
        self.qtoggle = True

    # def create_queue(ctx, queue):
    #     squeue = ''.join(str(e) for e in queue)
    #     embed = discord.Embed(
    #     colour = discord.Colour.red())
    # # embed.add_field(name=' ', value=' ', inline=False)
    #     embed.add_field(name='Among Us Queue: ', value=f'{squeue}', inline=False)
    #     await ctx.send("The queue has filled, Please hop in a voice channel and play Among us!\n", embed=embed)

    @commands.command(pass_context=True)
    async def AUQadd(self, ctx):
        ''' Add yourself to the queue!'''
        author = ctx.message.author
        if self.qtoggle == False:
            return

        if author.mention not in self.AUQqueue:
            self.Queue_Size = self.Queue_Size + 1
            await ctx.send('you have been added to the queue.')

            if self.Queue_Size > self.Max_Queue_Size:
               self.Queue_Size = self.Queue_Size - 1
               return
            else:
                self.AUQqueue.append(author.mention)
                embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
                embed.add_field(name='Among Us Queue: ', value=f'{self.AUQqueue}', inline=False)
                await ctx.send(embed=embed)
        else:
            await ctx.send('you are already in the queue!')
            
        if self.Queue_Size == self.Max_Queue_Size:
            embed = discord.Embed(
            colour = discord.Colour.red())
        # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Among Us Queue: ', value=f'{self.AUQqueue}', inline=False)
            await ctx.send(f"{self.AUQqueue}\nThe queue has filled, Please hop in a voice channel and play Among us!\n", embed=embed)
            self.AUQqueue = []
            self.Queue_Size = 0

    @commands.command(name='AUQLeave', pass_context=True)
    async def AUQremove(self, ctx):
        ''' Remove yourself from the queue'''
        author = ctx.message.author
        
        if author.mention in self.AUQqueue:
            self.AUQqueue.remove(author.mention)
            await ctx.send(f'you have been removed from the queue.\n')
            self.Queue_Size = self.Queue_Size - 1
            embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Among Us Queue: ', value=f'{self.AUQqueue}', inline=False)
            embed = discord.Embed(
                colour = discord.Colour.red())
            # embed.add_field(name=' ', value=' ', inline=False)
            embed.add_field(name='Among Us Queue: ', value=f'{self.AUQqueue}', inline=False)
            await ctx.send(embed=embed)

        else:
            await ctx.send('you were not in the queue.')
        ctx.send(embed=embed)
    @commands.command(name='AUQ', pass_context=True)
    async def _AUQqueue(self, ctx):
        ''' See who's up next!'''
        embed = discord.Embed(
            colour = discord.Colour.red())
         # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='Among Us Queue: ', value=f'{self.AUQqueue}', inline=False)
        message = embed
        await ctx.send(embed=message)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def AUQclear(self, ctx, Queue_Size):
        ''' Clears the queue'''
        self.AUQqueue = []
        self.Queue_Size = 0
        await ctx.send('Queue has been cleared')

    @commands.command(aliases=["AU_CQS", "AU_QS"])
    async def Check_Queue_Size_AU(self, ctx):
        await ctx.send(f"Queue size is {self.Queue_Size}\nMax Queue size is {self.Max_Queue_Size}")

    @commands.command()
    async def AUQStart(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.red())
    # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='Among Us Queue: ', value=f'{self.AUQqueue}', inline=False)
        await ctx.send(f"||{self.AUQqueue}||\nThe queue has filled, Please hop in a voice channel and play Among us!\n", embed=embed)
        self.AUQqueue = []
        self.Queue_Size = 0

    @commands.command()
    async def AUQPing(self, ctx):
        await ctx.send(f"{self.AUQqueue}, You have been summonned. If this is a queue start then you have {self.Queue_Size}. Start if people say so@.")
