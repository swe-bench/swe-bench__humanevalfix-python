

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y + y + x
def check(add):
    import random
    assert add(2, 3) == 5
    assert add(5, 7) == 12
check(add)
