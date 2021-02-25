from .musique import Music
from .AUQ import AmongUsQueue
from .roles import *
from .joinandleave import Welcome, Leave
from .helps import Helps
from .RLQ import RocketLeagueQueue
from .channel_settings import Channel_Changes
from .Streaming_Stuff import DiscordStreaming

def setup(bot):
  bot.add_cog(Music(bot))
  bot.add_cog(AmongUsQueue(bot))
  bot.add_cog(aroles(bot))
  bot.add_cog(rroles(bot))
  bot.add_cog(Welcome(bot))
  bot.add_cog(Leave(bot))
  bot.add_cog(Helps(bot))
  bot.add_cog(RocketLeagueQueue(bot))
  bot.add_cog(Channel_Changes(bot))
  bot.add_cog(DiscordStreaming(bot))