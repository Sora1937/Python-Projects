def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

input_numbers = [1, 6, 55, 10, 5]
result = find_largest(input_numbers)
print(result)