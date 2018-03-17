
# General Settings

STEEM_NODES = ["https://api.steemit.com", "https://rpc.buildteam.io"]
# how steem should be accessed; use: steempython | debug
STEEM_API_MODE = 'steempython'

# Steem Account Settings

STEEM_BOT_ACCOUNT = "storybot"
STEEM_BOT_POSTING_KEY = "discord.bot_token"

# Discord Bot Settings

DISCORD_BOT_TOKEN = "discord.bot_token"
DISCORD_HOOKS = [
    "https://discordapp.com/api/webhooks/410134452698611712/XVxNyJnVUJjDTfUL99N3i2oZzvQEhTpeWs1FRlI3sTiny6eykO3dQkARoQfWTDw63yGD",
    "https://discordapp.com/api/webhooks/410134521053315093/4M2Pv8u2j5BE08lmtmR4ZzbZkPyxSwP1Zuc6PMiasv7R5qZ8flxPI2gCVsc5mfXDj2n5"
]

try:
    from . local_settings import *
except ImportError:
    pass
