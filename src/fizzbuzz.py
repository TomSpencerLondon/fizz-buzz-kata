"""FizzBuzz kata implementation."""


def fizzbuzz_of(number):
    """Convert a number to FizzBuzz string.

    Args:
        number: Integer to convert

    Returns:
        String representation according to FizzBuzz rules
    """
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
