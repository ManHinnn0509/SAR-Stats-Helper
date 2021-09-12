import tkinter as tk
from tkinter import messagebox as msgbox

from config import *
from base64_imgs import dr_beagle_head_ico
from const import GAMEMODES, DATA_KEYS, INFO_KEYS

from util.time_utils import convertTime
from util.img_utils import getImgFromURL
from util.utils import dictFromLists, genLabelTextFromDict, setIcon

from sar import SAR_Player, getSessionTicket, getPlayFabID
from steam import SteamUser, getSteamID
from widgets import InfoFrame, DataFrame, InputFrame

def main():
    print("[DEBUG] Launching...")

    # Error handling here? or in the MainWindow?...
    # I'm just gonna keep it here first
    sessionTicket = getSessionTicket(PLAYFAB_AC, PLAYFAB_PW)
    if (sessionTicket == None):
        print("[ERROR] Unable to get session ticket. Please try again later")
        return
    print(f"[DEBUG] Session ticket: {sessionTicket}")
    
    root = tk.Tk()
    w = MainWindow(root, sessionTicket)
    root.mainloop()

    print("--- End of Program ---")

# --- MainWindow class for status checker

class MainWindow:
    # Just for telling what variables we're gonna have in this class
    steamUser = None
    sarPlayer = None

    playerAvatar = None
    profileURL = None
    steamID = None
    playFabID = None

    def __init__(self, master, sessionTicket):
        self.master = master

        # Window setting / info
        setIcon(self.master, dr_beagle_head_ico)
        master.title(TITLE)
        master.geometry(WINDOW_SIZE)
        master.resizable(RESIZE_W, RESIZE_H)

        """
        self.sessionTicket = getSessionTicket(PLAYFAB_AC, PLAYFAB_PW)
        if (self.sessionTicket == None):
            msgbox.showerror("ERROR", "Unable to generate session ticket. Now exiting...")
            return
        """
        self.sessionTicket = sessionTicket
        
        self.inputFrame = InputFrame(self, "Steam profile URL: ")
        self.infoFrame = InfoFrame(self, INFO_KEYS)

        self.dataFrames = [DataFrame(self, DATA_KEYS, mode, ipadx=8, padx=8) for mode in GAMEMODES]
    
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
        self.__updateData()

    def __updateData(self):
        """
            Private method (functon ?) for updating the data part.
        """

        # Make sure the order is the same as the GAMEMODE
        stats = [
            self.sarPlayer.getSoloStat(),
            self.sarPlayer.getDuosStat(),
            self.sarPlayer.getSquadsStat(),
            self.sarPlayer.getSAW_RebellionStat(),
            self.sarPlayer.getMysteryModeStat()
        ]

        dataKeys = list(DATA_KEYS)
        
        for i in range(0, len(self.dataFrames)):
            # Gamemode is also the "title"
            gamemode = GAMEMODES[i]

            # Only the value from the dict is needed. So extract the values from it
            statValues = list(stats[i].values())

            # Stat name & value pair
            pair = dictFromLists(dataKeys, statValues)
            lines = genLabelTextFromDict(pair)
            lines = gamemode + "\n" + lines

            self.dataFrames[i].label.config(text=lines)

    def __updateInfo(self):
        """
            Private method (functon ?) for updating the info part.
        """
        name = self.steamUser.personaName

        joinDateTime = convertTime(self.sarPlayer.accountCreateDateTime, returnString=True)
        joinDate = joinDateTime.split(" ")[0]

        # Order has to be the same as the keys
        infoValues = [name, joinDate, self.steamID, self.playFabID]
        infoDict = dictFromLists(INFO_KEYS, infoValues)

        newInfo = genLabelTextFromDict(infoDict, " ")
        self.playerAvatar = getImgFromURL(self.steamUser.avatarFullURL, AVATAR_PIXELS_X, AVATAR_PIXELS_Y)

        self.infoFrame.infoMsg.config(text=newInfo, image=self.playerAvatar)

if (__name__ == "__main__"):
    main()