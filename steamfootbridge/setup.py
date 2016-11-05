# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

from . import config

def do():
  with config.Configuration() as c:
    print "{} is userid".format(c._userid)
