#!/usr/bin/env python

from random import randint

random_num = randint(1,5)
secret = randint(0,100)
maxGuesses = 7
win = False

def find_gap():
        if int(input) > secret:
                difference = int(input) - secret
        else:
                difference = secret - int(input)
        score = difference * 2 + random_num
        print 'score : ' + str(score)

for guess in range(1,maxGuesses+1):
	print("Guess Number: %d" % guess)

	input = raw_input("Please enter a number between 1 and 100 ("+str(maxGuesses-guess)+" guesses remaining) ")
	if int(input) > secret:
		print "Secret is SMALLER than " + input
                find_gap()
	elif int(input) < secret:
		print "Secret is BIGGER than " + input
                find_gap()
	else:
		win = True
		break

if win == True:
	print "You WIN!"
else:
	print("Sorry, the number was %d" % secret)
