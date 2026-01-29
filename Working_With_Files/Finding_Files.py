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


# get_file_attributes("./OOP/Subfolder")  # Gets attributes of the specified file


# Traversing directories

def traverse_directory(folder):# Recursively traverses the specified directory and prints file paths
    for folderpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            print(f"\t{filename}")

#traverse_directory("./OOP")  # Traverses the specified directory


#copying files

import shutil

def copy_file(source, destination):# Copies a file from the source path to the destination path
    shutil.copy(source, destination)

def copy_folder(source, destination):# Copies an entire directory from the source path to the destination path
    shutil.copytree(source, destination)


#copy_file("./OOP/Subfolder/sample.txt", "./OOP/Subfolder/sample_copy.txt")  # Copies a file


#Moving files

def move_file(source, destination):# Moves a file from the source path to the destination path
    shutil.move(source, destination)


#move_file("./OOP", "./OOP_backup")
#move_file("./OOP/Subfolder/sample_copy.txt", "./OOP/sample_moved.txt")  # Moves a 


#Renaming files

from pathlib import Path

def rename_file_1(source, new_name):# Renames a file to the specified new name
    path = Path(source)
    path.rename(path.with_name(new_name))


def rename_file_2(source, new_name):# Renames a file to the specified new name using shutil
    os.rename(source, new_name)


#rename_file_1("./OOP/text.txt", "./OOP/new_text.txt")  # Renames a file
#rename_file_2("./OOP/new_text.txt", "./OOP/text.txt")  # Renames a file

# Deleting files and directories

def remove_file(file_path):# Deletes the specified file
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error: {file_path} : {e.strerror}")

    else:
        print(F"Error: {file_path} is not a valid file")


remove_file("./OOP/text.txt")  # Deletes a file