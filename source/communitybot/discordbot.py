import logging

from communitybot.narrations import Narrator
from communitybot.utils import (
    get_help_message
)

from discord.ext.commands import Bot

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()

narrations = Narrator()

description = '''**```-- storybot --
Below a list of available commands:```**
'''

bot = Bot(
    description=description,
    command_prefix="$",
    pm_help=False)
bot.remove_command('help')


@bot.event
async def on_ready():
    logger.info("Logged in")


@bot.command()
async def help():
    await bot.say(get_help_message(description))


@bot.group(pass_context=True)
async def story(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('Usage: $story list')


@story.command()
async def list():
    storyindex = narrations.index
    await bot.say("**Available stories**: " + ", ".join(storyindex.get_stories()))


@story.command()
async def begin(title):
    narrations.start_narration(title)
    await bot.say("**Told story**: %s" % title)