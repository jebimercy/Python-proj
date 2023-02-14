for Fizzbuzz in range(1, 100):
    Fizzbuzz = int(input("Enter a number"))

    if (Fizzbuzz % 3 == 0 and Fizzbuzz % 5 == 0):
        print("FizzBuzz")

    elif (Fizzbuzz % 3 == 0):
        print("Fizz")

    elif (Fizzbuzz % 5 == 0):
        print("Buzz")

    else:
        print("Enter another number")

