import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "blue", "green", "yellow", "black", "pink"]

your_name = turtle.textinput("Enter your name", "what is your name")


for x in range (100):
    t.pencolor( colors[ x % 6 ] )
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name)
    t.right(92)             
