from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ' '.join(strings)
def check(concatenate):
    assert concatenate([]) == ''
    assert concatenate(['a', 'b', 'c']) == 'abc'
check(concatenate)
