import os
from zipfile import ZipFile


def Unzip():
    # Makes new folder
    newZipFileName = input("What would you like to name your file? -> ")
    os.makedirs(os.path.join('.', newZipFileName))

    # Grabs zip file
    try:
        MainZipfile = input("what is the name of the zipfile -> ")
        zf = ZipFile(MainZipfile + ".zip")
        zf.extractall('./' + newZipFileName)
        unzippedDatasetPath = ('./' + newZipFileName)
        print("File has been extracted and stored here -> " + unzippedDatasetPath)
        zf.close()
        return unzippedDatasetPath

    except FileNotFoundError:
        print("Invalid Filename Provided")
    except PermissionError:
        print("Unauthorized access")