# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

import subprocess

from . import config

def do(appid):
  print "Executing appid {}".format(appid)
  # TODO: Should we explicitly start Steam if it isn't already running?
  # TODO: Figure out how to disable the overlay when running in this mode - we get two of them!
  subprocess.Popen(["wine", config.__wine_steam_path__, "-silent", "-applaunch", str(appid)])

