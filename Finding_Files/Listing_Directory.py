import os, fnmatch

def list_directory(folder):# Lists all files and directories in the specified folder
    for file in os.listdir(folder):
        print(file)


list_directory("./OOP")  # Lists files in the current directory

#list directories using the string method

def starts_with(folder, search):# Lists files and directories that start with the specified prefix
    for file in os.listdir(folder):
        if file.startswith(search):
            print(file)


def ends_with(folder, search):# Lists files and directories that end with the specified suffix
    for file in os.listdir(folder):
        if file.endswith(search):
            print(file)

#ends_with("./OOP", ".txt")  # Lists files ending with .txt in the current directory
#ends_with("./OOP", ".csv")
#ends_with("./OOP", ".py")
#starts_with("./OOP", "02_txt")  # Lists files starting with '02_txt' in the current directory


#listing directories using fnmatch(Helps to create more complex patterns and criteria)
def match(folder, search):# Lists files and directories that match the specified pattern
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, search):
            print(file)

#match("./OOP", "*.csv")
#match("./OOP", "*_file.csv")  # Lists all files in the current directory
#match("./OOP", "*1*_file.csv")

#Advanced pattern matching

def match(folder, search):# Lists files and directories that match the specified pattern
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, search):
            print(file)
#match("./OOP", "??_file.csv")  # Matches files with exactly two characters before '_file.csv'
#match("./OOP", "[0-9]_file.csv")  # Matches files starting with a single digit followed by '_file.csv'
#match("./OOP", "*_file*.*")

#Listing directories using glob module

from pathlib import Path

def glob_match(folder, search):# Lists files and directories that match the specified glob pattern
    path = Path(folder)
    for file in path.glob(search):
        print(file.name)

glob_match("./OOP", "*2*.t*")  # Lists all .csv files in the specified directory