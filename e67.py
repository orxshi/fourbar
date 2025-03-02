# Example 6.7 (p. 323)
# Velocity Analysis of a Fourbar Linkage with the Vector Loop Method

from e41 import *
from cmath import polar, phase


omega2 = 25 # rad/s

# Do the analysis for open circuit
theta3 = theta3_open
theta4 = theta4_open


omega3 = a * omega2 * sin(theta4 - theta2) / b / sin(theta3 - theta4)
omega4 = a * omega2 * sin(theta2 - theta3) / c / sin(theta4 - theta3)

print('omega3:', round(omega3, 3))
print('omega4:', round(omega4, 3))

VA  = a * omega2 * complex(-sin(theta2), cos(theta2))
VBA = b * omega3 * complex(-sin(theta3), cos(theta3))
VB  = c * omega4 * complex(-sin(theta4), cos(theta4))

'''
You can call the following two statements to print VA in Cartesian or polar form.
However, numbers are not pretty and you cannot round the numbers such as round(VA, 2).

print('VA:', VA)
print('VA:', polar(VA))
'''

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

# print Cartesian form of VB
print("VB_x: {:.2f}".format(VB.real))
print("VB_y: {:.2f}".format(VB.imag))

# print polar form of VB
print("VB_mag: {:.2f}".format(abs(VB)))
print("VB_ang: {:.2f}".format(degrees(phase(VB))))