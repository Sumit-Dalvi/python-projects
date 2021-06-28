#CardWars.py
import random
faces = ["one", "two", "three", "four", "five", "six", "seven",
                 'eight', "nine", "ten", "jack", "queen", "king", "ace"]
my_face = random.choice(faces)
your_face = random.choice(faces)
print("my card:", my_face,  " your card:" ,your_face)
if faces.index(my_face) > faces.index(your_face):
    print("I win!")
elif faces.index(my_face) < faces.index(your_face):
    print("you win!")
else:
    print("Tie!")
