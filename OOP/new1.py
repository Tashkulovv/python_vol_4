from math import pi, pow
class Rectangle:
    def __init__(self, a, b):
        self.width = a
        self.height = b


    def square(self):
        return round(self.width * self.height)


    def perimtr(self):
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, r):
        self.radius = r


    def square(self):
        return round(pi * pow(self.radius, 2), 2)

    def length(self):
        return round(2 * pi * self.radius)

