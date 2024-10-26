twoD_array = [[11, 12, 5, 2], 
              [15, 6, 10, 4], 
              [10, 8, 12, 5], 
              [12, 15, 8, 6]]

def diagonalDifference(arr):
    right = 0
    left = 0
    n = len(arr)
    for i in range(0, n):
        right += arr[i][i]
        left += arr[i][n - i - 1]
    return abs(right - left)

print(diagonalDifference(twoD_array))