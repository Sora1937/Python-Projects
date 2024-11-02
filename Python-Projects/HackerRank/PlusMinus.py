def plusMinus(arr):
    countNeg = 0
    countPos = 0
    countZero = 0

    # Find out how many positives negatives and zeros there are
    for x in arr:
        if x < 0:
            countNeg += 1
        elif x > 0:
            countPos += 1
        else:
            countZero += 1
    
    # Get the percentage of the array thats negative, positive, and zeros
    NegativePercent = countNeg / len(arr)
    PositivePercent = countPos / len(arr)
    ZeroPercent = countZero / len(arr)

    # Have the result return 6 numbers after the decimal point
    NegativePercent = "{:.6f}".format(NegativePercent)
    PositivePercent = "{:.6f}".format(PositivePercent)
    ZeroPercent = "{:.6f}".format(ZeroPercent)
    return NegativePercent, PositivePercent, ZeroPercent

print(plusMinus([-4, 3, -9, 0, 4, 1]))