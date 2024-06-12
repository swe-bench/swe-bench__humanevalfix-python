

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - i]:
            return False
    return True
def check(is_palindrome):
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
check(is_palindrome)
