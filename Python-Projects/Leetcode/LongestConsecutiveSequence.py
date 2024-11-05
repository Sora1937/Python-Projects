def longestConsecutive(nums):
    s = set(nums)
    longest = 0


    # This checks the numbers for a chain of consecutive numbers
    # It checks if the numbers starts a sequence, and if it does it checks how long it goes
    for num in nums:
        if num - 1 not in s:
            next_num = num + 1
            length = 1
            while next_num in s:
                next_num += 1
                length += 1
            longest = max(longest, length)

    return longest

print(longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))