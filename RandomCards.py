# RandomCards.py
import random
suits = ["clubs", "Diamonds", "spades", "hearts"]
faces = ["one", "two", "three", "four", "five", "six", "seven",
                 'eight', "nine", "ten", "jack", "queen", "king", "ace"]
my_face = random.choice(faces)
my_suits = random.choice(suits)
print('I have the', my_face , 'of', my_suits, )
