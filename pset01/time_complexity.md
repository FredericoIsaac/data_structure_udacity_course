# Time Complexity

>Time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. [***Akash Sharma***]

## Task 0

The runtime in task 0 is **O(n)**, n being the number of lines in the csv file, pass by every line of the file, then we get the values that we want in a order of **O(1)**

## Task 1

The runtime in this task is **O(n)** because we have to loops that ill iterate every line from the lists (the number of records given), the are two loops so O(n) + O(n) and the reading of both files O(n) + O(n). This ill be in a simplified way **O(n)**

# Task 2

Lesson learned: the values of time were a string, so comparing to strings with numeric values ill give us the string that was more ASCII value.
The time complexity is **O(n)**, we ill have to pass through all lines of the file and compare.

# Task 3

Time complexity is **O(n)**, because we have to pass to the file calls, then copy to a list to sort and then again **O(n)** to print each line.

# Task 4

Leasson Learned trying to compare a list to a set ill get wrong values
The time complexity is **O(n<sup>2</sup>)**, because the program pass through every line of the set created to compare to every element of the set.

    for number in possible_marketers:
    if number not in texts_sent or number not in texts_received:
        marketers.append(number)