

#creating zip files

import zipfile

to_zip = ['OOP/01_text.csv', 
              'OOP/02_text.csv',
             'OOP/02_text.txt',
             'OOP/Subfolder/01_file_text.csv']


def create_zip(zip_name, files, opt):# Creates a zip file containing the specified files
    with zipfile.ZipFile(zip_name, opt, allowZip64=True) as archive:
        for file in files:
            archive.write(file)

#create_zip('OOP.zip', to_zip, 'w')  # Creates a new zip file


#Adding files to an existing zip file

to_zip = ['OOP/01_text.csv', 
              'OOP/02_text.csv']


def add_to_zip(zip_name, files, opt):# Adds files to an existing zip file
    with zipfile.ZipFile(zip_name, opt, allowZip64=True) as archive:
        for file in files:
            list = archive.namelist()
            if file not in list:
                archive.write(file)
            else:
                print(f"{file} already exists in the archive.")

#add_to_zip('OOP.zip', to_zip, 'a')  # Adds files to an existing zip file


#Reading zip files

def read_zip(zip_name):# Reads and lists the contents of the specified zip file
    with zipfile.ZipFile(zip_name, 'r') as archive:
        list = archive.namelist()
        for filename in list:
            zfinfo = archive.getinfo(filename)
            print(f"\t{filename} => {zfinfo.file_size} bytes, {zfinfo.compress_size} bytes")

#read_zip('OOP.zip')  # Reads the contents of the specified zip file

#Extracting files from a zip file

def extract_file(zip_name, file, extract_path):# Extracts a file from the specified zip file to the given path
    with zipfile.ZipFile(zip_name, 'r') as archive:
        archive.extract(file, extract_path=extract_path)


def extract_all(zip_name, extract_path):# Extracts all files from the specified zip file to the given path
    with zipfile.ZipFile(zip_name, 'r') as archive:
        archive.extractall(extract_path=extract_path)


#extract_file('OOP.zip', 'OOP/01_text.csv', 'OOP_extracted')  # Extracts a specific file from the zip
#extract_all('OOP.zip', 'OOP_extracted_all')  # Extracts all files from the zip