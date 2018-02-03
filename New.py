from random import randint
from time import gmtime, strftime
import time
max_equations = 20
score = 0
yellow = '\033[33m'
red    = '\033[31m'
green  = '\033[32m'
reset  = '\033[0m'

filename = "score.txt"
myfile = open(filename, "a")

def change_nums():
    return [ randint(0,4), randint(0,12) ]

name = raw_input ('What is your name? ')

for i in range (max_equations):

    if i == 1:
        start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        begin = time.time()

    (num_a, num_b) = change_nums()

    while True:
        answer = raw_input ('%02d: %d * %d = ' % (i+1, num_a,num_b))
        if answer == ' ' or not answer.isdigit():
            print 'please try again'
        else:
            break

    if num_a * num_b != int(answer):
        print  red + "Incorrect" + reset
    else:
        print   green + "Correct" + reset
        score = score + 1

end = time.time()
print("%sGood job %s your score was: %d%% in %d seconds!" % (yellow,name,score * 100 / max_equations,end-begin))
myfile.write("%s %s got %d%% in %d seconds\n" % (start_time,name,score * 100 / max_equations,end - begin))
myfile.close()

