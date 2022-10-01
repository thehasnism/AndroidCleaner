import os
import sys
import tkinter as tk
from glob import glob
import threading

from tkinter import simpledialog
import shutil


def delFolder(path):
    for i in range(len(names)):
        try:
            shutil.rmtree(names[i] + path)
        except FileNotFoundError:
            print("Wrong file or file path at")
        else:
            continue


# C:/Users/devha/Documents/Test

if __name__ == '__main__':
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Folder Delete",
                                      prompt="Enter Path?:")

    names = glob(USER_INP + "/*/", recursive=True)

    p1 = threading.Thread(target=delFolder("/app/build"))
    p2 = threading.Thread(target=delFolder("/.gradle"))
    p3 = threading.Thread(target=delFolder("/.idea"))
    p4 = threading.Thread(target=delFolder("/app/release"))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
