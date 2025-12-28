#Functions

def greeting(name): # local scope
    print("Hello", name)

#main program
name1 = input("What is your name? \n")
greeting(name1)

name2 = input("What is your friend's name? \n")
greeting(name2)


def add_numbers(num1, num2):
    return num1 + num2
# Main program
def main():
    number1 = float(input("Enter first number: \n"))
    number2 = float(input("Enter second number: \n"))
    sum_result = add_numbers(number1, number2)
    print("The sum is:", sum_result)

main()