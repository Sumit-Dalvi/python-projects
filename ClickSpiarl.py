#ClickSpiral.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "blue", "yellow", "green", "white"]

def spiarl(x,y):
    print(x,y)
    t.pencolor(random.choice(colors))
    size = random.randint(10,50)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m * 2)
        t.left(99)

turtle.onscreenclick(spiarl)
