from turtle import *
from time import sleep, time
def get_number():
    while True:
        number = raw_input('How many times would you like the turtle to draw? ')
        if number == '' or not number.isdigit():
            print 'this is not a number'
            continue
        elif int(number) > 50:
            print 'This number is too big'
            continue
        else:
            break
    return number 

real_number = get_number()

setup(1630, 970)
Screen()
title("Colours!")
alex = Turtle()
showturtle()

def change_colours(a):
    alex.pencolor(a)

for i in range(10):
    change_colours("red")
    alex.forward(75/2)
    sleep(0.01)
    change_colours("blue")
    alex.forward(75/2)
    sleep(0.01)

for i in range(int(real_number) - 1):
        for i in range (20):
            change_colours("red")
            alex.backward(75/2)
            sleep(0.01)
            change_colours("blue")
            alex.backward(75/2)
            sleep(0.01)
        for i in range(20):
            change_colours("red")
            alex.forward(75/2)
            sleep(0.01)
            change_colours("blue")
            alex.forward(75/2)
            sleep(0.01)

sleep(5)
