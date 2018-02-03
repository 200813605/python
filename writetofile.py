#!/usr/bin/env python

filename = "nasser.txt"

# Open the file
myfile = open(filename, "w")

# Put stuff in file
for count in range(50):
    myfile.write(str(count)+'\n')

# Close file (very important)
myfile.close()
