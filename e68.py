# Example 6.8 (p. 197)
# Velocity Analysis of a Fourbar Crank-Slider Linkage with the Vector Loop Method

from e42 import *
from cmath import polar, phase


omega2 = -30 # rad/s

omega3 = a * cos(theta2) * omega2 / b / cos(theta3_open)

print('omega3:', round(omega3, 3))

ddot = -a * omega2 * sin(theta2) + b * omega3 * sin(theta3_open)

print('ddot:', round(ddot))

VA  = a * omega2 * complex(-sin(theta2), cos(theta2))
VAB = b * omega3 * complex(-sin(theta3_open), cos(theta3_open))
VBA = -VAB


# print Cartesian form of VA
print("VA_x: {:.2f}".format(VA.real))
print("VA_y: {:.2f}".format(VA.imag))

# print polar form of VA
print("VA_mag: {:.2f}".format(abs(VA)))
print("VA_ang: {:.2f}".format(degrees(phase(VA))))

# print Cartesian form of VBA
print("VBA_x: {:.2f}".format(VBA.real))
print("VBA_y: {:.2f}".format(VBA.imag))

# print polar form of VBA
print("VBA_mag: {:.2f}".format(abs(VBA)))
print("VBA_ang: {:.2f}".format(degrees(phase(VBA))))