"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Create a set of calls outgoing
outgoing_calls = set()
# Create a set of received calls
received_calls = set()

# Iterate over calls file and extract to the sets the numbers
for line in calls:
    outgoing_calls.add(line[0])
    received_calls.add(line[1])
# Create another set of possible_marketers
possible_marketers = set()
# Iterate over set received calls
# Give the condition to if set element is NOT in the another set element add to possible_marketers
for line in outgoing_calls:
    if line not in received_calls:
        possible_marketers.add(line)

# Create a set to text sent
texts_sent = set()
# Create a set to text received
texts_received = set()
# Iterate over text file and collect data
for text in texts:
    texts_sent.add(text[0])
    texts_received.add(text[1])

marketers = []
# Iterate if possible_marketers in text file remove() element
for number in possible_marketers:
    if number not in texts_sent or number not in texts_received:
        marketers.append(number)

marketers.sort()

print("These numbers could be telemarketers: ")
# Iterate over new list and print every line
for element in marketers:
    print(element)
