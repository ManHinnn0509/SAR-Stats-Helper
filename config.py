from os import getenv
from os.path import abspath

from dotenv import load_dotenv
load_dotenv()

# Global window settings
RESIZE_H = False
RESIZE_W = False
ICON_PATH = abspath("./img/icon/dr_beagle_head.ico")

# ------------------------------------------------------------------------

# Info frame constants
EXAMPLE_PROFILE_URL = "https://steamcommunity.com/id/AndiSlash/"
DEFAULT_AVATAR_PATH = abspath("./img/steam_default_avatar.png")
AVATAR_PIXELS_X = 80
AVATAR_PIXELS_Y = 80

# ------------------------------------------------------------------------

# Window setting (Menu Window)
TITLE_MENU_WINDOW = "SAR Player Stats Checker & Rank Monitor"
WINDOW_SIZE_MENU_WINDOW = "500x300"

# ------------------------------------------------------------------------

# Window setting (Stats checker)
TITLE_STATS_CHECKER = "SAR Player Stats Checker"
WINDOW_SIZE_STATS_CHECKER = "750x330"

# ------------------------------------------------------------------------

# Window setting (Rank monitor)
TITLE_RANK_MONITOR = "SAR Player Rank Monitor"
WINDOW_SIZE = "900x300"
SLEEP_SEC = 30              # Should be greater than / equals to 60

# For rank monitor
# For more category & stat keys, check out "const.py"
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
    "The Bwoking Dead": {
        'GamesCustom3': [0, 0],
        'KillsCustom3': [0, 0],
        'DeathsCustom3': [0, 0],
        'WinsCustom3': [0, 0],
        'MostKillsCustom3': [0, 0],
        'KillsCustom3Z': [0, 0],
        'DeathsCustom3Z': [0, 0],
        'MostKillsCustom3Z': [0, 0]
    },
    "Other": {
        "CoconutsAte": [0, 0],
        "MushroomsAte": [0, 0],
        "RatGG": [0, 0]
    }
}

# Other
SAR_EXP_PER_LEVEL = 4200

# From .env file
STEAM_API_KEY = getenv("STEAM_API_KEY")
PLAYFAB_EMAIL = getenv("PLAYFAB_EMAIL")
PLAYFAB_AC = getenv("PLAYFAB_AC")
PLAYFAB_PW = getenv("PLAYFAB_PW")