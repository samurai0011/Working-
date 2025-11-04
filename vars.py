#‌𝐄𝐋 𝐃𝐎𝐑𝐀𝐃𝐎
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22750400"))
API_HASH = environ.get("API_HASH", "a0213f361ff290f021156c8dad30195b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "5515754738"))
CREDIT = "𝐄𝐋 𝐃𝐎𝐑𝐀𝐃𝐎"
AUTH_USER = os.environ.get('AUTH_USERS', '5515754738').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
