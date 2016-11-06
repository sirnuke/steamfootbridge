# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

from . import config

def do():
  with config.Configuration() as c:
    print "{} is localconfigdir".format(c.get_wine_steam_userconfig_filename())
