

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)*2
    return squared
def check(sum_squares):
    # Check some simple cases
    assert sum_squares([1,2,3])==14, "This prints if this assert fails 1 (good for debugging!)"
    assert sum_squares([1,4,9])==98, "This prints if this assert fails 1 (good for debugging!)"
    assert sum_squares([1,3,5,7])==84, "This prints if this assert fails 1 (good for debugging!)"
    assert sum_squares([1.4,4.2,0])==29, "This prints if this assert fails 1 (good for debugging!)"
    assert sum_squares([-2.4,1,1])==6, "This prints if this assert fails 1 (good for debugging!)"
check(sum_squares)
