from math import pi


def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant
def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)