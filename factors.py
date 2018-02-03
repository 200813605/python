factors = []

def find_factors(number):
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)


def print_factors():
    print str.join(", ", (str(f) for f in factors))

a = input("What number would you like the factors of? ")

find_factors(a)
print_factors()