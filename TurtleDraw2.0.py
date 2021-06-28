#TurtleDraw2.0.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("red")
t.width(15)
turtle.onscreenclick(t.setpos)
