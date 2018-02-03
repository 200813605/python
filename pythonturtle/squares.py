import turtle
from time import sleep, time
wn = turtle.Screen()
bob = turtle.Turtle()
bob.pencolor("orange")
wn.bgcolor("blue")

squares = 0

for i in range(72):
    for i in range (4):
        bob.forward(150)
        bob.left(90)
    squares += 1
    print "%d squares have been drawn"%(squares,)
    bob.right(5)
print 'ART IS COMPLETE'
sleep(10)
    
