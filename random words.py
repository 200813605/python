#!/usr/bin/env python

from random import randint

words=['boom','kaboom','pow','kapow']

for num in range (0,51):

	randomnum = randint(0,len (words)-1)

	print num, words[randomnum]
