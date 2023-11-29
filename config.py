import os
import pyrogram 
import time
import pyrogram
from pyrogram import Client
from pyrogram import enums
import re
import logging
import logging.config
import requests
import logging
from dotenv import load_dotenv
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

LOGGER = logging

botStartTime2 = time.time()
if os.path.exists('config.env'):
    load_dotenv('config.env')

id_pattern = re.compile(r'^.\d+$') 

def is_enabled(value:str):
    return bool(str(value).lower() in ["true", "1", "e", "d"])

def get_config_from_url():
    CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', None)
    try:
        if len(CONFIG_FILE_URL) == 0: raise TypeError
        try:
            res = requests.get(CONFIG_FILE_URL)
            if res.status_code == 200:
                LOGGER.info("Config uzaktan alındı. Status 200.")
                with open('config.env', 'wb+') as f:
                    f.write(res.content)
                    f.close()
            else:
                LOGGER.error(f"Failed to download config.env {res.status_code}")
        except Exception as e:
            LOGGER.error(f"CONFIG_FILE_URL: {e}")
    except TypeError:
        pass

get_config_from_url()
if os.path.exists('config.env'): load_dotenv('config.env')

id_pattern = re.compile(r'^.\d+$')

LOGGER.info("--- CONFIGS STARTS HERE ---")


botStartTime2 = time.time()

class Config:

    APP_ID = os.environ.get("APP_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    OWNER_ID = os.environ.get("OWNER_ID", 'mmagneto') 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    KANAL = int(os.environ.get("KANAL", ""))
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", ""))
    OWNERS = list(set(x for x in os.environ.get("OWNERS", "1276627253").split()))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    SAVE_USER = "yes" 
