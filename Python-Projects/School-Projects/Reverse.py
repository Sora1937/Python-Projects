def string_reverse(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

print(string_reverse("Hello World"))