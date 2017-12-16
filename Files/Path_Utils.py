
import os
from os import path
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the OS
    print(os.name) # nt = Windows oder so
    # Check for item existence and type
    print("Item exists:",str(path.exists("textfile.txt")))
    print("Item is a File:",str(path.isfile("textfile.txt")))
    print("Item is a Directory:",str(path.isdir("textfile.txt")))

    # Work with file paths
    print("Items path:",str(path.realpath("textfile"))) # Gibt den ganzen Path aus
    print("Items path and name:",str(path.split(path.realpath("textfile.txt")))) # Separiert File Path und Name

    print("Last modified:",time.ctime(path.getmtime("textfile.txt")))


if  __name__ == "__main__":
    main()
