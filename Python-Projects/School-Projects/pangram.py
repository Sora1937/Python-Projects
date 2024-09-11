from string import ascii_lowercase

def is_pangram(string):
    alphabet = set(ascii_lowercase)
    return set(string.lower()) >= alphabet

print(is_pangram("The quick brown fox jumps over the lazy dog"))