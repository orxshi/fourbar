# This code synthesize can both quick- and non-quick-return four-bars
# See Section 5.2 (two-position synthesis for rocker output, p. 234)
# and Section 3.5 (quick return mechanisms, p. 119).

from Vector import *
import numpy as np


# input
c    = 80
T4   = 40
beta = 30
TR   = 1.0

# free choice
amin = 10 # minimum length (a) of link 2 # you may not like having a link to be much much smaller than others
tol = 0.01 # tolerance of error / precision


# convert degrees to radians
beta = radians(beta)
T4   = radians(T4)

alpha = (TR * 2 * pi) / (1 + TR) # eq. 3.1
delta = abs(pi - alpha) # eq. 3.2

K = np.linspace(2, 500, num = 1000)
T = np.linspace(-pi / 2, pi / 2, num = 100) # angle between B1-B2 and B1-O2 # if the angle is zero, the mechanism is non-quick return

R_O4 = Vector(x = 0, y = 0) # O4 is the origin
R_B1 = R_O4 + Vector.polar(c, T4)
R_B2 = R_O4 + Vector.polar(c, T4 + beta)
        
# The following double loop will synthesize a four-bar
for k in K:
    for t in T:

        # if O2 lies on B1-B2 chord (t = 0), then the mechanism is non-quick-return
        # otherwise, it is quick return

        # Draw a construction line through point B1 at the angle t | Step 3 of Ex. 3.9
        R_B1_B2 = R_B2 - R_B1
        R_B1_O2 = R_B1 + k * unit(rotate(R_B1_B2, t))

        R_O2    = R_B1 + R_B1_O2
        R_B2_O2 = R_O2 - R_B2

        # Angle between B1-O2 and B2-O2 must be delta
        # If not the chosen location of O2 cannot be accepted as a solution.
        # the current attempt may produce non-physical results # if so, continue with next iteration.
        try:
            e = abs(ang(R_B1_O2, R_B2_O2) - delta)
        except:
            continue

        d = mag(R_O2 - R_O4)
        # from Step 7 of Ex. 3.9
        # b + a = O2-B1
        # b - a = O2-B2
        # sum up two equation to get: b = (O2-B1 + O2-B2) / 2
        b = 0.5 * (mag(R_B1_O2) + mag(R_B2_O2))
        a = mag(R_B1_O2) - b

        if a < amin:
            continue

        if e < tol:
            print(round(a), round(b), round(c), round(d))
            exit()
