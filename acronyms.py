# Steps to finding acronyms in a text file
# 1. Ask the user what acronyms they want to find?
# 2. Open the file
# 3. Read each line in the file
# 4. Check if current acronym matches the user input
# 5. Print the definition.

# Opening file with python 'with' keyword using read mode

with open('acronyms.txt') as file:
    # Reading each line in the file
    result = file.read()
    print(result)


# Opening file with python 'with' keyword using readlines mode

with open('acronyms.txt') as file:
    # Reading each line in the file
    result = file.readlines()
    for line in result:
        print(line)

# Alonger way to close the file without 'with' keyword

file = open('acronyms.txt')
try: 
    # perform file operations
    pass
finally:
    file.close()


# A shorter way to close the file by just looping through each line

with open('acronyms.txt') as file:
    for line in file:
        print(line)


# Finding acronyms in the file
def find_acronym():
    look_up = input("What acronym do you want to look up? \n")

    found = False
    with open('acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
    if not found:
        print("Acronym not found.")

def add_acronym():
    acronym = input("Enter the acronym you want to add: \n")
    definition = input("Enter the definition of the acronym: \n")
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

# Main program
def main():
    # Ask the user if they want to find or add an acronym
    choice = input("Do you want to find (F) or add (A) an acronym? Enter F or A: \n")
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
    else:
        print("Invalid choice.")
main()
        