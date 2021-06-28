#HighCards.py
import random
suits = ["clubs", "Diamonds", "spades", "hearts"]
faces = ["one", "two", "three", "four", "five", "six", "seven",
                 'eight', "nine", "ten", "jack", "queen", "king", "ace"]
keep_going = True
while keep_going:
    my_face = random.choice(faces)
    my_suits = random.choice(suits)
    your_face = random.choice(faces)
    your_suits = random.choice(suits)
    print('I have the', my_face , 'of', my_suits, )
    print('you have the', your_face , 'of', your_suits, )
    if faces.index(my_face) > faces.index(your_face):
        print("I win!")
    elif faces.index(my_face) < faces.index(your_face):
        print("you win!")
    else:
        print("Tie!")
    answer = input("Hit [Enter] to keep going, or any key to [Exit]. " )
    keep_going = (answer == "")
