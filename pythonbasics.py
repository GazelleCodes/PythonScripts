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

