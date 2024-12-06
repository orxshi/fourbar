# See Section 5.2 (two-position synthesis for rocker output, p. 234)
# and Section 3.5 (quick return mechanisms, p. 119).

from Vector import *
import numpy as np


def syn_two_pos_rocker_out(c, T4, DT4, TR):

    alpha = (TR * 2 * pi) / (1 + TR)
    DT4 = DT4 * pi / 180
    T4 = T4 * pi / 180
    delta = abs(pi - alpha)

    N = np.linspace(2, 500, num = 100)
    T = np.linspace(0, pi / 2, num = 100)

    R_O4 = Vector(x = 0, y = 0)
    R_B1 = R_O4 + Vector.polar(c, T4)
    R_B2 = R_O4 + Vector.polar(c, T4 + DT4)
            
    for n in N:
            for t in T:

                    R_B1_O2 = Vector.polar(n, t + pi)
                    R_O2 = R_B1 + R_B1_O2

                    R_O2_B2_a = R_B2 - R_O2
                    R_O2_B2_b = Vector.polar(mag(R_O2_B2_a), t + delta)
                    R_B2_b = R_O2 + R_O2_B2_b
                    
                    e = abs(ang(R_O2_B2_a) - ang(R_O2_B2_b))

                    d = mag(R_O2 - R_O4)
                    b = 0.5 * (mag(R_B1_O2) + mag(R_O2_B2_a))
                    a = mag(R_B1_O2) - b

                    if a < 10: # optional minimum length for a.
                            continue

                    if e < 0.1:
                            if TR == 1:
                                    assert t == 0
                            return a, b, c, d

    assert False, 'No solution found'


a, b, c, d = syn_two_pos_rocker_out(c = 80, T4 = 40, DT4 = 30, TR = 1.0)
print(round(a), round(b), round(c), round(d))
