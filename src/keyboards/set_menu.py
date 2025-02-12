from aiogram import Bot
from aiogram.types import BotCommand

from src.lexicon import LEXICON_COMMANDS_BOTH


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in LEXICON_COMMANDS_BOTH.items()
    ]

    await bot.set_my_commands(main_menu_commands)
