import sys
from random import randint
max_dice_roll = 6
min_dice_roll = 1
for i in range (100):
    print ('random number generating...')
    print randint (min_dice_roll, max_dice_roll)
    answer = raw_input('whould you like to roll the dice again? ')
    final_answer = answer.lower()
    if final_answer == ('yes'):
        print('ok')
        continue
    else:
        sys.exit(0)

