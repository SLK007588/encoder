import os
from dotenv import load_dotenv
#import SmartEncoder.Database.db.myDB as db

load_dotenv()

class Config(object):
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS").split(",")]
	GOD = os.environ.get("GOD")
	REDIS_HOST = os.environ.get("REDIS_HOST")
	REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
	REDIS_PASS = os.environ.get("REDIS_PASS")
	DOWNLOAD_LOCATION = "downloads"

	TIMEOUT = int(os.environ.get("TIMEOUT", 30))

	URL = "https://paisakamalo.in/api?api=e31f8bd857b3a79bdb34932bce5c38a1d1bde29c&url="

# Config.AUTH_USERS = [6953453057,-1002038244305]
# Config.API_ID = 3281305
# Config.API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
# Config.BOT_TOKEN = "6785932421:AAFpqGFfXM8wVFXEJdrAdnTEsJBxZsFS2LM"
# Config.REDIS_HOST = "redis-19522.c8.us-east-1-4.ec2.cloud.redislabs.com"
# #redis-14044.c91.us-east-1-3.ec2.cloud.redislabs.com
# Config.REDIS_PASS = "AB7X2pYjowMkLQqOuM1rhwmXqBgKoGpk"
# #FEsHndW4SHTzcTJQWJYHpCDja6RmYnhf
# REDIS_PORT = "19522"
# #14044
# #.
