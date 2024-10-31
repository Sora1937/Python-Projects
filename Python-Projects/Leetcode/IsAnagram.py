class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # This quickly checks 2 strings if they're anagrams
        if sorted(s) == sorted(t):
            return True
        else:
            return False