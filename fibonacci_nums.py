import sys

a = input('How many fibonacci numbers would you like ')

seq=[1,1]

def generate_nums(a):
    if a == 1:
        print '[1]'
        sys.exit(0)
    for i in range(a-2):
        size = len(seq)
        seq.append(seq[size-2] + seq[size-1])
        
    print seq

generate_nums(a)