#On click Smiley.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
def draw_smileys(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Head
    t.pencolor("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #Left Ear
    t.setpos(x-55, y+75)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    #Right Ear
    t.setpos(x+55, y+75)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    # Left Eye
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Right Eye
    t.setpos(x+15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Mouth
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
turtle.onscreenclick(draw_smileys)
