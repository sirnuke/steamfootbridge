# SteamFootBridge

For when the [Regular Bridge] [SteamBridge] is too... *sketchy*.

## Installation

**./install.sh**, or normal Python tools via the included setup.py script.

## Requirements

* Linux Steam installed
* Wine Steam installed
  * Install to the default Wine prefix, or assure that the WINEPREFIX variable is set.
  * Will be started automatically by SteamFootBridge, if necessary.

## Usage

Installation includes an executable Python script named steamfootbridge.

~~Run **steamfootbridge setup** to configure the Wine Steam installation~~ Actually a no-op
right now.

Run **steamfootbridge download (appid)** to download the application corresponding to (appid)

Run **steamfootbridge execute (appid)** to run the application from within Wine Steam.
This can be added as a shortcut to Linux Steam, and will eventually be automagically added,
based on user settings and what's installed in Wine Steam.  Note that at the moment both Steam
clients will inject their own overlays, and it's against the laws of nature to be interacting
with two at a time.  For now, disable the overlay in one of the two Steam clients.


[SteamBridge]: https://github.com/sirnuke/steambridge
