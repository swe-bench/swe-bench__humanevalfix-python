

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.lower()
def check(flip_case):
    assert flip_case('Hello') == 'hELLO'
check(flip_case)
