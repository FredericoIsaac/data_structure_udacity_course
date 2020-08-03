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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create a set from all the numbers
numbers_set = set()
count = 0
# Get all numbers from texts and add to the set
for number in texts:
    numbers_set.add(number[0])
    numbers_set.add(number[1])

# Get all numbers from calls and add to the set
for number in calls:
    numbers_set.add(number[0])
    numbers_set.add(number[1])

print("There are {} different telephone numbers in the records.".format(len(numbers_set)))
