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
    # If is a new entry of the caller to the dict, else
    if call[0] not in number_time.keys():
        number_time[call[0]] = int(call[3])
    else:
        number_time[call[0]] += int(call[3])
    # If is a new entry of the callee to the dict, else
    if call[1] not in number_time.keys():
        number_time[call[1]] = int(call[3])
    else:
        number_time[call[0]] += int(call[3])

# See the dict.key that was max value
number_max = max(number_time.items(), key=operator.itemgetter(1))[0]


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number_max, number_time[number_max]))
