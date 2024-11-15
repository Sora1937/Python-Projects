def compareTriplets(a, b):
    Alice = 0
    Bob = 0
    score = []
    
    # This loop compares each number in the triplets and assigns points on which is higher
    # Tie equals 0 points
    for num1, num2 in zip(a, b):
        if num1 > num2:
            Alice += 1
        elif num1 < num2:
            Bob += 1
        else:
            continue

    # Recording the points
    score.append(Alice)
    score.append(Bob)

    return score

print(compareTriplets(input("Triple 1: "), input("Triple 2: ")))