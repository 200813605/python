from random import randint

red   = '\033[31m'
items = ['pears','apples','oranges','bananas','planes','trucks','parrots','amimals','cars','books','food','lions','diggers','compasses','leaves','chickens','wolves','clocks','kebabistan','potatoes']
verbs = ['were eaten by','kicked','ate','bought','were sent to school with','cooked','made','rode','stared at','hugged','were angered by','smashed','yelled at','wanted to become','were scared of','wore','flew to']

random_verb   = verbs[ randint(0,len(verbs)-1) ]
random_item   = items[ randint(0,len(items)-1) ]
random_amount = randint(0,100)


print("%sIn the year %d, %d%% of people %s %s !" % (red, randint(1000,2000), random_amount, random_verb, random_item))

#print red + 'In the year ' + str(randint(1000,2000)) +' ' +str(random_amount)+'% of people ' + str(random_verb) +' ' +str(random_item)
