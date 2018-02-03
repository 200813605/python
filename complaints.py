#!/usr/bin/env python

import datetime

filename = "Complaints.txt"
user = raw_input('What is your name? ')
complaint = raw_input ('What complaint do you have? ')
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open the file
myfile = open(filename, "a")

# Put stuff in file
myfile.write("%s [%s]: %s\n" % (now, user, complaint))

# Close file (very important)
myfile.close()
