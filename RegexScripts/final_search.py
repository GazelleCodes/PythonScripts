import re

# Getting the contents of the file
textfile = open('Final_Search.log', 'r')
filetext = textfile.read()
textfile.close()

# Getting IP Addresses

IP_Address = re.findall(r'\d+.\d+\.\d+\.\d+', filetext)
print(IP_Address)

# Getting Email Addresses

Email_Address = re.findall(r'\w+\@\w+\.\w+', filetext)
print(Email_Address)

# Getting Phone Numbers

Phone_Numbers = re.findall(r'\d+-\d+-\d+', filetext)
print(Phone_Numbers)

