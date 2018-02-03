import turtle
from time import sleep, time
import sys
wn = turtle.Screen()
alex = turtle.Turtle()
alex.pencolor("black")
wn.bgcolor("white")


def check_shape(shape):
    while True:
        if shape == 'triangle':
            angle = 120
            break
        elif shape == 'square':
            angle = 90
            break
        elif shape == 'pentagon':
            angle = 72
            break
        elif shape == 'hexagon':
            angle = 60
            break
        elif shape == 'heptagon':
            angle = 51
            break
        elif shape == 'octagon':
            angle = 45
            break
        elif shape == 'nonagon':
            angle = 40
            break
        elif shape == 'decagon':
            angle = 36
            break
        elif shape == 'circle':
            angle = 1
            break
        else :
            print'I do not recognize this shape'
            shape = raw_input('What shape do you want alex the turtle to draw? ')
    return [shape,angle]


while True:
    shape = raw_input('What shape do you want alex the turtle to draw? ')
    [shape,angle] = check_shape(shape)
    number = 360 / angle
    for i in range (number):
        if shape == 'circle':
            alex.forward(3)
            alex.left(1)
        else:
            alex.forward(100)
            alex.left(angle)
    sleep(2)
    turtle.reset()
    while True:
        repeat = raw_input ('Would you like alex to make another shape? ')
        if repeat == 'yes':
            break
        elif repeat == 'no':
            sys.exit(0)
        else:
            'Please answer correctly '
        
