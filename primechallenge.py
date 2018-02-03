primes = []
num = 0

while True:

    num += 1
    #print("num is %d" % num)

    isPrime = True
    
    for div in range (2, len(primes)):
        #print("Checking %d %% %d is %d" % (num, div, num % div))
        
        if num % primes[div] == 0:
            isPrime = False
            break

        #print("The length of primes is %d" % len(primes))
        
    if isPrime == True:
        primes.append(num)

    if len(primes)== 100:
        break


print (primes)
#good
#   real 0m0.061s
#   user 0m0.040s
#   sys  0m0.020s
#bad        
#   real 0m0.115s
#   user 0m0.100s
#   sys  0m0.010s
