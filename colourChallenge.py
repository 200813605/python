import sys

colours = {
    "green"    : 2  ,
    "red"      : 1  ,
    "blue"     : 4  ,
    "yellow"   : 3  ,
    "cyan"     : 6  ,
    "pink"     : 5  ,
    "lightGrey": 7  ,
    "darkGrey" : 60 
}

def mbaa():
    print'I do not know this colour'
    sys.exit(0)

def color(c):
    return '\033['+str(colours[c]+30)+"m"

def write():
    colour = raw_input("What colour would you like? ")

    if colour in colours:
        print color(colour) + "boo"
    else:
        mbaa()
  

write()
