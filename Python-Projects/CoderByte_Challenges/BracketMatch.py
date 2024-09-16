def BracketMatcher(strParam):
    left_bracket_counter = 0
    right_bracket_counter = 0

    for i in strParam:
        if (i == '('):
            left_bracket_counter += 1
        elif (i == ')'):
            right_bracket_counter += 1
        else:
            continue
    if (left_bracket_counter == right_bracket_counter):
        result = 1
    else:
        result = 0
    return result

print(BracketMatcher(input()))