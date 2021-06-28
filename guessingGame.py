# GuessingGame.py

import random
the_number = random.randint(1,100)
guess = int(input("Guess the number between 1 and 100 : " ))
while guess != the_number:
    if guess > the_number:
        print(guess, "was to high, Try again. ")
    if guess < the_number:
        print(guess, "was to low, Try again. ")
    guess = int(input("Guess again :  "))
print(guess, "was right, You win! ")
