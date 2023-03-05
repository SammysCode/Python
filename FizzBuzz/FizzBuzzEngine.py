
def FizzBuzz(value):

    if (value % 15 == 0):
        return "FizzBuzz"

    if (value % 5 == 0):
        return "Buzz"

    if (value % 3 == 0):
        return "Fizz"

    else:
        return value
