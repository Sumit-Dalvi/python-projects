import turtle
t = turtle.Pen()
t.speed(0)

number = int (turtle.numinput("number of sides or circle",
                              "How many sides or circle in your shape?", 6) )
shape = turtle.textinput("which shape do u want?",
                                                    "Enter 'p' for polygon or 'r' for Rosette:")
for x in range(number):
    if shape ==  'r':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
