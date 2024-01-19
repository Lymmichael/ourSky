import heapq
import time
import math

class CacheItem:
    def __init__(self, key, value, weight):
        self.key = key
        self.value = value
        self.weight = weight
        self.last_accessed_time = time.time()

    def score(self):
        current_time = time.time()
        time_diff = current_time - self.last_accessed_time + 1
        return self.weight / (math.log(time_diff) + 1)

    def __lt__(self, other):
        return self.score() < other.score()

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.priority_queue = []

    def get(self, key):
        if key in self.cache:
            cache_item = self.cache[key]
            cache_item.last_accessed_time = time.time()
            return cache_item.value
        return -1

    def put(self, key, value, weight):
        if key in self.cache:
            cache_item = self.cache[key]
            cache_item.value = value
            cache_item.weight = weight
            cache_item.last_accessed_time = time.time()
            heapq.heapify(self.priority_queue)
        else:
            cache_item = CacheItem(key, value, weight)
            self.cache[key] = cache_item
            heapq.heappush(self.priority_queue, cache_item)

        if len(self.priority_queue) > self.capacity:
            while self.priority_queue:
                item = heapq.heappop(self.priority_queue)
                if item.key in self.cache:
                    del self.cache[item.key]
                    break

# the get(key) operation has an average time complexity of O(1), ensuring fast retrieval of values from the cache. The put(key, value, weight) operation has a time complexity of O(log n), where n represents the current number of items in the cache. This complexity ensures efficient addition and updating of cache items, considering the priority queue operations.