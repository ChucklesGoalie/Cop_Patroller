import discord
from discord.ext import commands
import json
import os
import random

open_account = {}
get_bank_data = {}

class economy(commands.Bot):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command(aliases=['bal', 'b'])
    async def open_account(self, user):
        with open("mainbank.json", "r") as f:
            users = json.load(f)
        if str(user.id) in users:
            return False
        else: 
            users[str(user.id)]["wallet"] = 500
            users[str(user.id)]["bank"] = 500
        with open("mainbank.json", "r") as f:
            json.dump(users, f)
        return True

    async def balance(self, ctx, user):
        await open_account(self, ctx.author)

        users = get_bank_data()
        wallet_amount = users[str(user.id)]["wallet"]
        bank_amount = users[str(user.id)]["bank"]
        
        embed = discord.Embed(title = f"{ctx.author.name}'s balance", colour = discord.Colour.red)
        embed.add_field(name= "Wallet", value= wallet_amount)
        embed.add_field(name="Bank", value=bank_amount)
        await ctx.send(embed = embed)

    async def get_bank_data(self):
        with open("mainbank.json", "r") as f:
            users = json.load(f)
        return users

    @commands.command
    async def give(self, ctx, user):
        await open_account(ctx.author)

        users = await get_bank_data()

        earnings = random.randrange(101)
        await ctx.send(f"Someone gave you {earnings}")

        wallet_amount = users[str(user.id)]["wallet"]


