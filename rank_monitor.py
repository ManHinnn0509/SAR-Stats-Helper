import tkinter as tk
from tkinter import messagebox as msgbox
import tkinter

import steam
import widgets
from config import *
from const import INFO_KEYS
from base64_imgs import dr_beagle_head_ico

from sar import getSessionTicket, getPlayFabID, PlayerLeaderboard, SAR_Player
from util.img_utils import getImgFromURL
from util.time_utils import convertTime, getDateTimeNow
from util.utils import setIcon, dictFromLists, genLabelTextFromDict

def main():
    sessionTicket = getSessionTicket(PLAYFAB_AC, PLAYFAB_PW)
    if (sessionTicket == None):
        print("[ERROR] Unable to get session ticket. Please try again later")
        return
    
    print(f"[DEBUG] Session ticket: {sessionTicket}")

    root = tk.Tk()
    w = RankMonitor(root, sessionTicket, RANK_MONITOR_TEMPLATE)
    root.mainloop()

class RankMonitor:

    def __init__(self, master, sessionTicket: str, leaderboardTemplate: dict) -> None:
        self.master = master

        # Window (root) setting
        setIcon(self.master, dr_beagle_head_ico)
        master.title(TITLE_RANK_MONITOR)
        master.geometry(WINDOW_SIZE)
        master.resizable(RESIZE_W, RESIZE_H)

        self.sessionTicket = sessionTicket
        self.leaderboardTemplate = leaderboardTemplate

        self.inputFrame = widgets.InputFrame(self, "Steam profile URL: ")
        self.infoFrame = widgets.InfoFrame(self, INFO_KEYS)

        # Temp new button
        self.btn = tkinter.Button(self.master, text="Pause", command=self.__btnPress)
        self.btn.pack(pady=3)

        # Create data frames
        self.dataFrames = []
        for category, stat in self.leaderboardTemplate.items():
            temp = widgets.DataFrame(self, stat.keys(), category, ipadx=5, padx=5, anchor='n')
            self.dataFrames.append(temp)
        
        # Early declaration for future functions
        self.playerLeaderboard = None
        self.afterID = None
    
    def __btnPress(self):
        if (self.playerLeaderboard == None):
            return
        
        currentDateTime = getDateTimeNow()
        # Infinite loop not actived
        if (self.afterID == None):
            # If the "self.playerLeaderboard" is declared
            if not (self.playerLeaderboard == None):
                # Then call the updateLeaderboard() to resume the infinite loop
                print(f"[DEBUG | {currentDateTime}] RESUME LOOP")
                self.btn['text'] = "Pause"
                self.updateLeaderboard()
            
            # This return is needed (To prevent canceling the loop after resuming it)
            return
        
        print(f"[DEBUG | {currentDateTime}] CANCEL LOOP")
        # Cancels the infinite loop
        # And "deactive" it by setting the self.afterID into None
        self.master.after_cancel(self.afterID)
        self.afterID = None
        self.btn['text'] = "Resume"
    
    def exec(self, profileURL: str):
        
        self.profileURL = profileURL

        self.steamID = steam.getSteamID(self.profileURL, STEAM_API_KEY)
        if (self.steamID == None):
            msgbox.showerror("Invalid profile input", "Unable to get Steam ID")
            return
        
        self.playFabID = getPlayFabID(self.sessionTicket, self.steamID)
        if (self.playFabID == None):
            msgbox.showerror("Unable to get player's PlayFab ID", "Player doesn't exist / Try to restart this app")
            return
        
        self.steamUser = steam.SteamUser(STEAM_API_KEY, self.steamID, 0)
        self.sarPlayer = SAR_Player(self.sessionTicket, self.playFabID)
        self.__updateInfo()
        
        # Creates the PlayerLeaderboard object. Then "init" it
        self.playerLeaderboard = PlayerLeaderboard(self.sessionTicket, self.playFabID, self.leaderboardTemplate)
        self.updateLeaderboard()
        
    def updateLeaderboard(self):
        windowTitle = self.master.title()
        self.master.title(windowTitle + " " + "[REFRESHING...]")

        currentDateTime = getDateTimeNow()
        print(f"[DEBUG | {currentDateTime}] updateLeaderboard() call (SLEEP_SEC = {SLEEP_SEC})")

        updateResult = self.playerLeaderboard.update(replaceOldData=False)

        categories = list(updateResult.keys())
        for i in range(0, len(updateResult)):
            category = categories[i]
            dataFrame = self.dataFrames[i]

            newText = category + "\n"
            d = updateResult[category]
            for statKey, valueList in d.items():
                statValue = valueList[0]
                newPos = valueList[1]
                posDiff = valueList[2]

                arrow = "↑" if (posDiff >= 0) else "↓"

                # newText += f"{statKey}: {statValue} (# {newPos} | {arrow} {abs(posDiff)})" + "\n"
                newText += f"{statKey}: {statValue} #{newPos} ({arrow}{abs(posDiff)} )" + "\n"

            dataFrame.label.config(text=newText)
        
        # Call self again after SLEEP_SEC seconds
        # Infinite loop...
        self.afterID = self.master.after(SLEEP_SEC * 1000, self.updateLeaderboard)

        self.master.title(windowTitle)

        currentDateTime = getDateTimeNow()
        print(f"[DEBUG | {currentDateTime}] End of updateLeaderboard()")
    
    def __updateInfo(self):
        """
            Private method (functon ?) for updating the player info part.
        """
        name = self.steamUser.personaName
        levelInfo = f"{self.sarPlayer.currentLevel} ({self.sarPlayer.currentEXP} / {self.sarPlayer.expNeededToLevelUp})"

        joinDateTime = convertTime(self.sarPlayer.accountCreateDateTime, returnString=True)
        joinDate = joinDateTime.split(" ")[0]

        # Order has to be the same as the keys
        infoValues = [name, levelInfo, joinDate, self.steamID, self.playFabID]
        infoDict = dictFromLists(INFO_KEYS, infoValues)

        newInfo = genLabelTextFromDict(infoDict, " ")
        self.playerAvatar = getImgFromURL(self.steamUser.avatarFullURL, AVATAR_PIXELS_X, AVATAR_PIXELS_Y)

        self.infoFrame.infoMsg.config(text=newInfo, image=self.playerAvatar)

# ---

if (__name__ == "__main__"):
    main()