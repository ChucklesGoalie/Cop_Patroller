import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import random


class information(commands.Cog):
    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
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

    @commands.command(aliases=['getallwithrole', 'check_role'])
    async def role_check(self, ctx, *, role: discord.Role, member : discord.Member = None):
        members = "".join(f'{member.display_name}\n' for member in role.members)
        # await ctx.send(f'```{members}```')
        embed = discord.Embed(
            colour=discord.Colour.darker_grey(), timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="Role:", value=f'{role}')
        embed.add_field(name="Members:", value=f'{members}')

        await ctx.send(embed=embed)