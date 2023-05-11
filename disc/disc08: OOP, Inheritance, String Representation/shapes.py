import math
pi = math.pi

class Shape:
    """All geometric shapes will inherit from this Shape class."""
    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))
class Circle(Shape):
    """A circle is characterized by its radii"""
    def __init__(self, name, radius):
        super().__init__(name)  # pass in the parameter
        self.radius = radius

    def perimeter(self):
        """Returns the perimeter of a circle (2πr)"""
        return 2 * pi * self.radius

    def area(self):
        """Returns the area of a circle (πr^2)"""
        return pi * self.radius ** 2

class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. The area can also be done, but it's more inconvenient."""
    def __init__(self, name, num_sides, side_length):
        super().__init__(name)
        self.num_sides = num_sides
        self.side_length = side_length

    def perimeter(self):
        """Returns the perimeter of a regular polygon (the number of sides multiplied by side length)"""
        return self.side_length * self.num_sides
class Square(RegPolygon):
    def __init__(self, name, side_length):
        super().__init__(name, 4, side_length)

    def area(self):
        """Returns the area of a square (squared side length)"""
        return self.side_length ** 2

class Triangle(RegPolygon):
    """An equilateral triangle"""
    def __init__(self, name, side_length):
        super().__init__(name, 3, side_length)

    def area(self):
        """Returns the area of an equilateral triangle is (squared side length multiplied by the provided constant"""
        constant = math.sqrt(3)/4
        return self.side_length ** 2 * constant