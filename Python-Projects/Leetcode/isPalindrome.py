def isPalindrome(s):
    n = len(s)
    L = 0
    R = n - 1

    # This while loop is a 2 pointer method
    while L < R:

        # This makes sure the left pointer is on an alphanumeric value
        if not s[L].isalnum():
            L += 1
            continue

        # This makes sure the right pointer is on an alphanumeric value
        if not s[R].isalnum():
            R -= 1
            continue

        # This checks that the left pointer and right pointer are equal value 
        if s[L].lower() != s[R].lower():
            return False
        
        # Move the pointers after each check
        L += 1
        R -= 1

    return True


print(isPalindrome("Was it a car or a cat I saw?"))