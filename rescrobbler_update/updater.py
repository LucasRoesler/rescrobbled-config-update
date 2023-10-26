import os
import subprocess
from pathlib import Path

import toml


def update_config(config_path: Path):
    config_path = config_path.expanduser()
    data = toml.load(config_path)

    # Execute the playerctl --list-all command
    result = subprocess.run(["playerctl", "--list-all"], stdout=subprocess.PIPE)

    # Decode the output from bytes to string and split it into lines
    output = result.stdout.decode("utf-8").splitlines()

    # Find the firefox.instance value
    firefox_instance = next(
        (line for line in output if "firefox.instance" in line), None
    )
    if not firefox_instance:
        print("Firefox instance is not running")
        exit(0)

    print(f"Firefox instance: {firefox_instance}")
    # Update the player-whitelist in the data
    data["player-whitelist"] = [
        player if "firefox.instance" not in player else firefox_instance
        for player in data["player-whitelist"]
    ]

    # Write the data back to the TOML file
    config_path.write_text(toml.dumps(data))


def main():
    config_path = Path(
        os.environ.get("RESCROBBLED_CONFIG_PATH", "~/.config/rescrobbled/config.toml")
    )
    update_config(config_path)
