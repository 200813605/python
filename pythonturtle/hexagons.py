import turtle
from time import sleep, time
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pencolor("orange")
wn.bgcolor("blue")

hexagons = 0

for a in range (6):
    for i in range (6):
        alex.forward(75)
        alex.left(60)
        if i == 5:
            alex.right(60)
    hexagons += 1
    print "%d hexagons have been drawn"%(hexagons)
print'ART IS COMPLETE'
sleep(10)
