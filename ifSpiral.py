answer = input("do you want to see the spiral? y/n: ")
if answer == 'y' :
    print("working. . . .")
    import turtle
    t = turtle.Pen()
    t.speed(0)
    t.width(2)
    for x in range(100):
        t.forward(x*2)
        t.left(91)
print("Okey, we r done")
