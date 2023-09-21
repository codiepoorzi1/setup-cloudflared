import time
import sys

def print_message(minute):
    print(minute)
# Get the number of hours from the command line argument
hours = int(sys.argv[1])
minutes = hours * 60

# How many minutes
print("-----------------------")
print(minutes, "minutes")
print("-----------------------")
for minute in range(1, minutes + 1):
    print(minute, "minute /", minutes,"minutes")
    time.sleep(60)
