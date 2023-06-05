import os
import tomllib

from bot import Aurora
from dotenv import load_dotenv
from utils import Config, InvalidConfigException


def main() -> None:
    if not os.getenv("DISCORD_TOKEN"):
        raise InvalidConfigException("The DISCORD_TOKEN environment variable was not set.")

    with open("config.toml", "rb") as config_file:
        config = Config(tomllib.load(config_file))

    aurora = Aurora(config)
    aurora.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    load_dotenv()
    main()
