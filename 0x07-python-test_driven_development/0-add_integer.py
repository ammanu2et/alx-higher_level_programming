#!/usr/bin/python3
"""

This module adds two integers

"""

def add_integer(a, b=98):
    """
    function that adds two integers and return a result.

    Args:
        a: first number
        b: second number

    Returns:
         addition of the two integers.

    Raises:
        TypeError: If a or b are not integers or float numbers.

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        return int(a + b)
