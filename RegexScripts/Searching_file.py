import re


# Searching for a specific word in a line of a file
with open('sample1.txt', 'r') as file:
    for line in file:
        match = re.search('sample', line)
        if match:
            print("Found a match in line:", line)
            break



#searching for file name/extensions 

file_extension = ['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx']

with open('sample2.txt', 'r') as file:
    text = file.read()
    pattern = r'\b\w+\.(?:' + '|'.join(file_extension) + r')\b'
    matches = re.findall(pattern, text)

    print(matches)


# Searching for a specific pattern in a file (e.g., email addresses)

phone_pattern = r'\d{3}-\d{3}-\d{4}' 
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
zip_code_pattern = r'\b\d{5}(?:-\d{4})?\b'
order_number_pattern = r'\b[A-Z]{2}-\d{4}-\d{4}\b'
hex_color_pattern = r'#[A-Fa-f0-9]{6}'

with open('sample3.txt', 'r') as file:
    text = file.read()
    phone_matches = re.search(phone_pattern, text)
    email_matches = re.search(email_pattern, text)
    zip_code_matches = re.search(zip_code_pattern, text)
    order_number_matches = re.search(order_number_pattern, text)
    hex_color_matches = re.search(hex_color_pattern, text)

    if phone_matches:
        print("Phone number found:", phone_matches.group())
    if email_matches:
        print("Email address found:", email_matches.group())
    if zip_code_matches:
        print("Zip code found:", zip_code_matches.group())
    if order_number_matches:
        print("Order number found:", order_number_matches.group())
    if hex_color_matches:
        print("Hex color code found:", hex_color_matches.group())