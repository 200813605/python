import sys

msg = str
counter = 0
msg_out = []
msg_in = raw_input('What would you like encrypted? ')
for i in range(len(msg_in)):
    letter = ord(msg_in[counter]) #map[msg_in[counter]]
    msg_out.append(letter)
    counter += 1

# msg_out.split(',')
for i in range(len(msg_out)):
    msg.append(letter)
    
    #sys.stdout.write( "%x" % msg_out[i])

    print msg