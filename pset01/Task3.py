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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A:

# Create a set
number_formats = set()
# Go trhough wich line of the file calls (for loop)
for line in calls:
      # Condition: if line[0] starts with (080)
      if "(080)" in line[0]:
            # Compare every line[1] (receiving number) with area codes
            if "(0" in line[1]:
                  number_formats.add(line[1].split(sep=")")[0]+ ")")
            elif line[1][0] == "7" or line[1][0] == "8" or line[1][0] == "9":
                  number_formats.add(line[1][:4])
            elif line[1][:3] == "140":
                  number_formats.add("140")
                  
# Transform set to list so we can sort
prefixe = list(number_formats)
prefixe.sort()

print("The numbers called by people in Bangalore have codes:")
# Print each line
for element in prefixe:
      print(element)


# Part B:

# Variable to hold the number of calls
number_calls_from = 0
number_calls_to = 0

# Loop through calls and find who made a call to Bangalore from Bangalore
for line in calls:
      if line[0][:5] == "(080)":
            number_calls_from += 1
            if line[1][:5] == "(080)":
                  number_calls_to += 1 

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round((number_calls_to/number_calls_from)*100,2)))
