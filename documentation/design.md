# Design

## Goals

* Do not require any immediate dependencies to run on SteamOS.
* Implement both GUI and console interface within the same executable.
* Implement core functionality as a Python module.
* Implement API for integration into other tools.
* Do not require user to enter any credentials into SteamFootBridge
  itself.
* Be fully compliant with Steam terms of service.
* Use official APIs for interaction with Steam, where available.
* Limit all code to Python 2.7.
* Allow users to perform Steam client installation themselves.
* Track list of Wine prefixes, including which one is currently running.
* Automagically install necessary software, if possible.
* Minimize number of prompts, both for setup and execution.
* Allow multiple users to run in same installation.
* Allow mismatch between Linux and Wine user.
* Allow multiple installations of same game across different prefixes.
* Investigate using Winetricks for as many steps as possible.
* Investigate using Wine variants, such as PlayOnLinux or various
  CodeWeaver flavors.

## Functionality

### Determine Steam User

Query steam IDs of logged in user.  Failing that, get list of all users
who have logged in.  Failing that, offer interface for determining user
based on Steam Profile ID.

### Querying Game List

Using official Steam Web API, query and locally cache list of games
owned by user.  Periodically refresh cache, as well as UI for forcing
a refresh.  Do not prevent user from attempting to install games not
reported as owned, using input bar accepting names or application IDs.

### Setting up Wine prefixes

Track list of Wine prefixes, including automagically setting up new ones
on demand.  Reference the Linux client settings for configuration of
things like language.  Allow user to setup Steam client in the prefix,
if desired, to avoid user having to enter credentials in a software they
didn't initiate.  Consider automagically installing frequent dependencies.

### Installing Games

Given a user, Wine prefix, and application id, start the Wine steam client
in silent mode. Install the application using the Steam URL Handler.
Update internal state of application.

### Running Games

Given a user, Wine prefix, and application id, start the Wine steam
client, including stopping a client in the wrong prefix.  Fork and
quit from the main thread, to avoid locking the console or an incorrect
"User in non-Steam application" status.  Using Steam URL Handler, start
the game.  Do not attempt to track what games are currently running,
that's up to the user and Steam to manage.

### Uninstall Games

Installing, but using the uninstall command.
