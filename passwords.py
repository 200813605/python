import random
import sys

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
weak = ['wolf','shark','fox','chicken','rabbit','lion','otter','whale','rat','jaguar','camel','snake','rhino','pig','elephant','bear','tiger','lizard','monkey','seal','eagle','owl','skunk','donkey','badger','walrus']

pass_strength = raw_input('Whould you like a strong/medium/weak password')

if pass_strength == 'strong':
    pass_length = random.randint(10,13)
    password = []

elif pass_strength == 'medium':
    pass_length = random.randint(8,10)
    password = []

elif pass_strength == 'weak':
    password = random.choice(weak) + str(random.randint(11,99))
    print password
    sys.exit(0)

for i in range(pass_length):
    password.append(random.choice(chars))
print password