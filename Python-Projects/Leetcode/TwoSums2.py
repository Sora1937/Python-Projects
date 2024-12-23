nums = [11, 32, 43, 27]

def TwoSum(numbers, target):
    n = len(numbers)
    l = 0
    r = n-1

    # This goes through each element of the list from both sides and checks if they add to the target value
    while l < r:
        summ = numbers[l] + numbers[r]
        if summ == target:
            return [l+1, r+1]
        elif summ < target:
            l += 1
        else:
            r -= 1

            
print(TwoSum(nums, 59))