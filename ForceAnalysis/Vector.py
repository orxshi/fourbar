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
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __str__(self):
        return str(round(mag(self), 2)) + ' @ ' + str(round(degrees(angpos(self)), 2))


def zero_vector():
    return Vector(0, 0)

def ang(V):
    return atan2(V.y , V.x)

def angpos(V):
    t = atan2(V.y , V.x)
    if t < 0:
        t += 2 * pi
    return t

def mag(V):
    return sqrt(V.x**2 + V.y**2)

def unit(V):
    if mag(V) == 0:
        return zero_vector()
    return V * (1 / mag(V))

def rotate(V, T):
    a = V.x * cos(T) - V.y * sin(T)
    b = V.x * sin(T) + V.y * cos(T)
    return Vector(a, b)

def dot(V1, V2):
    return V1.x * V2.x + V1.y + V2.y

def ang2(V1, V2):
    # returns angle between V1 and V2 using dot product
    return asin(dot(V1, V2) / (mag(V1) * mag(V2)))

def sign(a):
    return a / abs(a)

def cross(V1, V2):
    # planar cross product
    return V1.x * V2.y - V1.y * V2.x