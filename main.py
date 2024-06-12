

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return b
def check(greatest_common_divisor):
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
check(greatest_common_divisor)
