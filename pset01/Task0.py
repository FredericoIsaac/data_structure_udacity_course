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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# Getting "texts" info asked

texts_incoming_number = texts[0][0]
texts_answering_number = texts[0][1]
texts_time = texts[0][2]

print("First record of texts, {} texts {} at time {}".format(texts_incoming_number, texts_answering_number, texts_time))

# Getting "calls" info asked

calls_incoming_number = calls[-1][0]
calls_answering_number = calls[-1][1]
calls_timestamp = calls[-1][2]
calls_time = calls[-1][3]

print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(calls_incoming_number, calls_answering_number, calls_timestamp, calls_time))