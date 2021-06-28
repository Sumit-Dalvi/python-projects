# RandomSpiral.py

import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "grey", "orange", "purple", "white"]

def random_spiral():
    for n in range(100):
        t.pencolor(random.choice(colors) )
        size = random.randint(10,40)

        x = random.randrange(-turtle.window_width()//2,
                                                     turtle.window_width()//2)
        y =random.randrange(-turtle.window_height()//2,
                                                    turtle.window_height()//2)
        t.penup()
        t.setpos(x,y)
        t.pendown()
        for m in range(size):
            t.forward(m*2)
            t.left(105)


