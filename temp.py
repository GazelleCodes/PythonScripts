# Ask the user what acronym they want to add
# Then ask the user what the definition is
# Open the file
#Write the new acronym and definition to the file

acronym = input("Enter the acronym you want to add: \n")
definition = input("Enter the definition of the acronym: \n")
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')