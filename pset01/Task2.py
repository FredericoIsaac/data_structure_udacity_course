import operator
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Create an empty dict
number_time = {}

# Iterate over the calls 
for call in calls:
    for num in call[:2]:
        number_time[num] = number_time.get(num, 0) + int(call[3])

# See the dict.key that was max value
number_max = max(number_time.items(), key=operator.itemgetter(1))


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number_max[0], number_max[1]))
