from os import getenv
from os.path import abspath

from dotenv import load_dotenv
load_dotenv()

# Window setting (Rank monitor)
TITLE_RANK_MONITOR = "SAR Player Rank Monitor"
WINDOW_SIZE = "650x300"
SLEEP_SEC = 60

# For rank monitor
# For more category & stat keys, check out const.py
RANK_MONITOR_TEMPLATE = {
    "Mystery Mode": {
        "DeathsCustom2": [0, 0],
        "GamesCustom2": [0, 0],
        "KillsCustom2": [0, 0],
        "MostKillsCustom2": [0, 0],
        "Top2Custom2": [0, 0],
        "WinsCustom2": [0, 0]
    },
    "Kill Statistics": {
        "KillsAK": [0, 0],
        "KillsMagnum": [0, 0],
        "KillsSMG": [0, 0],
        "KillsSniper": [0, 0]
    }, 
    "Other": {
        "CoconutsAte": [0, 0],
        "MushroomsAte": [0, 0],
        "RatGG": [0, 0]
    }
}

# Window setting (Stats checker)
TITLE = "SAR Player Stats Checker"
WINDOW_SIZE = "600x300"
RESIZE_H = False
RESIZE_W = False
ICON_PATH = abspath("./img/icon/dr_beagle_head.ico")

# Info frame constants
EXAMPLE_PROFILE_URL = "https://steamcommunity.com/id/AndiSlash/"
DEFAULT_AVATAR_PATH = abspath("./img/steam_default_avatar.png")
AVATAR_PIXELS_X = 64
AVATAR_PIXELS_Y = 64

# Other
SAR_EXP_PER_LEVEL = 4200

# From .env file
STEAM_API_KEY = getenv("STEAM_API_KEY")
PLAYFAB_EMAIL = getenv("PLAYFAB_EMAIL")
PLAYFAB_AC = getenv("PLAYFAB_AC")
PLAYFAB_PW = getenv("PLAYFAB_PW")