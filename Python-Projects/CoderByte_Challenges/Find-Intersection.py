def FindIntersection(strArr):
  first_half = set(strArr[0].split(", "))
  Second_half = set(strArr[1].split(", "))

  result = sorted(list(first_half.intersection(Second_half)), key=lambda str: int(str))
    
  return ','.join(result) if len(result) > 0 else False

# keep this function call here 
print(FindIntersection(input()))