from math import *

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def polar(cls, m, T):
        x = m * cos(T)
        y = m * sin(T)
        return cls(x, y)

    def __add__(self, R):
        x = self.x + R.x
        y = self.y + R.y
        return Vector(x=x, y=y)

    def __sub__(self, R):
        x = self.x - R.x
        y = self.y - R.y
        return Vector(x=x, y=y)

    def __mul__(self, S):
        x = self.x * S 
        y = self.y * S 
        return Vector(x=x, y=y)

    def __rmul__(self, S):
        x = self.x * S 
        y = self.y * S 
        return Vector(x=x, y=y)



def ang(V):
    #return 2 * pi - atan2(V.y , V.x)
    return atan2(V.y , V.x)

def mag(V):
    return sqrt(V.x**2 + V.y**2)

def unit(V):
    return V * (1 / mag(V))

def rotate(V, T):
    a = V.x * cos(T) - V.y * sin(T)
    b = V.x * sin(T) + V.y * cos(T)
    return Vector(a, b)
