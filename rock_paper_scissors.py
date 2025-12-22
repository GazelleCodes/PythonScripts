
import random
computers_choice = random.choice(['rock', 'paper', 'scissors'])
print("Computer's choice is:", computers_choice)

user_choice = input('Do you want rock, paper, scissors?') 

if user_choice == computers_choice:
    print("It's a tie!")
elif user_choice == 'rock' and computers_choice == 'scissors':
    print("You win!")
elif user_choice == 'paper' and computers_choice == 'rock':
    print("You win!")
elif user_choice == 'scissors' and computers_choice == 'paper':
    print("You win!")
else:
    print("You lose!Computer wins!")