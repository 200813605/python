import time
import sys
max_minutes = raw_input('How long do you want the timer?(in minutes) ')
run = raw_input("Start? > ")
mins = 0
if run == "start":
    while mins != max_minutes:
        print "<", mins," minutes have past>"
        time.sleep(60)
        mins += 1
    print"<<<<<<<<<<<<<<<<<<<<<<<<<",max_minutes," minutes>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    sys.exit(0)
