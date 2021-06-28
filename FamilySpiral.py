# familySpiral.py

import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "pink", "green", "orange",
             "white" ]
family = []
name = turtle.textinput("My Family",
                                       "Enter a name, or just hit [ENTER] to end")

while name  != "":
    family.append(name)
    name = turtle.textinput("My Family",
                                       "Enter a name, or just hit [ENTER] to end")
for x in range(100):
    t.pencolor(colors[x%len(family) ] )
    t.penup()
    t.forward(x)
    t.pendown()
    t.write(family[x%len(family) ] ,  font = ("Arial", int( (x+4)/4), "bold") )
    t.left(360/len(family) + 2)
