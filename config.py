
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "22642704"))
API_HASH = os.environ.get("API_HASH", "878698447412869d1b30bf929f32e86f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6891941362:AAGOJb9yFjcOMSzYt3luftxXcVmf_WSRb2c")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1032438381")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://ruban9124:karthi9124@shortner.z4mawxq.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1032438381")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1032438381)
ADMINS.append(964915467)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001935351726")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "teamuhdbackup1") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://graph.org/file/64e817b1888bc0fe8ebc4.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "True"
SHORTNER_LINK = "https://shrinkforearn.in/"
CHANNEL_LINK = "https://t.me/REMOVIESOFFICIAL"
