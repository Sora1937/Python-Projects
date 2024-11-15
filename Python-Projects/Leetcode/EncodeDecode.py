class Solution:

    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s  # Example of output is "4#strs"
        return res
    
    def decode(self, str):
        res, i = [], 0

        # This while loop looks at the int at the beginning of the string, then looks that far ahead of the "#"
        # Then it appends the string to a list and looks at the next number
        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res