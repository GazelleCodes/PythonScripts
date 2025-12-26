print(5 / 8)
# Addition and division
print(4 + 5)
print(10 / 2)

# Subtraction
print(5 - 5)

# Multiplication
print(3 * 5)

# VARIABLE ASSIGNMENT

# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Create the variables monthly_savings and num_months

monthly_savings = 10

num_months = 4


# Multiply monthly_savings and num_months
new_savings = monthly_savings * num_months 

# Print new_savings
print (new_savings)

# DATA TYPES
# Create a variable half
half = 0.5

# Create a variable intro
intro = "Hello! How are you?"

# Create a variable is_good
is_good = True

#==
savings = 100
new_savings = 40

# Calculate total_savings using savings and new_savings
total_savings = savings + new_savings
print(total_savings)

# Print the type of total_savings
print(type(total_savings))

intro = "Hello! How are you?"

# Assign sum of intro and intro to doubleintro
doubleintro = intro * 2

# Print out doubleintro
print(doubleintro)

#----------------
amount = 200
tax = 0.07
total = amount + amount * tax
print(total)

# Data type conversion functions
amount = int(10.6)
print(amount)

amount = float(10.6)
print(amount)

# String Concatenation
hello = "Hello "
name = "Alice"
greeting = hello + name
print(greeting)

# # Input Function
# hello = "Hello "
# name = input("What is your name?\n")
# greeting = hello + name
# print(greeting)

# # Age Calculator
# age = int(input("How old are you?\n"))
# decades = age // 10
# years = age % 10
# print(" you are " + str(decades) + " decades and " + str(years) +  " years old ")

#conditional statements 
#if, else--------
# temperature = 90
# if temperature > 80:
#     print("It's too hot!")
#     print("Drink a lot of water.")


temperature = 45
if temperature > 80:
    print("It's too hot!")
    print("Drink a lot of water.") 
elif temperature < 50:
    print("It's too cold!")
    print("Drink a hot beverage.")
else: 
    print("Have a nice day!")   

# Logical Operators
temperature = 75 
if temperature > 80 or temperature < 60:
    print("It's hot, stay inside!")
else:
    print("Enjoy your day!")


temperature = 75 
forecast = "rainy"
if temperature < 80 and forecast != "rainy":
    print("Stay inside!")
else:
    print("Enjoy your day!")

temperature = 75 
forecast = "Sunny"
if temperature < 80 and forecast != "rainy":
    print("Stay outside!")
else:
    print("Enjoy your day!")

forecast = "rainy"
if not forecast == "rainy":
    print("Stay outside!")
else:
    print("Stay inside!")

raining = True

if raining:
    print("Take an umbrella!")
else:
    print("Enjoy your day!")

if not raining:
    print("Enjoy your day!")
else:
    print("Take an umbrella!")

# LISTS AND LOOPS

acronyms = ['LOL', 'OMG', 'TTYL']

acronyms.append('FYI')
acronyms.append('IDK')
acronyms.append('BRB')
acronyms.append('SMH')

acronyms.remove('TTYL') 
del acronyms[1]
print(acronyms)

# check if Exists in List
acronyms = ['LOL', 'OMG', 'TTYL']
word = 'BFN'

if word in acronyms:
    print(word + " is in the list!")
else:
    print(word + " is NOT in the list!")

# Loop through a list
acronyms = ['LOL', 'OMG', 'TTYL', 'BFN', 'FYI']
for acronym in acronyms:
    print(acronym)



# EXPENSES CALCULATOR
expenses = [25.6, 15, 3, 20, 50, 10.5, 7.25]
total = sum(expenses)
print("you spent a total of $", total, sep = '')

# EXPENSES CALCULATOR using loop
expenses = [25.6, 15, 3, 20, 50, 10.5, 7.25]
sum_expenses = 0
for expense in expenses:
    sum_expenses += expense
print("you spent a total of $", sum_expenses, sep = '')


# Syntax of a for loop

for i in range(7):
    print(i)

#Adding input to expenses calculator
# total = 0
# expenses = []
# num_expenses = int(input("How many expenses do you have? \n"))
# for i in range(num_expenses):
#     expenses.append(float(input("Enter expense: \n")))

# total = sum(expenses)
# print("You spent a total of $", total, sep = '')

# Creating Dictionaries

acronyms = {}
acronyms['LOL'] = 'Laughing Out Loud'
acronyms['OMG'] = 'Oh My God'
acronyms['TTYL'] = 'Talk To You Later'

print(acronyms)

# Updating a dictionary
acronyms = {'LOL': 'Laughing Out Loud', 
            'OMG': 'Oh My God', 
            'TTYL': 'Talk To You Later'}
acronyms['OMG'] = 'Oh My Goodness'
print(acronyms )

# Deleting from a dictionary
acronyms = {'LOL': 'Laughing Out Loud', 
            'OMG': 'Oh My God', 
            'TTYL': 'Talk To You Later'}

del acronyms['LOL']
print(acronyms)

#Getting an item that is not in the dictionary

acronyms = {'LOL': 'Laughing Out Loud', 
            'OMG': 'Oh My God', 
            'TTYL': 'Talk To You Later'}
definition = acronyms.get('BFN')
print(definition)  # Prints: None

# Using a loop to go through a dictionary
acronyms = {'LOL': 'Laughing Out Loud', 
            'OMG': 'Oh My God', 
            'TTYL': 'Talk To You Later'}
definition = acronyms.get('BFN')

if definition:
    print(definition)
else:
    print("That acronym is not in the dictionary.")

#Using Dictionary to translate a sentence
acronyms = {'LOL': 'Laughing Out Loud', 
            'IDK': "I Don't Know", 
            'TBH': 'To Be Honest',}
sentence = 'IDK'  +  'what happened'  +  'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)  

#List of lists

menus = [['egg', 'spam', 'bacon'],
            ['Yam', 'sandwich', 'beans'],
            ['pasta', 'salad', 'chicken'] ]
print("Breakfast menu:\t", menus[0][1]) 
print("Lunch menu:\t", menus[1])
print("Dinner menu:\t", menus[2])

# Use a dictionary to store lists instead of lists of lists
menus = {
    'breakfast': ['egg', 'spam', 'bacon'],
    'lunch': ['Yam', 'sandwich', 'beans'],
    'dinner': ['pasta', 'salad', 'chicken']
}
print("Breakfast menu:\t", menus['breakfast'])
print("Lunch menu:\t", menus['lunch'])
print("Dinner menu:\t", menus['dinner'])


#Using a dictionary key and value in a  for loop

menus = {
    'breakfast': ['egg', 'spam', 'bacon'],
    'lunch': ['Yam', 'sandwich', 'beans'],
    'dinner': ['pasta', 'salad', 'chicken']
}
for meal, menu in menus.items():
    print(meal, ':', menu)

# Using dictionary to represent objects
car = {
    'Name': 'Toyota',
    'model': 'Corolla',
    'year': 2020,
    'color': 'blue'
}

print('I have', car.get('Name'), car.get('model'), 'from', car.get('year'), 'in', car.get('color'), 'color.')


# Making a HTTP request in a virtual environment

import requests

response = requests.get('http://api.open-notify.org/astros.json')
jason = response.json()

print(jason)

print('The people currently in space are :')
for person in jason['people']:
    print(person['name'])