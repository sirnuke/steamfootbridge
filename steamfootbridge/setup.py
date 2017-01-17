# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

from . import config

import steam

# TODO: Does capitalization mater?
__root_userconfig_key__     = 'UserLocalConfigStore'
__friends_userconfig_key__  = 'friends'
__autologin_friends_key__   = 'AutoSignIntoFriends'
__system_userconfig_key__   = 'system'
__enable_game_overlay_key__ = 'EnableGameOverlay'

# TODO: Option to disable setting friends autologin
# TODO: Option to disable setting overlay disabled
# TODO: Option to avoid touching the userconfig at all
def do():
  with config.Configuration() as c:
    path = c.get_wine_steam_userconfig_filename()
    print("Reading {}".format(path))

    with open(path, 'r') as f:
      userconfig = steam.vdf.load(f)

    _base_setup_userconfig(userconfig)
    _set_disable_friends_auto_login(userconfig)
    _set_disable_overlay(userconfig)

    print("Writing updated {}".format(path))
    with open(path, 'w') as f:
      steam.vdf.dump(userconfig, f)

def _base_setup_userconfig(userconfig):
  if not __root_userconfig_key__ in userconfig:
    userconfig[__root_userconfig_key__] = {}
  root = userconfig[__root_userconfig_key__]

  if not __friends_userconfig_key__ in root:
    root[__friends_userconfig_key__] = {}

  if not __system_userconfig_key__ in root:
    root[__system_userconfig_key__] = {}

def _set_disable_friends_auto_login(userconfig):
  userconfig[__root_userconfig_key__][__friends_userconfig_key__][__autologin_friends_key__] = '0'

def _set_disable_overlay(userconfig):
  userconfig[__root_userconfig_key__][__system_userconfig_key__][__enable_game_overlay_key__] = '0'
