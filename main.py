
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    return sorted(words)[0]
def check(find_max):
    # Check some simple cases
    assert (find_max(["name", "of", "string"]) == "string"), "t1"
    assert (find_max(["name", "enam", "game"]) == "enam"), 't2'
    assert (find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"), 't3'
check(find_max)
