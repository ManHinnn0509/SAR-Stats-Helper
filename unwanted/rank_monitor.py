"""
import base64
import os
import tkinter as tk
from tkinter import messagebox as msgbox

from config import *
from const import INFO_KEYS, LEADERBOARD_POSITIONS_TEMPLATE
from base64_imgs import dr_beagle_head_ico

from util.time_utils import convertTime
from util.utils import dictFromLists, genLabelTextFromDict, getImgFromURL

from sar import SAR_Player, getSessionTicket, getPlayFabID
from steam import SteamUser, getSteamID
from widgets import InputFrame, DataFrame, InfoFrame

def main():
    
    sessionTicket = "CFAC1812652C4BE9--4E8A1F69E85FCA61-D36D-8D973956D91C008-cRcbgDKXzWEnyDzeKZYV7SHbRWfr1bze6Zr4tkMZrAk="
    
    

    root = tk.Tk()
    w = RankMonitorWindow(root, sessionTicket)
    root.mainloop()

    print("--- End of Program ---")

class RankMonitorWindow:
    WINDOW_SIZE_RANK_MONITOR = "800x550"
    TITLE_RANK_MONITOR = "SAR Rank Monitor"
    GAMEMODE_KEYS = set(LEADERBOARD_POSITIONS_TEMPLATE.keys())

    profileURL = None
    steamID = None
    playFabID = None

    def __init__(self, master, sessionTicket) -> None:
        self.master = master
        self.sessionTicket = sessionTicket

        # Window setting / info
        self.__setIcon()
        # master.iconbitmap(ICON_PATH)
        master.title(self.TITLE_RANK_MONITOR)
        master.geometry(self.WINDOW_SIZE_RANK_MONITOR)
        master.resizable(RESIZE_W, RESIZE_H)

        self.inputFrame = InputFrame(self, "INPUT: ")
        self.infoFrame = InfoFrame(self, INFO_KEYS)

        self.template = LEADERBOARD_POSITIONS_TEMPLATE
        self.wantedKeys = {"Kill Statistics", "Mystery Mode"}
        # self.unwantedKeys = set(self.template.keys()) - self.wantedKeys

        self.wantedCategories = self.__filterWanted(self.template)

        self.dataFrames = []
        for k1, v1 in self.wantedCategories.items():
            title = k1
            keys = v1.keys()
            self.dataFrames.append(DataFrame(mainWindow=self, dataKeys=keys, title=title + "\n", ipadx=8, padx=8))
    
    def exec(self, profileURL):
        self.profileURL = profileURL

        self.steamID = getSteamID(self.profileURL, STEAM_API_KEY)
        if (self.steamID == None):
            msgbox.showerror("Invalid profile input", "Unable to get Steam ID")
            return
        
        self.playFabID = getPlayFabID(self.sessionTicket, self.steamID)
        if (self.playFabID == None):
            msgbox.showerror("Unable to get player's PlayFab ID", "Player doesn't exist / Try to restart this app")
            return
        
        self.steamUser = SteamUser(STEAM_API_KEY, self.steamID, 0)
        self.sarPlayer = SAR_Player(self.sessionTicket, self.playFabID)

        self.__updateInfo()

    def __updateInfo(self):
        name = self.steamUser.personaName

        joinDateTime = convertTime(self.sarPlayer.accountCreateDateTime, returnString=True)
        joinDate = joinDateTime.split(" ")[0]

        # Order has to be the same as the keys
        infoValues = [name, joinDate, self.steamID, self.playFabID]
        infoDict = dictFromLists(INFO_KEYS, infoValues)

        newInfo = genLabelTextFromDict(infoDict, " ")
        self.playerAvatar = getImgFromURL(self.steamUser.avatarFullURL, AVATAR_PIXELS_X, AVATAR_PIXELS_Y)

        self.infoFrame.infoMsg.config(text=newInfo, image=self.playerAvatar)

    def __filterWanted(self, d: dict):
        return {k: v for k, v in d.items() if (k in self.wantedKeys)}
    
    def __setIcon(self):
        "This is for the .exe file"
        
        tempIconFileName = "temp_icon.ico"
        tempIcon = open(tempIconFileName, "wb+")

        tempIcon.write(base64.b64decode(dr_beagle_head_ico))
        tempIcon.close()

        self.master.iconbitmap(tempIconFileName)
        os.remove(tempIconFileName)

if (__name__ == "__main__"):
    main()
"""