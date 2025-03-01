"""
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # Use OrderedDict to maintain order of keys

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the key to the end of the cache to indicate its recent use
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Move the key to the end of the cache to indicate its recent use
            self.cache.move_to_end(key)
        self.cache[key] = value  # Always update the key
        if len(self.cache) > self.capacity:
            # Remove the first item in the OrderedDict to get under capacity
            self.cache.popitem(last=False)


"""
Test Cases
"""

lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
assert lru_cache.get(1) == 1
lru_cache.put(3, 3)
assert lru_cache.get(2) == -1
lru_cache.put(4, 4)
assert lru_cache.get(1) == -1
assert lru_cache.get(3) == 3
assert lru_cache.get(4) == 4

print("All test cases passed!")


"""
Time Complexity: O(1) for get and put because we are using an OrderedDict
Space Complexity: O(n) for the OrderedDict
"""

# Next: 460-lfu-cache.py
