from anim import Animation
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin, asin, atan2, sqrt


nframes = 1000

# The lengths of the links
a = 40 # Link 2: Input
b = 120 # Link 3: Coupler
c = 20 # Link 4
# ground link will have changing length (d)


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


for i in range(nframes):

    T4[i] = pi / 2
    T3[i] = asin((-c * sin(T4[i]) - a * sin(T2[i])) / b)
    d = a * cos(T2[i]) + b * cos(T3[i]) + c * cos(T4[i])

    get_positions(T2[i], T3[i], T4[i])


print(min(l4x), max(l4x))



anim = Animation([], l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, nframes)
plt.show()
