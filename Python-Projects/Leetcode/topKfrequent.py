numbers = [1,2,2,3,3,3]

import heapq
from collections import Counter

def topKfrequent(nums, k):
    # Get a frequency of each element
    counter = Counter(nums)
    heap = []

    # Go through each key and value/frequency in the counter list
    for key, val in counter.items():

        # If the length of the heap is less than the target, push more elements into the heap until its equal
        if len(heap) < k:
            heapq.heappush(heap, (val, key))

        # If its the same length, push the next on and pop off the lowest frequency/value
        else:
            heapq.heappushpop(heap, (val, key))
    

    # Return the key for each element in the heap
    return[h[1] for h in heap]

print(topKfrequent(numbers, 1))