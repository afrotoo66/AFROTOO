import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "T_Y_E_X")
    CHANNEL = os.environ.get("CHANNEL", "T_Y_E_X")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/1105de1e03f0ba27ba095.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/1105de1e03f0ba27ba095.jpg")
    OWNER_ID = os.environ.get("OWNER_ID", "")

