import tkinter as tk

from config import AVATAR_PIXELS_X, AVATAR_PIXELS_Y
from base64_imgs import steam_default_avatar_png

from util.utils import genLabelText
from util.img_utils import imgFromBase64

class InfoFrame:
    def __init__(self, mainWindow, infoKeys) -> None:
        self.mainWindow = mainWindow
        self.master = self.mainWindow.master
        self.infoKeys = infoKeys

        infoFrame = tk.Frame(self.master)

        # Loads the default avatar
        self.avatar = imgFromBase64(steam_default_avatar_png, AVATAR_PIXELS_X, AVATAR_PIXELS_Y)

        # No longer uses this one because of the .exe path problem...
        # self.avatar = readImgFromPath(DEFAULT_AVATAR_PATH, AVATAR_PIXELS_X, AVATAR_PIXELS_Y)

        # Creates field with default values
        defaultValue = "-"
        self.infoMsg = tk.Label(
            infoFrame,
            justify=tk.LEFT,
            compound='left',
            image=self.avatar,
            text=genLabelText(
                [i + ": " + defaultValue for i in self.infoKeys], " "
            )
        )

        # Add self.row option (?)
        self.infoMsg.grid(row=1, column=0)

        self.infoFrame = infoFrame
        self.infoFrame.pack()