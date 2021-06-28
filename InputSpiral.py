import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval(input("enter any numebr between :  ")  )
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
    t.pencolor(colors[x%sides] )
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 91)
    t.width(x*sides/100)
