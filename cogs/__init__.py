from .mainbank import economy
from .musique import Music
from .AUQ import AmongUsQueue
from .roles import *
from.polls import Poll
from .joinandleave import Welcome, Leave
from .helps import Helps
from .RLQ import RocketLeagueQueue

def setup(bot):
  bot.add_cog(economy(bot))
  bot.add_cog(Music(bot))
  bot.add_cog(AmongUsQueue(bot))
  bot.add_cog(aroles(bot))
  bot.add_cog(rroles(bot))
  bot.add_cog(Poll(bot))
  bot.add_cog(Welcome(bot))
  bot.add_cog(Leave(bot))
  bot.add_cog(Helps(bot))
  bot.add_cog(RocketLeagueQueue(bot))