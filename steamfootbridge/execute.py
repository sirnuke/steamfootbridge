# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

import subprocess

from . import config

def do(appid):
  print("Executing appid {}".format(appid))
  with config.Configuration() as c:
    # TODO: Should we explicitly start Steam if it isn't already running?
    subprocess.Popen(["wine", c.get_wine_steam_windows_executable(), "-silent", "-applaunch",
      str(appid)])
