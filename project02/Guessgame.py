# Guessing Game
'''
Create a Word Guessing Game
Create a word guessing game. The computer will guess a number.
Use python package random to generate a random number.
import random
random_number = random.randInt(1,5)

will generate a random number from specified range or use
from random import randint
random_number = randint(1,5)

The game should keep running until user guesses the number. Use while function.

Keep the track of user tries. When user guess the number, show the number of tries being used to guess the number.

'''

import random

while True:
    try:
        user_guess = int(input("Enter your guess (1-5): "))
        if not 1 <= user_guess <= 5:
            print("Please enter a number between 1 and 5.")
            continue
        computer_guess = random.randint(1, 5)
        if user_guess == computer_guess:
            print("You win!")
        else:
            print(f"You lose! The number was {computer_guess}")

    except ValueError:
        print("Invalid input. Please enter a number.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break
    
    
