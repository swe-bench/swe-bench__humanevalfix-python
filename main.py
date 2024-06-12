
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 1) if lst[i]%2 == 0])
def check(add):
    # Check some simple cases
    assert add([4, 2, 6, 7]) == 2
    # Check some edge cases that are easy to work out by hand.
check(add)
