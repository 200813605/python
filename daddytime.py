from datetime import date
import time

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

userbdaymonth = raw_input("What month is your birthday in ? ")
userbdayday = raw_input("What day is your birthday ? ")
try:
   userbdaymonthint = int(userbdaymonth)
except ValueError:
   print("That's not a number!")

try:
   userbdaydayint = int(userbdayday)
except ValueError:
   print("That's not a number!")

#dateStuff
secondsPerDay = 60 * 60 * 24
tomorrow = date.fromtimestamp(time.time())
print "Today is "+ tomorrow.strftime("%A %d, %B %Y")

today = date.today()
my_birthday = date(today.year,userbdaymonthint,userbdaydayint)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
    my_birthday
time_to_birthday = abs(my_birthday - today)
print "There are " + str (time_to_birthday.days) + " days untill your birthday"
