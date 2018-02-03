#Ghost Game
import sys
from random import randint
feeling_brave = True
score = 0

print 'Ghost Game'
while feeling_brave :
    ghost_door = randint (1,3)
    print '\nFive doors ahead...'
    print'A ghost behind one'
    print'Which door do you open?'
    door = raw_input ('1, 2, 3, 4 or 5?   ')
    door_num = int(door)
    if door_num >= 6 :
        print 'There is no door number ' + str(door_num)
        sys.exit()
    if door_num == ghost_door :
        print 'GHOST!'
        feeling_brave = False
    else:
        print 'No ghost, you\'re safe'
        print 'you enter the next room...'
        score += 1
print 'Run away!'
print 'Game over! You scored', score
