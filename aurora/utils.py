from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import disnake

if TYPE_CHECKING:
    from bot import Aurora


class InvalidConfigException(Exception):
    pass


class Config:
    def __init__(self, config: dict[str, Any], /) -> None:
        self.config = config

    @property
    def prefix(self) -> str | list[str]:
        return cast(str | list[str], self.config["prefix"])

    @property
    def extensions(self) -> list[str]:
        return cast(list[str], self.config["extensions"])

    def get_activity(self, bot: Aurora, /) -> disnake.BaseActivity | None:
        return disnake.Game(f"{len(bot.guilds)} servers")
