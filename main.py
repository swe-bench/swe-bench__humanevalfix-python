

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n - i == 0:
            return i
def check(largest_divisor):
    assert largest_divisor(15) == 5
check(largest_divisor)
