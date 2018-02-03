
#!/usr/bin/env python


def myFunction(a,b):
        print "Got up to "+str(a)
        return b

for number in range (0,16):
        if number == 0 :
                print '0 10'
        elif number == 1 :
                print '1 11'
        elif number > 1 and number <= 4 :
                print number, number + 10
	elif number > 4 and number <= 8 :
                print number, number - 10
	elif number > 8 and number <= 12 :
                print number, number * 10
	else : print("%d %dR%d" % (number, number / 10, number % 10))


greet = 'bye'
print(myFunction (number,greet))
