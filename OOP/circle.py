import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def area(self):
        return f"Area: {math.pi * (self.radius ** 2)}"
    
    def circumference(self):
        return f"Circumference: {2 * math.pi * self.radius}"

c= Circle(5)
print(c)
print(c.area(), c.circumference())