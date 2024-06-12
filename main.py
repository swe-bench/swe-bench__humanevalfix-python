
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([x for idx, x in enumerate(lst) if idx%2==1 and x%2==1])
def check(solution):
    # Check some simple cases
    assert solution([5, 8, 7, 1])    == 12
    assert solution([3, 3, 3, 3, 3]) == 9
    assert solution([30, 13, 24, 321]) == 0
    # Check some edge cases that are easy to work out by hand.
check(solution)
