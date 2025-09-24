from collections import OrderedDict

class LRUCache:
    __slots__ = ('data', 'capacity')

    def __init__(self, capacity: int):
        self.data: Dict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))

    def put(self, key: int, value: int) -> None:
        try:
            self.data.move_to_end(key)
            self.data[key] = value
        except KeyError:
            self.data[key] = value
            if len(self.data) > self.capacity:
                self.data.popitem(last=False)

    # final solution
    # Purpose: The class creates an LRU (Least Recently Used) cache, which keeps only a fixed number of key-value pairs. When the cache is full and a new item is added, it removes the least recently used item.

# Methods:

# get(key): Returns the value for a key if present and marks it as most recently used; returns -1 if absent.

# put(key, value): Adds or updates a key-value pair, moving the key to the most recent position. If the cache exceeds its capacity, evicts the least recently used item.

# LRU Policy: The cache automatically tracks usage and ensures the oldest/least used key is discarded first when space is needed.

# Efficiency: Both operations (get and put) run in O(1) time.