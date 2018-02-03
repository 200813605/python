from random import randint
from time import gmtime, strftime
import time

# Define colors
red    = '\033[31m'
green  = '\033[32m'
yellow = '\033[33m'
reset  = '\033[0m'

# Set the output filename
filename = "sub and add score.txt"
max_equations = 10
score = 0
signs = ['+','-']



def change_signs():
    a = randint(0,1)
    return signs[a]

def change_nums():
    a = randint(10,20)
    b = randint(10,20)
    if a > b :
        return [a,b]
    else:
        return [b,a]


#
# Game starts here
#

#
# Get player name
#
while True:
    name = raw_input ('What is your name? ')
    if name == ' ' or not name.isalpha():
        print 'This is not a name'
    else:
        break

begin = time.time()

for i in range (max_equations):
    (num_a, num_b) = change_nums()
    (sign) = change_signs()
    while True:
        start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        answer = raw_input("%d %s %d = "%(num_a,sign,num_b))
        if answer == ' ' or not answer.isdigit():
            print 'please try again'
        else:
            break
    if int(answer) == eval("num_a" + sign + "num_b"):
        print green + 'correct' + reset
        score += 1
    else:
        print red + 'incorrect' + reset

# Print results
print("%sGood job %s your score was: %d%% in %d seconds!" % (yellow,name,score * 100 / max_equations,time.time()-begin))

# Open the file
myfile = open(filename, "a")
# Write score
myfile.write("%s %s got %d%% in %d seconds\n" % (start_time,name,score * 100 / max_equations,time.time() - begin))
# Close file
myfile.close()
