# Rescrobbled Config Updater 

This is a small helper script for [Rescrobbled](https://github.com/InputUsername/rescrobbled). I needed this because I use YouTube Music as a Progressive Web App in Firefox and I use the `player-whitelist` feature of Rescrobbled. The PWA has a unique name every time it is started, so it requires frequent updates to the `~/.config/rescrobbled/config.toml`

This script uses [`playerctl`](https://github.com/altdesktop/playerctl) to look up the unique name of the PWA and updates the config file accordingly.


## Installation

1. Install Python 3.12 or higher
2. Build using `poetry build`
3. Install using `pip install dist/rescrobbler_config-0.1.0-py3-none-any.whl`
