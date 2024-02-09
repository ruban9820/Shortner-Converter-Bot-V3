import asyncio
import datetime
import logging
import logging.config
import sys
from pyrogram import *
from pyrogram.errors.exceptions.not_acceptable_406 import *
from config import *
from database import *
from database.users import *
from helpers import *
from pyshorteners import *

# Configure logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Setup logger
logger = logging.getLogger(__name__)

async def start(client):
    me = await client.get_me()
    client.owner = await client.get_users(int(OWNER_ID))
    client.username = f'@{me.username}'
    temp.BOT_USERNAME = me.username
    temp.FIRST_NAME = me.first_name
    if not await db.get_bot_stats():
        await db.create_stats()
    banned_users = await filter_users({"banned": True})
    async for user in banned_users:
        temp.BANNED_USERS.append(user["user_id"])
    logging.info(LOG_STR)
    await broadcast_admins(client, '** Bot started successfully **\n\nBot By @DKBOTZ')
    logging.info('Bot started')

async def stop(client):
    await client.stop()
    logging.info("Bot stopped. Bye.")

if __name__ == "__main__":
    # Initialize client and plugins
    plugins = dict(
        root="plugins"
    )
    dkbotz = Client(
        "Mdisk-Pro",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )

    # Register start and stop handlers
    dkbotz.start = start
    dkbotz.stop = stop

    # Run the client
    dkbotz.run()
