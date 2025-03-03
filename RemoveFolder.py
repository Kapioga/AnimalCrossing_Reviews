import os

def removeFolder():
    removeFolderPrompt = input("Would you like to remove a folder? [Y/N] -> ")
    if removeFolderPrompt == 'Y' or removeFolderPrompt == 'y':
        try:
            removeFolderName = input("Whats the name of the folder? -> ")
            os.remove("./" + removeFolderName)
            print(removeFolderName + " folder has been removed!")
        except FileNotFoundError:
            print("Invalid Folder name")
        except PermissionError:
            print("Unauthorized access")
    else:
        print("Proceed!")