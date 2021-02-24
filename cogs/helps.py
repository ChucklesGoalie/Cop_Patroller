import discord
from discord.ext import commands

class Helps(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #We delete default help command
    client = commands.Bot
    #Embeded help with list and details of commands
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.darker_grey())
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='ping', value='Bot responds with Pong! as well with the latency of the response time.', inline=False)
        embed.add_field(name='ping_mention', value='The bot responds with "Pong!", pings you and responds with latency of the response time', inline=False)
        embed.add_field(name='whois', value="See when a user has joined Rocket Wars discord, as well as joined discord. You'll be able to see roles and their ID.", inline=False)
        embed.add_field(name='getallwithrole | /role_check', value='see who has a certain role', inline=False)
        # embed.add_field(name=' ', value=' ', inline=False)
        embed.add_field(name='help', value='Shows this message.', inline=False)
        embed.add_field(name='updates', value='Shows Version, Updates and bug fixes', inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def admin_help(self, ctx):
        embed = discord.Embed(
            color = discord.Colour.darker_grey())
        embed.set_author(name='Administrator Help : List of Administrator comands available')
        embed.add_field(name='ping', value='Bot responds with Pong! as well with the latency of the response time.', inline=False)
        embed.add_field(name='ping_mention', value='The bot responds with "Pong!", pings you and responds with latency of the response time', inline=False)
        embed.add_field(name='whois', value="See when a user has joined Rocket Wars discord, as well as joined discord. You'll be able to see roles and their ID.", inline=False)
        embed.add_field(name='getallwithrole | /role_check', value='see who has a certain role', inline=False)
        embed.add_field(name='mute {@member}', value='Mutes a specific person', inline=False)
        embed.add_field(name='unmute {@member}', value='UnMutes a specific person', inline=False)
        embed.add_field(name='kick {@member}', value='Kicks a person from the server', inline=False)
        embed.add_field(name='ban {@member}', value='Bans a person from the server', inline=False)
        embed.add_field(name='clear {amount of messages}', value='Removes x amount of messages. (Default is 3 messages)', inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def Music_Help(self, ctx):
        embed = discord.Embed(
            colour = discord.Colour.darker_grey())
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='Join (j)', value='Joins your Voice Channel', inline=False)
        embed.add_field(name='Leave', value='Leaves your Voice Channel', inline=False)
        embed.add_field(name='play <link>', value="Plays a Youtube song [Spotify not supported :( ]", inline=False)
        embed.add_field(name='pause', value='Pauses Music playing', inline=False)
        embed.add_field(name='stop', value='Pauses music and clears queue', inline=False)
        embed.add_field(name='Loop', value='Loops current song', inline=False)
        embed.add_field(name='shuffle', value='Shuffles Current Queue', inline=False)
        embed.add_field(name='remove <song # in queue>', value='Removes that song in queue', inline=False)
        # embed.add_field(name=' ', value=' ', inline=False)
        await ctx.send(embed=embed) 