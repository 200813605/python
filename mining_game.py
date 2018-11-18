from random import randint
import time
import sys

num = 0
money = 0
inventory = []

z = 'stone'
y = 'iron'
x = 'gold'
w = 'diamond'

stone = 0
iron = 0
gold = 0
diamond = 0

stone_money = 100
iron_money = 500
gold_money = 2000
diamond_money = 5000

def question(q):
    while True:
        answer = raw_input(q)
        if answer.lower()[0] == "y": return True
        if answer.lower()[0] == "n": return False

if question("Would you like to go mining? (Y/N) "):
    print''
else: 
    sys.exit(0)

while True:
    num = randint(0,50)
    if num <= 30 :
        print 'You mined a block of stone'
        inventory.append ('stone')

    elif num >30 and num <43:
        print 'You mined some iron'
        inventory.append ('iron')

    elif num >43 and num <48:
        print 'You mined some gold'
        inventory.append ('gold')
    else:
        print 'You mined a diamond'
        inventory.append ('diamond')

    time.sleep(0.5)

     
    if question ("Would you like to go mining again? (Y/N) "):
        print''
        continue

    else:
        if question("Would you like to check your inventory? (Y/N) "):
            print''
            print inventory

        else:
            if question("Would you like to sell your inventory? (Y/N) "):
                if z in inventory:
                    money += stone_money
                
                if y in inventory:
                    money += iron_money

                if x in inventory:
                    money += gold_money

                if w in inventory:
                    money += diamond_money

                print'You now have $'+ str(money)
            else:
                break
            
    if question ("Would you like to go mining again? (Y/N) "):
        print''
        continue

    else:
        break