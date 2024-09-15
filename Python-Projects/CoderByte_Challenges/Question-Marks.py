def QuestionsMarks(strParam):
  count = 0
  strParam = list(strParam)

  for i in strParam:
    if (i == "?"):
      count += 1
  if (count >= 3):
    result = True
  else: 
    result = False
  return result

# keep this function call here 
print(QuestionsMarks(input()))