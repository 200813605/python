#!/usr/bin/env python

from random import randint
import os

steps = 0

max_width = 10
max_height = 10
max_mines = 10
field = [['X']*max_width for _ in range(max_height)]
hideMines = True

colors = {
    "red" : '\033[91m',
    "reset": '\033[0m',
    "bold": '\033[1m'
}


def showField():
    os.system('clear')
    print "  ",
    for x in range(0,max_width):
        print ("%02d" % (x+1)),
    print
    
    for x in range(0,max_width):
        print ("%02d " % (x+1))  ,
        for y in range(0,max_height):
            if hideMines == False:
                if field[x][y] == "*":
                    print ("%s%s%s " % (colors["red"], field[x][y], colors["reset"])),
                else:    
                    print ("%s%s%s " % (colors["bold"], field[x][y], colors["reset"])),
            else:
                char = field[x][y]
                if char == "*": char = "X"
                print ("%s%s%s " % (colors["bold"], char, colors["reset"])),
        print


def hideMines():
    for m in range(0,max_mines+1):
        x = randint(0,max_width-1)
        y = randint(0,max_height-1)
        field[x][y] = "*"

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

hideMines()


while True:
    steps = steps + 1
    showField()

    print
    print "Steps: " + str(steps)


    while True:
        x = raw_input ('Enter the X of a safe pot ')
        if isInt(x) and int(x) >= 0 and int(x) <= max_width:
            x = int(x) - 1
            break

    while True:
        y = raw_input ('Enter the Y of a safe spot ')
        if isInt(y) and int(y) >= 0 and int(y) <= max_height:
            y = int(y) - 1
            break

    if field[x][y] == '*':
        print"you died" 
        hideMines = False
        showField()
        break
    else:
        field[x][y] = ' '
