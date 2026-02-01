# Reading and Writing Text Files in Python

def read_txt(file_path):# Reads and prints the contents of a text file
    with open(file_path) as file:
        content = file.read()
        print(content)

def read_txt_by_line(file_path):# Reads and prints the contents of a text file line by line
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            print(line, end='')
            line = file.readline()

def write_new_txt(file_name, new_content):# Writes the specified content to a text file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(new_content)


def append_txt(file_name, additional_content):# Appends the specified content to a text file
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(additional_content)


# Example usage:
# read_txt('./OOP/02_text.txt')  # Reads and prints the entire content of the text file
# read_txt_by_line('./OOP/02_text.txt')  # Reads and prints the text file line by line
# write_new_txt('./OOP/new_file.txt', 'This is a new file created using Python.')  # Creates a new text file and writes content to it
# append_txt('./OOP/new_file.txt', 'This line is appended to the existing file.')  # Appends content to the existing text file
        