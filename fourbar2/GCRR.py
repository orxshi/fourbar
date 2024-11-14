# Input is the shortest (GCRR)

from anim import Animation
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin, atan2, sqrt


nframes = 1000

# The lengths of the links
a = 40 # Link 2: Input
b = 120 # Link 3: Coupler
c = 80 # Link 4
d = 100 # Link 1: Ground


def get_positions(t2, t3, t4):

    l1x[i] = 0
    l1y[i] = 0

    l2x[i] = l1x[i] + a * cos(t2)
    l2y[i] = l1y[i] + a * sin(t2)

    l3x[i] = l2x[i] + b * cos(t3)
    l3y[i] = l2y[i] + b * sin(t3)

    l4x[i] = l3x[i] + c * cos(t4)
    l4y[i] = l3y[i] + c * sin(t4)


# Allocate space for angles
T1  = np.empty(nframes)
T2  = np.linspace(0, 2 * pi, num=nframes)
T3  = np.empty(nframes)
T4  = np.empty(nframes)

# Allocate space for positions
l1x = np.empty(nframes)
l1y = np.empty(nframes)
l2x = np.empty(nframes)
l2y = np.empty(nframes)
l3x = np.empty(nframes)
l3y = np.empty(nframes)
l4x = np.empty(nframes)
l4y = np.empty(nframes)


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

    # There are two T3 and T4 angles. Choose correct combination.
    # Uncomment undesired ones.

    T3[i]  = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))
    #T3[i] = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))

    #T4[i]  = 2 * atan2((-E - sqrt(E**2 - 4 * D * F)) , (2 * D))
    T4[i] = 2 * atan2((-E + sqrt(E**2 - 4 * D * F)) , (2 * D))

    get_positions(T2[i], T3[i], T4[i])

    # (l4 - d) should end up at the origin. We impose 0.1 tolerance in the matching test.
    assert(abs(l4x[i] - d) < 0.1)
    assert(abs(l4y[i] - 0) < 0.1)



anim = Animation([], l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, nframes)
plt.show()
