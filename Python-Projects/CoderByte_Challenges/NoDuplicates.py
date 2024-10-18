text = "Hello World!"
letters = [x for x in text]
end_string = ""

for letter in letters:
    if letter in end_string:
        continue
    else:
        end_string += letter

print(end_string)