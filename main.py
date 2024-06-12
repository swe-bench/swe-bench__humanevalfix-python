
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5('text').hexdigest() if text else None
def check(string_to_md5):
    # Check some simple cases
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    # Check some edge cases that are easy to work out by hand.
    assert True
check(string_to_md5)
