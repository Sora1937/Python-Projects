def anagram(x, y):
    newX = sorted(x.lower())
    newY = sorted(y.lower())
    if newX == newY:
        status = True
    else: status = False
    return status

string1 = 'Hello You'
string2 = 'You Hello'
print(anagram(string1, string2))