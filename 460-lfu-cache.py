"""
Hard

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3
 

Constraints:

1 <= capacity <= 104
0 <= key <= 105
0 <= value <= 109
At most 2 * 105 calls will be made to get and put.
"""

from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}  # {key -> (value, count)}
        # Use a dictionary of OrderedDicts to keep track of the order of keys for each count
        # {count -> OrderedDict[key -> value]}
        self.count_to_keys = defaultdict(OrderedDict)
        self.min_count = 0  # Save the minimum count for quick access

    def get(self, key: int) -> int:
        if not key in self.key_to_value:
            return -1
        self.increment_counts(key)  # Access increments the count
        return self.key_to_value[key][0]  # Return the value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_value:  # If the key exists
            count = self.increment_counts(key)  # Increment the count(s)
            self.key_to_value[key] = (value, count)  # Update the value/new count
            return
        if len(self.key_to_value.values()) >= self.capacity:  # If the cache is full
            # Remove the least recently used key
            remove_key, _ = self.count_to_keys[self.min_count].popitem(last=False)
            self.key_to_value.pop(remove_key)
        self.key_to_value[key] = (value, 1)  # Add the new key/value/count to the cache
        self.count_to_keys[1][key] = value
        self.min_count = 1  # Set the new minimum count

    def increment_counts(self, key: int) -> None:
        value, count = self.key_to_value[key]  # Get the value and count
        self.count_to_keys[count].pop(key)  # Remove the key from the current count
        self.count_to_keys[count + 1][key] = value  # Add the key to the next count
        self.key_to_value[key] = (value, count + 1)  # Update the value/new count
        # If the current count is the minimum and there are no keys with that count, update the minimum count
        if count == self.min_count and len(self.count_to_keys[count]) == 0:
            self.min_count = count + 1
        return count + 1  # Return the new count


"""
Test Cases
"""

lfu_cache = LFUCache(2)
lfu_cache.put(1, 1)
lfu_cache.put(2, 2)
assert lfu_cache.get(1) == 1
lfu_cache.put(3, 3)
assert lfu_cache.get(2) == -1
assert lfu_cache.get(3) == 3
lfu_cache.put(4, 4)
assert lfu_cache.get(1) == -1
assert lfu_cache.get(3) == 3
assert lfu_cache.get(4) == 4

print("All test cases passed!")


"""
Time Complexity: O(1) for get and put operations
Space Complexity: O(n) where n is the capacity of the cache
"""

# Previous: 146-lru-cache.py
