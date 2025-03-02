# Page 201
# AN INVERTED #3 CRANK‑SLIDER POSITION SOLUTION

from anim import Animation
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin, asin, atan2, sqrt


nframes = 1000

# Link lengths
a = 40
c = 20
d = 80
# coupler will have variable length (b)

gamma = pi / 2


def get_positions(t2, t3, t4):

    l1x[i] = 0
    l1y[i] = 0

    l2x[i] = l1x[i] + a * cos(t2)
    l2y[i] = l1y[i] + a * sin(t2)

    l3x[i] = l2x[i] - b * cos(t3)
    l3y[i] = l2y[i] - b * sin(t3)

    l4x[i] = l3x[i] - c * cos(t4)
    l4y[i] = l3y[i] - c * sin(t4)


# Allocate space for angles
theta1 = np.empty(nframes)
theta2 = np.linspace(0, 2 * pi, num=nframes)
theta3 = np.empty(nframes)
theta4 = np.empty(nframes)

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

    P =  a * sin(theta2[i]) * sin(gamma) + (a * cos(theta2[i]) - d) * cos(gamma)
    Q = -a * sin(theta2[i]) * cos(gamma) + (a * cos(theta2[i]) - d) * sin(gamma)
    R = -c * sin(gamma)

    S = R - Q
    T = 2 * P
    U = Q + R

    theta4[i] = 2 * atan2(-T + sqrt(T ** 2 - 4 * S * U), 2 * S)
    theta3[i] = theta4[i] + gamma

    b = (a * sin(theta2[i]) - c * sin(theta4[i])) / sin(theta3[i])

    get_positions(theta2[i], theta3[i], theta4[i])





anim = Animation([], l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, nframes)
plt.show()
