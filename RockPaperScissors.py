# RockPaperScissors.py
import random
choices = ["rock", "paper", "scissors"]
player = input("do u want to be rock ,  paper  , scissors or (quit) ")
while player  !=  "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("u chose ", player , "and the computer chose", computer , ".")
    if player == computer:
        print("it's a tie")
    elif player == "rock":
        if computer == "scissors":
            print("you win!")
        else:
            print("computer win!")
    elif player == "paper":
            if computer == "rock":
                print("you win!")
            else:
                print("computer win!")
    elif player == "scissors":
        if computer =="paper":
            print("you win!")
        else:
            print("computer win!")
    else:
        print("there was some sort of error")
    print()
    player = input("do u want to be rock ,  paper  , scissors or (quit) ")
        
