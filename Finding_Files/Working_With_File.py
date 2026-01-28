# Getting file attributes


import os
from datetime import datetime

def get_date(timestamp):# Converts a timestamp to a human-readable date format
    return datetime.utcfromtimestamp(timestamp).strftime("%d %b %Y %H:%M:%S")

def get_file_attributes(folder):# Retrieves and prints various attributes of the specified file
    with os.scandir(folder) as dir:
        for file in dir:
            if file in dir:
                info = file.stat()
                print(f"Modified {get_date(info.st_mtime)} {file.name}")


get_file_attributes("./OOP/Subfolder")  # Gets attributes of the specified file
                
                