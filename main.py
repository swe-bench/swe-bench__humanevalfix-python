

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string) - 1
def check(strlen):
    assert strlen('') == 0
    assert strlen('abc') == 3
check(strlen)
