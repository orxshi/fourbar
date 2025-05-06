from Vector import Vector, mag, ang
from math import radians, cos, sin, pi
from forceloop import forceloop
from constants import *
import matplotlib.pyplot as plt
import numpy as np

def balance(a, b, c):

    b3 = mag(CG3_LRCS)
    phi3 = ang(CG3_LRCS)

    l2 = a
    l3 = b
    l4 = c

    # initials
    initial2 = m2 * CG2_LRCS
    initial4 = m4 * CG4_LRCS

    mr2x = m3 * (b3 * l2 * cos(phi3) / l3 - l2)
    mr2y = m3 * (b3 * l2 * sin(phi3) / l3)

    mr4x = -m3 * b3 * l4 * cos(phi3) / l3
    mr4y = -m3 * b3 * l4 * sin(phi3) / l3

    mr2 = Vector(mr2x, mr2y)
    mr4 = Vector(mr4x, mr4y)

    # initial + X = final
    # X = final - initial

    cw2 = mr2 - initial2
    cw4 = mr4 - initial4

    print(mag(cw2), ang(cw2) * 180 / pi)
    print(mag(cw4), ang(cw4) * 180 / pi)

    return cw2, cw4


# Weights
w2 = 1.5 # lb
w3 = 7.7 # lb
w4 = 5.8 # lb

# compute masses of links
m2 = w2 / g
m3 = w3 / g
m4 = w4 / g

# Mass moment of inertias
IG2 = 0.4 # lb.in.s^2
IG3 = 1.5 # lb.in.s^2
IG4 = 0.8 # lb.in.s^2

CG1_LRCS  = Vector.polar(19, radians(0))
CG2_LRCS  = Vector.polar(3, radians(30))
CG3_LRCS  = Vector.polar(9, radians(45))
CG4_LRCS  = Vector.polar(5, radians(0))

forceloop(m2, m3, m4, IG2, IG3, IG4, CG2_LRCS, CG3_LRCS, CG4_LRCS)


cw2, cw4 = balance(a, b, c)

# assume counter masses are the same as associates
# r2 = mag(cw2) / m2
# r4 = mag(cw4) / m4

# new CG = (m2 * CG2 + m2 * r2) / (2 * m2)
# new CG = (m2 * CG2 + cw2) / (2 * m2)
CG2_LRCS_new = (m2 * CG2_LRCS + cw2) / (2 * m2)
CG4_LRCS_new = (m4 * CG4_LRCS + cw4) / (2 * m4)

G2_CG2 = CG2_LRCS - CG2_LRCS_new
G4_CG4 = CG4_LRCS - CG4_LRCS_new

G2_r2 = cw2 / m2 - CG2_LRCS_new
G4_r4 = cw4 / m4 - CG4_LRCS_new

IG2 = m2 * mag(G2_CG2) ** 2 + m2 * mag(G2_r2) ** 2
IG4 = m4 * mag(G4_CG4) ** 2 + m4 * mag(G4_r4) ** 2

m2 *= 2
m4 *= 2

CG2_LRCS = CG2_LRCS_new
CG4_LRCS = CG4_LRCS_new

forceloop(m2, m3, m4, IG2, IG3, IG4, CG2_LRCS, CG3_LRCS, CG4_LRCS)


# todo: draw counter weights for given theta in the example.