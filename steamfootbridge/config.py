# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

# TODO: There's probably better ways of determining the path of Wine Steam
# NOTE: No explict \"s around the path.  They're necessary when running as an actual shell to keep
#       the shell from parsing the slash and whatnot, but are actually stripped out when passed
#       to Wine.
__wine_steam_path__ = "C:\\\\Program Files (x86)\\\\Steam\\\\Steam.exe"
