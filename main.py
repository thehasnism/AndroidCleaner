import os
import tkinter as tk
from tkinter import filedialog
import threading
import shutil


def delFolder(base_path, relative_path):
    full_path = os.path.join(base_path, relative_path)

    if os.path.exists(full_path):  # Only proceed if the folder exists
        try:
            shutil.rmtree(full_path)
            print(f"Deleted: {full_path}")
        except Exception as e:
            print(f"Error deleting {full_path}: {e}")
    else:
        print(f"Folder not found: {full_path}")


def delete_folders_in_projects(root_path):
    # List of relative paths to delete
    paths_to_delete = [
        "app/build",
        "main/build",
        ".gradle",
        ".idea",
        "app/release"
    ]

    # Iterate through all directories within the root_path
    for dirpath, dirnames, filenames in os.walk(root_path):
        for path in paths_to_delete:
            # Check if path is within the current directory
            full_path = os.path.join(dirpath, path)
            if os.path.exists(full_path):  # Only start a thread if the folder exists
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