import os
import sys
import yaml
import dotenv
from loguru import logger

try:
    dotenv.load_dotenv(dotenv_path=".env")
except Exception as exception:
    logger.error("Failed to load .env file: %s", exception)

TG_TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

config_yaml = yaml.load(open(os.path.join(sys.path[0], 'src/config/config.yaml'), "r"), Loader=yaml.FullLoader)