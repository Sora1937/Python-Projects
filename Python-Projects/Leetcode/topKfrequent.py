numbers = [1,2,2,3,3,3]

import heapq
from collections import Counter

def topKfrequent(nums, k):
    counter = Counter(nums)
    heap = []

    for key, val in counter.items():
        if len(heap) < k:
            heapq.heappush(heap, (val, key))
        else:
            heapq.heappushpop(heap, (val, key))
    
    return[h[1] for h in heap]

print(topKfrequent(numbers, 1))