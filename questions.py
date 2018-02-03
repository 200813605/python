#!/usr/bin/env python

from random import randint

questions=['What did you have for dinner last night?','What did you have for breakfast?']
starter='which age group are you in?'
default = 'what is your name'
randomquestion = randint(0,len (questions)-1)

print'age 1-5 = a,age 5-9 = b, 9-13 = c, 15+ = d'

agegroup = raw_input (starter)

if agegroup == 'a': raw_input ('Hello Hana, '+questions[randomquestion] + ' ')
elif agegroup == 'b': raw_input ('Hello Leila, '+questions[randomquestion] + ' ')
elif agegroup == 'c': raw_input ('Hello Nasser, '+questions[randomquestion] + ' ')
else: 
    name = raw_input ('Hello, what is your name? ')
    raw_input("Hi %s, how are you? " % name)
