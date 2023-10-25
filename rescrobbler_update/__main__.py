import os
from pathlib import Path

from rescrobbler_update.main import update_config



if __name__ == "__main__":
    config_path = Path(
        os.environ.get("RESCROBBLED_CONFIG_PATH", "~/.config/rescrobbled/config.toml")
    )
    update_config(config_path)
