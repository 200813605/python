from datetime import date
import time
colors = {
   'red':'\033[91m',
   'reset':'\033[0m'
          }

def getdate(question,min,max):
   while True:
      personinput = raw_input(question)
      try:
         userinput = int(personinput)  
      except:
         if number == 1:
            pass
         else:
            print(colors['red'] + "That's not a number!" + colors['reset'])


weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

userbdaymonth = raw_input("What month is your birthday in? [1-12]")
userbdayday = raw_input("What day is your birthday? [1-31]")
try:
   userbdaymonthint = int(userbdaymonth)
except:
   print(colors['red'] + "That's not a number!"+colors['reset'])
   thing = 1

if thing == 1:
   pass
else:
   try:
      userbdaydayint = int(userbdayday)
   except:
      print("That's not a number!")

#dateStuff
secondsPerDay = 60 * 60 * 24
tomorrow = date.fromtimestamp(time.time())
print "Today is " + tomorrow.strftime("%A %d, %B %Y" +" and" )

today = date.today()
my_birthday = date(today.year,userbdaymonthint,userbdaydayint)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
    my_birthday
time_to_birthday = abs(my_birthday - today)
print "There are " + str (time_to_birthday.days) + " days untill your birthday"
