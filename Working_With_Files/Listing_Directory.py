import os

def list_directory(folder):# Lists all files and directories in the specified folder
    for file in os.listdir(folder):
        print(file)


list_directory("./OOP")  # Lists files in the current directory

#list directories using the string method

