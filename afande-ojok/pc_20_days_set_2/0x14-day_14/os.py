# Working with os

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the os
    print(os.name)

    # Check for item existence and type
    print("Item exists: ", str(path.exists("textfile.txt")))
    print("Item is a file: ", path.isfile("textfile.txt"))
    print("Item is a directory: ", path.isdir("textfile.txt"))

    # Work with file paths
    print("Item's path: ", path.realpath("textfile.txt"))
    print("Item's path and name: ", path.split(path.realpath("textfile.txt")))

if __name__ == "__main__":
    main()