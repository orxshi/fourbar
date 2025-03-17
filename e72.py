# Example 7.2 (p. 368)
# Acceleration Analysis of a Fourbar Linkage with the Vector Loop Method

from e67 import *


alpha2 = 15 # rad/s^2

A = c * sin(theta4)
B = b * sin(theta3)
C = a * alpha2 * sin(theta2)\
  + a * omega2 ** 2 * cos(theta2)\
  + b * omega3 ** 2 * cos(theta3)\
  - c * omega4 ** 2 * cos(theta4)
D = c * cos(theta4)
E = b * cos(theta3)
F = a * alpha2 * cos(theta2)\
  - a * omega2 ** 2 * sin(theta2)\
  - b * omega3 ** 2 * sin(theta3)\
  + c * omega4 ** 2 * sin(theta4)

alpha3 = (C * D - A * F) / (A * E - B * D)
alpha4 = (C * E - B * F) / (A * E - B * D)

print('alpha3:', round(alpha3, 3))
print('alpha4:', round(alpha4, 3))

from Vector import Vector, rotate, sign, unit, mag

# some acceleration values in the book are wrong

# R, V, A can be defined in a function to avoid repetition and errors
def RVA(theta, omega, alpha, m):
    R = Vector.polar(m, theta)
    V = omega * rotate(R, pi / 2)
    A = alpha * m * unit(V) - omega ** 2 * R
    return R, V, A

RA, VA, AA    = RVA(theta2, omega2, alpha2, a)
RBA, VBA, ABA = RVA(theta3, omega3, alpha3, b)
RB, VB, AB    = RVA(theta4, omega4, alpha4, c)

# Just to test AA.x and AA.y
# AAx = -a * alpha2 * sin(theta2) - a * omega2 ** 2 * cos(theta2)
# AAy =  a * alpha2 * cos(theta2) - a * omega2 ** 2 * sin(theta2)

print(AA.x, AA.y)
print(ABA.x, ABA.y)
print(ABA.x, ABA.y)



