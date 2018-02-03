import turtle
from time import sleep, time
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pencolor("orange")
wn.bgcolor("blue")

circles = 0

for a in range (10):
    for b in range (360):
        alex.forward(2)
        alex.left(1)
    circles += 1
    print "%d circles have been drawn"%(circles)
    alex.right(5)
print 'ART IS COMPLETE'
    
sleep(5)
