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
# Create The winner, assume that is the first number in the file
winner_index = 0
time_winner = calls[0][3]
# Create a index to keep track
index = 0

# Iterate every line of the file
for line in calls:
    # Compare values os time spent for the call
    if int(line[3]) > int(time_winner):
        time_winner = line[3]
        winner_index = index

    # Increment index as such we pass to other line of the file
    index += 1

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(calls[winner_index][0], calls[winner_index][3]))
