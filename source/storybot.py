import argparse
import sys
import logging

import communitybot.settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig()

runners = ["discordbot", "narration"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run")

    args = parser.parse_args()
    runner = args.run

    if runner and runner not in runners:
        sys.exit("%s is not in available runners. Options: %s" % (args.run, runners))

    if runner == "discordbot":
        from communitybot.discordbot import bot
        bot.run(communitybot.settings.DISCORD_BOT_TOKEN)
    elif runner == "narration":
        from communitybot.narrations import Narrator
        narrator = Narrator()
        title = 'teststory'
        narrator.start_narration(title)


if __name__ == '__main__':
    main()
