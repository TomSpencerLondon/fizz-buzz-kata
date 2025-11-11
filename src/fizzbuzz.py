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
    else:
        return str(number)
