# Example 7.2 (p. 368)
# Acceleration Analysis of a Fourbar Linkage with the Vector Loop Method

# from vel import *
from Vector import Vector, rotate, unit, mag
from math import pi, cos, sin


def VelAcc(R, omega, alpha):
    # Returns tangential velocity and (tan and norm) acceleration
    V = omega * rotate(R, pi / 2)
    A = alpha * mag(R) * unit(V) - omega ** 2 * R
    return V, A

def acc(a, b, c, d, theta2, theta3, theta4, omega2, omega3, omega4, alpha2):
    
  # gravitational acceleration
  g = 386 # in/s^2


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

  # print('alpha3:', round(alpha3, 3))
  # print('alpha4:', round(alpha4, 3))

  return alpha3, alpha4