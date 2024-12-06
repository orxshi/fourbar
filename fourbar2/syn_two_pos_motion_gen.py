# TWO-POSITION MOTION GENERATION BY ANALYTICAL SYNTHESIS
# Section 5.4
# Page 236
# Numbers are from Example 5.1

from Vector import *
import numpy as np
from math import pi, cos, sin, atan2, sqrt
import matplotlib.pyplot as plt


nframes = 1000

z = 1.298
s = 1.035
phi = 26.5 * pi / 180
psi = 104.1 * pi / 180
beta2 = 38.4 * pi / 180
gamma2 = 85.6 * pi / 180

alpha2 = 43.3 * pi / 180
delta2 = 165.2 * pi / 180
p21 = 2.416

# WZ dyad

A = cos(beta2) - 1
B = sin(beta2)
C = cos(alpha2) - 1
D = sin(alpha2)
E = p21 * cos(delta2)
F = p21 * sin(delta2)

O2 = Vector(0, 0)

Z1 = Vector.polar(z, phi)

W1x = (A * (-C * Z1.x + D * Z1.y + E) + B * (-C * Z1.y - D * Z1.x + F)) / (-2 * A)
W1y = (A * (-C * Z1.y - D * Z1.x + F) + B * (C * Z1.x - D * Z1.y - E)) / (-2 * A)

W1 = Vector(W1x, W1y)
theta = ang(W1)

# US dyad

S1 = Vector.polar(s, psi)

A = cos(gamma2) - 1
B = sin(gamma2)
C = cos(alpha2) - 1
D = sin(alpha2)

U1x = (A * (-C * S1.x + D * S1.y + E) + B * (-C * S1.y - D * S1.x + F)) / (-2 * A)
U1y = (A * (-C * S1.y - D * S1.x + F) + B * (C * S1.x - D * S1.y - E)) / (-2 * A)

U1 = Vector(U1x, U1y)
sigma = ang(U1)

# Lenghts

V1 = Z1 - S1

a = mag(W1)
b = mag(V1)
c = mag(U1)
d = mag(W1 + V1 - U1)

R1 = O2 + W1
R2 = R1 + V1
R3 = R2 - U1
R4 = R3 - O2
R5 = R1 + Z1

print(asin(mag(Z1)/mag(V1)) * 180 / pi)

#print(mag(W1), theta * 180 / pi)
#print(mag(U1), sigma * 180 / pi)
print(a, b, c, d)

fig, axes = plt.subplots()
plt.plot([O2.x, W1.x], [O2.y, W1.y], 'k')
plt.plot([R2.x, W1.x], [R2.y, W1.y], 'b')
plt.plot([R2.x, R3.x], [R2.y, R3.y], 'r')
plt.plot([O2.x, R3.x], [O2.y, R3.y], 'g')
plt.plot([R1.x, R5.x], [R1.y, R5.y], 'b')
plt.plot([R2.x, R5.x], [R2.y, R5.y], 'b')

plt.show()

