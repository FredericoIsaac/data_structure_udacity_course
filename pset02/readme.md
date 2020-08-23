

## Problem 1 - Least Recently Used Cache (LRU)

>Your job is to use an appropriate data structure(s) to implement the cache.

>In case of a cache hit, your get() operation should return the appropriate value.
>In case of a cache miss, your get() should return -1.
>While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
>All operations must take O(1) time.

>For the current problem, you can consider the size of cache = 5.

Source: [Problem 1 - Udacity](https://classroom.udacity.com/nanodegrees/nd256/parts/b835ca8d-4269-4ca3-b911-c8ceb9cc0aa0/modules/a5f68248-862f-4a72-8682-24b86e2f6d61/lessons/a640374a-90af-40ad-85ff-1c6ce3948219/concepts/d4a73c15-f614-4674-80f4-2449ef50abc4)

* The popitem() method removes the item that was last inserted into the dictionary.

## Problem 2 - Finding Files

Source: https://docs.python.org/3.7/library/os.path.html#

* Goal: For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

* Python's ***os*** module:
    * os.path.isdir(path): Return True if path is an existing directory
    * os.path.isfile(path): Return True if path is an existing regular file.
    * os.listdir(path='.'): Return a list containing the names of the entries in the directory given by path. 
    * os.path.join(path, *paths): Join one or more path components intelligently. The return value is the concatenation of path...

* Forbidden the use of ***os.walk()***.

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