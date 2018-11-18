import time

highest=100
lowest = 0
guess = (highest - lowest ) /2
guesses = 0

print'Think of a number between 1 and 100...'
time.sleep(5)

answer = raw_input ('Are you ready? Y/N ')

if answer == 'n' or answer == 'N':
    time.sleep(3)

print'The computer will enter a number and you will have to say whether your number is higher or lower than that number (type higher, lower or correct)'

while True:

    a=raw_input(str(guess) +'? ')

    if a == 'higher':  lowest = guess
    else :  highest = guess
        
    guess = (highest - lowest) / 2 + lowest
    guesses += 1
    print 'Guesses:' + str(guesses)
    if a == 'correct':
        print 'Hooray it took me ' + str(guesses) + ' guesses to guess your number!'
        break