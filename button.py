from Tkinter import *
from random import randint
def roll():
    text.delete(0.0,END)
    text.insert(END, str(randint(1,6)))
window = Tk()
window.title('Dice Roller')
HEIGHT = 500
WIDTH = 800
c = Canvas (window, width = WIDTH, height= HEIGHT, bg = 'lightblue')
text = Text(window, width = 1, height = 1)
buttonA = Button(window, text = 'Press to roll!', command = roll)
text.pack()
buttonA.pack()
c.pack()
