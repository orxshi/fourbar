import numpy as np
from math import pi, sqrt
from force import force
from Vector import angpos, mag, Vector, cross
import matplotlib.pyplot as plt
from constants import *








def forceloop(m2, m3, m4, IG2, IG3, IG4, CG2_LRCS, CG3_LRCS, CG4_LRCS):

    Th = []
    Fs = []
    reso = 100
    Theta_rad = np.linspace(0, 2 * pi, reso)[:-1]
    Theta_deg = np.linspace(0, 360, reso)[:-1]
    T12 = []
    Ms = []

    for theta2 in Theta_rad:
        
        x = force(a, b, c, d, theta2, omega2, alpha2, m2, m3, m4, IG2, IG3, IG4, CG2_LRCS, CG3_LRCS, CG4_LRCS)

        F12x = x[0]
        F12y = x[1]
        F14x = x[6]
        F14y = x[7]

        F12 = Vector(F12x, F12y)
        F14 = Vector(F14x, F14y)

        # shaking force
        fs = -(F12 + F14)

        Th.append(angpos(fs))
        Fs.append(mag(fs))

        RO4 = Vector.polar(d, 0)
        Ms.append(-x[8] + cross(RO4, -F14))

        T12.append(x[8])
    
    # Shaking force
    fig = plt.figure()
    ax = plt.subplot(polar=True)
    ax.vlines(Th, 0, Fs)
    plt.show()

    # Shaking moment about O2
    plt.plot(Theta_deg, Ms)
    plt.show()

# forceloop()

# # Shaking force
# fig = plt.figure()
# ax = plt.subplot(polar=True)
# ax.vlines(Th, 0, Fs)
# plt.show()

# # Shaking moment about O2
# plt.plot(Theta_deg, Ms)
# plt.show()