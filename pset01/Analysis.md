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

The first lines the time complexity is **O(n)**, because we have to pass to the file calls, then copy to a list to sort and then again **O(n)** to print each line, then as inbuilt sort functions is being used the time complexity is now **O(nlog n)**, as **O(nlog n)** is greater than **O(n)** the complex time of this program is **O(nlog n)**.

# Task 4

Leasson Learned trying to compare a list to a set ill get wrong values
The time complexity is **O(nlog n)**, because the program as inbuilt sort being user that hence the complexity to **O(nlog n)**.
