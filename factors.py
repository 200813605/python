#variables
factors = []

'''
#functions

def find_factors(number):
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)


def print_factors(number):
    print"There are %d factors of %d"%(len(factors), number)
    print str.join(", ", (str(f) for f in factors))

def ask_factors():
    a = input("What number would you like the factors of? ")
    global a

find_factors(a)
print_factors(a)

'''
answer = raw_input("What would you like to do (HCF,LCM,factors)? ")

if answer.upper() == 'HCF':
    print 'a'

elif answer.upper() == 'LCM':  
    print 'b'

elif answer.lower() == 'factors':
    print 'c'

else:
    print'd'