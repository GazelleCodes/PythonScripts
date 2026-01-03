# Cleaning up file on desktop
# Make the folder CleanedUp/
# List the files in the Desktop/ folder 
# For each file in the Desktop/ folder
# Move the file to CleanedUp/ folder

import os

folder = r"\Users\HP\OneDrive - Wageningen University & Research\Documents\VS Code\PythonScripts"

entries  = os.scandir(folder)

for entry in entries:
    print(entry.name)
    if os.path.isfile(entry):
        print("File:", entry.name)
    elif os.path.isdir(entry):
        print("Directory:", entry.name)
       
