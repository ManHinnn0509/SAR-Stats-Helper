import tkinter as tk

from config import EXAMPLE_PROFILE_URL

class InputFrame:
    def __init__(self, mainWindow, inputLabelText="Input here") -> None:
        self.mainWindow = mainWindow
        self.master = self.mainWindow.master
        self.inputLabelText = inputLabelText

        inputFrame = tk.Frame(self.master)

        # Label
        self.inputLB = tk.Label(inputFrame, text=self.inputLabelText)
        self.inputLB.grid(row=0, column=0)

        # Input
        self.inputEntry = tk.Entry(inputFrame, width=40)
        self.inputEntry.insert(0, EXAMPLE_PROFILE_URL)
        self.inputEntry.bind('<Return>', lambda event: self.__press())   # The lambda is for ignoring the event object
        self.inputEntry.grid(row=0, column=1)

        # Submit button
        self.inputButton = tk.Button(inputFrame, text="Submit", command=self.__press)
        self.inputButton.grid(row=0, column=2)

        self.inputFrame = inputFrame
        self.inputFrame.pack()
    
    def __press(self):
        # Sets the profile URL from entry
        # Then do a function call(s)

        # Assume the input is a custom Steam ID if it's not starting with "https://"
        # Then format a profile URL with the ID
        s = self.inputEntry.get()
        if not (s.startswith("https://")):
            s = f"https://steamcommunity.com/id/{s}/"
        
        self.mainWindow.exec(s)