def FizzBuzz(n):
    num = 1
    while num <= int(n):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

        num += 1

FizzBuzz(int(input("Give me a number: ")))