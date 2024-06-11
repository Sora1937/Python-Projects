from collections import Counter

def find_first_non_repeated(string):
    char_counts = Counter(string)
    for char in string:
        if char_counts[char] == 1:
            return char
    return None

print(find_first_non_repeated('abracadabra'))