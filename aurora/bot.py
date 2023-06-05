import disnake
from disnake.ext import commands, tasks
from utils import Config

INTENTS = disnake.Intents.default()
INTENTS.message_content = True


class Aurora(commands.Bot):
    def __init__(self, config: Config, /) -> None:
        super().__init__(
            intents=INTENTS,
            command_prefix=config.prefix,
            allowed_mentions=disnake.AllowedMentions.none(),
        )
        self.config = config

        for extension in config.extensions:
            self.load_extension(extension)

    async def on_ready(self) -> None:
        self.change_activity.start()

    @tasks.loop()
    async def change_activity(self) -> None:
        await self.change_presence(activity=self.config.get_activity(self))
