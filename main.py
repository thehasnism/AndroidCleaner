import os
import sys
import tkinter as tk
from tkinter import filedialog
import threading
import shutil


def delFolder(base_path, relative_path):
    full_path = os.path.join(base_path, relative_path)
    try:
        shutil.rmtree(full_path)
        print(f"Deleted: {full_path}")
    except FileNotFoundError:
        print(f"File not found: {full_path}")
    except Exception as e:
        print(f"Error deleting {full_path}: {e}")


def delete_folders_in_projects(root_path):
    # List of relative paths to delete
    paths_to_delete = [
        "app/build",
        ".gradle",
        ".idea",
        "app/release"
    ]

    # Iterate through all directories within the root_path
    for dirpath, dirnames, filenames in os.walk(root_path):
        for path in paths_to_delete:
            thread = threading.Thread(target=delFolder, args=(dirpath, path))
            thread.start()


if __name__ == '__main__':
    ROOT = tk.Tk()
    ROOT.withdraw()

    # Open a directory selection dialog
    USER_INP = filedialog.askdirectory(title="Select Folder")

    if USER_INP:  # Check if the user selected a directory
        delete_folders_in_projects(USER_INP)

        print("Deletion initiated. Check console for deleted folder messages.")
    else:
        print("No directory selected.")