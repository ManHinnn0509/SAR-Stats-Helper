import tkinter as tk
from tkinter.constants import LEFT

from util.utils import genLabelText

class DataFrame:
    
    def __init__(self, mainWindow, dataKeys, title="", side=LEFT, ipadx=0, padx=0, anchor='center') -> None:
        self.mainWindow = mainWindow
        self.master = self.mainWindow.master

        self.dataKeys = dataKeys
        self.title = title
        self.side = side
        self.ipadx = ipadx
        self.padx = padx
        self.anchor = anchor

        self.dataFrame = tk.Frame(self.master)

        self.label = tk.Label(
            self.dataFrame,
            justify=tk.CENTER,
            text=self.__genLines()
        )
        self.label.grid()

        self.dataFrame.pack(side=self.side, ipadx=self.ipadx, padx=self.padx, anchor=self.anchor)
    
    def __genLines(self, value="-"):
        # Title + data lines
        lines = genLabelText([i + ": " + str(value) for i in self.dataKeys], "")
        lines = self.title + "\n" + lines
        return lines