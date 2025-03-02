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


def get_toggles(TA, TB):

    # returns two toggle positions

    ang_0  = 999
    ang_pi = 999

    for i in range(nframes):

        dif = abs(TA[i] - TB[i])

        if abs(dif - pi) < ang_0:
            ang_0 = abs(dif - pi)
            frm_0 = i

        if abs(dif - 2 * pi) < ang_pi:
            ang_pi = abs(dif - 2 * pi)
            frm_pi = i

    return [frm_0, frm_pi]


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


# make a list of forward stroke positions for link 1
dx_forw = np.linspace(77.46, 158.74, num=int(nframes/2))
# make a list of backward stroke positions for link 1
dx_back = np.flip(dx_forw)
# make a complete list of positions for link 1
l4x = np.concatenate([dx_forw, dx_back])


for i, d in enumerate(l4x):

    T4[i] = pi / 2

    K1 = b**2 - a**2 - c**2 - d**2
    K2 = -2 * a * c
    K3 = 2 * a * d

    A = K1 - K3
    B = 2 * K2
    C = K1 + K3

    T2[i]  = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))
    #T2[i] = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))
    T3[i]  = asin((-c - a * sin(T2[i])) / b)

    get_positions(T2[i], T3[i], T4[i])

    # (l4 - d) should end up at the origin. We impose 0.1 tolerance in the matching test.
    assert(abs(l4x[i] - d) < 0.1)
    assert(abs(l4y[i] - 0) < 0.1)


toggles = get_toggles(T2, T3)

anim = Animation(toggles, l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, nframes)
plt.show()
