
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
    return (even_count, odd_count)
def check(even_odd_count):
    # Check some simple cases
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    # Check some edge cases that are easy to work out by hand.
    assert True
check(even_odd_count)
