import tkinter as tk

from config import *

from config import TITLE_MENU_WINDOW
from base64_imgs import dr_beagle_head_ico, dr_beagle_png

from util.utils import setIcon
from util.img_utils import imgFromBase64

from sar import getSessionTicket
from stats_checker import StatsChecker
from rank_monitor import RankMonitor

from sys import platform

# These Classes should stay in this .py file
# Since it's created for this .py file & only being used in this .py file

def main():

    sessionTicket = getSessionTicket(PLAYFAB_EMAIL, PLAYFAB_PW)
    if (sessionTicket == None):
        print("Unable to get session ticket. Now returning...")
        return
    
    print(f"[DEBUG] Session ticket: {sessionTicket}")

    root = tk.Tk()
    w = MenuWindow(root, sessionTicket)

    BG_COLOR = '#e0e0e0'
    root.configure(bg=BG_COLOR)
    w.appInfo.label.configure(bg=BG_COLOR)

    root.mainloop()
    print("--- End of Program ---")

class MenuWindow:
    def __init__(self, master, sessionTicket) -> None:
        self.master = master

        if(platform != "linux" and platform != "linux2"):
            setIcon(master, dr_beagle_head_ico)
        master.title(TITLE_MENU_WINDOW)
        master.geometry(WINDOW_SIZE_MENU_WINDOW)
        master.resizable(RESIZE_W, RESIZE_H)

        self.sessionTicket = sessionTicket

        self.appInfo = AppInfoFrame(self.master)

        self.statsCheckButton = SpawnWindowButton(
            self, 
            False, [self.sessionTicket],
            TITLE_STATS_CHECKER,
            1, 0, 5
        )

        self.rankMonitorButton = SpawnWindowButton(
            self,
            True, [self.sessionTicket, RANK_MONITOR_TEMPLATE],
            TITLE_RANK_MONITOR,
            2, 0, 5
        )

class AppInfoFrame:
    def __init__(self, mainWindow) -> None:
        self.mainWindow = mainWindow
        self.master = self.mainWindow.master

        self.img = imgFromBase64(dr_beagle_png)

        frame = tk.Frame(self.master)

        self.textInfo = '''
            SAR Stats Checker & Rank Monitor

            By ManHinnn0509
        '''

        self.label = tk.Label(
            frame,
            compound='left',
            image=self.img,
            text=self.textInfo
        )
        self.label.grid()
        
        self.frame = frame
        self.frame.pack()

class SpawnWindowButton:
    def __init__(self, mainWindow, isRankMonitor, classArgs, buttonText, row=0, column=0, pady=0) -> None:
        self.mainWindow = mainWindow
        self.master = self.mainWindow.master
        
        # This is a button that spawns RankMonitor window
        self.isRankMonitor = isRankMonitor
        # The arg that the class needed for __init__()
        self.classArgs = classArgs

        self.buttonText = buttonText

        self.row = row
        self.column = column
        self.pady = pady

        self.buttonWidth = 20

        frame = tk.Frame(self.master)

        self.button = tk.Button(frame, text=self.buttonText, command=self.__spawnWindow)
        self.button.grid(row=self.row, column=self.column)

        self.frame = frame
        self.frame.pack(pady=self.pady)
    
    def __spawnWindow(self):
        self.newWindow = tk.Toplevel(self.mainWindow.master)

        if (self.isRankMonitor):
            self.windowToSpawn = RankMonitor(self.newWindow, self.classArgs[0], self.classArgs[1])
        else:
            self.windowToSpawn = StatsChecker(self.newWindow, self.classArgs[0])
        

if (__name__ == "__main__"):
    main()