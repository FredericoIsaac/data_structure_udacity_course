# Time Complexity

>Time complexity of an algorithm quantifies the amount of time taken by an algorithm to run as a function of the length of the input. [***Akash Sharma***]

## Task 0

The runtime in task 0 is **O(n)**, n being the number of lines in the csv file, pass by every line of the file, then we get the values that we want in a order of **O(1)**

>you are doing a get operation in a list and that takes constant time no matter the size of the input. You can use [this](https://wiki.python.org/moin/TimeComplexity) and [this](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt) as reference for the time complexity of built in methods. Just to note: In this ND, you are allowed to assume put and get operations for Python sets and dictionaries as O(1), even for the worst case. We assume the underlying hash tables are sophisticated enough and n collisions are unlikely to occur. [***Udacity - Review***]

## Task 1

The runtime in this task is **O(n)** because we have to loops that ill iterate every line from the lists (the number of records given), the are two loops so O(n) + O(n) and the reading of both files O(n) + O(n). This ill be in a simplified way **O(n)**

# Task 2

Lesson learned: the values of time were a string, so comparing to strings with numeric values ill give us the string that was more ASCII value.
The time complexity is **O(2n)**, because of the nestes for loop.

>There is a nested for loop but the length of the nested loop is very small (just 2 for calls[:2]). So that will be O(2n) which is simplified to O(n). You will only have quadratic time if the two loops are iterating over a large range of values. [***Udacity - Review***]

# Task 3

The first lines the time complexity is **O(n)**, because we have to pass to the file calls, then copy to a list to sort and then again **O(n)** to print each line, then as inbuilt sort functions is being used the time complexity is now **O(nlog n)**, as **O(nlog n)** is greater than **O(n)** the complex time of this program is **O(nlog n)**.

# Task 4

Leasson Learned trying to compare a list to a set ill get wrong values
The time complexity is **O(nlog n)**, because the program as inbuilt sort being user that hence the complexity to **O(nlog n)**.
