# SYNTHESIS FOR A SPECIFIED FIXED PIVOT LOCATION
# Section 5.9
# Page 257
# Input are from Example 5.3

from Vector import *
import numpy as np
from math import pi, cos, sin, atan2, sqrt, radians
import matplotlib.pyplot as plt
from scipy import linalg


P1 = Vector(0, 0)

# Given variables
P21 = Vector(-0.244, 0.013)
P31 = Vector(-0.542, 0.029)
alpha2 = radians(-11.34)
alpha3 = radians(-22.19)

# Assumed variables
O2 = Vector(-1.712, 0.033)
O4 = Vector(0.288 , 0.033)

# WZ dyad

R1 = P1 - O2
R2 = P1 + P21 - O2
R3 = P1 + P31 - O2

zeta1 = ang(R1)
zeta2 = ang(R2)
zeta3 = ang(R3)

C1 = mag(R3)  * cos(alpha2 + zeta3) - mag(R2) * cos(alpha3 + zeta2)
C2 = mag(R3)  * sin(alpha2 + zeta3) - mag(R2) * sin(alpha3 + zeta2)
C3 = mag(R1)  * cos(alpha3 + zeta1) - mag(R3) * cos(zeta3)
C4 = -mag(R1) * sin(alpha3 + zeta1) + mag(R3) * sin(zeta3)
C5 = mag(R1)  * cos(alpha2 + zeta1) - mag(R2) * cos(zeta2)
C6 = -mag(R1) * sin(alpha2 + zeta1) + mag(R2) * sin(zeta2)

A1 = -C3**2 - C4**2
A2 = C3 * C6 - C4 * C5
A3 = -C4 * C6 - C3 * C5
A4 = C2 * C3 + C1 * C4
A5 = C4 * C5 - C3 * C6
A6 = C1 * C3 - C2 * C4

K1 = A2 * A4 + A3 * A6
K2 = A3 * A4 + A5 * A6
K3 = 0.5 * (A1**2 - A2**2 - A3**2 - A4**2 - A6**2)

beta3 = 2 * atan2(K2 + sqrt(K1**2 + K2**2 - K3**2), K1 + K3)
#beta3 = 2 * atan2(K2 - sqrt(K1**2 + K2**2 - K3**2), K1 + K3)
# animate too see what trivial solution means

beta2 = atan2(-(A3 * sin(beta3) + A2 * cos(beta3) + A4),
               -(A5 * sin(beta3) + A3 * cos(beta3) + A6))


# US dyad

R1 = P1 - O4
R2 = P1 + P21 - O4
R3 = P1 + P31 - O4

zeta1 = ang(R1)
zeta2 = ang(R2)
zeta3 = ang(R3)

C1 = mag(R3)  * cos(alpha2 + zeta3) - mag(R2) * cos(alpha3 + zeta2)
C2 = mag(R3)  * sin(alpha2 + zeta3) - mag(R2) * sin(alpha3 + zeta2)
C3 = mag(R1)  * cos(alpha3 + zeta1) - mag(R3) * cos(zeta3)
C4 = -mag(R1) * sin(alpha3 + zeta1) + mag(R3) * sin(zeta3)
C5 = mag(R1)  * cos(alpha2 + zeta1) - mag(R2) * cos(zeta2)
C6 = -mag(R1) * sin(alpha2 + zeta1) + mag(R2) * sin(zeta2)

A1 = -C3**2 - C4**2
A2 = C3 * C6 - C4 * C5
A3 = -C4 * C6 - C3 * C5
A4 = C2 * C3 + C1 * C4
A5 = C4 * C5 - C3 * C6
A6 = C1 * C3 - C2 * C4

K1 = A2 * A4 + A3 * A6
K2 = A3 * A4 + A5 * A6
K3 = 0.5 * (A1**2 - A2**2 - A3**2 - A4**2 - A6**2)

gamma3 = 2 * atan2(K2 + sqrt(K1**2 + K2**2 - K3**2), K1 + K3)
#gamma3 = 2 * atan2(K2 - sqrt(K1**2 + K2**2 - K3**2), K1 + K3)
# animate too see what trivial solution means

gamma2 = atan2(-(A3 * sin(gamma3) + A2 * cos(gamma3) + A4),
               -(A5 * sin(gamma3) + A3 * cos(gamma3) + A6))

print('beta2 =', round(degrees(beta2), 2))
print('beta3 =', round(degrees(beta3), 2))
print('gamma2 =', round(degrees(gamma2), 2))
print('gamma3 =', round(degrees(gamma3), 2))
