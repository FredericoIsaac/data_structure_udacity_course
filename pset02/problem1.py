# Least Recently Used (LRU) cache

# TODO

# In case of a cache hit, your get() operation should return the appropriate value.

# In case of a cache miss, your get() should return -1.

# While putting an element in the cache, your put() / set() operation must insert the element.
# If the cache is full, you must write code that removes the least recently used entry first and then insert the element.

# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.


class LRU_Cache(object):
    
    def __init__(self, capacity=5):
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        # The popitem() method removes the item that was last inserted into the dictionary.
        pass



our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry