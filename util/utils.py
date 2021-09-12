import tkinter as tk
import base64
import os

def setIcon(root: tk.Tk, base64Icon: str):
    "Sets the window's icon. This function is made for the .exe file"

    tempIconFileName = "temp_icon.ico"
    tempIcon = open(tempIconFileName, "wb+")

    tempIcon.write(base64.b64decode(base64Icon))
    tempIcon.close()

    root.iconbitmap(tempIconFileName)
    os.remove(tempIconFileName)

def isDigit(i):
    try:
        temp = int(i)
    except ValueError as e:
        return False
    return True

def dictFromLists(keyList, valueList):
    return dict(zip(keyList, valueList))

def genLabelText(l: list, pad=''):
    """
        Generates multiline label for Frames
    """
    pad = str(pad)
    temp = [pad + str(i) for i in l]
    return '\n'.join(temp)

def genLabelTextFromDict(d: dict, pad=''):
    """
        Generates multiline label from dict

        Example format: \n
        KEY_1: VALUE_1
        KEY_2: VALUE_2 
    """
    pad = str(pad)

    lines = []
    for k, v in d.items():
        line = pad + str(k) + ": " + str(v)
        lines.append(line)
    
    return '\n'.join(lines)