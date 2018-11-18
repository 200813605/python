from random import randint

while True:
    amount = raw_input ('How many random numbers would you like (please enter a number between 1 and 100) ')
    
    try:
        number = int(amount)
    except:
        print 'Please enter a number'
        continue

    if number < 1 or number > 100 :
        print'please enter a number between 1 and 100'
        continue

    else:
        break
print'random numbers:'
for i in range(number):
            print randint(0,10)
