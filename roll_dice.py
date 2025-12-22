import random 

roll = random.randint(1, 6)
guess = int(input("Guess the dice roll: \n "))
if guess == roll:
    print("Correct! You rolled a" + str(roll))
else:
    print("Wrong! The computer rolled a " + str(roll))