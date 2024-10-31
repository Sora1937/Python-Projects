nums=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]

from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    # Initiating a Hashset so it can't have duplicates
    h = set()

    # Looking through each element
    for num in nums:
        h.add(num)

    # This turns the Hashset into a sorted list 
    h = sorted(list(h))
    nums = sorted(nums)

    # This compares the original list to the Hashset to check for duplicates
    if nums == h:
        return False
    else:
        return True
        

print(hasDuplicate(nums))