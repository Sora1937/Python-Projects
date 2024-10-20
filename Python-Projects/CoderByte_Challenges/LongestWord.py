import string

def LongestWord(sen):

  translator = str.maketrans('', '', string.punctuation)
  cleaned_text = sen.translate(translator)

  senList = cleaned_text.split(' ')

  currentLongest = ""

  for word in senList:
    if len(word) > len(currentLongest):
      currentLongest = word

  return currentLongest

# keep this function call here 
print(LongestWord(input()))


