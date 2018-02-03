from random import randint
import time
import sys

thing = {
    "awesome" : ["awesome work"]          ,
    "good"    : ["well done" ,"good job"] ,
    "ok"      : ["try again"]             ,
    "bad"     : ["you can do better"]
}

colors = {
        "green"  : '\033[92m'  ,
        "red"    : '\033[91m'  ,
        "reset"  : '\033[0m'   ,
        "blue"   : '\033[94m'  ,
        "yellow" : '\033[93m'  ,
        "cyan"   : '\033[96m'
}

score = 0

def getName():
    while True :
        username = raw_input('What is your name? ').lower().capitalize()
        if username == "" or not username.isalpha(): print 'I didn\'t get that'
        else: return username

def randomize(l):
    ran = randint(0, len(l)-1)
    return l[ran]

def saveScore(u,s,t):
    print colors["yellow"] + "Saving Results..."

    # Open the file
    scorefile = open('score.test', "a")

    # Put stuff in file    
    scorefile.write("name: %s, score: %d, time: %d seconds\n" % (u,s,t))

    # Close file (very important)
    scorefile.close()
    
def playgame():
 begin = time.time()
 for number in range (0,10):

        random1 = randint (0,6)
        random2 = randint (0,6)

        msg = colors['blue'] + "[" + str(number+1) + "]" + colors['reset']
        msg += " " + str ( random1) + ' * ' + str(random2) + ' = '

        while True:
            if msg.lower() == "q":
                sys.exit(0)
                break
            try:
                numbers = int(raw_input (msg))    
                break
            except:
                print "Please try again"
        
        if numbers == (random1 * random2):
                print("%scorrect%s, %s" % (colors ["green"], colors["reset"], randomize (thing["good"])))
                score+=1
        else:
                print("%sincorrect%s, the answer is %d" % (colors["red"], colors["reset"],random1 * random2))                
        end = time.time()
   

username = getName()
print("Hello %s " % (username))
print("key:\n Q = Quit")
while True :
    confirm = raw_input("type 'I am ready'")
    confirm = confirm.lower()
    if confirm == 'i am ready':
        break
    else :
        print"I didn't get that"
playgame()
    
print ("Your score is %d/10 in %d seconds" % (score, end-begin))
if score >= 7:
    print colors ["cyan"] + (thing["awesome"][0]) + colors["reset"]
else:
    print colors ["cyan"] + (thing["bad"][0]) + colors["reset"]
saveScore(username, score, end-begin)
