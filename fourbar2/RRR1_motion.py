# Ground is the shortest (RRR1)

from anim_motion import Animation
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin, acos, atan2, sqrt


nframes = 1000

# The lengths of the links
a = 2.4669035392921197 # Link 2: Input
b = 1.47616572201359 # Link 3: Coupler
c = 1.4856279407910054 # Link 4
d = 1.7007994988171315 # Link 1: Ground
z = 1.298
s = 1.035


def get_toggles_analytically():

    # See figure 4.20 (p. 211) and equation 4.37 (p.212).

    T_min = acos((a**2 + d**2 - b**2 - c**2) / (2 * a * d) + (b * c) / (a * d))
    T_max = acos((a**2 + d**2 - b**2 - c**2) / (2 * a * d) - (b * c) / (a * d))

    return T_min, T_max


def get_toggles(TA, TB):

    # returns two toggle positions

    ang_0  = 999
    ang_pi = 999

    for i in range(nframes):

        dif = abs(TA[i] - TB[i])

        if abs(dif - pi) < ang_0:
            ang_0 = abs(dif - pi)
            frm_0 = i

        if abs(dif - 0) < ang_pi:
            ang_pi = abs(dif - 0)
            frm_pi = i

    return [frm_0, frm_pi]


def get_positions(t2, t3, t4, phi, psi):

    l1x[i] = 0
    l1y[i] = 0

    l2x[i] = l1x[i] + a * cos(t2)
    l2y[i] = l1y[i] + a * sin(t2)

    l3x[i] = l2x[i] + b * cos(t3)
    l3y[i] = l2y[i] + b * sin(t3)

    l4x[i] = l3x[i] + c * cos(t4)
    l4y[i] = l3y[i] + c * sin(t4)

    l5x[i] = l2x[i] + z * cos(phi)
    l5y[i] = l2y[i] + z * sin(phi)

    l6x[i] = l3x[i] + s * cos(psi)
    l6y[i] = l3y[i] + s * sin(psi)


#T_min, T_max = get_toggles_analytically()
T_min, T_max = 0.14254149630753243, 0.14254149630753243 + 38.4 * pi / 180


# Allocate space for angles
T1 = np.empty(nframes)

T2_forw = np.linspace(T_min + 0.0001, T_max - 0.0001, num=int(nframes/2))
T2_back = np.flip(T2_forw)
T2 = np.concatenate([T2_forw, T2_back])
T3 = np.empty(nframes)
T4 = np.empty(nframes)
phi = np.empty(nframes)
psi = np.empty(nframes)
alpha2_forw = np.linspace(0, 43.3 * pi / 180, num=int(nframes/2))
alpha2_back = np.flip(alpha2_forw)
alpha2 = np.concatenate([alpha2_forw, alpha2_back])

# Allocate space for positions
l1x = np.empty(nframes)
l1y = np.empty(nframes)
l2x = np.empty(nframes)
l2y = np.empty(nframes)
l3x = np.empty(nframes)
l3y = np.empty(nframes)
l4x = np.empty(nframes)
l4y = np.empty(nframes)
l5x = np.empty(nframes)
l5y = np.empty(nframes)
l6x = np.empty(nframes)
l6y = np.empty(nframes)


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

    phi[i] = 26.5 * pi / 180 - 1.1066135686116216 + alpha2[i]
    psi[i] = 104.1 * pi / 180 - 1.1066135686116216 + alpha2[i]
    #print(phi[i], cos(phi[i]), sin(phi[i]))

    get_positions(T2[i], T3[i], T4[i], phi[i], psi[i])
    #print(l2y[i], l5y[i])
    #assert(False)

    # (l4 - d) should end up at the origin. We impose 0.1 tolerance in the matching test.
    assert(abs(l4x[i] - d) < 0.1)
    assert(abs(l4y[i] - 0) < 0.1)
    assert abs(l6x[i] - l5x[i]) < 0.1, abs(l6x[i] - l5x[i])


#print(phi)
toggles = get_toggles(T3, T4)

anim = Animation(toggles, l1x, l1y, l2x, l2y, l3x, l3y, l4x, l4y, l5x, l5y, nframes)
plt.show()