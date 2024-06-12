

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 0.5
def check(triangle_area):
    assert triangle_area(5, 3) == 7.5
check(triangle_area)
