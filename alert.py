from random import randint

alert = {
    'birthday' : 'Happy Birthday',
    'ok'   : [ 'Today was a normal day',]
}

def randomize(l):
    ran = randint(0, len(l)-1)
    return l[ran]


for count in range (1000) :
    if count % 365 == 0 :
        print 
    else :
        print randomize(alert['ok'])
