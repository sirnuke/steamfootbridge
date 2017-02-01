# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

import os, re, shutil, string, subprocess, tempfile

# NOTE: No explict \"s around the path.  They're necessary when running as an actual shell to keep
#       the shell from parsing the slash and whatnot, but are actually stripped out when passed
#       to Wine.
__wine_registry_steam_key__ = "HKEY_CURRENT_USER\Software\Valve\Steam"
__wine_registry_dump_file__ = "steam-registry.txt"
__wine_registry_steam_executable__ = "SteamExe"
__wine_registry_steam_path__ = "SteamPath"
__wine_steam_user_directories__ = "/userdata"
__wine_steam_userconfig_file__ = "/config/localconfig.vdf"

class Configuration:
  def __init__(self):
    pass

  def __enter__(self):
    self._temp_directory = tempfile.mkdtemp("steamfootbridge")
    self._read_registry_keys()
    self._userid = self._determine_current_user()
    return self

  def __exit__(self, exception_type, exception_value, traceback):
    shutil.rmtree(self._temp_directory)

  def get_wine_steam_windows_executable(self):
    return self._wine_steam_windows_executable

  def get_wine_steam_windows_path(self):
    return self._wine_steam_windows_path

  def get_wine_steam_path(self):
    return self._wine_steam_path

  def get_current_user(self):
    return self._userid

  def get_wine_steam_userconfig_filename(self):
    return "{}{}/{}{}".format(self.get_wine_steam_path(), __wine_steam_user_directories__,
        self._userid, __wine_steam_userconfig_file__)

  def _determine_current_user(self):
    directories = os.listdir(self._wine_steam_path.decode() + __wine_steam_user_directories__)
    if len(directories) == 0:
      raise StandardException("No users found!  Have you logged into Wine Steam?")
    elif len(directories) > 1:
      raise StandardException("Mulitple users found! This will evenatually be handled correctly")
    else:
      return directories[0]


  # TODO: This is awfully slow, and it's /probably/ fine to just get the Wine Prefix and do a
  #       direct search through user.reg - and probably considerably faster.
  # TODO: Should handle not finding keys or regedit error or whatever
  # TODO: It's probably a good idea to cache this if sticking with regedit, and re-read on request
  #       or if the path isn't valid
  # TODO: Should check to make sure executable actually exists, and path is a directory
  def _read_registry_keys(self):
    subprocess.call(["regedit", "-E",
      "{}/{}".format(self._temp_directory, __wine_registry_dump_file__),
      __wine_registry_steam_key__])
    self._wine_steam_windows_path = None
    self._wine_steam_windows_executable = None
    with open("{}/{}".format(self._temp_directory, __wine_registry_dump_file__)) as f:
      for line in f:
        result = re.search("\"SteamExe\"=\"(.*)\"", line)
        if result:
          self._wine_steam_windows_executable = result.group(1)

        result = re.search("\"SteamPath\"=\"(.*)\"", line)
        if result:
          self._wine_steam_windows_path = result.group(1)
    if self._wine_steam_windows_path == None:
      raise StandardException("Unable to determine the SteamPath")
    if self._wine_steam_windows_executable == None:
      raise StandardException("Unable to determine the SteamExe")
    self._wine_steam_path = subprocess.check_output(["winepath",
      self._wine_steam_windows_path]).strip()
