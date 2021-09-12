import json
import requests as req

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from sar.exceptions import *
from sar.sar_player import SAR_Player
from sar.player_leaderboard import PlayerLeaderboard

def getSessionTicket(playFab_AC, playFab_PW):
    """
        Gets session ticket for SAR via LoginWithPlayFab() \n
        See https://d36d.playfabapi.com/Client/LoginWithPlayFab
    """

    TITLE_ID = "D36D"
    apiURL = "https://d36d.playfabapi.com/Client/LoginWithPlayFab"

    body = {
        "Username": playFab_AC,
        "Password": playFab_PW,
        "TitleId": TITLE_ID
    }

    r = req.post(url=apiURL, verify=False, json=body)
    try:
        rJSON = r.json()
        return rJSON["data"]["SessionTicket"]
    except:
        return None

def getPlayFabID(sessionTicket, steamID):
    """
        Gets a player's PlayFab ID using his/her Steam ID \n
        See https://titleId.playfabapi.com/Client/GetPlayFabIDsFromSteamIDs
    """

    url = "https://titleId.playfabapi.com/Client/GetPlayFabIDsFromSteamIDs"

    headers = {
        "Host": "d36d.playfabapi.com",
        "User-Agent": "UnityPlayer/2018.4.27f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
        "X-PlayFabSDK": "UnitySDK-2.84.200402",
        "X-Authorization": sessionTicket,
        "Content-Type": "application/json",
    }

    steamID = int(steamID)
    bodyDict = {
        "SteamStringIDs": [
            steamID
        ]
    }

    # Make it into String
    body = json.dumps(bodyDict)
    
    r = req.post(url=url, headers=headers, data=body, verify=False)
    try:
        data = r.json()
        return data["data"]["Data"][0]["PlayFabId"]
    except:
        return None