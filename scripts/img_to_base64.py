import os
import sys
import base64

"""
    Reads all contents in a directory then turn them into Base 64 strings
    And finally write them as a variable into a .py file
"""

def main():
    outputFileName = "base64_imgs.py"
    root = "./img"

    # From: https://stackoverflow.com/questions/19309667/recursive-os-listdir
    imgs = [os.path.join(dp, f).replace("\\", "/") for dp, dn, fn in os.walk(os.path.expanduser(root)) for f in fn]
    
    variables = []

    for img in imgs:
        fileName = img.split("/")[-1]
        variableName = fileName.replace(".", "_")

        b = readBytes(img)
        if (b == None):
            print(f"Unable to read bytes from [{img}]")
            continue

        b64Str = base64.b64encode(b).decode()

        line = f"{variableName} = \"{b64Str}\"" + "\n\n"
        variables.append(line)

    with open(outputFileName, "w+") as f:
        for v in variables:
            f.write(v)

    print("--- End of Program ---")

def readBytes(p: str):
    try:
        with open(p, "rb") as f:
            return f.read()
    except:
        return None

if (__name__ == "__main__"):
    main()