from Vector import *
import numpy
from link import grashof


def syn_two_pos_rocker_out(c, T4, beta, condition):
    
    K = numpy.linspace(-10, 10, num = 100)

    for k in K:

        R_O4 = Vector(x = 0, y = 0)
        R_4 = R_O4 + Vector(c, T4)
        R_B1 = R_O4 + R_4 * cos(T4)
        R_B2 = R_O4 + R_4 * cos(T4 + beta)

        M = R_B2 - R_B1

        R_O2 = R_B1 + k * M
        a = 0.5 * mag(M)

        #R_O2_B1 = R_B1 - R_O2
        #unit(R_O2_B1)

        b = mag(R_B1 - R_O2) - a
        d = mag(R_O4 - R_O2)

        Tc, cond, code = grashof(a, b, c, d)

        if cond == condition:
            return a, b, c, d


    assert(False)
