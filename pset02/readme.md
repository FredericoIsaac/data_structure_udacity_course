# Project

The goal of this project is use different data structures that is used in day to day of a software developer

## Problem 1 - Least Recently Used Cache (LRU)

At first i has thinking in Queue but with key-value pairs ill not work, unless the key is the index. 

So i decided to use the OrderedDict(), "An OrderedDict is a dictionary subclass that remembers the order in which its contents are added."

The popitem(last=False) method removes the item that was first inserted into the dictionary. 

### Time Complexity

Do the fact of the limitation of capacity in the cache i discard the hashing approach duo to the risk of collision being to high.

With the approach of OrderDict() the time complexity asked is being met **O(1)**

### Space Complexity

> Ordered dict in Python version 2.7 consumes more memory than normal dict. This is due to the underlying Doubly Linked List implementation for keeping the order. In Python 2.7 Ordered Dict is not dict subclass, it’s a specialized container from collections module. [Source](https://www.geeksforgeeks.org/ordereddict-in-python/).

Besides the above the structure is strictly linked to the **capacity**, so ill be **O(n)**


## Problem 2 - Finding Files

Source: https://docs.python.org/3.7/library/os.path.html#

* Goal: For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c" using recursion

### Time Complexity

The time complexity is dependant on the number of iterations that are launched. Being in this case dependent on **depth** and **width** of folders, resulting in a **O(d*w)**. 

### Space Complexity

Is dependent on the number of returns the function does and the number of found files, **O(n))** , **n being number of files**.


## Problem 3 - Data Compression

>In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data).

>A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. **The Huffman Coding** is a lossless data compression algorithm.

[Visualization of Huffman Coding](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)

## Problem 4 - Active Directory


## Problem 5 - Blockchain

We will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

## Problem 6 - Union and Intersection of Two Linked Lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

## Operations Time Complexity

* Source: https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/

|  Operation | Example  | Average Case  | Amortised Worst Case |
|---|---|---|---|
| Pop Item  | d.popitem()  | O(1)  | O(1)  |
| Pop  | d.pop(item)  | O(1)  | O(N)  |
|   |   |   |   |



* In the respective "problem_1.py" files, include at least 3 test cases for each solution.
    * For each test case, write the function call with the input you want to test and print it to the console".
    * On the next line, comment out the output you expect to see from that function call. At least 2 of these must be edge cases, testing inputs such as null values, empty inputs, unusually large values, etc.


# Bibliography

* OrderedDict():
    * https://pymotw.com/2/collections/ordereddict.html

* import os:
    * https://docs.python.org/3.7/library/os.path.html#