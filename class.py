class Fruit():

    def __init__(self, details):
        self.name = details[0]
        self.shape = details[2]
        self.color = details[1]

    def describe(self):
        print("Your %s is  %s and %s."%(self.name, self.color, self.shape))

fruits = []
#class get_product():
#    def get_info(self,a,b,c):
#        while True:
#            if self == '' or not self.isalpha():
#                print "This is not a %s !"%self
#                continue
#            else:
#                fruits.append[a,b,c]
#                break
#        
#fruit_name = raw_input("what is your fruit called? ")
#fruit_shape = raw_input("What is your fruit's shape? ")
#fruit_colour = raw_input("What is your fruit's colour? ")
#
#get_product = fruit_name
#get_product = fruit_shape
#get_product = fruit_colour
#for fruit in fruits:
#    fruit.describe()
#

def get_fruit():

    name = get_input("What is your fruit's name?")
    color = get_input("What is your fruit's color?")
    shape = get_input("What is your fruit's shape?")
    return (name, color, shape)

def get_input(question):
   while True:
      answer = raw_input(question+ " ")
      if answer == "":
          print("I did not understand")
      else:
          break
   return answer


fruits = []

while True:
    details = get_fruit()
    fruits.append(Fruit(details))
    print("You now have %d fruits in your basket" % len(fruits))
    repeat = raw_input("Would you like to add another fruit? Y/N ")
    if repeat.lower() != 'y' and repeat.lower() != 'yes':
        break

for fruit in fruits:  fruit.describe()

