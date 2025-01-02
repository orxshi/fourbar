# THREE-POSITION MOTION GENERATION BY ANALYTICAL SYNTHESIS
# Section 5.7
# Page 247
# Input are from Example 5.2

from Vector import *
import numpy as np
from math import pi, cos, sin, atan2, sqrt, radians
import matplotlib.pyplot as plt
from scipy import linalg


# Total number of variables: 14
# Number of equations: 4 (2 from WZ dyad, 2 from US dyad)
# 10 variables must be given or chosen

# All variables: 18
# w, z, u, s,
# theta, sigma,
# phi, psi,
# beta2, beta3,
# gamma2, gamma3,
# p21, p31, delta2, delta3,
# alpha2, alpha3

# Defined variables: 6
# p21, p31, delta2, delta3
# alpha2, alpha3

# Assumed variables: 4
# beta2, beta3,
# gamma2, gamma3

# Solved variables: 8
# w, z, u, s,
# theta, sigma
# phi, psi

# Number of equations: 8
# 4 from Equation 5.26
# 2 from geometry:
# Once you solve for Wx, Wy, you get theta
# Once you solve for Ux, Uy, you get sigma
# Once you solve for Zx, Zy, you get phi
# Once you solve for Sx, Sy, you get psi


# Given variables in Example 5.2 are as follows:
# Location vectors of precision point
p21 = 2.798
p31 = 3.919
delta2 = radians(-31.19)
delta3 = radians(-16.34)
# Angle change of coupler from 1st and 2nd position
alpha2 = radians(-45)
# Angle change of coupler from 1st and 3rd position
alpha3 = radians(9.3)
# Free choices in Example 5.2 are as follows:
# Subtended angle between 1st and 2nd positions of link 2
beta2  = radians(342.3)
# Subtended angle between 1st and 3rd positions of link 2
beta3  = radians(324.8)
# Subtended angle between 1st and 2rd positions of link 4
gamma2 = radians(30.9)
# Subtended angle between 1st and 3rd positions of link 4
gamma3 = radians(80.6)


# WZ dyad

A = cos(beta2) - 1
B = sin(beta2)
C = cos(alpha2) - 1
D = sin(alpha2)
E = p21 * cos(delta2)
F = cos(beta3) - 1
G = sin(beta3)
H = cos(alpha3) - 1
K = sin(alpha3)
L = p31 * cos(delta3)
M = p21 * sin(delta2)
N = p31 * sin(delta3)

AA = np.array(
[
    [A, -B, C, -D],
    [F, -G, H, -K],
    [B, A , D, C ],
    [G, F , K, H ]
])
b = np.array([E, L, M, N]).reshape((4, 1))
x = linalg.inv(AA) @ b

W1 = Vector(x[0][0], x[1][0])
Z1 = Vector(x[2][0], x[3][0])

theta = ang(W1)

## US dyad

A = cos(gamma2) - 1
B = sin(gamma2)
F = cos(gamma3) - 1
G = sin(gamma3)

AA = np.array(
[
    [A, -B, C, -D],
    [F, -G, H, -K],
    [B, A , D, C ],
    [G, F , K, H ]
])
x = linalg.inv(AA) @ b

U1 = Vector(x[0][0], x[1][0])
S1 = Vector(x[2][0], x[3][0])

sigma = ang(U1)

# Lengths

O = Vector(0, 0)

O2 = O - Z1 - W1
O4 = O - S1 - U1

V1 = Z1 - S1

a = mag(W1)
b = mag(V1)
c = mag(U1)
d = mag(W1 + V1 - U1)

R1 = O + W1
R2 = R1 + V1
R3 = R2 - U1
R4 = R3 - O
R5 = R1 + Z1

# The angle between V1 and Z1 is found using definition of dot product
# Z . V = |Z| |V| cos T
dot_ZV = Z1.x * V1.x + Z1.y * V1.y
ang_ZV = acos(dot_ZV / mag(Z1) / mag(V1))

print('{:40} = {:.3f} deg'.format('Angle between V1 and Z1', degrees(ang_ZV)))
print('{:40} = {:.3f} deg'.format('Angle between link 1 and horizontal', degrees(ang(R4))))
print('a = {:.3f}'.format(a))
print('b = {:.3f}'.format(b))
print('c = {:.3f}'.format(c))
print('d = {:.3f}'.format(d))
print('mag(Z1) = {:.3f}'.format(mag(Z1)))
print('mag(S1) = {:.3f}'.format(mag(S1)))
print('theta = {:.3f}'.format(degrees(theta)))
print('O2 = ({:.3f}, {:.3f})'.format(O2.x, O2.y))
print('O4 = ({:.3f}, {:.3f})'.format(O4.x, O4.y))

from get_type import *
typ, code = get_type(a, b, c, d)
print(typ, code)

## The following is for graphically checking out the results
fig, axes = plt.subplots()
axes.set_aspect('equal', adjustable='box')
plt.plot([O2.x, W1.x], [O2.y, W1.y], 'k')
plt.plot([R2.x, W1.x], [R2.y, W1.y], 'b')
plt.plot([R2.x, R3.x], [R2.y, R3.y], 'r')
plt.plot([O2.x, R3.x], [O2.y, R3.y], 'g')
plt.plot([R1.x, R5.x], [R1.y, R5.y], 'b')
plt.plot([R2.x, R5.x], [R2.y, R5.y], 'b')
plt.show()
