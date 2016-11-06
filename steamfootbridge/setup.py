# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

from . import config

import steam

def do():
  with config.Configuration() as c:
    path = c.get_wine_steam_userconfig_filename()
    print "Updating {}".format(path)
    with open(path) as f:
      userconfig = steam.vdf.load(f)
