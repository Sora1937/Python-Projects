def compareTriplets(a, b):
    Alice = 0
    Bob = 0
    score = []
    
    for num1, num2 in zip(a, b):
        if num1 > num2:
            Alice += 1
        elif num1 < num2:
            Bob += 1
        else:
            continue
    score.append(Alice)
    score.append(Bob)
    return score

print(compareTriplets([10, 5, 3], [2, 5, 4]))