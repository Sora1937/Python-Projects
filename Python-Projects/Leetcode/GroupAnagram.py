strs = ["act","pots","tops","cat","stop","hat"]

from collections import defaultdict

def GroupAnagram(strList):
    # Initiate a dictionary to hold the strings
    anagram_dict = defaultdict(list)

    # This for loop creates a frequency key for each word
    for s in strList:
        count = [0] * 26

        # This for loop goes through each letter of the string to get the frequency of each letter
        # This will be used for a key in our dictionary
        for c in s:
            count[ord(c) - ord('a')] += 1

        # This takes the key, puts it in the list and then we return the original value of each key 
        key = tuple(count)
        anagram_dict[key].append(s)


    return anagram_dict.values()

    
print(GroupAnagram(strs))