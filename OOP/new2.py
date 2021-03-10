from math import pi, pow

class Cube:
    def __init__(self, a, b, c):
        self.length = a
        self.width = b
        self.heigth = c

        self.__squareSurface = 2 * (a * b + a * c + b * c)
        self.__volume = a * b * c


    def S(self):
        return round(self.__squareSurface, 2)

    def V(self):
        return round(self.__volume, 2)

class Ball:
    def __init__(self, r):
        self.radius = r


    def S(self):
        s = 4 * pi * pow(self.radius, 3)
        return round(s, 2)

    def V(self):
        v = (4 / 3) * pi * pow(self.radius, 3)
        return round(v, 2)