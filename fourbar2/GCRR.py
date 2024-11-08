from anim import Animation, plt
import numpy
from math import pi, cos, sin, atan2, sqrt

frames = 1000


# Input is the shortest (GCRR)
a = 40
b = 120
c = 80
d = 100

def coor(t2, t3, t4):

    l1x[i] = 0
    l1y[i] = 0

    l2x[i] = l1x[i] + a * cos(t2)
    l2y[i] = l1y[i] + a * sin(t2)

    l3x[i] = l2x[i] + b * cos(t3)
    l3y[i] = l2y[i] + b * sin(t3)

    l4x[i] = l3x[i] + c * cos(t4)
    l4y[i] = l3y[i] + c * sin(t4)


T1  = numpy.empty(frames)
T2  = numpy.linspace(0, 2 * pi, num=frames)
T3  = numpy.empty(frames)
T3x = numpy.empty(frames)
T4  = numpy.empty(frames)
T4x = numpy.empty(frames)

l1x = numpy.empty(frames)
l1y = numpy.empty(frames)

l2x = numpy.empty(frames)
l2y = numpy.empty(frames)

l3x = numpy.empty(frames)
l3y = numpy.empty(frames)

l4x = numpy.empty(frames)
l4y = numpy.empty(frames)

for i, t2 in enumerate(T2):

    K1 = d / a
    K2 = d / b
    K3 = (c**2 - a**2 - b**2 - d**2) / (2 * a * b)
    K4 = d / c
    K5 = (b**2 - c**2 - a**2 - d**2) / (2 * a * c)

    A = cos(t2) - K1 + K2 * cos(t2) + K3
    B = -2 * sin(t2)
    C = K1 + (K2 - 1) * cos(t2) + K3
    D = cos(t2) - K1 + K4 * cos(t2) + K5
    E = -2 * sin(t2)
    F = K1 + (K4 - 1) * cos(t2) + K5

    T3[i]  = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))
    T3x[i] = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))

    T4[i]  = 2 * atan2((-E - sqrt(E**2 - 4 * D * F)) , (2 * D))
    T4x[i] = 2 * atan2((-E + sqrt(E**2 - 4 * D * F)) , (2 * D))

    coor(T2[i], T3[i], T4x[i])

    assert(abs(l4x[i] - d) < 0.1)
    assert(abs(l4y[i] - 0) < 0.1)


anim = Animation([], l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, frames)
plt.show()
